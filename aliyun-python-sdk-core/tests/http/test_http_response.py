# coding=utf-8
import os
import sys

from tests import unittest, MyServer

from aliyunsdkcore.http.http_response import HttpResponse
from aliyunsdkcore.http.protocol_type import HTTPS


from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


class TestHttpResponse(unittest.TestCase):

    def test_http_request(self):
        res = HttpResponse()
        self.assertFalse(res.get_ssl_enabled())
        res.set_ssl_enable(True)
        self.assertTrue(res.get_ssl_enabled())
        res = HttpResponse(protocol=HTTPS)
        self.assertTrue(res.get_ssl_enabled())

    @staticmethod
    def do_request(client, request):
        with MyServer() as s:
            client.do_action_with_exception(request)
            return s.content

    @staticmethod
    def init_client():
        return AcsClient("access_key_id", "access_key_secret",
                         timeout=120, port=51352)

    def test_http_debug(self):
        os.environ.setdefault('DEBUG', 'SDK')

        http_debug = os.environ.get('DEBUG')
        if http_debug is not None and http_debug.lower() == 'sdk':
            request = CommonRequest(
                domain="ecs.aliyuncs.com",
                version="2014-05-26",
                action_name="DescribeRegions")
            request.set_endpoint("localhost")
            make_request = HttpResponse(request.endpoint, '/')
            request.headers = {'User-Agent': 'ALIBABACloud'}

            content = make_request.prepare_http_debug(request, '>')
            self.assertTrue('User-Agent' in content)

            client = self.init_client()
            response = self.do_request(client, request)
            if sys.version_info[0] == 3:
                response = make_request.prepare_http_debug(response, '<')
                self.assertTrue('User-Agent' in response)

        os.environ.pop('DEBUG', None)
