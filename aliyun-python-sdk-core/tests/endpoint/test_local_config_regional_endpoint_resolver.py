# coding=utf-8

from tests import unittest

from aliyunsdkcore.endpoint.local_config_regional_endpoint_resolver \
    import LocalConfigRegionalEndpointResolver
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest


class TestLocalConfigRegionalEndpointResolver(unittest.TestCase):
    def test_resolver(self):
        resolver = LocalConfigRegionalEndpointResolver()
        request = ResolveEndpointRequest("", "", "", "")
        self.assertEqual(resolver.resolve(request), None)
        self.assertEqual(resolver._make_endpoint_entry_key(
            "ecs", "cn-huhehaote"), "ecs.cn-huhehaote")
        request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "")
        self.assertEqual(resolver.resolve(request),
                         'ecs.cn-huhehaote.aliyuncs.com')
        self.assertTrue(resolver.is_region_id_valid(request))
        # resolver.put_endpoint_entry("ecs", "my-endpoint-for-cnhuhehaote-ecs")
        # request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "")
        # self.assertEqual(resolver.resolve(request), "my-endpoint-for-cnhuhehaote-ecs")
        # self.assertTrue(resolver.is_region_id_valid(request))
        request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "innerAPI")
        self.assertEqual(resolver.resolve(request), None)
        # _get_normalized_product_code
        self.assertEqual(resolver._get_normalized_product_code(
            "cloudapi"), "apigateway")
        self.assertEqual(resolver._get_normalized_product_code("ecs"), "ecs")
        self.assertEqual(len(resolver.get_valid_region_ids_by_product('ecs')), 19)
        self.assertIsNone(resolver.get_valid_region_ids_by_product('xxx'))
        self.assertTrue(resolver.is_product_code_valid(request))

    def test_resolver_with_jsonstr(self):
        resolver = LocalConfigRegionalEndpointResolver("{}")
        request = ResolveEndpointRequest("", "", "", "")
        self.assertEqual(resolver.resolve(request), None)
        self.assertEqual(resolver._make_endpoint_entry_key(
            "ecs", "cn-huhehaote"), "ecs.cn-huhehaote")
        request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "")
        self.assertEqual(resolver.resolve(request), None)
        self.assertFalse(resolver.is_region_id_valid(request))
        resolver.put_endpoint_entry(
            "ecs.cn-huhehaote", "my-endpoint-for-cnhuhehaote-ecs")
        request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "")
        self.assertEqual(resolver.resolve(request),
                         "my-endpoint-for-cnhuhehaote-ecs")
        self.assertFalse(resolver.is_region_id_valid(request))
        request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "innerAPI")
        self.assertEqual(resolver.resolve(request), None)
        # _get_normalized_product_code
        self.assertEqual(resolver._get_normalized_product_code(
            "cloudapi"), "cloudapi")
        self.assertEqual(resolver._get_normalized_product_code("ecs"), "ecs")
