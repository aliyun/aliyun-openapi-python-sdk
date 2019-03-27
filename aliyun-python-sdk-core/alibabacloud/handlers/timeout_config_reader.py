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
from alibabacloud.utils import load_json_from_data_dir
DEFAULT_READ_TIMEOUT = 10
DEFAULT_CONNECTION_TIMEOUT = 5
_api_timeout_config_data = load_json_from_data_dir._load_json_from_data_dir("timeout_config.json")


class TimeoutConfigReader(RequestHandler):
    # TODO 把对 timeout_config.json 的读取逻辑放到 ClientConfig 那一层
    # client config 不能处理  涉及到产品的product—code
    # TODO request级别仅对读取配置进行处理，用户不设置request层级的timeout
    def handle_request(self, context):
        context.http_request.timeout = (self._connection_timeout(context.config),
                                        self._read_timeout(context.api_request, context.config))

    def handle_response(self, context):
        # context 实际是request
        pass

    @staticmethod
    def _connection_timeout(config):
        return config.connection_timeout or DEFAULT_CONNECTION_TIMEOUT

    @staticmethod
    def _read_timeout(request, config):
        path = '"{0}"."{1}"."{2}"'.format(request.get_product().lower(), request.get_version(),
                                          request.get_action_name())
        file_read_timeout = jmespath.search(path, _api_timeout_config_data)
        return file_read_timeout or config.read_timeout or DEFAULT_READ_TIMEOUT
