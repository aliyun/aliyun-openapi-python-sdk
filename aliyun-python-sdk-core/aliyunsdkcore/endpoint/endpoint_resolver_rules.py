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

from aliyunsdkcore.endpoint.endpoint_resolver_base import EndpointResolverBase


class EndpointResolverRules():
    def __init__(self, *args, **kwargs):
        self.product_code_valid = False
        self.region_id_valid = False
        self.endpoint_data = None

    def set_endpoint_data(self, endpoint_data):
        self.endpoint_data = endpoint_data

    def get_endpoint_data(self):
        return self.endpoint_data

    def import_endpoint_data(self, request):
        return __import__(
            '.'.join(['aliyunsdk'+request.product_code,
                      'endpoint', 'endpoint_data']), globals(), locals(),
            ['endpoint', 'end'], 0)

    def resolve(self, request):
        try:
            if self.endpoint_data is None:
                endpoint_data = self.import_endpoint_data(request)
                self.set_endpoint_data(endpoint_data)
        except ModuleNotFoundError:
            return None
        else:
            endpoint_data = self.get_endpoint_data()
            endpoint = endpoint_data.getEndpoint(
                request.region_id, request.request_network)
            if endpoint is not None and endpoint != "":
                self.product_code_valid = True
                self.region_id_valid = True
                return endpoint
            return None

    def is_product_code_valid(self, request):
        return self.product_code_valid

    def is_region_id_valid(self, request):
        return self.region_id_valid

    def get_valid_region_ids_by_product(self, product_code):
        return []
