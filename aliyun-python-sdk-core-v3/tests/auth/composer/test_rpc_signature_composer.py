# coding=utf-8

from tests import unittest

from mock import MagicMock, patch
from aliyunsdkcore.auth.composer.rpc_signature_composer import get_signed_url


class TestRpcSignatureComposer(unittest.TestCase):

    @patch("aliyunsdkcore.utils.parameter_helper.get_iso_8061_date")
    @patch("aliyunsdkcore.utils.parameter_helper.get_uuid")
    def test_get_signed_url(self, mock_get_iso_8061_date, mock_get_uuid):
        mock_get_iso_8061_date.return_value = "2018-12-04T04:03:12Z"
        mock_get_uuid.return_value = "7e1c7d12-7551-4856-8abb-1938ccac6bcc"
        url = get_signed_url({}, 'access_key_id',
                             'access_key_secret', 'JSON', 'GET', {})
        mock_get_iso_8061_date.assert_called_once_with()
        mock_get_uuid.assert_called_once_with()
        # self.assertEqual(url, '/?SignatureVersion=1.0'
        #                       '&Format=JSON'
        #                       '&Timestamp=7e1c7d12-7551-4856-8abb-1938ccac6bcc'
        #                       '&AccessKeyId=access_key_id'
        #                       '&SignatureMethod=HMAC-SHA1'
        #                       '&SignatureType='
        #                       '&Signature=5AYPtZduFYvj3ETTIQlivGqL7Ic%3D'
        #                       '&SignatureNonce=2018-12-04T04%3A03%3A12Z')

    @patch("aliyunsdkcore.utils.parameter_helper.get_iso_8061_date")
    @patch("aliyunsdkcore.utils.parameter_helper.get_uuid")
    def test_get_signed_url_with_none_params(self, mock_get_iso_8061_date, mock_get_uuid):
        mock_get_iso_8061_date.return_value = "2018-12-04T04:03:12Z"
        mock_get_uuid.return_value = "7e1c7d12-7551-4856-8abb-1938ccac6bcc"
        url = get_signed_url(None, 'access_key_id',
                             'access_key_secret', 'JSON', 'GET', {})
        mock_get_iso_8061_date.assert_called_once_with()
        mock_get_uuid.assert_called_once_with()
        # self.assertEqual(url, '/?SignatureVersion=1.0'
        #                       '&Format=JSON'
        #                       '&Timestamp=7e1c7d12-7551-4856-8abb-1938ccac6bcc'
        #                       '&AccessKeyId=access_key_id'
        #                       '&SignatureMethod=HMAC-SHA1'
        #                       '&SignatureType='
        #                       '&Signature=5AYPtZduFYvj3ETTIQlivGqL7Ic%3D'
        #                       '&SignatureNonce=2018-12-04T04%3A03%3A12Z')

    @patch("aliyunsdkcore.utils.parameter_helper.get_iso_8061_date")
    @patch("aliyunsdkcore.utils.parameter_helper.get_uuid")
    def test_get_signed_url_with_signature_param(self, mock_get_iso_8061_date, mock_get_uuid):
        mock_get_iso_8061_date.return_value = "2018-12-04T04:03:12Z"
        mock_get_uuid.return_value = "7e1c7d12-7551-4856-8abb-1938ccac6bcc"
        url = get_signed_url(
            {'Signature': 'so what'}, 'access_key_id', 'access_key_secret', 'JSON', 'GET', {})
        mock_get_iso_8061_date.assert_called_once_with()
        mock_get_uuid.assert_called_once_with()
        # self.assertEqual(url, '/?SignatureVersion=1.0'
        #                       '&Format=JSON'
        #                       '&Timestamp=7e1c7d12-7551-4856-8abb-1938ccac6bcc'
        #                       '&AccessKeyId=access_key_id'
        #                       '&SignatureMethod=HMAC-SHA1'
        #                       '&SignatureType='
        #                       '&Signature=5AYPtZduFYvj3ETTIQlivGqL7Ic%3D'
        #                       '&SignatureNonce=2018-12-04T04%3A03%3A12Z')
