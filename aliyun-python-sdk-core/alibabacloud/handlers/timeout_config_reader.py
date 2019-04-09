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
    # TODO 把对 timeout_config.json 的读取逻辑放到 ClientConfig 那一层 by 青塘
    # client config 不能处理  涉及到产品的product—code
    # TODO request级别仅对读取配置进行处理，用户不设置request层级的timeout
    def handle_request(self, context):
        context.http_request.timeout = (self._connection_timeout(context.config),
                                        self._read_timeout(context))

    def handle_response(self, context):
        # context 实际是request
        pass

    @staticmethod
    def _connection_timeout(config):
        return config.connection_timeout or DEFAULT_CONNECTION_TIMEOUT

    @staticmethod
    def _read_timeout(context):
        file_read_timeout = None
        product_code = context.client.product_code
        product_version = context.client.product_version
        action_name = context.api_request.action_name
        if product_code is not None and product_version is not None \
                and action_name is not None:
            path = '"{0}"."{1}"."{2}"'.format(product_code.lower(), product_version,
                                              action_name)
            file_read_timeout = jmespath.search(path, _api_timeout_config_data)
        return file_read_timeout or context.config.read_timeout or DEFAULT_READ_TIMEOUT
