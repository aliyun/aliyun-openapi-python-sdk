# coding=utf-8

from tests import unittest
from aliyunsdkcore.vendored.six import PY2

from alibabacloud.utils import parameter_helper as helper


class TestShaHmac1(unittest.TestCase):
    def test_get_uuid(self):
        uuid = helper.get_uuid()
        self.assertEqual(36, len(uuid))
        self.assertNotEqual(helper.get_uuid(), helper.get_uuid())

    def test_md5_sum(self):
        self.assertEqual("ERIHLmRX2uZmssDdxQnnxQ==",
                         helper.md5_sum("That's all folks!!"))
        self.assertEqual("GsJRdI3kAbAnHo/0+3wWJw==",
                         helper.md5_sum("中文也没啥问题"))

    def test_get_iso_8061_date(self):
        s = helper.get_iso_8061_date()
        self.assertEqual(20, len(s))
        # from 3.1 assertRegexpMatches rename assertRegex
        if PY2:
            self.assertRegexpMatches(
                s, '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$')
        else:
            self.assertRegex(
                s, '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$')

    def test_get_rfc_2616_date(self):
        s = helper.get_rfc_2616_date()
        self.assertEqual(29, len(s))
        # from 3.1 assertRegexpMatches rename assertRegex
        if PY2:
            self.assertRegexpMatches(
                s,
                '^[A-Z][a-z]{2}, [0-9]{2} [A-Z][a-z]{2} [0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2} GMT$')
        else:
            self.assertRegex(
                s,
                '^[A-Z][a-z]{2}, [0-9]{2} [A-Z][a-z]{2} [0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2} GMT$')
