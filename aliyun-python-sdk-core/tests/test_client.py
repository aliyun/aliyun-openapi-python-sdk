# coding=utf-8

from tests import unittest, MyServer

from aliyunsdkcore.request import RpcRequest
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
