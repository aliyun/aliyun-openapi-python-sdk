import json
import os
import time

from alibabacloud.exceptions import ClientException
from alibabacloud.credentials import AccessKeyCredentials
from alibabacloud.credentials import BearerTokenCredentials
from alibabacloud.credentials import SecurityCredentials

from alibabacloud.utils.ini_helper import load_config
from alibabacloud.credentials.assume_role_caller import AssumeRoleCaller


class CredentialsProvider(object):

    def provide(self):
        raise NotImplementedError


class StaticCredentialsProvider(CredentialsProvider):

    def __init__(self, credentials):
        self.credentials = credentials

    def provide(self):
        return self.credentials


class CachedCredentialsProvider(CredentialsProvider):

    def __init__(self):
        self._cached_credentials = None

    def provide(self):

        return self._cached_credentials


class RotatingCredentialsProvider(CachedCredentialsProvider):

    def __init__(self, period, refresh_factor):
        self._period = period
        self._refresh_factor = refresh_factor
        self._last_update_time = 0
        self._expiration = 0
        CachedCredentialsProvider.__init__(self)

    @property
    def is_expiring(self):
        now = time.time()
        return self._expiration - now < self._period * (1 - self._refresh_factor)

    def rotate_credentials(self):
        raise NotImplementedError

    def provide(self):
        if self._cached_credentials is None or self.is_expiring:
            self._expiration = 0
            self._cached_credentials = self.rotate_credentials()
            self._last_update_time = time.time()
            if not self._expiration:
                self._expiration = self._last_update_time + self._period
        return self._cached_credentials


class RamRoleCredentialsProvider(RotatingCredentialsProvider):

    SESSION_PERIOD = 3600
    REFRESH_FACTOR = 0.8

    def __init__(self, client_config, access_key_credentials, role_arn,
                 role_session_name='DefaultSessionName'):
        self.client_config = client_config
        self.access_key_credentials = access_key_credentials
        self.role_arn = role_arn
        self.role_session_name = role_session_name
        self._fetcher = AssumeRoleCaller(client_config,
                                         StaticCredentialsProvider(access_key_credentials))
        RotatingCredentialsProvider.__init__(self, self.SESSION_PERIOD, self.REFRESH_FACTOR)

    def rotate_credentials(self):
        context = self._fetcher.fetch(self.role_arn, self.role_session_name,
                                      self.SESSION_PERIOD)
        response = json.loads(context.http_response.text)
        return SecurityCredentials(
            response.get("Credentials").get("AccessKeyId"),
            response.get("Credentials").get("AccessKeySecret"),
            response.get("Credentials").get("SecurityToken"),
        )


class ProfileCredentialsProvider(CredentialsProvider):

    def __init__(self, client_config, credentials_config_file_name, profile_name):
        self.environ = os.environ
        profile = self._load_profile(credentials_config_file_name, profile_name)
        self.client_config = client_config
        self._inner_provider = self._get_provider_by_profile(profile)

    @staticmethod
    def _load_profile(config_file_name, profile_name):
        full_path = os.path.expanduser(config_file_name)
        if not os.path.isfile(full_path):
            raise ClientException("Failed to find config file for SDK: " + full_path)
        config = load_config(full_path)
        profile = config.get(profile_name, {})
        if 'type' not in profile:
            raise ClientException('The Credentials file (%s) can not find the needed param "type".'
                                  % full_path)
        return profile

    def _get_provider_by_profile(self, profile):

        def _get_value(key):
            if key not in profile:
                raise ClientException(
                    "{0} must be set for credentials type {1}.".format(key, type_))
            return profile[key]

        type_ = profile.get('type')
        if not type_:
            type_ = 'access_key'  # use access_key for default type

        if type_ == 'access_key':
            return StaticCredentialsProvider(AccessKeyCredentials(
                _get_value('access_key_id'),
                _get_value('access_key_secret'),
            ))

        elif type_ == 'ecs_ram_role':
            return InstanceProfileCredentialsProvider(_get_value('role_name'))

        elif type_ == 'ram_role_arn':
            return RamRoleCredentialsProvider(
                self.client_config,
                AccessKeyCredentials(
                    _get_value('access_key_id'),
                    _get_value('access_key_secret'),
                ), _get_value('role_arn'), role_session_name=_get_value('role_session_name'))

        elif type_ == 'bearer_token':
            return StaticCredentialsProvider(BearerTokenCredentials(
                _get_value('bearer_token'),
            ))

        elif type_ == 'rsa_key_pair':
            raise ClientException("RSA Key Pair credentials are not supported.")

        elif type_ == 'sts_token':
            return StaticCredentialsProvider(SecurityCredentials(
                _get_value('access_key_id'),
                _get_value('access_key_secret'),
                _get_value('security_token'),
            ))

        else:
            raise Exception("Unexpected credentials type: " + type_)

    def provide(self):
        return self._inner_provider.provide()


class EnvCredentialsProvider(CachedCredentialsProvider):

    ENV_NAME_FOR_ACCESS_KEY_ID = 'ALIBABA_CLOUD_ACCESS_KEY_ID'
    ENV_NAME_FOR_ACCESS_KEY_SECRET = 'ALIBABA_CLOUD_ACCESS_KEY_SECRET'

    def __init__(self):
        CachedCredentialsProvider.__init__(self)

        if self.ENV_NAME_FOR_ACCESS_KEY_ID in os.environ and \
                self.ENV_NAME_FOR_ACCESS_KEY_SECRET in os.environ:

            access_key_id = os.environ.get(self.ENV_NAME_FOR_ACCESS_KEY_ID)
            access_key_secret = os.environ.get(self.ENV_NAME_FOR_ACCESS_KEY_SECRET)
            if access_key_id is None:
                raise ClientException(
                    'Environment variable %s cannot be empty.' % self.ENV_NAME_FOR_ACCESS_KEY_ID)
            if access_key_secret is None:
                raise ClientException(
                    'Environment variable %s cannot be empty.' %
                    self.ENV_NAME_FOR_ACCESS_KEY_SECRET)

            self._cached_credentials = AccessKeyCredentials(
                access_key_id=access_key_id,
                access_key_secret=access_key_secret)


class InstanceProfileCredentialsProvider(RotatingCredentialsProvider):

    REFRESH_FACTOR = 0.8
    DEFAULT_ECS_SESSION_TOKEN_DURATION = 3600 * 6
    URL_PATH = 'http://100.100.100.200/latest/meta-data/ram/security-credentials/'

    def __init__(self, role_name):
        self.role_name = role_name
        RotatingCredentialsProvider.__init__(self, self.DEFAULT_ECS_SESSION_TOKEN_DURATION,
                                             self.REFRESH_FACTOR)

    def rotate_credentials(self):

        from alibabacloud.vendored import requests
        r = requests.get(url=self.URL_PATH + self.role_name)
        data = json.loads(r.text)
        if data.get("Code") != "Success":
            message = "Failed to get instance profile. Code=" + data.get("Code")
            raise ClientException(message)

        expiration = data.get("Expiration")
        if expiration:
            self._expiration = time.mktime(time.strptime(expiration, '%Y-%m-%dT%H:%M:%SZ'))
        else:
            # FIXME Why?
            self._expiration = expiration

        return SecurityCredentials(
            data['AccessKeyId'],
            data['AccessKeySecret'],
            data['SecurityToken'],
        )


class ChainedCredentialsProvider(CredentialsProvider):

    def __init__(self, provider_chain):
        self._provider_chain = provider_chain

    def provide(self):
        for provider in self._provider_chain:
            credentials = provider.provide()
            if credentials:
                return credentials


class PredefinedChainCredentialsProvider(ChainedCredentialsProvider):

    def __init__(self, client_config, credentials_config_file_name, profile_name, role_name):
        provider_chain = [
            EnvCredentialsProvider(),
            ProfileCredentialsProvider(client_config, credentials_config_file_name, profile_name),
        ]
        if role_name:
            provider_chain.append(InstanceProfileCredentialsProvider(role_name))

        ChainedCredentialsProvider.__init__(self, provider_chain)


class DefaultChainedCredentialsProvider(PredefinedChainCredentialsProvider):

    ENV_NAME_FOR_CREDENTIALS_FILE = 'ALIBABA_CLOUD_CREDENTIALS_FILE'
    DEFAULT_NAME_FOR_CREDENTIALS_FILE = '~/.alibabacloud/credentials'

    def __init__(self, client_config, profile_name='default'):
        credentials_config_file = self._get_config_file_name()
        role_name = self._get_config('role_name')
        PredefinedChainCredentialsProvider.__init__(self, client_config,
                                                    credentials_config_file, profile_name,
                                                    role_name)

    def _get_config_file_name(self):
        if self.ENV_NAME_FOR_CREDENTIALS_FILE in os.environ and \
                os.environ[self.ENV_NAME_FOR_CREDENTIALS_FILE]:
            return os.environ[self.ENV_NAME_FOR_CREDENTIALS_FILE]
        else:
            return self.DEFAULT_NAME_FOR_CREDENTIALS_FILE

    @staticmethod
    def _get_config(config_name):
        env_name = 'ALIBABA_CLOUD_' + config_name.upper()
        if env_name in os.environ:
            return os.environ.get(env_name)
