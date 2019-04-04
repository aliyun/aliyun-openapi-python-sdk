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


class MiniRAMClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider):
        AlibabaCloudClient.__init__(self, client_config, credentials_provider)
        self.product_code = "Sts"
        self.product_version = "2015-04-01"
        self.location_service_code = 'sts'
        self.location_endpoint_type = "openAPI"

    def assume_role(self, role_arn=None, role_session_name=None, duration_seconds=None):
        api_request = APIRequest('AssumeRole', 'GET', 'https', 'RPC')
        api_request._params = {
            "RoleArn": role_arn,
            "RoleSessionName": role_session_name,
            "DurationSeconds": duration_seconds,
        }
        return self._handle_request(api_request)


class AssumeRoleCaller:

    def __init__(self, client_config, credentials_provider):
        self._client = MiniRAMClient(client_config, credentials_provider)

    def fetch(self, role_arn, role_session_name, session_period):
        return self._client.assume_role(role_arn, role_session_name, session_period)
