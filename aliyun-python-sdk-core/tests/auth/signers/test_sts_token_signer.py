# coding=utf-8

from tests import unittest

from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkcore.auth.signers.sts_token_signer import StsTokenSigner
from aliyunsdkcore.request import RpcRequest, RoaRequest


class TestStsTokenSigner(unittest.TestCase):
    def test_sts_token_signer(self):
        credential = StsTokenCredential(
            'sts_access_key_id', 'sts_access_key_secret', 'sts_token')
        signer = StsTokenSigner(credential)
        # for rpc
        request = RpcRequest("product", "version", "action_name")
        self.assertIsNone(request.get_query_params().get("SecurityToken"))
        headers, url = signer.sign('cn-hangzhou', request)
        self.assertEqual(headers, {'x-sdk-invoke-type': 'normal'})
        self.assertEqual(request.get_query_params().get("SecurityToken"), 'sts_token')
        # self.assertEqual(url, "/?SignatureVersion=1.0&Format=None"
        # "&Timestamp=2018-12-02T11%3A03%3A01Z&RegionId=cn-hangzhou"
        # "&AccessKeyId=access_key_id&SignatureMethod=HMAC-SHA1&Version=version"
        # "&Signature=AmdeJh1ZOW6PgwM3%2BROhEnbKII4%3D&Action=action_name"
        # "&SignatureNonce=d5e6e832-7f95-4f26-9e28-017f735721f8&SignatureType=')
        request = RoaRequest("product", "version", "action_name", uri_pattern="/")
        request.set_method('get')
        self.assertIsNone(request.get_headers().get("x-acs-security-token"))
        headers, url = signer.sign('cn-hangzhou', request)
        self.assertEqual(request.get_headers().get("x-acs-security-token"), 'sts_token')
