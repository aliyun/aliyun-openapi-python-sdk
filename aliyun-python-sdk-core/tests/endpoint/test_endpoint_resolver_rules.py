
from tests import unittest

from aliyunsdkcore.endpoint.endpoint_resolver_rules import EndpointResolverRules
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest


class TestDefaultEndpointResolver(unittest.TestCase):
    def test_resolver(self):
        # clinet = Mock()
        resolver = EndpointResolverRules(None)
        # can not be resolved
        request = ResolveEndpointRequest("foo", "test", "", "", "public")
        endpoint = resolver.resolve(request)
        self.assertEqual(None, endpoint)

    def test_resolver_has_endpoint(self):
        resolver = EndpointResolverRules(None)
        request = ResolveEndpointRequest("foo", "test", "", "", "public")
        endpoint_data = EndpointData()
        resolver.set_endpoint_data(endpoint_data)
        endpoint = resolver.resolve(request)
        self.assertEqual("bar", endpoint)

    def test_resolver_reginoal(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        resolver.set_endpoint_data(endpoint_data)
        request = ResolveEndpointRequest(
            "cn-hangzhou", "test", "", "", "public")
        endpoint = resolver.resolve(request)
        self.assertEqual("test.cn-hangzhou.aliyuncs.com", endpoint)

    def test_resolver_central(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        endpoint_data.endpoint_regional = "central"
        resolver.set_endpoint_data(endpoint_data)
        request = ResolveEndpointRequest(
            "cn-hangzhou", "test", "", "", "public")
        endpoint = resolver.resolve(request)
        self.assertEqual("test.aliyuncs.com", endpoint)

    def test_resolver_network(self):
        resolver = EndpointResolverRules(None)
        endpoint_data = EndpointData()
        resolver.set_endpoint_data(endpoint_data)
        request = ResolveEndpointRequest(
            "cn-hangzhou", "test", "", "", "vpc")
        endpoint = resolver.resolve(request)
        self.assertEqual("test-vpc.cn-hangzhou.aliyuncs.com", endpoint)


class EndpointData():
    def __init__(self):
        self.endpoint_map = None
        self.endpoint_regional = None
        self.iniEndpointData()

    def getEndpointMap(self):
        return self.endpoint_map

    def getEndpointRegional(self):
        return self.endpoint_regional

    def iniEndpointData(self):
        self.endpoint_map = {
            "foo": "bar",
        }
        self.endpoint_regional = "regional"

    def getEndpoint(self, region_id, network=None):
        if(network is None or network == ""):
            network = "public"

        endpoint_map = self.getEndpointMap()
        endpoint_regional = self.getEndpointRegional()
        endpoint = ""
        for key in endpoint_map:
            if (key == region_id):
                endpoint = endpoint_map[key]
                break

        if endpoint == "":
            if endpoint_regional == "regional":
                endpoint = "test<network>.<region_id>.aliyuncs.com"
            else:
                endpoint = "test<network>.aliyuncs.com"
            if network != "public":
                endpoint = endpoint.replace("<network>", "-"+network)
            else:
                endpoint = endpoint.replace("<network>", "")
            endpoint = endpoint.replace("<region_id>", region_id.lower())

        return endpoint
