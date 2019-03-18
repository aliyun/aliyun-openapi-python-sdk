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
import jmespath
from alibabacloud.handlers import RequestHandler
DEFAULT_READ_TIMEOUT = 10
DEFAULT_CONNECTION_TIMEOUT = 5
_api_timeout_config_data = aliyunsdkcore.utils._load_json_from_data_dir("timeout_config.json")


class TimeoutHandler(RequestHandler):

    def handle_request(self, context):
        request = context.request
        config = context.config
        context.timeout = (self.connection_timeout(request, config),
                           self.read_timeout(request, config))

    def handle_response(self, request, response):
        # context 实际是request
        pass

    @staticmethod
    def connection_timeout(request, config):
        return request.connection_timeout or config.connection_timeout \
               or DEFAULT_CONNECTION_TIMEOUT

    @staticmethod
    def read_timeout(request, config):
        path = '"{0}"."{1}"."{2}"'.format(request.product.lower(), request.version,
                                          request.action_name)
        file_connection_timeout = jmespath.search(path, _api_timeout_config_data)
        return request.connection_timeout or file_connection_timeout \
               or config.connection_timeout or DEFAULT_CONNECTION_TIMEOUT
