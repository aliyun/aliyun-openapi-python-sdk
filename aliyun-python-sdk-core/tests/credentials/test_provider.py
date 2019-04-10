# coding=utf-8

import os
from unittest import mock

from alibabacloud.credentials import AccessKeyCredentials, SecurityCredentials
from alibabacloud.credentials.provider import StaticCredentialsProvider, CachedCredentialsProvider, \
    RotatingCredentialsProvider, CredentialsProvider, \
    ProfileCredentialsProvider, ChainedCredentialsProvider, EnvCredentialsProvider, \
    DefaultChainedCredentialsProvider
from alibabacloud.exceptions import ClientException
from tests import unittest

class TestProvider(unittest.TestCase):

    def test_credentials_provider(self):
        credentials_provider = CredentialsProvider()
        try:
            credentials_provider.provide()
        except NotImplementedError as e:
            self.assertEqual(type(e), NotImplementedError)

    def test_static_credentials_provider(self):
        ak = AccessKeyCredentials("123", "456")
        static_credentials = StaticCredentialsProvider(ak)
        self.assertEqual(static_credentials.provide(), ak)

    def test_cached_credentials_provider(self):
        cached_credentials = CachedCredentialsProvider()
        self.assertEqual(cached_credentials.provide(), None)

    def test_rotating_credentials_provider(self):
        rotating_credentials = RotatingCredentialsProvider(3600, 0.8)
        self.assertEqual(rotating_credentials.is_expiring, True)

        try:
            rotating_credentials.rotate_credentials()
        except NotImplementedError as e:
            self.assertEqual(type(e), NotImplementedError)

        rotating_credentials.rotate_credentials = mock.Mock(return_value=SecurityCredentials(None, None, None))
        self.assertEqual(type(rotating_credentials.provide()), SecurityCredentials)

        rotating_credentials = RotatingCredentialsProvider(-36000000000, 0)
        rotating_credentials._cached_credentials = AccessKeyCredentials(None, None)
        self.assertEqual(type(rotating_credentials.provide()), AccessKeyCredentials)

    def test_profile_credentials_provider(self):
        profile_credentials = ProfileCredentialsProvider("ClientConfig()", "~/.alibabacloud/credentials", "default")
        profile = profile_credentials._load_profile("~/.alibabacloud/credentials", "default")
        self.assertTrue(profile)

        with self.assertRaises(ClientException) as e:
            profile_credentials._load_profile("abc", None)
        self.assertEqual(str(e.exception), "Failed to find config file for SDK: abc")

        full_path = os.path.expanduser("~/.alibabacloud/credentials")
        with self.assertRaises(ClientException) as e:
            profile_credentials._load_profile("~/.alibabacloud/credentials", "abc")
        self.assertEqual(str(e.exception), 'The Credentials file (%s) can not find the needed param "type".'
                         % full_path)

        ak_dict = {'type': 'access_key', 'access_key_id': 'qwe', 'access_key_secret': 'abc'}
        provider_profile = profile_credentials._get_provider_by_profile(ak_dict)
        self.assertEqual(type(provider_profile), StaticCredentialsProvider)
        type_dict_error = {'type': 'type_error'}
        with self.assertRaises(Exception) as e:
            profile_credentials._get_provider_by_profile(type_dict_error)
        self.assertEqual(str(e.exception), "Unexpected credentials type: type_error")
        ak_dict_error = {'type': 'access_key'}
        with self.assertRaises(ClientException) as e:
            profile_credentials._get_provider_by_profile(ak_dict_error)
        self.assertEqual(str(e.exception), "access_key_id must be set for credentials type access_key.")

        self.assertEqual(type(profile_credentials.provide()), AccessKeyCredentials)

    def test_chained_credentials_provider(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = "key_id"
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = "key_secret"
        provider_chain1 = [
            EnvCredentialsProvider(),
            ProfileCredentialsProvider("ClientConfig()", "~/.alibabacloud/credentials", "default"),
        ]
        chained_credentials = ChainedCredentialsProvider(provider_chain1)
        self.assertEqual(chained_credentials.provide().access_key_id, "key_id")
        self.assertEqual(chained_credentials.provide().access_key_secret, "key_secret")

        provider_chain2 = [
            ProfileCredentialsProvider("ClientConfig()", "~/.alibabacloud/credentials", "default"),
        ]
        chained_credentials = ChainedCredentialsProvider(provider_chain2)
        self.assertEqual(type(chained_credentials.provide()), AccessKeyCredentials)

    def test_default_chained_credentials_provider(self):
        default_credentials = DefaultChainedCredentialsProvider(None)
        self.assertEqual(default_credentials._get_config_file_name(), "~/.alibabacloud/credentials")
        os.environ["ALIBABA_CLOUD_CREDENTIALS_FILE"] = "abc"
        self.assertEqual(default_credentials._get_config_file_name(), "abc")

        os.environ["ALIBABA_CLOUD_AK"] = "secret_key"
        ak = default_credentials._get_config("ak")
        self.assertEqual(ak, "secret_key")

