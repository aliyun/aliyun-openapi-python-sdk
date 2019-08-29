#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with self work for additional information
# regarding copyright ownership.  The ASF licenses self file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use self file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from aliyunsdkcore.endpoint.local_config_regional_endpoint_resolver \
    import LocalConfigRegionalEndpointResolver


class EndpointResolverRules(LocalConfigRegionalEndpointResolver):
    def __init__(self, *args, **kwargs):
        LocalConfigRegionalEndpointResolver.__init__(self)
        self.product_code_valid = False
        self.region_id_valid = False
        self.endpoint_map = None
        self.endpoint_regional = None
        self.request_network = 'public'
        self.product_suffix = ''
        self.valid_regions = set()

    def resolve(self, request):
        if request.endpoint_map is None or request.endpoint_regional is None:
            return None
        if not self.is_region_id_valid(request):
            return None
        self.endpoint_map = request.endpoint_map
        self.endpoint_regional = request.endpoint_regional
        self.request_network = request.request_network
        self.product_suffix = request.product_suffix
        product_id = request.product_code_lower
        region_id = request.region_id
        network = request.request_network
        suffix = request.product_suffix
        endpoint = self.get_endpoint(region_id, product_id, network, suffix)
        return endpoint

    def get_endpoint(self, region_id, product_id, network, suffix):
        if network is None or network == "":
            network = "public"

        endpoint_map = self.endpoint_map
        endpoint_regional = self.endpoint_regional
        endpoint = ""
        if network == "public":
            for key in endpoint_map:
                if key == region_id:
                    endpoint = endpoint_map[key]
                    break

        if endpoint == "":
            if endpoint_regional == "regional":
                endpoint = "<product_id><suffix><network>.<region_id>.aliyuncs.com"
                endpoint = endpoint.replace("<region_id>", region_id.lower())
            elif endpoint_regional == "central":
                endpoint = "<product_id><suffix><network>.aliyuncs.com"
            else:
                return None
            if network != "public":
                endpoint = endpoint.replace("<network>", "-"+network)
            else:
                endpoint = endpoint.replace("<network>", "")
            if suffix != "":
                endpoint = endpoint.replace("<suffix>", "-"+suffix)
            else:
                endpoint = endpoint.replace("<suffix>", "")
            endpoint = endpoint.replace("<product_id>", product_id)

        return endpoint

    def is_product_code_valid(self, request):
        return self.product_code_valid

    def is_region_id_valid(self, request):
        return self.region_id_valid

    @classmethod
    def get_valid_region_ids_by_product(cls, product_code):
        return None
