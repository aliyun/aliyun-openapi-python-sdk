# coding=utf-8
import sys

from tests import unittest, MyServer

from aliyunsdkcore.request import RpcRequest, RoaRequest, CommonRequest
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.client import AcsClient


class TestAcsClient(unittest.TestCase):

    @staticmethod
    def do_request(client, request):
        with MyServer() as s:
            client.do_action_with_exception(request)
            return s.content

    def test_acs_client(self):
        with self.assertRaises(ClientException) as ex:
            AcsClient()
        self.assertEqual(ex.exception.error_code, "SDK.InvalidCredential")
        self.assertEqual(
            ex.exception.message,
            "Need a ak&secret pair or public_key_id&private_key pair to auth.")
        client = AcsClient(ak="access_key_id", secret="access_key_secret")
        self.assertEqual(client.get_access_key(), "access_key_id")
        self.assertEqual(client.get_access_secret(), "access_key_secret")
        # region id
        self.assertEqual(client.get_region_id(), "cn-hangzhou")
        client.set_region_id('cn-shanghai')
        self.assertEqual(client.get_region_id(), "cn-shanghai")
        # auto retry
        self.assertTrue(client.is_auto_retry())
        client.set_auto_retry(False)
        self.assertFalse(client.is_auto_retry())
        # max retry num
        self.assertEqual(client.get_max_retry_num(), None)
        client.set_max_retry_num(10)
        self.assertEqual(client.get_max_retry_num(), 10)
        # user agent
        self.assertEqual(client.get_user_agent(), None)
        client.set_user_agent('new-user-agent')
        self.assertEqual(client.get_user_agent(), "new-user-agent")
        # port
        self.assertEqual(client.get_port(), 80)
        self.assertIsNone(client.get_location_service())

    def test_parse_error_info_from_response_body(self):
        code, body = AcsClient._parse_error_info_from_response_body("{}")
        self.assertEqual(code, "SDK.UnknownServerError")
        self.assertEqual(body, "ServerResponseBody: {}")
        code, body = AcsClient._parse_error_info_from_response_body(
            '{"Code":"code", "Message":"message"}')
        self.assertEqual(code, "code")
        self.assertEqual(body, "message")
        code, body = AcsClient._parse_error_info_from_response_body(
            'invalid json')
        self.assertEqual(code, "SDK.UnknownServerError")
        self.assertEqual(body, "ServerResponseBody: invalid json")

    def test_resolve_endpoint(self):
        client = AcsClient("id", "aks", region_id='', port=51352)
        req = RpcRequest(
            'sts',
            '2020',
            'test'
        )
        req.endpoint = 'localhost'
        req.request_network = ''
        req.product_suffix = ''
        self.do_request(client, req)

        try:
            client._resolve_endpoint(req)
        except Exception as e:
            self.assertEqual("No such region ''. Please check your region ID.", e.message)

        client.set_region_id('cn@hangzhou')
        try:
            client._resolve_endpoint(req)
        except Exception as e:
            self.assertEqual('The parameter region_id not match with ^[a-zA-Z0-9_-]+$', e.message)

    def test_json_content_type(self):
        client = AcsClient("id", "aks", region_id='cn-hangzhou', port=51352)
        request = RpcRequest(
            'sts',
            '2020',
            'test'
        )
        request.endpoint = 'localhost'
        request.set_method('POST')
        request.set_content_type('application/json')
        request.add_body_params('key', 'value')
        response = self.do_request(client, request)
        if sys.version_info.major == 2:
            headers = {
                item.split(':')[0]: item.split(':')[1]
                for item in response.headers.headers
            }
        else:
            headers = dict(response.headers._headers)
        self.assertEqual('application/json', headers['Content-Type'].strip('\r\n '))

    def test_xml_content_type(self):
        client = AcsClient("id", "aks", region_id='cn-hangzhou', port=51352)
        request = RpcRequest(
            'sts',
            '2020',
            'test'
        )
        request.endpoint = 'localhost'
        request.set_method('POST')
        request.add_body_params('key', 'value')
        request.set_content_type('application/xml')
        response = self.do_request(client, request)
        if sys.version_info.major == 2:
            headers = {
                item.split(':')[0]: item.split(':')[1]
                for item in response.headers.headers
            }
        else:
            headers = dict(response.headers._headers)
        self.assertEqual('application/xml', headers['Content-Type'].strip('\r\n '))

    def test_http_proxy(self):
        client = AcsClient(
            "id",
            "aks",
            region_id='cn-hangzhou',
            proxy={'http': 'http://127.0.0.1:8080'}
        )
        request = RpcRequest(
            'sts',
            '2020',
            'test'
        )
        try:
            client.do_action_with_exception(request)
        except ClientException as e:
            self.assertEqual(e.get_error_code(), 'SDK.HttpError')
            self.assertIn('Cannot connect to proxy', e.message)

    def test_http_header(self):
        client = AcsClient("id", "aks", region_id='cn-hangzhou', port=51352)
        rpc_request = RpcRequest(
            product='sts',
            version='2020',
            action_name='test'
        )
        rpc_request.endpoint = 'localhost'
        rpc_request.request_network = ''
        rpc_request.product_suffix = ''
        rpc_request.add_header('key', 'value')
        rpc_request.add_header('x-sdk-client', 'python/5.0.0')
        response = self.do_request(client, rpc_request)
        self.assertEqual(response.headers['key'], 'value')
        self.assertEqual(response.headers['x-sdk-client'], 'python/2.0.0')

        roa_request = RoaRequest(
            product='sts',
            version='2020',
            action_name='test',
            method='GET',
            uri_pattern='/test'
        )
        roa_request.endpoint = 'localhost'
        roa_request.request_network = ''
        roa_request.product_suffix = ''
        roa_request.add_header('key', 'value')
        roa_request.add_header('x-acs-region-id', 'test')
        roa_request.add_header('x-acs-version', 'test')
        roa_request.add_header('Authorization', 'test')
        response = self.do_request(client, roa_request)
        self.assertEqual(response.headers['key'], 'value')
        self.assertEqual(response.headers['x-sdk-client'], 'python/2.0.0')
        self.assertEqual(response.headers['x-acs-region-id'], 'cn-hangzhou')
        self.assertEqual(response.headers['x-acs-version'], '2020')
        self.assertNotEqual(response.headers['Authorization'], 'test')

        rpc_request = CommonRequest(
            product='sts',
            version='2020',
            action_name='test'
        )
        rpc_request.endpoint = 'localhost'
        rpc_request.request_network = ''
        rpc_request.product_suffix = ''
        rpc_request.add_header('key', 'value')
        response = self.do_request(client, rpc_request)
        self.assertEqual(response.headers['key'], 'value')
