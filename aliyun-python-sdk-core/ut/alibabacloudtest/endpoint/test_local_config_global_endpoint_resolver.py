# coding=utf-8

from tests import unittest

from aliyunsdkcore.endpoint.local_config_global_endpoint_resolver \
    import LocalConfigGlobalEndpointResolver
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest


class TestLocalConfigGlobalEndpointResolver(unittest.TestCase):
    def test_resolver(self):
        resolver = LocalConfigGlobalEndpointResolver()
        request = ResolveEndpointRequest("", "", "", "")
        self.assertEqual(resolver.resolve(request), None)
        self.assertEqual(resolver._make_endpoint_entry_key("ram"), "ram")
        request = ResolveEndpointRequest("cn-huhehaote", "ram", "", "")
        self.assertEqual(resolver.resolve(request), 'ram.aliyuncs.com')
        self.assertTrue(resolver.is_region_id_valid(request))
        request = ResolveEndpointRequest("cn-huhehaote", "ram", "", "innerAPI")
        self.assertEqual(resolver.resolve(request), None)
        # _get_normalized_product_code
        self.assertEqual(resolver._get_normalized_product_code(
            "cloudapi"), "apigateway")
        self.assertEqual(resolver._get_normalized_product_code("ram"), "ram")

    def test_resolver_with_jsonstr(self):
        resolver = LocalConfigGlobalEndpointResolver("{}")
        request = ResolveEndpointRequest("", "", "", "")
        self.assertEqual(resolver.resolve(request), None)
        self.assertEqual(resolver._make_endpoint_entry_key("ram"), "ram")
        request = ResolveEndpointRequest("cn-huhehaote", "ram", "", "")
        self.assertEqual(resolver.resolve(request), None)
        self.assertFalse(resolver.is_region_id_valid(request))
        request = ResolveEndpointRequest("cn-huhehaote", "ram", "", "innerAPI")
        self.assertEqual(resolver.resolve(request), None)
