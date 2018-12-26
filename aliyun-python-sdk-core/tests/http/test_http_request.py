# coding=utf-8

from tests import unittest

from aliyunsdkcore.http.http_request import HttpRequest


class TestHTTPRequest(unittest.TestCase):

    def test_http_request(self):
        req = HttpRequest("host")
        # body
        self.assertEqual(req.get_body(), None)
        req.set_body("body")
        self.assertEqual(req.get_body(), "body")
        # content
        self.assertEqual(req.get_content(), None)
        # req.set_content(None, "utf8", "raw")
        # self.assertEqual(req.get_content(), None)
        req.set_content("content", "utf8", "raw")
        self.assertEqual(req.get_content(), "content")
        self.assertEqual(len(req.get_headers()), 3, "has 3 keys")
        req.set_content(None, "utf8", "raw")
        self.assertEqual(req.get_content(), None)
        self.assertEqual(len(req.get_headers()), 0, "has 3 keys")

        # content type
        self.assertEqual(req.get_content_type(), None)
        req.set_content_type("json")
        self.assertEqual(req.get_content_type(), "json")

        # encoding
        self.assertEqual(req.get_encoding(), None)
        req.set_encoding("utf8")
        self.assertEqual(req.get_encoding(), "utf8")

        # headers
        self.assertEqual(len(req.get_headers()), 0, "has 0 keys")
        # self.assertEqual(req.get_header_value(req.content_type), None)
        req.put_header_parameter("key", "value")
        self.assertEqual(len(req.get_headers()), 1, "has 1 keys")
        self.assertEqual(req.get_header_value("key"), "value")
        req.put_header_parameter(None, None)
        self.assertEqual(len(req.get_headers()), 1, "has 1 keys")
        req.remove_header_parameter(None)
        self.assertEqual(len(req.get_headers()), 1, "has 1 keys")
        req.remove_header_parameter("inexist_key")
        self.assertEqual(len(req.get_headers()), 1, "has 1 keys")

        # method
        self.assertEqual(req.get_method(), None)
        req.set_method("POST")
        self.assertEqual(req.get_method(), "POST")

        # host
        self.assertEqual(req.get_host(), 'host')
        req.set_host("newhost")
        self.assertEqual(req.get_host(), "newhost")

        # url
        self.assertEqual(req.get_url(), '/')
        req.set_url("/url")
        self.assertEqual(req.get_url(), "/url")
