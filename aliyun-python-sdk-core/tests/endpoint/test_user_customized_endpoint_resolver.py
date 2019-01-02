# coding=utf-8

from tests import unittest

from aliyunsdkcore.endpoint.user_customized_endpoint_resolver import UserCustomizedEndpointResolver
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest


class TestUserCustomizedEndpointResolver(unittest.TestCase):
    def test_resolver(self):
        resolver = UserCustomizedEndpointResolver()
        request = ResolveEndpointRequest("", "", "", "")
        self.assertEqual(resolver.resolve(request), None)
        self.assertEqual(resolver._make_endpoint_entry_key(
            "ecs", "cn-huhehaote"), "ecs.cn-huhehaote")
        request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "")
        self.assertEqual(resolver.resolve(request), None)
        self.assertFalse(resolver.is_region_id_valid(request))
        resolver.put_endpoint_entry(
            "cn-huhehaote", "ecs", "my-endpoint-for-cnhuhehaote-ecs")
        request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "")
        self.assertEqual(resolver.resolve(request),
                         "my-endpoint-for-cnhuhehaote-ecs")
        self.assertTrue(resolver.is_region_id_valid(request))
        resolver.reset()
        self.assertEqual(resolver.resolve(request), None)
