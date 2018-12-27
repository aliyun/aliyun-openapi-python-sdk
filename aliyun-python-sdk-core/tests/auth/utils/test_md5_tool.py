# coding=utf-8

import unittest

from aliyunsdkcore.auth.utils import md5_tool


class TestMd5Tool(unittest.TestCase):
    def test_md5_tool(self):
        self.assertEqual("ERIHLmRX2uZmssDdxQnnxQ==",
                         md5_tool.get_md5_base64_str("That's all folks!!"))
        self.assertEqual("GsJRdI3kAbAnHo/0+3wWJw==",
                         md5_tool.get_md5_base64_str("中文也没啥问题"))
