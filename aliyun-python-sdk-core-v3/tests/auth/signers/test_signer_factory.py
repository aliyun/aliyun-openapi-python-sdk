# coding=utf-8

from tests import unittest
import os

from aliyunsdkcore.auth.signers.signer_factory import SignerFactory
from aliyunsdkcore.auth.credentials \
    import AccessKeyCredential, StsTokenCredential, RamRoleArnCredential, \
    RsaKeyPairCredential, EcsRamRoleCredential
from aliyunsdkcore.auth.signers.access_key_signer import AccessKeySigner
from aliyunsdkcore.auth.signers.sts_token_signer import StsTokenSigner
from aliyunsdkcore.auth.signers.ram_role_arn_signer import RamRoleArnSigner
from aliyunsdkcore.auth.signers.ecs_ram_role_signer import EcsRamRoleSigner
from aliyunsdkcore.auth.signers.rsa_key_pair_signer import RsaKeyPairSigner
from aliyunsdkcore.acs_exception.exceptions import ClientException

from mock import MagicMock, patch, Mock


class TestSignerFactory(unittest.TestCase):
    def test_ak(self):
        cred = {'ak': 'access_key_id', 'secret': 'access_key_secret'}
        signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsInstance(signer, AccessKeySigner)

    @patch.dict("os.environ", {
        'ALIYUN_ACCESS_KEY_ID': 'ak_id_from_env',
        'ALIYUN_ACCESS_KEY_SECRET': 'ak_secret_from_env'
    })
    def test_credential_from_env(self):
        cred = {}
        signer = SignerFactory.get_signer(
            cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsInstance(signer, AccessKeySigner)
        self.assertEqual("ak_id_from_env", signer._credential.access_key_id)

    def test_credential(self):
        # access key signer
        cred = {'credential': AccessKeyCredential(
            'access_key_id', 'access_key_secret')}
        signer = SignerFactory.get_signer(
            cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsInstance(signer, AccessKeySigner)
        # sts token signer
        cred = {'credential': StsTokenCredential(
            'sts_access_key_id', 'sts_access_key_secret', 'sts_token')}
        signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsInstance(signer, StsTokenSigner)

        # Ram Role Arn Credential
        cred = {'credential': RamRoleArnCredential(
            'sts_access_key_id', 'sts_access_key_secret', 'role_arn', 'session_role_name')}
        signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsInstance(signer, RamRoleArnSigner)

        # ecs ram role signer
        cred = {'credential': EcsRamRoleCredential('role_name')}
        signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsInstance(signer, EcsRamRoleSigner)

        # RsaKeyPairCredential
        public_key_path = os.path.join(os.path.dirname(
            __file__), "..", "..", "fixtures", "id_rsa.pub")
        public_key_id = open(public_key_path).read()
        private_key_path = os.path.join(os.path.dirname(
            __file__), "..", "..", "fixtures", "id_rsa")
        private_key_id = open(private_key_path).read()

        cred = {'credential': RsaKeyPairCredential(
            public_key_id, private_key_id, session_period=3600)}
        signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsInstance(signer, RsaKeyPairSigner)

        cred = {'public_key_id': public_key_id,
                'private_key': private_key_id,
                'session_period': 3600}
        signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsInstance(signer, RsaKeyPairSigner)

        # other
        cred = {'credential': {}}
        signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsNone(signer)

    def test_no_info(self):
        cred = {}
        with self.assertRaises(ClientException) as ce:
            SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        self.assertEqual("SDK.InvalidCredential", ce.exception.error_code)
        self.assertEqual(
            "Need a ak&secret pair or public_key_id&private_key pair to auth.",
            ce.exception.message)
