# coding=utf-8

from tests import unittest

from mock import MagicMock, patch, Mock

from aliyunsdkcore.auth.credentials import RamRoleArnCredential
from aliyunsdkcore.auth.signers.ram_role_arn_signer import RamRoleArnSigner
from aliyunsdkcore.request import RpcRequest, RoaRequest
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.compat import ensure_bytes


class TestRamRoleArnSigner(unittest.TestCase):
    def do_action_200(self, request, signer):
        return 200, {}, ensure_bytes('{"Credentials":{"AccessKeyId":"access_key_id",\
            "AccessKeySecret":"access_key_secret",\
            "SecurityToken":"security_token"}}'), None

    def do_action_400(self, request, signer):
        return 400, {}, 'XXXX', None

    def test_ecs_ram_role_signer(self):
        credential = RamRoleArnCredential(
            "sts_access_key_id", "sts_access_key_secret", "role_arn", "session_role_name")
        signer = RamRoleArnSigner(credential, self.do_action_200)
        self.assertEqual("session_role_name",
                         signer._credential.session_role_name)
        credential = RamRoleArnCredential(
            "sts_access_key_id", "sts_access_key_secret", "role_arn", "")
        signer2 = RamRoleArnSigner(credential, None)
        self.assertTrue(
            signer2._credential.session_role_name.startswith("aliyun-python-sdk-"))

        request = RpcRequest("product", "version", "action_name")
        headers, url = signer.sign('cn-hangzhou', request)
        self.assertEqual(request.get_query_params().get(
            "SecurityToken"), 'security_token')
        # # self.assertEqual(url, '/?SignatureVersion=1.0&Format=None"
        # "&Timestamp=2018-12-02T11%3A03%3A01Z&RegionId=cn-hangzhou"
        # "&AccessKeyId=access_key_id&SignatureMethod=HMAC-SHA1&Version=version"
        # "&Signature=AmdeJh1ZOW6PgwM3%2BROhEnbKII4%3D&Action=action_name"
        # "&SignatureNonce=d5e6e832-7f95-4f26-9e28-017f735721f8&SignatureType=')
        request = RoaRequest("product", "version",
                             "action_name", uri_pattern="/")
        request.set_method('get')
        self.assertIsNone(request.get_headers().get("x-acs-security-token"))
        headers, url = signer.sign('cn-hangzhou', request)
        self.assertEqual(request.get_headers().get(
            "x-acs-security-token"), 'security_token')

        request = RpcRequest("product", "version", "action_name")
        signer3 = RamRoleArnSigner(credential, self.do_action_400)
        with self.assertRaises(ServerException) as ex:
            signer3.sign('cn-hangzhou', request)
        self.assertEqual(
            "refresh session token failed, server return: XXXX", ex.exception.message)
