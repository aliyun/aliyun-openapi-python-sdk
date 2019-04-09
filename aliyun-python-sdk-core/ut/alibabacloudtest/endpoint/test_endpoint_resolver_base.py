
from tests import unittest

from aliyunsdkcore.endpoint.user_customized_endpoint_resolver import UserCustomizedEndpointResolver
from aliyunsdkcore.endpoint.endpoint_resolver_base import EndpointResolverBase
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from aliyunsdkcore.acs_exception.exceptions import ClientException


class TestEndpointResolverBase(unittest.TestCase):
    def test_resolver(self):
        resolver = EndpointResolverBase()
        with self.assertRaises(NotImplementedError):
            resolver.is_region_id_valid(None)
        with self.assertRaises(NotImplementedError):
            resolver.get_endpoint_key_from_request(None)

