# coding=utf-8

from tests import unittest

from mock import MagicMock, patch, Mock

from aliyunsdkcore.auth.credentials import EcsRamRoleCredential
from aliyunsdkcore.auth.signers.ecs_ram_role_signer import EcsRamRoleSigner
from aliyunsdkcore.request import RpcRequest, RoaRequest

from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.compat import ensure_bytes


class TestEcsRamRoleSigner(unittest.TestCase):
    @patch("aliyunsdkcore.auth.signers.ecs_ram_role_signer.urlopen")
    def test_ecs_ram_role_signer(self, mock_urlopen):
        credential = EcsRamRoleCredential("role")
        signer = EcsRamRoleSigner(credential)
        request = RpcRequest("product", "version", "action_name")
        res = Mock()
        res.read.return_value = ensure_bytes('{"Code": "Success","AccessKeyId":"access_key_id",\
            "AccessKeySecret":"access_key_secret","Expiration":"2019-01-25T10:45:23Z",\
            "SecurityToken": "security_token"}')
        mock_urlopen.return_value = res
        headers, url = signer.sign('cn-hangzhou', request)
        mock_urlopen.assert_called_once_with(
            'http://100.100.100.200/latest/meta-data/ram/security-credentials/role')
        self.assertEqual(request.get_query_params().get(
            "SecurityToken"), 'security_token')
        # self.assertEqual(url, '/?SignatureVersion=1.0&Format=None"
        # "&Timestamp=2018-12-02T11%3A03%3A01Z&RegionId=cn-hangzhou"
        # "&AccessKeyId=access_key_id&SignatureMethod=HMAC-SHA1"
        # "&Version=version&Signature=AmdeJh1ZOW6PgwM3%2BROhEnbKII4%3D"
        # "&Action=action_name&SignatureNonce=d5e6e832-7f95-4f26-9e28-017f735721f8&SignatureType=')
        request = RoaRequest("product", "version",
                             "action_name", uri_pattern="/")
        request.set_method('get')
        self.assertIsNone(request.get_headers().get("x-acs-security-token"))
        headers, url = signer.sign('cn-hangzhou', request)
        self.assertEqual(request.get_headers().get(
            "x-acs-security-token"), 'security_token')

    @patch("aliyunsdkcore.auth.signers.ecs_ram_role_signer.urlopen")
    def test_ecs_ram_role_signer_unsuccess(self, mock_urlopen):
        credential = EcsRamRoleCredential("role")
        signer = EcsRamRoleSigner(credential)
        request = RpcRequest("product", "version", "action_name")
        res = Mock()
        res.read.return_value = ensure_bytes('{"Code": "400"}')
        mock_urlopen.return_value = res
        with self.assertRaises(ServerException) as ex:
            signer.sign('cn-hangzhou', request)

        self.assertEqual(
            "refresh Ecs sts token err, code is 400", ex.exception.message)
