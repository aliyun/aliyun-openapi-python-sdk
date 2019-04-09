
from tests import unittest

from mock import MagicMock, patch, Mock

from aliyunsdkcore.endpoint.default_endpoint_resolver import DefaultEndpointResolver
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from aliyunsdkcore.acs_exception.exceptions import ClientException


class TestDefaultEndpointResolver(unittest.TestCase):
    def test_resolver(self):
        # clinet = Mock()
        resolver = DefaultEndpointResolver(None)
        # can not be resolved
        request = ResolveEndpointRequest("mars", "ecs", "", "")
        with self.assertRaises(ClientException) as ex:
            resolver.resolve(request)
        self.assertEqual(ex.exception.error_code, "SDK.EndpointResolvingError")
        self.assertEqual(ex.exception.message,
                         "No such region 'mars'. Please check your region ID.")
        resolver.put_endpoint_entry("mars", "ecs", "mars-endpoint-for-ecs")
        self.assertEqual(resolver.resolve(request), "mars-endpoint-for-ecs")
