# coding=utf-8

from tests import unittest

from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest


class TestResolveEndpointRequest(unittest.TestCase):
    def test_request(self):
        r = ResolveEndpointRequest(
            "cn-hangzhou", "product_code", "location_service_code", "innerAPI")
        self.assertFalse(r.is_open_api_endpoint())
        r = ResolveEndpointRequest(
            "cn-hangzhou", "product_code", "location_service_code", "openAPI")
        self.assertTrue(r.is_open_api_endpoint())
        r = ResolveEndpointRequest(
            "cn-hangzhou", "product_code", "location_service_code", None)
        self.assertTrue(r.is_open_api_endpoint())
