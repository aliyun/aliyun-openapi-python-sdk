# coding=utf-8

from tests import unittest

from aliyunsdkcore.endpoint.location.DescribeEndpointsRequest \
    import DescribeEndpointsRequest


class TestDescribeEndpointsRequest(unittest.TestCase):
    def test_request(self):
        r = DescribeEndpointsRequest()
        self.assertEqual(r.get_ServiceCode(), None)
        r.set_ServiceCode("servicecode")
        self.assertEqual(r.get_ServiceCode(), 'servicecode')
        self.assertEqual(r.get_Id(), None)
        r.set_Id("id")
        self.assertEqual(r.get_Id(), 'id')
        self.assertEqual(r.get_Type(), None)
        r.set_Type("type")
        self.assertEqual(r.get_Type(), 'type')
