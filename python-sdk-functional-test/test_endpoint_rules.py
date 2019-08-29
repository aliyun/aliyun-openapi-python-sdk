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
from base import SDKTestBase

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
from aliyunsdkcore.endpoint.endpoint_resolver_rules import EndpointResolverRules


class EndpointRulesTest(SDKTestBase):

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
        resolver_chain.append(EndpointResolverRules())
        resolver_chain.append(self._location_service_endpoint_resolver)

        self._endpoint_resolver = ChainedEndpointResolver(resolver_chain)

    def resolve(self, region_id, product_code, location_service_code=None, endpoint_type=None, request=None):
        resolve_request = ResolveEndpointRequest(region_id, product_code,
                                         location_service_code, endpoint_type)
        if request:
            resolve_request.request_network = request.request_network
            resolve_request.product_suffix = request.product_suffix
            resolve_request.endpoint_map = request.endpoint_map
            resolve_request.endpoint_regional = request.endpoint_regional
        return self._endpoint_resolver.resolve(resolve_request)

    def test_endpoint_rules(self):
        client = self.init_client(region_id="cn-hangzhou")
        from aliyunsdkedas.request.v20170801.ListApplicationRequest import ListApplicationRequest
        request = ListApplicationRequest()
        self.init_env(None, client)
        endpoint = self.resolve("cn-hangzhou", "Edas", "edas", "openApi", request=request)
        self.assertEqual(endpoint, "edas.cn-hangzhou.aliyuncs.com")
