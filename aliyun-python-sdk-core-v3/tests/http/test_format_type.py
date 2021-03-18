# coding=utf-8

from tests import unittest

from aliyunsdkcore.http.format_type import map_format_to_accept, map_accept_to_format


class TestFormatType(unittest.TestCase):

    def test_map_format_to_accept(self):
        self.assertEqual(map_format_to_accept("XML"), "application/xml")
        self.assertEqual(map_format_to_accept("JSON"), "application/json")
        self.assertEqual(map_format_to_accept(
            "OTHERE"), "application/octet-stream")

    def test_map_accept_to_format(self):
        self.assertEqual(map_accept_to_format("application/xml"), "XML")
        self.assertEqual(map_accept_to_format("text/xml"), "XML")
        self.assertEqual(map_accept_to_format("application/json"), "JSON")
        self.assertEqual(map_accept_to_format("text/html"), "RAW")
