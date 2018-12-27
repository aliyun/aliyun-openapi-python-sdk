# coding=utf-8

from tests import unittest

from mock import MagicMock, patch, Mock

from aliyunsdkcore.endpoint.location_service_endpoint_resolver \
    import LocationServiceEndpointResolver
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest

from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.compat import ensure_bytes


class TestLocationServiceEndpointResolver(unittest.TestCase):
    def test_location_service_endpoint(self):
        resolver = LocationServiceEndpointResolver(None)
        self.assertEqual(resolver._location_service_endpoint,
                         "location-readonly.aliyuncs.com")
        resolver.set_location_service_endpoint("new location endpoint")
        self.assertEqual(resolver._location_service_endpoint,
                         "new location endpoint")

    def test_get_endpoint_key_from_request(self):
        resolver = LocationServiceEndpointResolver(None)
        request = ResolveEndpointRequest(
            "cn-huhehaote", "ecs", "servicecode", "")
        self.assertEqual("ecs.servicecode.cn-huhehaote.openAPI",
                         resolver.get_endpoint_key_from_request(request))

    def test_resolver(self):
        resolver = LocationServiceEndpointResolver(None)
        # no location_service_code
        request = ResolveEndpointRequest("", "", "", "")
        self.assertEqual(resolver.resolve(request), None)
        # invalid products
        resolver._invalid_product_codes.add("invalid_product")
        request = ResolveEndpointRequest(
            "cn-huhehaote", "invalid_product", "servicecode", "")
        self.assertEqual(resolver.resolve(request), None)
        # invalid region id
        resolver._invalid_region_ids.add("invalid_region_id")
        request = ResolveEndpointRequest(
            "invalid_region_id", "product", "servicecode", "")
        self.assertEqual(resolver.resolve(request), None)
        # match cache
        request = ResolveEndpointRequest(
            "region_id", "product", "servicecode", "")
        resolver.endpoints_data["product.servicecode.region_id.openAPI"] = "the fake endpoint"
        self.assertEqual(resolver.resolve(request), "the fake endpoint")

    def test_is_region_id_valid(self):
        resolver = LocationServiceEndpointResolver(None)
        request = ResolveEndpointRequest(
            "region_id", "product", "", "")
        self.assertFalse(resolver.is_region_id_valid(request))
        resolver._invalid_region_ids.add("invalid_region_id")
        request = ResolveEndpointRequest(
            "invalid_region_id", "product", "servicecode", "")
        self.assertFalse(resolver.is_region_id_valid(request))

    def test_is_product_code_valid(self):
        resolver = LocationServiceEndpointResolver(None)
        request = ResolveEndpointRequest(
            "region_id", "product", "", "")
        self.assertFalse(resolver.is_product_code_valid(request))
        resolver._invalid_product_codes.add("invalid_product")
        request = ResolveEndpointRequest(
            "region_id", "invalid_product", "servicecode", "")
        self.assertFalse(resolver.is_product_code_valid(request))

    def test_resolver_with_location(self):
        client = Mock()
        client.do_action_with_exception.return_value = ensure_bytes(
            '{"Code": "Success","Endpoints": {"Endpoint": []}}')

        resolver = LocationServiceEndpointResolver(client)
        request = ResolveEndpointRequest(
            "region_id", "product", "servicecode", "")
        self.assertEqual(resolver.resolve(request), None)

    def test_resolver_with_location2(self):
        client = Mock()
        client.do_action_with_exception.return_value = ensure_bytes(
            '{"Code": "Success","Endpoints": {"Endpoint": [{"ServiceCode":"servicecode",' +
            '"Type":"innerAPI","Endpoint":"the inner endpoint"},{"ServiceCode":"servicecode",' +
            '"Type":"openAPI","Endpoint":"the endpoint"}]}}')
        resolver = LocationServiceEndpointResolver(client)
        request = ResolveEndpointRequest(
            "region_id", "product", "servicecode", "")
        self.assertEqual(resolver.resolve(request), "the endpoint")

    def test_resolver_with_server_exception(self):
        client = Mock()
        client.do_action_with_exception.side_effect = ServerException(
            "OTHER_ERROR_CODE", "msg")
        resolver = LocationServiceEndpointResolver(client)
        request = ResolveEndpointRequest(
            "region_id", "product", "servicecode", "")
        with self.assertRaises(ServerException) as ex:
            resolver.resolve(request)
        self.assertEqual(ex.exception.error_code, "OTHER_ERROR_CODE")
        self.assertEqual(
            ex.exception.message, "msg")

    def test_resolver_with_server_exception_invalid_regionid(self):
        client = Mock()
        client.do_action_with_exception.side_effect = ServerException(
            "InvalidRegionId", "The specified region does not exist.")
        resolver = LocationServiceEndpointResolver(client)
        request = ResolveEndpointRequest(
            "region_id", "product", "servicecode", "")
        self.assertEqual(resolver.resolve(request), None)
        client.do_action_with_exception.side_effect = ServerException(
            "Illegal Parameter", "Please check the parameters")
        resolver = LocationServiceEndpointResolver(client)
        request = ResolveEndpointRequest(
            "region_id", "product", "servicecode", "")
        self.assertEqual(resolver.resolve(request), None)
