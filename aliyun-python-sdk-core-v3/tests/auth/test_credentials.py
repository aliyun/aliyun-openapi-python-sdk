# coding=utf-8

from tests import unittest

from aliyunsdkcore.auth.credentials import AccessKeyCredential, StsTokenCredential,\
    RamRoleArnCredential
from aliyunsdkcore.auth.credentials import EcsRamRoleCredential, RsaKeyPairCredential


class TestCredentials(unittest.TestCase):
    def test_AccessKeyCredential(self):
        cdtl = AccessKeyCredential("access_key_id", "access_key_secret")
        self.assertEqual("access_key_id", cdtl.access_key_id)
        self.assertEqual("access_key_secret", cdtl.access_key_secret)

    def test_StsTokenCredential(self):
        c = StsTokenCredential("sts_access_key_id",
                               "sts_access_key_secret", "sts_token")
        self.assertEqual("sts_access_key_id", c.sts_access_key_id)
        self.assertEqual("sts_access_key_secret", c.sts_access_key_secret)
        self.assertEqual("sts_token", c.sts_token)

    def test_RamRoleArnCredential(self):
        c = RamRoleArnCredential(
            "sts_access_key_id", "sts_access_key_secret", "role_arn", "session_role_name")
        self.assertEqual("sts_access_key_id", c.sts_access_key_id)
        self.assertEqual("sts_access_key_secret", c.sts_access_key_secret)
        self.assertEqual("role_arn", c.role_arn)
        self.assertEqual("session_role_name", c.session_role_name)

    def test_EcsRamRoleCredential(self):
        c = EcsRamRoleCredential("role_name")
        self.assertEqual("role_name", c.role_name)

    def test_RsaKeyPairCredential(self):
        c = RsaKeyPairCredential("public_key_id", "private_key", 1200)
        self.assertEqual("public_key_id", c.public_key_id)
        self.assertEqual("private_key", c.private_key)
        self.assertEqual(1200, c.session_period)
        # default session_period
        c = RsaKeyPairCredential("public_key_id", "private_key")
        self.assertEqual(3600, c.session_period)
