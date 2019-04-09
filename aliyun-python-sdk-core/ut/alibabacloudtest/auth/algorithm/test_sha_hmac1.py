# coding=utf-8

from tests import unittest

from aliyunsdkcore.auth.algorithm import sha_hmac1 as hmac1
from aliyunsdkcore.vendored import six


class TestShaHmac1(unittest.TestCase):
    def test_sha_hmac1(self):
        result = hmac1.get_sign_string("source", "secret")
        self.assertEqual(result, "Jv4yi8SobFhg5t1C7nWLbhBSFZQ=")
        result = hmac1.get_sign_string("中文unicode", "secret")
        self.assertEqual(result, "szlfHs3WVaO/HgY3Cg7/uyXDaRw=")
        result = hmac1.get_sign_string(
            "中文unicode", unicode("secret") if six.PY2 else "secret")
        self.assertEqual(result, "szlfHs3WVaO/HgY3Cg7/uyXDaRw=")
        self.assertEqual(hmac1.get_signer_name(), "HMAC-SHA1")
        self.assertEqual(hmac1.get_signer_type(), "")
        self.assertEqual(hmac1.get_signer_version(), "1.0")
