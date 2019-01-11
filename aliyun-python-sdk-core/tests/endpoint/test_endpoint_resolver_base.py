
from tests import unittest

from aliyunsdkcore.endpoint.user_customized_endpoint_resolver import UserCustomizedEndpointResolver
from aliyunsdkcore.endpoint.endpoint_resolver_base import EndpointResolverBase
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from aliyunsdkcore.acs_exception.exceptions import ClientException


class TestEndpointResolverBase(unittest.TestCase):
    def test_resolver(self):
        with self.assertRaises(TypeError):
            resolver = EndpointResolverBase()

