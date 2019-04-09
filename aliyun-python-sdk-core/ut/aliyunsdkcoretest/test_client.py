# coding=utf-8

from tests import unittest

from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.client import AcsClient


class TestAcsClient(unittest.TestCase):

    def test_acs_client(self):
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
