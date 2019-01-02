
from tests import unittest

from aliyunsdkcore.endpoint.user_customized_endpoint_resolver import UserCustomizedEndpointResolver
from aliyunsdkcore.endpoint.chained_endpoint_resolver import ChainedEndpointResolver
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from aliyunsdkcore.acs_exception.exceptions import ClientException


class TestChainedEndpointResolver(unittest.TestCase):
    def test_resolver(self):
        user = UserCustomizedEndpointResolver()
        chain = [
            user
        ]
        resolver = ChainedEndpointResolver(chain)
        # can not be resolved
        request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "")
        with self.assertRaises(ClientException) as ex:
            resolver.resolve(request)
        self.assertEqual(ex.exception.error_code, "SDK.EndpointResolvingError")
        self.assertEqual(ex.exception.message,
                         "No endpoint for product 'ecs'.\n"
                         "Please check the product code, or set an endpoint for your request "
                         "explicitly.\n"
                         "See https://www.alibabacloud.com/help/doc-detail/92074.htm\n")

        user.put_endpoint_entry("cn-huhehaote", "ecs",
                                "my-endpoint-for-cnhuhehaote-ecs")
        # can not be resolved with cn-hangzhou
        request = ResolveEndpointRequest("cn-hangzhou", "ecs", "", "")
        with self.assertRaises(ClientException) as ex:
            resolver.resolve(request)
        self.assertEqual(ex.exception.error_code, "SDK.EndpointResolvingError")
        self.assertEqual(
            ex.exception.message, "No such region 'cn-hangzhou'. Please check your region ID.")
        # cn-hangzhou and ecs is valid
        user.put_endpoint_entry("cn-hangzhou", "rds",
                                "my-endpoint-for-cn-hangzhou-rds")
        with self.assertRaises(ClientException) as ex:
            resolver.resolve(request)
        self.assertEqual(ex.exception.error_code, "SDK.EndpointResolvingError")
        self.assertEqual(
            ex.exception.message, "No endpoint in the region 'cn-hangzhou' for product 'ecs'.\n"
            "You can set an endpoint for your request explicitly.\n"
            "See https://www.alibabacloud.com/help/doc-detail/92074.htm\n")
        # can be resolved
        request = ResolveEndpointRequest("cn-huhehaote", "ecs", "", "")
        self.assertEqual(resolver.resolve(request),
                         "my-endpoint-for-cnhuhehaote-ecs")
