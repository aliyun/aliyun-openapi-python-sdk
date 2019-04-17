# coding=utf-8

from alibabacloud.credentials import AccessKeyCredentials
from alibabacloud.credentials.provider import CredentialsProvider, StaticCredentialsProvider, \
    ChainedCredentialsProvider, CachedCredentialsProvider, RotatingCredentialsProvider
from tests import unittest


class TestCredentialsHandler(unittest.TestCase):

    def test_credentials_handler(self):
        credentials_provider = CredentialsProvider()
        with self.assertRaises(NotImplementedError) as e:
            credentials_provider.provide()
        self.assertEqual(type(e.exception), NotImplementedError)

        static_credentials = StaticCredentialsProvider(AccessKeyCredentials("ak", "secret_key"))
        self.assertEqual(type(static_credentials.provide()), AccessKeyCredentials)

        provider_chain = [CachedCredentialsProvider()]
        chained_credentials = ChainedCredentialsProvider(provider_chain)
        self.assertEqual(chained_credentials.provide(), None)

