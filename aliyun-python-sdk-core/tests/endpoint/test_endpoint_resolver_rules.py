
from tests import unittest

from aliyunsdkcore.endpoint.endpoint_resolver_rules import EndpointResolverRules
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest


class TestDefaultEndpointResolver(unittest.TestCase):
    def test_resolver(self):
        # clinet = Mock()
        resolver = EndpointResolverRules(None)
        # can not be resolved
        request = ResolveEndpointRequest("region_id", "product_code", "", "")
        endpoint = resolver.resolve(request)
        self.assertEqual(None, endpoint)

    def test_resolver_has_endpoint(self):
        resolver = EndpointResolverRules(None)
        request = ResolveEndpointRequest("cn-hangzhou", "product_code", "", "")
        endpoint_data = EndpointData()
        request.endpoint_map = endpoint_data.endpoint_map
        request.endpoint_regional = endpoint_data.endpoint_regional
        endpoint = resolver.resolve(request)
        self.assertEqual("mock.endpoint", endpoint)

    def test_resolver_reginoal(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        request = ResolveEndpointRequest(
            "cn-beijing", "test", "", "")
        request.endpoint_map = endpoint_data.endpoint_map
        request.endpoint_regional = endpoint_data.endpoint_regional
        endpoint = resolver.resolve(request)
        self.assertEqual("test.cn-beijing.aliyuncs.com", endpoint)

    def test_resolver_central(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        endpoint_data.endpoint_regional = "central"
        request = ResolveEndpointRequest(
            "cn-beijing", "test", "", "")
        request.endpoint_map = endpoint_data.endpoint_map
        request.endpoint_regional = endpoint_data.endpoint_regional
        endpoint = resolver.resolve(request)
        self.assertEqual("test.aliyuncs.com", endpoint)

    def test_resolver_network(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        request = ResolveEndpointRequest(
            "cn-beijing", "test", "", "")
        request.endpoint_map = endpoint_data.endpoint_map
        request.endpoint_regional = endpoint_data.endpoint_regional
        request.request_network = "vpc"
        endpoint = resolver.resolve(request)
        self.assertEqual("test-vpc.cn-beijing.aliyuncs.com", endpoint)

    def test_resolver_network_special_endpoint(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        request = ResolveEndpointRequest(
            "foo", "test", "", "")
        request.endpoint_map = endpoint_data.endpoint_map
        request.endpoint_regional = endpoint_data.endpoint_regional
        request.request_network = "vpc"
        endpoint = resolver.resolve(request)
        self.assertEqual("test-vpc.foo.aliyuncs.com", endpoint)


class EndpointData():
    def __init__(self):
        self.endpoint_map = {
            "cn-hangzhou": "mock.endpoint",
        }
        self.endpoint_regional = "regional"
