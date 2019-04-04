# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
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

from alibabacloud.client import AlibabaCloudClient
from alibabacloud.request import APIRequest
DEFAULT_LOCATION_SERVICE_ENDPOINT = "location-readonly.aliyuncs.com"


class MiniLocationClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider):
        AlibabaCloudClient.__init__(self, client_config, credentials_provider)
        self.product_code = "Location"
        self.product_version = "2015-06-12"
        self.location_service_code = None
        self.location_endpoint_type = "openAPI"

    def describe_endpoint(self, region_id=None, endpoint_type=None, location_service_code=None):
        api_request = APIRequest('DescribeEndpoints', 'GET', 'https', 'RPC')
        api_request._params = {
            "Id": region_id,
            "Type": endpoint_type,
            "ServiceCode": location_service_code,
        }
        api_request.endpoint = DEFAULT_LOCATION_SERVICE_ENDPOINT
        return self._handle_request(api_request)


class DescribeEndpointCaller:

    def __init__(self, client_config, credentials_provider):
        self._client = MiniLocationClient(client_config, credentials_provider)

    def fetch(self, region_id, endpoint_type, location_service_code):
        return self._client.describe_endpoint(region_id, endpoint_type, location_service_code)
