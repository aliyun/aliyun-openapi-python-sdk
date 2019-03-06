# coding:utf-8

from aliyunsdkcore.acs_exception import error_msg
from aliyunsdkcore.acs_exception import error_code
from aliyunsdkcore.acs_exception import exceptions
from aliyunsdkcore.credentials.credentials import AccessKeyCredential, StsTokenCredential, \
    RamRoleArnCredential, EcsRamRoleCredential, RsaKeyPairCredential, BearTokenCredential
from aliyunsdkcore.auth.signers import access_key_signer
from aliyunsdkcore.auth.signers import sts_token_signer
from aliyunsdkcore.auth.signers import ram_role_arn_signer
from aliyunsdkcore.auth.signers import ecs_ram_role_signer
from aliyunsdkcore.auth.signers import rsa_key_pair_signer
from aliyunsdkcore.auth.signers import bear_token_signer


class SignerFactory(object):
    @staticmethod
    def get_signer(credentials, region_id, do_action_api, debug=False):
        signing_type_map = {
            AccessKeyCredential: access_key_signer.AccessKeySigner,
            StsTokenCredential: sts_token_signer.StsTokenSigner,
            RamRoleArnCredential: ram_role_arn_signer.RamRoleArnSigner,
            EcsRamRoleCredential: ecs_ram_role_signer.EcsRamRoleSigner,
            RsaKeyPairCredential: rsa_key_pair_signer.RsaKeyPairSigner,
            BearTokenCredential: bear_token_signer.BearTokenSigner,
        }
        for credential, sign_func in signing_type_map.items():
            if isinstance(credentials, credential):
                return sign_func(credentials, region_id=region_id, do_action_api=do_action_api,
                                 debug=debug)
        raise exceptions.ClientException(error_code.SDK_INVALID_CREDENTIAL,
                                         error_msg.get_msg('SDK_INVALID_CREDENTIAL'))
