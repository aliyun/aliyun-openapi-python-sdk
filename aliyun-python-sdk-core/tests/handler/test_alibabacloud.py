import os

from alibabacloud.client import ClientConfig
from alibabacloud.credentials.provider import EnvCredentialsProvider
from alibabacloud.retry.retry_policy import get_default_retry_policy, RetryPolicy, NO_RETRY_POLICY
from alibabacloud.utils.ini_helper import load_config
from tests import unittest

class TestAlibabaCloudClient(unittest.TestCase):

    def test_read_from_env(self):
        client_config = ClientConfig()
        os.environ["DEBUG"] = "SDK"
        os.environ["HTTPS_PROXY"] = "111.177.165.144:9999"
        os.environ["HTTP_PROXY"] = "139.196.137.255:8118"
        client_config.read_from_env()
        self.assertEqual(client_config.https_proxy, "111.177.165.144:9999")
        self.assertEqual(client_config.http_proxy, "139.196.137.255:8118")
        self.assertEqual(client_config.enable_http_debug, "SDK")

    def test_read_from_profile(self):
        client_config = ClientConfig()
        client_config.config_file = None
        profile = {}
        os.environ["ALIBABA_CLOUD_CONFIG_FILE"] = "../../tests/.alibabacloud/credentials"
        env_config_file_path = os.environ.get("ALIBABA_CLOUD_CONFIG_FILE")
        full_path = os.path.expanduser(env_config_file_path)
        loaded_config = load_config(full_path)
        profile = loaded_config.get("default", {})
        self.assertTrue(profile)

        for key in dir(client_config):
            if profile.get(key) is not None and getattr(client_config, key) is None:
                setattr(client_config, key, profile.get(key))
                self.assertTrue(profile.get(key))

    def test_update_config(self):
        request_config = ClientConfig(connection_timeout=5, read_timeout=10)
        client_request = ClientConfig()
        client_request._update_config(request_config)
        self.assertEqual(client_request.connection_timeout, 5)
        self.assertEqual(client_request.read_timeout, 10)

    def test_default_chained_credentials_provider(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = "ak"
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = "secret"
        env_credentials = EnvCredentialsProvider()
        self.assertEqual(env_credentials._cached_credentials.access_key_id, "ak")
        self.assertEqual(env_credentials._cached_credentials.access_key_secret, "secret")

    def test_get_default_retry_policy(self):
        retry_policy = get_default_retry_policy(max_retry_times=10)
        self.assertEqual(type(retry_policy), RetryPolicy)
        self.assertEqual(type(NO_RETRY_POLICY), RetryPolicy)


