import json
import os
import time

from alibabacloud.exception import ClientException
from alibabacloud.credentials import AccessKeyCredentials
from alibabacloud.credentials import BearerTokenCredentials
from alibabacloud.credentials import SecurityCredentials

from aliyunsdkcore.acs_exception import error_code
from aliyunsdkcore.acs_exception import exceptions
from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.compat import ensure_string
from aliyunsdkcore.acs_exception import error_msg
from aliyunsdkcore.request import RpcRequest
from aliyunsdkcore.auth.algorithm import sha_hmac256

from alibabacloud.utils.ini_helper import load_config


# from rsa to AccessKeyCredential
class GetSessionAkRequest(RpcRequest):

    def __init__(self):
        RpcRequest.__init__(self, product='Sts', version='2015-04-01',
                            action_name='GenerateSessionAccessKey',
                            signer=sha_hmac256)
        self.set_protocol_type('https')

    def get_duration_seconds(self):
        return self.get_query_params().get("DurationSeconds")

    def set_duration_seconds(self, duration_seconds):
        self.add_query_param('DurationSeconds', duration_seconds)

    def get_public_key_id(self):
        return self.get_query_params().get('PublicKeyId')

    def set_public_key_id(self, public_key_id):
        self.add_query_param('PublicKeyId', public_key_id)


class RsaKeyPairFetcher(object):
    _MIN_SESSION_PERIOD = 900
    _MAX_SESSION_PERIOD = 3600
    REGION_ID = 'ap-northeast-1'

    def __init__(self, profile):
        session_period = profile.get('session_period')
        if session_period < self._MIN_SESSION_PERIOD or \
           session_period > self._MAX_SESSION_PERIOD:
            raise exceptions.ClientException(
                error_code.SDK_INVALID_SESSION_EXPIRATION,
                error_msg.get_msg('SDK_INVALID_SESSION_EXPIRATION').format(
                    self._MIN_SESSION_PERIOD,
                    self._MAX_SESSION_PERIOD))
        self._public_key_id = profile.get('public_key_id')
        self._private_key = profile.get('private_key_file')
        self._session_period = profile.session_period
        self._last_update_time = 0
        # self._schedule_interval = credential.session_period if debug \
        #     else max(credential.session_period * 0.8, 5)
        from aliyunsdkcore.client import AcsClient
        self._sts_client = AcsClient(
            self._public_key_id, self._private_key, self.REGION_ID)
        self._session_credential = {}

    @property
    def is_expiration(self):
        now = int(time.time())
        return now - self._last_update_time > (self._session_period * 0.8)

    def get_profile(self):
        if self.is_expiration:
            request = GetSessionAkRequest()
            request.set_method("GET")
            request.set_duration_seconds(self._session_period)

            try:
                response_str = self._sts_client.do_action_with_exception(request)
                response = json.loads(response_str.decode('utf-8'))
                session_ak = str(response.get(
                    "SessionAccessKey").get("SessionAccessKeyId"))
                session_sk = str(response.get(
                    "SessionAccessKey").get("SessionAccessKeySecret"))
                self._last_update_time = int(time.time())

                self._session_credential['access_key_id'] = session_ak
                self._session_credential['access_key_secret'] = session_sk

                return self._session_credential
            except exceptions.ServerException as srv_ex:
                if srv_ex.error_code == 'InvalidAccessKeyId.NotFound' or \
                   srv_ex.error_code == 'SignatureDoesNotMatch':
                    raise exceptions.ClientException(error_code.SDK_INVALID_CREDENTIAL,
                                                     error_msg.get_msg('SDK_INVALID_CREDENTIAL'))
                else:
                    raise
        return {}


# profile map to credentials
class ProfileResolve:

    def __init__(self, profile):
        self.profile = profile

    def get_resolve_func(self):
        mapping = {
            'access_key': self.resolve_type_of_access_key,
            'ecs_ram_role': self.resolve_type_of_ecs_ram_role,
            'ram_role_arn': self.resolve_type_of_ram_role_arn,
            'bearer_token': self.resolve_type_of_bearer_token,
            'rsa_key_pair': self.resolve_type_of_rsa_key_pair,
            'sts_token': self.resolve_type_of_security_token,
        }
        return mapping[self.profile['type']]

    def resolve_type_of_access_key(self):
        access_key_id = self.profile.get('access_key_id')
        access_key_secret = self.profile.get('access_key_secret')
        return AccessKeyCredentials(access_key_id, access_key_secret)

    def resolve_type_of_ecs_ram_role(self):
        fetcher = InstanceMetadataFetcher(self.profile)
        profile = fetcher.get_profile()
        return SecurityCredentials(**profile)

    def resolve_type_of_ram_role_arn(self):
        fetcher = RamRoleArnFetcher(self.profile)
        profile = fetcher.get_profile()
        return SecurityCredentials(**profile)

    def resolve_type_of_rsa_key_pair(self):
        fetcher = RsaKeyPairFetcher(**self.profile)
        profile = fetcher.get_profile()
        return AccessKeyCredentials(**profile)

    def resolve_type_of_bearer_token(self):
        bearer_token = self.profile.get('bearer_token')
        return BearerTokenCredentials(bearer_token)

    def resolve_type_of_security_token(self):
        access_key_id = self.profile.get('access_key_id')
        access_key_secret = self.profile.get('access_key_secret')
        sts_token = self.profile.get('security_token')
        return SecurityCredentials(access_key_id, access_key_secret, sts_token)


class CredentialsProvider(object):

    # if no credentials got, return None
    def load(self):
        return None


class StaticCredentialsProvider(CredentialsProvider):

    def __init__(self, credentials):
        self.credentials = credentials

    def load(self):
        return self.credentials


# from ram role arn to SecurityCredential
class RamRoleCredentialsProvider(CredentialsProvider):

    SESSION_PERIOD = 3600
    REFRESH_SCALE = 0.8
    RETRY_DELAY_FAST = 3
    PRIORITY = 1

    def __init__(self, access_key_credentials, role_arn, role_session_name='DefaultSessionName'):
        self._last_update_time = 0
        self.access_key_credentials = access_key_credentials
        self.role_arn = role_arn
        self.role_session_name = role_session_name
        self._cached_credentials = None

    @property
    def is_expiring(self):
        now = int(time.time())
        return now - self._last_update_time > (self.SESSION_PERIOD * self.REFRESH_SCALE)

    def load(self):
        if self.is_expiring or self._cached_credentials is None:

            client = self._create_client()

            request = CommonRequest(product="Sts", version='2015-04-01', action_name='AssumeRole')
            request.set_method('POST')
            request.set_protocol_type('https')
            request.add_query_param('RoleArn', self.role_arn)
            request.add_query_param('RoleSessionName', self.role_session_name)
            request.add_query_param('DurationSeconds', self.SESSION_PERIOD)
            request.set_accept_format('JSON')

            body = client.handle_request(request)
            response = json.loads(body)
            self._last_update_time = int(time.time())

            self._cached_credentials = SecurityCredentials(
                response.get("Credentials").get("AccessKeyId"),
                response.get("Credentials").get("AccessKeySecret"),
                response.get("Credentials").get("SecurityToken"),
            )

        return self._cached_credentials

    def _create_client(self):
        """Create an STS client using the source credentials."""
        # 接受AK和token的方式传递
        from alibabacloud.client import ClientConfig, AlibabaCloudClient
        client_config = ClientConfig()

        # FIXME modify this region-id
        client_config.region_id = 'cn-hangzhou'
        client = AlibabaCloudClient(client_config,
                                    StaticCredentialsProvider(self.access_key_credentials))
        return client


class ProfileCredentialsProvider(CredentialsProvider):
    ENV_NAME_FOR_CREDENTIALS_FILE = 'ALIBABA_CLOUD_CREDENTIALS_FILE'
    DEFAULT_NAME_FOR_CREDENTIALS_FILE = ['~/.alibabacloud/credentials']

    def __init__(self, profile_name=None):
        self._profile_name = profile_name
        self.environ = os.environ

    def load(self):
        self._loaded_config = {}

        if self.ENV_NAME_FOR_CREDENTIALS_FILE in self.environ:

            env_file_path = self.environ.get(self.ENV_NAME_FOR_CREDENTIALS_FILE)
            if env_file_path is None:
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

        fetcher = ProfileResolve(profile=profile)
        get_credentials = fetcher.get_resolve_func()
        credentials = get_credentials()
        return credentials


class InstanceCredentialsProvider(CredentialsProvider):
    REFRESH_SCALE = 0.8
    URL_PATH = 'http://100.100.100.200/latest/meta-data/ram/security-credentials/'

    def __init__(self, role_name):
        self.role_name = role_name
        self._last_update_time = 0
        self._expiration = 0
        self._cached_credentials = None

    @property
    def is_expiring(self):
        now = int(time.time())
        return now - self._last_update_time > (self._expiration * self.REFRESH_SCALE)

    def load(self):
        if self.is_expiring or self._cached_credentials is None:
            from aliyunsdkcore.vendored import requests
            r = requests.get(url=self.URL_PATH + self.role_name)
            data = json.loads(r.text)
            if data.get("Code") != "Success":
                message = "Failed to get instance profile. Code=" + data.get("Code")
                raise ClientException(message)

            expiration = data.get("Expiration")
            if expiration:
                self._expiration = time.mktime(time.strptime(expiration, '%Y-%m-%dT%H:%M:%SZ'))
            else:
                self._expiration = expiration
            self._last_update_time = int(time.time())

            return SecurityCredentials(
                data['AccessKeyId'],
                data['AccessKeySecret'],
                data['SecurityToken'],
            )

        return self._cached_credentials


class DefaultCredentialsProvider(CredentialsProvider):

    ENV_NAME_FOR_CREDENTIALS_FILE = 'ALIBABA_CLOUD_CREDENTIALS_FILE'
    DEFAULT_NAME_FOR_CREDENTIALS_FILE = '~/.alibabacloud/credentials'
    ENV_NAME_FOR_ACCESS_KEY_ID = 'ALIBABA_CLOUD_ACCESS_KEY_ID'
    ENV_NAME_FOR_ACCESS_KEY_SECRET = 'ALIBABA_CLOUD_ACCESS_KEY_SECRET'

    def __init__(self, profile_name='default'):
        self.profile_name = profile_name

        self._profile = self._read_profile()

        self._provider = self._get_static_provider_from_env()
        if self._provider:
            return

        self._provider = self._get_instance_profile_credentials_provider()
        if self._provider:
            return

        # providers = [
        #     EnvProvider(),
        #     ProfileCredentialsProvider(profile_name=profile_name),
        #     InstanceCredentialsProvider(),
        # ]

    def _read_profile(self):
        env_file_path = os.environ.get(self.ENV_NAME_FOR_CREDENTIALS_FILE)
        if env_file_path is None:
            env_file_path = self.DEFAULT_NAME_FOR_CREDENTIALS_FILE

        if env_file_path is None:
            raise ClientException(
                'Credentials',
                'The specified credential file path (%s) is invalid.' % env_file_path
            )
        full_path = os.path.expanduser(env_file_path)
        self._loaded_config = load_config(full_path)
        profile = self._loaded_config.get(self.profile_name, {})
        return profile

    def _get_config(self, config_name):
        env_name = 'ALIBABA_CLOUD_' + config_name.upper()
        if env_name in os.environ:
            return os.environ.get(env_name)
        elif config_name in self._profile:
            return self._profile[config_name]
        return None

    def _get_static_provider_from_env(self):
        if self.ENV_NAME_FOR_ACCESS_KEY_ID in os.environ:
            access_key_id = os.environ.get(self.ENV_NAME_FOR_ACCESS_KEY_ID)
            if access_key_id is None:
                raise ClientException(
                    'Credentials',
                    'Environment variable %s cannot be empty.' % self.ENV_NAME_FOR_ACCESS_KEY_ID)
            access_key_secret = os.environ.get(self.ENV_NAME_FOR_ACCESS_KEY_SECRET)
            if access_key_secret is None:
                raise ClientException(
                    'Credentials',
                    'Environment variable %s cannot be empty.' %
                    self.ENV_NAME_FOR_ACCESS_KEY_SECRET)

            credentials = AccessKeyCredentials(
                access_key_id=access_key_id,
                access_key_secret=access_key_secret)
            return StaticCredentialsProvider(credentials)

    def _get_instance_profile_credentials_provider(self):
        role_name = self._get_config('role_name')
        if role_name:
            return InstanceCredentialsProvider(role_name)

    def _get_provider_from_profile(self):
        pass

    def load(self):
        return self._provider.load()
