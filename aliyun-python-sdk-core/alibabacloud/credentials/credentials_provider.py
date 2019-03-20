import json
import os
import time

from aliyunsdkcore.acs_exception.exceptions import ClientException
from alibabacloud.credentials.credentials import AccessKeyCredentials, BearTokenCredentials, SecurityCredentials

from aliyunsdkcore.auth.signers.access_key_signer import AccessKeySigner
from aliyunsdkcore.acs_exception import error_code
from aliyunsdkcore.acs_exception import exceptions
from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.compat import ensure_string
from aliyunsdkcore.acs_exception import error_msg
from aliyunsdkcore.request import RpcRequest
from aliyunsdkcore.auth.algorithm import sha_hmac256

from alibabacloud.utils.ini_helper import load_config




# load config
class DefaultCredentialsProvider(object):
    def __init__(self, credentials):
        providers = [
            UserProvider(credentials),
        ]
        self.providers = providers

    def load_credentials(self):
        for provider in self.providers:
            credentials = provider.load()
            if credentials is not None:
                return credentials
        return None


class CredentialsProvider(object):

    # if no credentials got, return None
    def load(self):
        return None


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
            profile = credentials.get('credentials')
            if access_key_id is not None and len(access_key_id) > 0:
                access_key_secret = credentials.get('access_key_secret')
                if access_key_secret is None or len(access_key_secret) == 0:
                    raise ClientException(
                        'Credentials',
                        'Param access_key_secret can not be empty.')
                return AccessKeyCredentials(
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
                profile = {
                    'public_key_id': 'public_key_id',
                    'private_key': 'private_key',
                    'session_period': 'session_period',
                    'type': 'rsa_key_pair'
                }
                fetcher = ProfileResolve(profile=profile)
                get_credentials = fetcher.get_resolve_func()
                return get_credentials()
            elif profile is not None:
                # 这里要兼容，其实就是token, 保留原本的ecsramrole等，进行反射处理
                return credential
            else:
                return None

        return fetch_credentials

