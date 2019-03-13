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

DEFAULT_HANDLERS = [
    HttpHeaderHandler,
    EndpointHandler,
    TimeoutHandler,
    RetryHandler,
    LogHandler,
    SignerHandler,
    ServerErrorHandler,
    HttpHandler
]

DEFAULT_FORMAT = 'JSON'

from alibabacloud.handlers import RequestContext


class ClientConfig:
    """
    处理client级别的所有的参数
    """
    def __init__(self, access_key_id=None, access_key_secret=None, region_id=None,
                 enable_retry_policy=True, max_retry_times=None, user_agent=None,
                 extra_user_agent=None, enable_https=True, http_port=None, https_port=None,
                 connection_timeout=None, read_timeout=None, accept_format=DEFAULT_FORMAT,
                 resolve_endpoint_cls=None, specific_signer=None):

        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.region_id = region_id
        self.enable_retry_policy = enable_retry_policy
        self.max_retry_times = max_retry_times
        self.user_agent = user_agent
        self.extra_user_agent = extra_user_agent
        self.enable_https = enable_https
        self.http_port = http_port
        self.https_port = https_port
        self.connection_timeout = connection_timeout
        self.read_timeout = read_timeout
        # yan 添加的
        self.accept_format = accept_format
        self.resolve_endpoint_cls = resolve_endpoint_cls or ResolveEndpointRequest
        self.specific_signer = specific_signer

        self.http_debug = http_debug
        self.proxy_https = os.environ.get('HTTPS_PROXY') or os.environ.get(
            'https_proxy')
        self.proxy_http = os.environ.get(
            'HTTP_PROXY') or os.environ.get('http_proxy')
        # 用户硬编码传参、环境变量、读配置文件的获取参数的方式
        # TODO assign more attributes


class AlibabaCloudClient:

    def __init__(self, client_config, credentials_provider):
        self.config = client_config
        self.credentials_provider = credentials_provider
        self.handlers = []

    def _handle_request(self, request):
        # TODO handle different types of request
        context = RequestContext()
        context.request = request
        context.config = self.config

        for handler in self.handlers:
            # 所有的一系列handler实际是组装参数,获取endpoint等等的数据
            if hasattr(handler, 'handle_request'):
                result = handler.handle_request(context)
                if result is not None:
                    return result
        http_request = context.http_request

        # 应该返回原始的response
        context.response = http_request.get_response_object()

        for handler in reversed(self.handlers):
            if hasattr(handler, 'handle_response'):
                result = handler.handle_response(context)
                return result
