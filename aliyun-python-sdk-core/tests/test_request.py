# coding=utf-8
import sys
from tests import unittest

from mock import MagicMock, patch

from aliyunsdkcore.request import AcsRequest, RpcRequest, RoaRequest, \
    CommonRequest, get_default_protocol_type, set_default_protocol_type
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.compat import ensure_string, ensure_bytes


class TestRequest(unittest.TestCase):

    def test_default_protocol_type(self):
        self.assertEqual(get_default_protocol_type(), "http")
        set_default_protocol_type("https")
        self.assertEqual(get_default_protocol_type(), "https")
        with self.assertRaises(ClientException) as ex:
            set_default_protocol_type("WSS")
        self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
        self.assertEqual(ex.exception.message,
                         "Invalid 'protocol_type', should be 'http' or 'https'")
        set_default_protocol_type("http")

        r = RpcRequest("product", "version", "action_name")
        self.assertEqual(r.get_protocol_type(), 'http')
        r = RpcRequest("product", "version", "action_name", protocol='https')
        self.assertEqual(r.get_protocol_type(), 'https')
        r = RpcRequest("product", "version", "action_name", protocol='http')
        self.assertEqual(r.get_protocol_type(), 'http')

    def test_rpc_request(self):
        r = RpcRequest("product", "version", "action_name")
        # accept format
        self.assertIsNone(r.get_accept_format())
        r.set_accept_format('json')
        self.assertEqual(r.get_accept_format(), "json")
        # action name
        self.assertEqual(r.get_action_name(), "action_name")
        r.set_action_name('new action name')
        self.assertEqual(r.get_action_name(), "new action name")
        # body params
        self.assertDictEqual(r.get_body_params(), {})
        r.set_body_params({'key': 'value'})
        self.assertDictEqual(r.get_body_params(), {'key': 'value'})
        r.add_body_params("key2", "value2")
        self.assertDictEqual(r.get_body_params(), {
            'key': 'value', 'key2': 'value2'})
        # content
        self.assertIsNone(r.get_content())
        r.set_content("content")
        self.assertEqual(r.get_content(), "content")
        # headers
        self.assertDictEqual(r.get_headers(), {'x-sdk-invoke-type': 'normal'})
        r.set_headers({})
        self.assertDictEqual(r.get_headers(), {})
        r.add_header("key", "value")
        self.assertDictEqual(r.get_headers(), {"key": "value"})
        # location endpoint type
        self.assertEqual(r.get_location_endpoint_type(), 'openAPI')
        # no set_location_endpoint_type ??
        # location_service_code
        self.assertEqual(r.get_location_service_code(), None)
        r.set_location_service_code('new service code')
        self.assertEqual(r.get_location_service_code(), 'new service code')
        # method
        self.assertEqual(r.get_method(), 'GET')
        r.set_method('POST')
        self.assertEqual(r.get_method(), 'POST')
        # product
        self.assertEqual(r.get_product(), 'product')
        r.set_product('new-product')
        self.assertEqual(r.get_product(), 'new-product')
        # protocol_type
        self.assertEqual(r.get_protocol_type(), "http")
        r.set_protocol_type('https')
        self.assertEqual(r.get_protocol_type(), "https")
        # query params
        self.assertDictEqual(r.get_query_params(), {})
        r.set_query_params({'key': 'value'})
        self.assertDictEqual(r.get_query_params(), {'key': 'value'})
        r.add_query_param("key2", "value2")
        self.assertDictEqual(r.get_query_params(), {
            'key': 'value', "key2": "value2"})
        # signed_header
        self.assertEqual(r.get_signed_header(), {})
        r.add_header("x-acs-xxx", "value")
        self.assertDictEqual(r.get_signed_header(), {"x-acs-xxx": "value"})
        # style
        self.assertEqual(r.get_style(), "RPC")
        # uri params
        self.assertEqual(r.get_uri_params(), None)
        r.set_uri_params({'user': "jacksontian"})
        self.assertDictEqual(r.get_uri_params(), {'user': 'jacksontian'})
        # uri pattern
        self.assertEqual(r.get_uri_pattern(), None)
        r.set_uri_pattern('/users/:userid')
        self.assertEqual(r.get_uri_pattern(), '/users/:userid')
        # version
        self.assertEqual(r.get_version(), "version")
        r.set_version('2014-10-18')
        self.assertEqual(r.get_version(), "2014-10-18")
        # user-agent
        self.assertEqual(r.get_headers().get('User-Agent'), None)
        r.set_user_agent("user-agent")
        self.assertEqual(r.get_headers().get('User-Agent'), "user-agent")
        # content-type
        self.assertEqual(r.get_headers().get('Content-Type'), None)
        r.set_content_type("application/json")
        self.assertEqual(r.get_headers().get(
            'Content-Type'), "application/json")
        # endpoint
        self.assertEqual(r.endpoint, None)
        r.set_endpoint('endpoint')
        self.assertEqual(r.endpoint, "endpoint")

    @patch("aliyunsdkcore.utils.parameter_helper.get_iso_8061_date")
    @patch("aliyunsdkcore.utils.parameter_helper.get_uuid")
    def test_rpc_request_get_url(self, mock_get_iso_8061_date, mock_get_uuid):
        mock_get_iso_8061_date.return_value = "2018-12-04T04:03:12Z"
        mock_get_uuid.return_value = "7e1c7d12-7551-4856-8abb-1938ccac6bcc"
        # url
        r = RpcRequest("product", "version", "action_name")
        url = r.get_url("regionid", "accesskeyid", "secret")
        mock_get_iso_8061_date.assert_called_once_with()
        mock_get_uuid.assert_called_once_with()
        if sys.version > '3':
            # self.assertEqual(url,
            #                  "/?Version=version&Action=action_name&Format=None&RegionId=regionid"
            #                  "&Timestamp=7e1c7d12-7551-4856-8abb-1938ccac6bcc"
            #                  "&SignatureMethod=HMAC-SHA1&SignatureType=&SignatureVersion=1.0"
            #                  "&SignatureNonce=2018-12-04T04%3A03%3A12Z&AccessKeyId=accesskeyid"
            #                  "&Signature=Ej4GsaOI7FJyN00E5OpDHHCx2vk%3D")
            # with none query params
            r.set_query_params(None)
            url = r.get_url("regionid", "accesskeyid", "secret")
            # self.assertEqual(url,
            #                  "/?Version=version&Action=action_name&Format=None&RegionId=regionid"
            #                  "&Timestamp=7e1c7d12-7551-4856-8abb-1938ccac6bcc"
            #                  "&SignatureMethod=HMAC-SHA1&SignatureType=&SignatureVersion=1.0"
            #                  "&SignatureNonce=2018-12-04T04%3A03%3A12Z&AccessKeyId=accesskeyid"
            #                  "&Signature=Ej4GsaOI7FJyN00E5OpDHHCx2vk%3D")
            # with region id key
            r.set_query_params({'RegionId': 'regionid'})
            url = r.get_url("regionid", "accesskeyid", "secret")
            # self.assertEqual(url,
            #                  "/?RegionId=regionid&Version=version&Action=action_name&Format=None"
            #                  "&Timestamp=7e1c7d12-7551-4856-8abb-1938ccac6bcc"
            #                  "&SignatureMethod=HMAC-SHA1&SignatureType=&SignatureVersion=1.0"
            #                  "&SignatureNonce=2018-12-04T04%3A03%3A12Z&AccessKeyId=accesskeyid"
            #                  "&Signature=Ej4GsaOI7FJyN00E5OpDHHCx2vk%3D")
        else:
            self.assertEqual(url,
                             "/?SignatureVersion=1.0&Format=None"
                             "&Timestamp=7e1c7d12-7551-4856-8abb-1938ccac6bcc&RegionId=regionid"
                             "&AccessKeyId=accesskeyid&SignatureMethod=HMAC-SHA1&Version=version"
                             "&Signature=Ej4GsaOI7FJyN00E5OpDHHCx2vk%3D&Action=action_name"
                             "&SignatureNonce=2018-12-04T04%3A03%3A12Z&SignatureType=")
            # with none query params
            r.set_query_params(None)
            url = r.get_url("regionid", "accesskeyid", "secret")
            self.assertEqual(url,
                             "/?SignatureVersion=1.0&Format=None"
                             "&Timestamp=7e1c7d12-7551-4856-8abb-1938ccac6bcc&RegionId=regionid"
                             "&AccessKeyId=accesskeyid&SignatureMethod=HMAC-SHA1&Version=version"
                             "&Signature=Ej4GsaOI7FJyN00E5OpDHHCx2vk%3D&Action=action_name"
                             "&SignatureNonce=2018-12-04T04%3A03%3A12Z&SignatureType=")
            # with region id key
            r.set_query_params({'RegionId': 'regionid'})
            url = r.get_url("regionid", "accesskeyid", "secret")
            self.assertEqual(url,
                             "/?SignatureVersion=1.0&Format=None"
                             "&Timestamp=7e1c7d12-7551-4856-8abb-1938ccac6bcc""&RegionId=regionid"
                             "&AccessKeyId=accesskeyid&SignatureMethod=HMAC-SHA1&Version=version"
                             "&Signature=Ej4GsaOI7FJyN00E5OpDHHCx2vk%3D&Action=action_name"
                             "&SignatureNonce=2018-12-04T04%3A03%3A12Z&SignatureType=")

    def test_roa_request(self):
        r = RoaRequest("product", "version", "action_name")
        # accept format
        self.assertEqual(r.get_accept_format(), "RAW")
        r.set_accept_format('json')
        self.assertEqual(r.get_accept_format(), "json")
        # action name
        self.assertEqual(r.get_action_name(), "action_name")
        r.set_action_name('new action name')
        self.assertEqual(r.get_action_name(), "new action name")
        # body params
        self.assertDictEqual(r.get_body_params(), {})
        r.set_body_params({'key': 'value'})
        self.assertDictEqual(r.get_body_params(), {'key': 'value'})
        r.add_body_params("key2", "value2")
        self.assertDictEqual(r.get_body_params(), {'key': 'value', 'key2': 'value2'})
        # content
        self.assertIsNone(r.get_content())
        r.set_content("content")
        self.assertEqual(r.get_content(), "content")
        # headers
        self.assertDictEqual(r.get_headers(), {'x-sdk-invoke-type': 'normal'})
        r.set_headers({})
        self.assertDictEqual(r.get_headers(), {})
        r.add_header("key", "value")
        self.assertDictEqual(r.get_headers(), {"key": "value"})
        # location endpoint type
        self.assertEqual(r.get_location_endpoint_type(), 'openAPI')
        # no set_location_endpoint_type ??
        # location_service_code
        self.assertEqual(r.get_location_service_code(), None)
        r.set_location_service_code('new service code')
        self.assertEqual(r.get_location_service_code(), 'new service code')
        # method
        self.assertEqual(r.get_method(), None)
        r.set_method('POST')
        self.assertEqual(r.get_method(), 'POST')
        # product
        self.assertEqual(r.get_product(), 'product')
        r.set_product('new-product')
        self.assertEqual(r.get_product(), 'new-product')
        # protocol_type
        self.assertEqual(r.get_protocol_type(), "http")
        r.set_protocol_type('https')
        self.assertEqual(r.get_protocol_type(), "https")
        # query params
        self.assertDictEqual(r.get_query_params(), {})
        r.set_query_params({'key': 'value'})
        self.assertDictEqual(r.get_query_params(), {'key': 'value'})
        r.add_query_param("key2", "value2")
        self.assertDictEqual(r.get_query_params(), {'key': 'value', "key2": "value2"})
        # signed_header
        # self.assertEqual(r.get_signed_header("region_id", "access_key_id",
        # "access_key_secret"), {})
        # r.add_header("x-acs-xxx", "value")
        # self.assertDictEqual(r.get_signed_header(), {"x-acs-xxx": "value"})
        # style
        self.assertEqual(r.get_style(), "ROA")
        # uri params
        self.assertEqual(r.get_uri_params(), None)
        r.set_uri_params({'user': "jacksontian"})
        self.assertDictEqual(r.get_uri_params(), {'user': 'jacksontian'})
        # uri pattern
        self.assertEqual(r.get_uri_pattern(), None)
        r.set_uri_pattern('/users/:userid')
        self.assertEqual(r.get_uri_pattern(), '/users/:userid')
        # version
        self.assertEqual(r.get_version(), "version")
        r.set_version('2014-10-18')
        self.assertEqual(r.get_version(), "2014-10-18")
        # user-agent
        self.assertEqual(r.get_headers().get('User-Agent'), None)
        r.set_user_agent("user-agent")
        self.assertEqual(r.get_headers().get('User-Agent'), "user-agent")
        # content-type
        self.assertEqual(r.get_headers().get('Content-Type'), None)
        r.set_content_type("application/json")
        self.assertEqual(r.get_headers().get('Content-Type'), "application/json")
        # path_params
        self.assertEqual(r.get_path_params(), None)
        r.add_path_param("userid", "jacksontian")
        r.add_path_param("repo", "snow")
        self.assertEqual(r.get_path_params(), {"userid": "jacksontian", "repo": "snow"})
        r.set_path_params({"userid": "linatian"})
        self.assertEqual(r.get_path_params(), {"userid": "linatian"})

    def test_roa_request_get_url(self):
        r = RoaRequest("product", "version", "action_name")
        r.set_uri_pattern('/users/[user]')
        r.set_path_params({'user': 'jacksontian'})
        url = r.get_url("regionid", "accesskeyid", "secret")
        self.assertEqual(url, "/users/jacksontian")

    @patch("aliyunsdkcore.utils.parameter_helper.get_rfc_2616_date")
    def test_get_signed_header(self, mock_get_rfc_2616_date):
        r = RoaRequest("product", "version", "action_name", headers={})
        r.set_uri_pattern('/users/[user]')
        r.set_path_params({'user': 'jacksontian'})
        r.set_method('GET')
        mock_get_rfc_2616_date.return_value = "2018-12-04T03:25:29Z"
        headers = r.get_signed_header("regionid", "accesskeyid", "secret")
        mock_get_rfc_2616_date.assert_called_once_with()
        self.assertDictEqual(headers, {
            'Accept': 'application/octet-stream',
            'Authorization': 'acs accesskeyid:Lq1u0OzLW/uqLQswxwhne97Umlw=',
            'Date': '2018-12-04T03:25:29Z',
            'x-acs-region-id': 'regionid',
            'x-acs-signature-method': 'HMAC-SHA1',
            'x-acs-signature-version': '1.0',
            'x-acs-version': 'version'
        })

        r.set_query_params(None)
        headers = r.get_signed_header("regionid", "accesskeyid", "secret")
        self.assertDictEqual(headers, {
            'Accept': 'application/octet-stream',
            'Authorization': 'acs accesskeyid:Lq1u0OzLW/uqLQswxwhne97Umlw=',
            'Date': '2018-12-04T03:25:29Z',
            'x-acs-region-id': 'regionid',
            'x-acs-signature-method': 'HMAC-SHA1',
            'x-acs-signature-version': '1.0',
            'x-acs-version': 'version'
        })

        r.set_query_params({'RegionId': 'regionid'})
        headers = r.get_signed_header("regionid", "accesskeyid", "secret")
        self.assertDictEqual(headers, {
            'Accept': 'application/octet-stream',
            'Authorization': 'acs accesskeyid:Lq1u0OzLW/uqLQswxwhne97Umlw=',
            'Date': '2018-12-04T03:25:29Z',
            'x-acs-region-id': 'regionid',
            'x-acs-signature-method': 'HMAC-SHA1',
            'x-acs-signature-version': '1.0',
            'x-acs-version': 'version'
        })

        r.set_content("content")
        headers = r.get_signed_header("regionid", "accesskeyid", "secret")
        self.assertDictEqual(headers, {
            'Accept': 'application/octet-stream',
            'Authorization': 'acs accesskeyid:u2RdkokGTtn2BhUmzUNJjVUh448=',
            'Content-MD5': 'mgNkuembtIDdJeHwKEyFVQ==',
            'Date': '2018-12-04T03:25:29Z',
            'x-acs-region-id': 'regionid',
            'x-acs-signature-method': 'HMAC-SHA1',
            'x-acs-signature-version': '1.0',
            'x-acs-version': 'version'
        })

    def test_common_request(self):
        r = CommonRequest()
        # accept format
        self.assertIsNone(r.get_accept_format())
        r.set_accept_format('json')
        self.assertEqual(r.get_accept_format(), "json")
        # action name
        self.assertEqual(r.get_action_name(), None)
        r.set_action_name('new action name')
        self.assertEqual(r.get_action_name(), "new action name")
        # body params
        self.assertDictEqual(r.get_body_params(), {})
        r.set_body_params({'key': 'value'})
        self.assertDictEqual(r.get_body_params(), {'key': 'value'})
        r.add_body_params("key2", "value2")
        self.assertDictEqual(r.get_body_params(), {'key': 'value', 'key2': 'value2'})
        # content
        self.assertIsNone(r.get_content())
        r.set_content("content")
        self.assertEqual(r.get_content(), "content")
        # headers
        self.assertDictEqual(r.get_headers(), {'x-sdk-invoke-type': 'common'})
        r.set_headers({})
        self.assertDictEqual(r.get_headers(), {})
        r.add_header("key", "value")
        self.assertDictEqual(r.get_headers(), {"key": "value"})
        # location endpoint type
        self.assertEqual(r.get_location_endpoint_type(), 'openAPI')
        # no set_location_endpoint_type ??
        # location_service_code
        self.assertEqual(r.get_location_service_code(), None)
        r.set_location_service_code('new service code')
        self.assertEqual(r.get_location_service_code(), 'new service code')
        # method
        self.assertEqual(r.get_method(), 'GET')
        r.set_method('POST')
        self.assertEqual(r.get_method(), 'POST')
        # product
        self.assertEqual(r.get_product(), None)
        r.set_product('new-product')
        self.assertEqual(r.get_product(), 'new-product')
        # protocol_type
        self.assertEqual(r.get_protocol_type(), "http")
        r.set_protocol_type('https')
        self.assertEqual(r.get_protocol_type(), "https")
        # query params
        self.assertDictEqual(r.get_query_params(), {})
        r.set_query_params({'key': 'value'})
        self.assertDictEqual(r.get_query_params(), {'key': 'value'})
        r.add_query_param("key2", "value2")
        self.assertDictEqual(r.get_query_params(), {'key': 'value', "key2": "value2"})

        # uri params
        self.assertEqual(r.get_uri_params(), None)
        r.set_uri_params({'user': "jacksontian"})
        self.assertDictEqual(r.get_uri_params(), {'user': 'jacksontian'})
        # uri pattern
        self.assertEqual(r.get_uri_pattern(), None)
        r.set_uri_pattern('/users/:userid')
        self.assertEqual(r.get_uri_pattern(), '/users/:userid')
        # url
        # version
        self.assertEqual(r.get_version(), None)
        r.set_version('2014-10-18')
        self.assertEqual(r.get_version(), "2014-10-18")
        # user-agent
        self.assertEqual(r.get_headers().get('User-Agent'), None)
        r.set_user_agent("user-agent")
        self.assertEqual(r.get_headers().get('User-Agent'), "user-agent")
        # content-type
        self.assertEqual(r.get_headers().get('Content-Type'), None)
        r.set_content_type("application/json")
        self.assertEqual(r.get_headers().get('Content-Type'), "application/json")
        # domain
        self.assertEqual(r.get_domain(), None)
        r.set_domain("new-domain")
        self.assertEqual(r.get_domain(), "new-domain")

        # path_params
        self.assertEqual(r.get_path_params(), None)
        r.add_path_param("userid", "jacksontian")
        r.add_path_param("repo", "snow")
        self.assertEqual(r.get_path_params(), {"userid": "jacksontian", "repo": "snow"})
        r.set_path_params({"userid": "linatian"})
        self.assertEqual(r.get_path_params(), {"userid": "linatian"})

    def test_trans_to_acs_request_rpc(self):
        r = CommonRequest()
        # signed_header
        with self.assertRaises(ClientException) as ex:
            r.trans_to_acs_request()
        self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
        self.assertEqual(ex.exception.message,
                         "common params [version] is required, cannot be empty")
        r.set_version("version")
        with self.assertRaises(ClientException) as ex:
            r.trans_to_acs_request()
        self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
        self.assertEqual(ex.exception.message,
                         "At least one of [action] and [uri_pattern] has a value")
        r.set_action_name('action_name')
        with self.assertRaises(ClientException) as ex:
            r.trans_to_acs_request()
        self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
        self.assertEqual(ex.exception.message,
                         "At least one of [domain] and [product_name] has a value")
        r.set_product('product')
        r.trans_to_acs_request()
        self.assertEqual(r.get_style(), "RPC")

    def test_trans_to_acs_request_to_roa(self):
        r = CommonRequest()
        # signed_header
        with self.assertRaises(ClientException) as ex:
            r.trans_to_acs_request()
        self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
        self.assertEqual(ex.exception.message,
                         "common params [version] is required, cannot be empty")
        r.set_version("version")
        with self.assertRaises(ClientException) as ex:
            r.trans_to_acs_request()
        self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
        self.assertEqual(ex.exception.message,
                         "At least one of [action] and [uri_pattern] has a value")
        r.set_uri_pattern("/users/:userid")
        with self.assertRaises(ClientException) as ex:
            r.trans_to_acs_request()
        self.assertEqual(ex.exception.error_code, "SDK.InvalidParams")
        self.assertEqual(ex.exception.message,
                         "At least one of [domain] and [product_name] has a value")
        r.set_product('product')
        r.trans_to_acs_request()
        self.assertEqual(r.get_style(), "ROA")

    def test_common_request_get_url(self):
        r = CommonRequest()
        r.set_version("version")
        r.set_uri_pattern('/users/[userid]')
        r.set_path_params({"userid": "jacksontian"})
        r.set_product('product')
        r.trans_to_acs_request()
        self.assertEqual(r.get_style(), "ROA")
        url = r.get_url("regionid", "accesskeyid", "secret")
        self.assertEqual(url, "/users/jacksontian")

    @patch("aliyunsdkcore.utils.parameter_helper.get_rfc_2616_date")
    def test_common_request_get_signed_header(self, mock_get_rfc_2616_date):
        r = CommonRequest()
        r.set_version("version")
        r.set_uri_pattern('/users/[userid]')
        r.set_path_params({"userid": "jacksontian"})
        r.set_product('product')
        r.trans_to_acs_request()
        self.assertEqual(r.get_url("regionid", "accesskeyid", "secret"), "/users/jacksontian")
        self.assertEqual(r.get_style(), "ROA")
        mock_get_rfc_2616_date.return_value = "2018-12-04T03:25:29Z"
        headers = r.get_signed_header("regionid", "accesskeyid", "secret")
        mock_get_rfc_2616_date.assert_called_once_with()
        self.assertDictEqual(headers, {
            'Accept': 'application/octet-stream',
            'Authorization': 'acs accesskeyid:Lq1u0OzLW/uqLQswxwhne97Umlw=',
            'Date': '2018-12-04T03:25:29Z',
            'x-acs-region-id': 'regionid',
            'x-acs-signature-method': 'HMAC-SHA1',
            'x-acs-signature-version': '1.0',
            'x-acs-version': 'version',
            'x-sdk-invoke-type': 'common'
        })
