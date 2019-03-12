import os
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.credentials.credentials import AccessKeyCredential, StsTokenCredential, \
    RamRoleArnCredential, EcsRamRoleCredential, BearTokenCredential, RsaKeyPairCredential
from aliyunsdkcore.credentials.utils import load_config


# load config
class DefaultCredentialsProvider(object):
    def __init__(self, credentials):
        profile_name = credentials.get('profile_name') or 'default'
        providers = [
            UserProvider(credentials),
            EnvProvider(),
            ProfileCredentialsProvider(profile_name=profile_name),
            InstanceCredentialsProvider(),
        ]
        self.providers = providers

    def load_credentials(self):
        for provider in self.providers:
            credentials = provider.load()
            if credentials is not None:
                return credentials
        return None


class CredentialsProvider(object):
    @staticmethod
    def load():
        return True


class UserProvider(CredentialsProvider):
    def __init__(self, credentials):
        self.credentials = credentials

    def load(self):
        if self.credentials:
            fetcher = self._create_credentials_fetcher()
            credentials = fetcher()
            return credentials
        else:
            return None

    def _create_credentials_fetcher(self):
        credentials = self.credentials

        def fetch_credentials():
            access_key_id = credentials.get('access_key_id')
            public_key_id = credentials.get('public_key_id')
            credential = credentials.get('credentials')
            if access_key_id is not None and len(access_key_id) > 0:
                access_key_secret = credentials.get('access_key_secret')
                if access_key_secret is None or len(access_key_secret) == 0:
                    raise ClientException(
                        'Credentials',
                        'Param access_key_secret can not be empty.')
                return AccessKeyCredential(
                    access_key_id=access_key_id,
                    access_key_secret=access_key_secret)
            elif public_key_id is not None and len(public_key_id) > 0:
                private_key = credentials.get('private_key')
                if private_key is None or len(private_key) == 0:
                    raise ClientException(
                        'Credentials',
                        'Param private_key can not be empty.')
                session_period = credentials.get('session_period')
                if session_period is None or len(private_key) == 0:
                    raise ClientException(
                        'Credentials',
                        'Param session_period can not be empty.')
                return RsaKeyPairCredential(
                    public_key_id=public_key_id,
                    private_key=private_key,
                    session_period=session_period)
            elif credential is not None:
                return credential
            else:
                return None

        return fetch_credentials


class EnvProvider(CredentialsProvider):
    ENV_NAME_FOR_ACCESS_KEY_ID = 'ALIBABA_CLOUD_ACCESS_KEY_ID'
    ENV_NAME_FOR_ACCESS_KEY_SECRET = 'ALIBABA_CLOUD_ACCESS_KEY_SECRET'

    def __init__(self):
        self.environ = os.environ

    def load(self):

        if self.ENV_NAME_FOR_ACCESS_KEY_ID in self.environ:
            fetcher = self._create_credentials_fetcher()
            credentials = fetcher()
            return credentials
        else:
            return None

    def _create_credentials_fetcher(self):
        environ = self.environ

        def fetch_credentials():
            access_key_id = environ.get(self.ENV_NAME_FOR_ACCESS_KEY_ID)
            if access_key_id is None or len(access_key_id) == 0:
                raise ClientException(
                    'Credentials',
                    'Environment variable %s cannot be empty.' % self.ENV_NAME_FOR_ACCESS_KEY_ID)
            access_key_secret = environ.get(self.ENV_NAME_FOR_ACCESS_KEY_SECRET)
            if access_key_secret is None or len(access_key_secret) == 0:
                raise ClientException(
                    'Credentials',
                    'Environment variable %s cannot be empty.' %
                    self.ENV_NAME_FOR_ACCESS_KEY_SECRET)

            credential = AccessKeyCredential(
                access_key_id=access_key_id,
                access_key_secret=access_key_secret)
            return credential

        return fetch_credentials


class ProfileResolve:
    def __init__(self, profile):
        self.profile = profile

    def resolve_type_of_access_key(self):
        access_key_id = self.profile.get('access_key_id')
        access_key_secret = self.profile.get('access_key_secret')
        return AccessKeyCredential(access_key_id, access_key_secret)

    def resolve_type_of_ecs_ram_role(self):
        role_name = self.profile.get('role_name')
        return EcsRamRoleCredential(role_name)

    def resolve_type_of_ram_role_arn(self):
        access_key_id = self.profile.get('access_key_id')
        access_key_secret = self.profile.get('access_key_secret')
        role_arn = self.profile.get('role_arn')
        session_name = self.profile.get('session_name')
        return RamRoleArnCredential(
            access_key_id,
            access_key_secret,
            role_arn,
            session_name
        )

    def resolve_type_of_bearer_token(self):
        bearer_token = self.profile.get('bearer_token')
        return BearTokenCredential(bearer_token)

    def resolve_type_of_rsa_key_pair(self):
        public_key_id = self.profile.get('public_key_id')
        private_key_file = self.profile.get('private_key_file')
        session_period = self.profile.get('session_period')
        return RsaKeyPairCredential(public_key_id, private_key_file, session_period)

    def resolve_type_of_sts_token(self):
        access_key_id = self.profile.get('access_key_id')
        access_key_secret = self.profile.get('access_key_secret')
        sts_token = self.profile.get('sts_token')
        return StsTokenCredential(access_key_id, access_key_secret, sts_token)


class ProfileCredentialsProvider(CredentialsProvider):
    ENV_NAME_FOR_CREDENTIALS_FILE = 'ALIBABA_CLOUD_CREDENTIALS_FILE'
    DEFAULT_NAME_FOR_CREDENTIALS_FILE = ['/etc/.alibabacloud/credentials',
                                         '~/.alibabacloud/credentials']

    def __init__(self, profile_name=None):
        self._profile_name = profile_name
        self.environ = os.environ

    def load(self):
        self._loaded_config = {}

        if self.ENV_NAME_FOR_CREDENTIALS_FILE in self.environ:

            env_file_path = self.environ.get(self.ENV_NAME_FOR_CREDENTIALS_FILE)
            if env_file_path is None or len(env_file_path) == 0:
                raise ClientException(
                    'Credentials',
                    'The specified credential file path (%s) is invalid.' % env_file_path
                )
            full_path = os.path.expanduser(env_file_path)
            self._loaded_config = load_config(full_path)
            profile = self._loaded_config.get(self._profile_name, {})
            # can't find type
            if 'type' not in profile:
                raise ClientException(
                    'Credentials',
                    'The Credentials file (%s) can not find the needed param "type".' % full_path
                )
            return self._load_credentials_from_ini_type(profile)

        else:
            potential_locations = self.DEFAULT_NAME_FOR_CREDENTIALS_FILE
            for filename in potential_locations:
                try:
                    self._loaded_config = load_config(filename)
                    break
                except Exception:
                    continue
            profile = self._loaded_config.get(self._profile_name, {})

            if 'type' in profile:
                return self._load_credentials_from_ini_type(profile)
        return None

    @staticmethod
    def _load_credentials_from_ini_type(profile):

        profile_type = profile.get('type')
        resolve_profile = ProfileResolve(profile=profile)

        credentials_map = {
            'access_key': resolve_profile.resolve_type_of_access_key,
            'ecs_ram_role': resolve_profile.resolve_type_of_ecs_ram_role,
            'ram_role_arn': resolve_profile.resolve_type_of_ram_role_arn,
            'bearer_token': resolve_profile.resolve_type_of_bearer_token,
            'rsa_key_pair': resolve_profile.resolve_type_of_rsa_key_pair,
            'sts_token': resolve_profile.resolve_type_of_sts_token,
        }
        get_credentials = credentials_map[profile_type]
        credentials = get_credentials()
        return credentials


class InstanceCredentialsProvider(CredentialsProvider):
    ENV_NAME_FOR_ECS_METADATA = 'ALIBABA_CLOUD_ECS_METADATA'

    def __init__(self):
        self.environ = os.environ

    def load(self):
        if self.ENV_NAME_FOR_ECS_METADATA in self.environ:
            meta_data = self.environ.get(self.ENV_NAME_FOR_ECS_METADATA)
            if meta_data is None or len(meta_data) == 0:
                raise ClientException(
                    'Credentials',
                    'Environment variable %s cannot be empty.' % self.ENV_NAME_FOR_ECS_METADATA
                )
            role_name = meta_data
            credentials = EcsRamRoleCredential(role_name)
            return credentials
        else:
            return None
