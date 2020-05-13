# Copyright 2018 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from base import SDKTestBase
from mock import MagicMock, patch
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdkram.request.v20150501.ListAccessKeysRequest import ListAccessKeysRequest
from aliyunsdkros.request.v20150901.DescribeResourcesRequest import DescribeResourcesRequest
from aliyunsdkcloudapi.request.v20160714.DescribeApisRequest import DescribeApisRequest
import aliyunsdkcore.acs_exception.error_code as error_code

from aliyunsdkcore.endpoint.user_customized_endpoint_resolver import UserCustomizedEndpointResolver
from aliyunsdkcore.endpoint.local_config_regional_endpoint_resolver \
    import LocalConfigRegionalEndpointResolver
from aliyunsdkcore.endpoint.local_config_global_endpoint_resolver \
    import LocalConfigGlobalEndpointResolver
from aliyunsdkcore.endpoint.location_service_endpoint_resolver \
    import LocationServiceEndpointResolver
from aliyunsdkcore.endpoint.chained_endpoint_resolver import ChainedEndpointResolver
from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from aliyunsdkcore.endpoint.default_endpoint_resolver import DefaultEndpointResolver


class NewEndpointTest(SDKTestBase):

    def setUp(self):
        SDKTestBase.setUp(self)
        DefaultEndpointResolver.predefined_endpoint_resolver = UserCustomizedEndpointResolver()

    def init_env(self, test_local_config=None, client=None):
        resolver_chain = []

        self._user_customized_endpoint_resolver = UserCustomizedEndpointResolver()
        if test_local_config is None:
            self._local_config_regional_endpoint_resolver = LocalConfigRegionalEndpointResolver()
            self._local_config_global_endpoint_resolver = LocalConfigGlobalEndpointResolver()
        else:
            self._local_config_regional_endpoint_resolver = \
                LocalConfigRegionalEndpointResolver(test_local_config)
            self._local_config_global_endpoint_resolver = \
                LocalConfigGlobalEndpointResolver(test_local_config)
        if client is not None:
            self._location_service_endpoint_resolver = LocationServiceEndpointResolver(client)
        else:
            self._location_service_endpoint_resolver = LocationServiceEndpointResolver(self.client)

        resolver_chain.append(self._user_customized_endpoint_resolver)
        resolver_chain.append(self._local_config_regional_endpoint_resolver)
        resolver_chain.append(self._local_config_global_endpoint_resolver)
        resolver_chain.append(self._location_service_endpoint_resolver)

        self._endpoint_resolver = ChainedEndpointResolver(resolver_chain)

    def resolve(self, region_id, product_code, location_service_code=None, endpoint_type=None):
        request = ResolveEndpointRequest(region_id, product_code,
                                         location_service_code, endpoint_type)
        return self._endpoint_resolver.resolve(request)

    def test_products_with_location_service(self):
        request = DescribeRegionsRequest()
        response = self.client.do_action_with_exception(request)

    def test_products_without_location_service(self):
        request = ListAccessKeysRequest()
        response = self.client.do_action_with_exception(request)

    def test_add_new_endpoint_manually(self):
        my_client = self.init_client("cn-ningbo")
        request = DescribeRegionsRequest()
        try:
            response = my_client.do_action_with_exception(request)
            assert False
        except ClientException as e:
            self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
            self.assertEqual(
                "No such region 'cn-ningbo'. Please check your region ID.",
                e.get_error_msg()
            )

        my_client.add_endpoint(
            "cn-ningbo",  # which does not exist at all
            "Ecs",
            "abc.cn-ningbo.endpoint-test.exception.com"
        )

        with patch.object(
                my_client._endpoint_resolver,
                'resolve',
                wraps=my_client._endpoint_resolver.resolve
        ) as monkey:
            monkey.side_effect = ClientException(
                error_code.SDK_HTTP_ERROR,
                "abc.cn-ningbo.endpoint-test.exception.com")
            request2 = DescribeRegionsRequest()
            try:
                response2 = my_client.do_action_with_exception(request2)
                assert False
            except ClientException as e:
                self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
                self.assertEqual("abc.cn-ningbo.endpoint-test.exception.com", e.get_error_msg())

    def test_add_existing_endpoint_manually(self):
        my_client = self.init_client("cn-hangzhou")
        request = DescribeRegionsRequest()
        response = my_client.do_action_with_exception(request)

        my_client.add_endpoint(
            "cn-hangzhou",
            "Ecs",
            "abc.cn-hangzhou.endpoint-test.exception.com")

        with patch.object(
                my_client._endpoint_resolver,
                'resolve'
        ) as monkey:
            monkey.side_effect = ClientException(
                error_code.SDK_HTTP_ERROR,
                "abc.cn-hangzhou.endpoint-test.exception.com")
            request2 = DescribeRegionsRequest()
            try:
                response2 = my_client.do_action_with_exception(request2)
                assert False
            except ClientException as e:
                self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
                self.assertEqual("abc.cn-hangzhou.endpoint-test.exception.com", e.get_error_msg())

    def test_regional_endpoint_comes_from_local_config(self):
        test_config = """
            {
                "regional_endpoints" : {
                    "abc" : {
                        "mars-ningbo" : "ecs.mars-ningbo.aliyuncs.com"
                    }
                }
            }
        """

        self.init_env(test_config)

        self.assertEqual(
            "ecs.mars-ningbo.aliyuncs.com",
            self.resolve("mars-ningbo", "abc")
        )

    def test_global_endpoint_comes_from_local_config(self):
        test_config = """
            {
                "regional_endpoints" : {
                    "abc" : {
                        "mars-ningbo" : "ecs.mars-ningbo.aliyuncs.com"
                    }
                },
                "global_endpoints" : {
                    "abc" : "ecs.mars.aliyuncs.com"
                },
                "regions" : ["mars-ningbo", "mars-hangzhou", "mars-shanghai"]
            }
        """

        self.init_env(test_config)

        self.assertEqual(
            "ecs.mars-ningbo.aliyuncs.com",
            self.resolve("mars-ningbo", "abc")
        )
        self.assertEqual(
            "ecs.mars.aliyuncs.com",
            self.resolve("mars-hangzhou", "abc")
        )
        self.assertEqual(
            "ecs.mars.aliyuncs.com",
            self.resolve("mars-shanghai", "abc")
        )

    def test_endpoint_comes_from_location_service(self):
        self.init_env("{}")  # empty local config
        with patch.object(
                self._location_service_endpoint_resolver,
                '_call_location_service',
                wraps=self._location_service_endpoint_resolver._call_location_service
        ) as monkey:
            for i in range(3):
                self.assertEqual(
                    "ecs-cn-hangzhou.aliyuncs.com",
                    self.resolve("cn-hangzhou", "ecs", "ecs", None)
                )

        self.assertEqual(1, monkey.call_count)

    def test_location_service_miss(self):
        self.init_env("{}")  # empty local config

        with patch.object(
                self._location_service_endpoint_resolver,
                '_call_location_service',
                wraps=self._location_service_endpoint_resolver._call_location_service
        ) as monkey:

            self.assertEqual(0, monkey.call_count)
            # No openAPI data
            for i in range(3):
                try:
                    self.resolve("cn-hangzhou", "Ram", "ram", "openAPI")
                    assert False
                except ClientException as e:
                    self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
                    self.assertTrue(e.get_error_msg().startswith(
                        "No endpoint in the region 'cn-hangzhou' for product 'Ram'."
                    ))

            self.assertEqual(1, monkey.call_count)

            # Bad region ID
            for i in range(3):
                try:
                    self.resolve("mars", "Ram", "ram", "openAPI")
                    assert False
                except ClientException as e:
                    self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
                    self.assertEqual(
                        "No such region 'mars'. Please check your region ID.",
                        e.get_error_msg()
                    )

            self.assertEqual(2, monkey.call_count)
            # Bad region ID with another product
            try:
                self.resolve("mars", "Ecs", "ecs", "openAPI")
                assert False
            except ClientException as e:
                self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
                self.assertEqual("No such region 'mars'. Please check your region ID.",
                                 e.get_error_msg())

            self.assertEqual(2, monkey.call_count)

            # Bad product code
            for i in range(3):
                try:
                    self.resolve("cn-hangzhou", "InvalidProductCode",
                                 "InvalidProductCode", "openAPI")
                    assert False
                except ClientException as e:
                    self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
                    self.assertTrue(e.get_error_msg().startswith(
                        "No endpoint for product 'InvalidProductCode'.\n"
                        "Please check the product code, "
                        "or set an endpoint for your request explicitly.\n"
                    ))

            # Bad product code with another region ID
            try:
                self.resolve("cn-beijing", "InvalidProductCode", "InvalidProductCode", "openAPI")
                assert False
            except ClientException as e:
                self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
                self.assertTrue(e.get_error_msg().startswith(
                    "No endpoint for product 'InvalidProductCode'.\n"
                    "Please check the product code, "
                    "or set an endpoint for your request explicitly.\n")
                )
            self.assertEqual(3, monkey.call_count)

    def test_try_to_get_endpoint_with_invalid_region_id(self):
        self.init_env()
        try:
            self.resolve("mars", "Ecs")
            assert False
        except ClientException as e:
            self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
            self.assertEqual(
                "No such region 'mars'. Please check your region ID.",
                e.get_error_msg()
            )

    def test_try_to_get_endpoint_with_invalid_product_code(self):
        self.init_env()
        try:
            self.resolve("cn-beijing", "InvalidProductCode")
            assert False
        except ClientException as e:
            self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
            self.assertTrue(e.get_error_msg().startswith(
                "No endpoint for product 'InvalidProductCode'.\n"
                "Please check the product code, "
                "or set an endpoint for your request explicitly.\n")
            )

    def test_inner_api_endpoint(self):
        self.init_env()
        self.assertEqual(
            "ram-share.aliyuncs.com",
            self.resolve("cn-hangzhou", "Ram", "ram", "innerAPI")
        )

    def test_get_inner_api_endpoint_bypass_local_config(self):
        test_config = """
            {
                "regional_endpoints" : {
                    "ram" : {
                        "cn-hangzhou" : "ram.mars-ningbo.aliyuncs.com"
                    }
                },
                "global_endpoints" : {
                    "ram" : "ram.mars.aliyuncs.com"
                }
            }
        """
        self.init_env(test_config)
        self.assertEqual(
            "ram-share.aliyuncs.com",
            self.resolve("cn-hangzhou", "Ram", "ram", "innerAPI")
        )

    def test_get_inner_api_endpoint_by_manually_adding(self):
        self.init_env()
        self._user_customized_endpoint_resolver.put_endpoint_entry(
            "cn-hangzhou",
            "Ram",
            "ram.cn-hangzhou.endpoint-test.exception.com"
        )
        self.assertEqual(
            "ram.cn-hangzhou.endpoint-test.exception.com",
            self.resolve("cn-hangzhou", "Ram", "ram", "innerAPI")
        )

    def test_can_not_connect_location_service(self):
        self.init_env()
        self._location_service_endpoint_resolver.set_location_service_endpoint(
            "location-on-mars.aliyuncs.com")

        try:
            self.resolve("cn-hangzhou", "Ecs", "ecs", "innerAPI")
            assert False
        except ClientException as e:
            self.assertEqual("SDK.HttpError", e.get_error_code())

    def test_invalid_access_key_id(self):
        client = AcsClient("BadAccessKeyId", self.access_key_secret, "cn-hangzhou")
        self.init_env(None, client)
        try:
            self.resolve("cn-hangzhou", "Ecs", "ecs", "innerAPI")
            assert False
        except ServerException as e:
            self.assertEqual("InvalidAccessKeyId.NotFound", e.get_error_code())

    def test_invalid_access_key_secret(self):

        client = AcsClient(self.access_key_id, "BadAccessKeySecret", "cn-hangzhou")
        self.init_env(None, client)
        try:
            self.resolve("cn-hangzhou", "Ecs", "ecs", "innerAPI")
            assert False
        except ServerException as e:
            self.assertEqual("InvalidAccessKeySecret", e.get_error_code())

    def test_local_clock_screw_when_call_location_service(self):
        # Not implemented
        pass

    def test_call_rpc_request_with_client(self):
        request = DescribeRegionsRequest()
        response = self.client.do_action_with_exception(request)

    def test_call_roa_request_with_client(self):
        request = DescribeResourcesRequest()
        request.set_StackId("StackId")
        request.set_StackName("StackName")
        try:
            response = self.client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("StackNotFound", e.get_error_code())

    def test_location_service_code_not_equals_product_code(self):
        request = DescribeApisRequest()
        response = self.client.do_action_with_exception(request)

    def test_location_service_code_not_equals_product_code2(self):
        self.init_env("{}")
        client = self.init_client(region_id="cn-hangzhou")
        client._endpoint_resolver = self._endpoint_resolver

        with patch.object(
                self._location_service_endpoint_resolver,
                '_call_location_service',
                wraps=self._location_service_endpoint_resolver._call_location_service
        ) as monkey:
            for i in range(3):
                request = DescribeApisRequest()
                client.do_action_with_exception(request)

        self.assertEqual(1, monkey.call_count)

        self.init_env()
        client._endpoint_resolver = self._endpoint_resolver

    def test_add_endpoint_static(self):
        from aliyunsdkcore.profile.region_provider import add_endpoint, modify_point

        my_client = self.init_client("cn-ningbo")
        request = DescribeRegionsRequest()
        try:
            response = my_client.do_action_with_exception(request)
            assert False
        except ClientException as e:
            self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
            self.assertEqual(
                "No such region 'cn-ningbo'. Please check your region ID.",
                e.get_error_msg()
            )

        add_endpoint(
            "Ecs",  # which does not exist at all
            "cn-ningbo",
            "abc.cn-ningbo.endpoint-test.exception.com"
        )

        with patch.object(
                my_client._endpoint_resolver,
                'resolve',
                wraps=my_client._endpoint_resolver.resolve
        ) as monkey:
            monkey.side_effect = ClientException(
                error_code.SDK_HTTP_ERROR,
                "abc.cn-ningbo.endpoint-test.exception.com")
            request2 = DescribeRegionsRequest()
            try:
                response2 = my_client.do_action_with_exception(request2)
                assert False
            except ClientException as e:
                self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
                self.assertEqual("abc.cn-ningbo.endpoint-test.exception.com", e.get_error_msg())

        DefaultEndpointResolver.predefined_endpoint_resolver.reset()

    def test_doc_help_sample(self):
        from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
        request = DescribeInstancesRequest()
        request.set_endpoint("ecs-cn-hangzhou.aliyuncs.com")
        response = self.client.do_action_with_exception(request)

    def test_r_kvstore(self):
        resolver = DefaultEndpointResolver(self.client)
        request = ResolveEndpointRequest("cn-hangzhou", "R-kvstore", None, None)
        self.assertEqual("r-kvstore.aliyuncs.com", resolver.resolve(request))

    def test_dts_regions(self):
        resolver = DefaultEndpointResolver(self.client)
        request = ResolveEndpointRequest("cn-chengdu", "dts", None, None)

        expected_message = "No endpoint in the region 'cn-chengdu' for product 'dts'.\n" \
                           "You can set an endpoint for your request explicitly.\n" \
                           "Or you can use the other available regions: ap-southeast-1 " \
                           "cn-beijing cn-hangzhou cn-hongkong cn-huhehaote cn-qingdao " \
                           "cn-shanghai cn-shenzhen cn-zhangjiakou\n" \
                           "See https://www.alibabacloud.com/help/doc-detail/92074.htm\n"
        try:
            resolver.resolve(request)
            assert False
        except ClientException as e:
            self.assertEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
            self.assertEqual(expected_message, e.get_error_msg())

    def test_bssopenapi_resolve(self):
        resolver = DefaultEndpointResolver(self.client)
        request = ResolveEndpointRequest("cn-hangzhou", "BssOpenApi", None, None)
        self.assertEqual("business.aliyuncs.com", resolver.resolve(request))

        request = ResolveEndpointRequest("eu-west-1", "BssOpenApi", None, None)
        self.assertEqual("business.ap-southeast-1.aliyuncs.com", resolver.resolve(request))

        from aliyunsdkbssopenapi.request.v20171214.GetOrderDetailRequest \
            import GetOrderDetailRequest
        request = GetOrderDetailRequest()

        request.set_OrderId("blah")
        try:
            self.client.do_action_with_exception(request)
        except ServerException as e:
            self.assertNotEqual("SDK.EndpointResolvingError", e.get_error_code())

    def test_faas_resolve(self):
        resolver = DefaultEndpointResolver(self.client)
        request = ResolveEndpointRequest("cn-hangzhou", "faas", None, None)
        self.assertEqual("faas.cn-hangzhou.aliyuncs.com", resolver.resolve(request))
        client = self.init_client(region_id="cn-hangzhou")

        from aliyunsdkfaas.request.v20170824.DescribeLoadTaskStatusRequest \
            import DescribeLoadTaskStatusRequest
        request = DescribeLoadTaskStatusRequest()
        request.set_FpgaUUID("blah")
        request.set_InstanceId("blah")
        request.set_RoleArn("blah")

        try:
            client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertNotEqual(error_code.SDK_ENDPOINT_RESOLVING_ERROR, e.get_error_code())
