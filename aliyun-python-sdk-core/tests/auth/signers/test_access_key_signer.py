# coding=utf-8

from tests import unittest

from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.signers.access_key_signer import AccessKeySigner
from aliyunsdkcore.request import RpcRequest


class TestAccessKeySigner(unittest.TestCase):
    def test_accesskey_signer(self):
        credential = AccessKeyCredential('access_key_id', 'access_key_secret')
        signer = AccessKeySigner(credential)
        request = RpcRequest("product", "version", "action_name")
        headers, url = signer.sign('cn-hangzhou', request)
        self.assertEqual(headers, {'x-sdk-invoke-type': 'normal'})
        # self.assertEqual(url, '/?SignatureVersion=1.0'
        #                       '&Format=None'
        #                       '&Timestamp=2018-12-02T11%3A03%3A01Z'
        #                       '&RegionId=cn-hangzhou'
        #                       '&AccessKeyId=access_key_id'
        #                       '&SignatureMethod=HMAC-SHA1'
        #                       '&Version=version'
        #                       '&Signature=AmdeJh1ZOW6PgwM3%2BROhEnbKII4%3D'
        #                       '&Action=action_name'
        #                       '&SignatureNonce=d5e6e832-7f95-4f26-9e28-017f735721f8'
        #                       '&SignatureType=')
