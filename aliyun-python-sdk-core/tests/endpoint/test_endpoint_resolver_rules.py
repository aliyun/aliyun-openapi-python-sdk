
from tests import unittest

from aliyunsdkcore.endpoint.endpoint_resolver_rules import EndpointResolverRules
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest


class TestDefaultEndpointResolver(unittest.TestCase):
    def test_resolver(self):
        # clinet = Mock()
        resolver = EndpointResolverRules(None)
        # can not be resolved
        request = ResolveEndpointRequest("foo", "test", "", "")
        endpoint = resolver.resolve(request)
        self.assertEqual(None, endpoint)

    def test_resolver_has_endpoint(self):
        resolver = EndpointResolverRules(None)
        request = ResolveEndpointRequest("foo", "test", "", "")
        endpoint_data = EndpointData()
        resolver.endpoint_map = endpoint_data.endpoint_map
        resolver.endpoint_regional = endpoint_data.endpoint_regional
        endpoint = resolver.resolve(request)
        self.assertEqual("bar", endpoint)

    def test_resolver_reginoal(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        resolver.endpoint_map = endpoint_data.endpoint_map
        resolver.endpoint_regional = endpoint_data.endpoint_regional
        request = ResolveEndpointRequest(
            "cn-hangzhou", "test", "", "")
        endpoint = resolver.resolve(request)
        self.assertEqual("test.cn-hangzhou.aliyuncs.com", endpoint)

    def test_resolver_central(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        endpoint_data.endpoint_regional = "central"
        resolver.endpoint_map = endpoint_data.endpoint_map
        resolver.endpoint_regional = endpoint_data.endpoint_regional
        request = ResolveEndpointRequest(
            "cn-hangzhou", "test", "", "")
        endpoint = resolver.resolve(request)
        self.assertEqual("test.aliyuncs.com", endpoint)

    def test_resolver_network(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        resolver.endpoint_map = endpoint_data.endpoint_map
        resolver.endpoint_regional = endpoint_data.endpoint_regional
        request = ResolveEndpointRequest(
            "cn-hangzhou", "test", "", "")
        request.request_network = "vpc"
        endpoint = resolver.resolve(request)
        self.assertEqual("test-vpc.cn-hangzhou.aliyuncs.com", endpoint)

    def test_resolver_network_special_endpoint(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        resolver.endpoint_map = endpoint_data.endpoint_map
        resolver.endpoint_regional = endpoint_data.endpoint_regional
        request = ResolveEndpointRequest(
            "foo", "test", "", "")
        request.request_network = "vpc"
        endpoint = resolver.resolve(request)
        self.assertEqual("test-vpc.foo.aliyuncs.com", endpoint)


class EndpointData():
    def __init__(self):
        self.endpoint_map = {
            "foo": "bar",
        }
        self.endpoint_regional = "regional"

