# coding=utf-8

import unittest
import os

from aliyunsdkcore.auth.signers.signer_factory import SignerFactory
from aliyunsdkcore.auth.credentials import AccessKeyCredential, StsTokenCredential
from aliyunsdkcore.auth.credentials import RamRoleArnCredential, RsaKeyPairCredential
from aliyunsdkcore.auth.credentials import EcsRamRoleCredential
from aliyunsdkcore.auth.signers.access_key_signer import AccessKeySigner
from aliyunsdkcore.auth.signers.sts_token_signer import StsTokenSigner
from aliyunsdkcore.auth.signers.ram_role_arn_signer import RamRoleArnSigner
from aliyunsdkcore.auth.signers.ecs_ram_role_singer import EcsRamRoleSigner
from aliyunsdkcore.auth.signers.rsa_key_pair_signer import RsaKeyPairSigner


class TestSignerFactory(unittest.TestCase):
    def test_ak(self):
        cred = {'ak': 'access_key_id', 'secret': 'access_key_secret'}
        signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        self.assertIsInstance(signer, AccessKeySigner)

    def test_credential(self):
        # # access key signer
        # cred = {'credential': AccessKeyCredential('access_key_id', 'access_key_secret')}
        # signer = SignerFactory.get_signer(cred['credential'], 'cn-hangzhou', 'do-action-api')
        # self.assertIsInstance(signer, AccessKeySigner)
        #
        # # sts token signer
        # cred = {'credential': StsTokenCredential('sts_access_key_id', 'sts_access_key_secret',
        #                                          'sts_token')}
        # signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        # self.assertIsInstance(signer, StsTokenSigner)
        #
        # # Ram Role Arn Credential
        # cred = {'credential': RamRoleArnCredential('sts_access_key_id', 'sts_access_key_secret',
        #                                            'role_arn', 'session_role_name')}
        # signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        # self.assertIsInstance(signer, RamRoleArnSigner)
        #
        # # ecs ram role signer
        # cred = {'credential': EcsRamRoleCredential('role_name')}
        # signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        # self.assertIsInstance(signer, EcsRamRoleSigner)
        #
        # # RsaKeyPairCredential
        # public_key_path = os.path.join(os.path.dirname(__file__), "..", "..", "fixtures",
        #                                "id_rsa.pub")
        # public_key_id = open(public_key_path).read()
        # private_key_path = os.path.join(os.path.dirname(__file__), "..", "..",
        #                                 "fixtures", "id_rsa")
        # private_key_id = open(private_key_path).read()
        #
        # cred = {
        #     'credential': RsaKeyPairCredential(public_key_id, private_key_id,
        #                                        session_period=3600)}
        # signer = SignerFactory.get_signer(cred, 'cn-hangzhou', 'do-action-api')
        # self.assertIsInstance(signer, RsaKeyPairSigner)
        pass
