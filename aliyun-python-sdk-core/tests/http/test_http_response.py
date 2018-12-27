# coding=utf-8

from tests import unittest

from aliyunsdkcore.http.http_response import HttpResponse
from aliyunsdkcore.http.protocol_type import HTTPS


class TestHttpResponse(unittest.TestCase):

    def test_http_request(self):
        res = HttpResponse()
        self.assertFalse(res.get_ssl_enabled())
        res.set_ssl_enable(True)
        self.assertTrue(res.get_ssl_enabled())
        res = HttpResponse(protocol=HTTPS)
        self.assertTrue(res.get_ssl_enabled())
