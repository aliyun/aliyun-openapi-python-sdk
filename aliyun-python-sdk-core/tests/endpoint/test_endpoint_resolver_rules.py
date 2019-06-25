
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
        resolver.set_endpoint_data(
            endpoint_data.getEndpointMap(), endpoint_data.getEndpointRegional())
        endpoint = resolver.resolve(request)
        self.assertEqual("bar", endpoint)

    def test_resolver_reginoal(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        resolver.set_endpoint_data(
            endpoint_data.getEndpointMap(), endpoint_data.getEndpointRegional())
        request = ResolveEndpointRequest(
            "cn-hangzhou", "test", "", "")
        endpoint = resolver.resolve(request)
        self.assertEqual("test.cn-hangzhou.aliyuncs.com", endpoint)

    def test_resolver_central(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        endpoint_data.endpoint_regional = "central"
        resolver.set_endpoint_data(
            endpoint_data.getEndpointMap(), endpoint_data.getEndpointRegional())
        request = ResolveEndpointRequest(
            "cn-hangzhou", "test", "", "")
        endpoint = resolver.resolve(request)
        self.assertEqual("test.aliyuncs.com", endpoint)

    def test_resolver_network(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        resolver.set_endpoint_data(
            endpoint_data.getEndpointMap(), endpoint_data.getEndpointRegional())
        request = ResolveEndpointRequest(
            "cn-hangzhou", "test", "", "")
        request.set_request_network("vpc")
        endpoint = resolver.resolve(request)
        self.assertEqual("test-vpc.cn-hangzhou.aliyuncs.com", endpoint)


class EndpointData():
    def __init__(self):
        self.endpoint_map = {
            "foo": "bar",
        }
        self.endpoint_regional = "regional"

    def getEndpointMap(self):
        return self.endpoint_map

    def getEndpointRegional(self):
        return self.endpoint_regional
