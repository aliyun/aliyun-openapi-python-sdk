# coding:utf-8

from aliyunsdkcore.acs_exception import error_msg
from aliyunsdkcore.acs_exception import error_code
from aliyunsdkcore.acs_exception import exceptions
from alibabacloud.signer import access_key_signer
from alibabacloud.signer import security_signer
from alibabacloud.signer import bearer_token_signer


from alibabacloud.credentials.credentials import AccessKeyCredential,  BearTokenCredential, SecurityCredential


class SignerFactory(object):
    @staticmethod
    def get_signer(credentials):
        signing_type_map = {
            AccessKeyCredential: access_key_signer.AccessKeySigner,
            SecurityCredential: security_signer.SecuritySigner,
            BearTokenCredential: bearer_token_signer.BearTokenSigner
        }
        for credential, sign_func in signing_type_map.items():
            if isinstance(credentials, credential):
                return sign_func(credentials)
        raise exceptions.ClientException(error_code.SDK_INVALID_CREDENTIAL,
                                         error_msg.get_msg('SDK_INVALID_CREDENTIAL'))
