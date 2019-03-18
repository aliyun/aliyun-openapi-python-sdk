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
import os
from alibabacloud.handlers import RequestContext

DEFAULT_HANDLERS = [
    HttpHeaderHandler,  # 获取请求头
    EndpointHandler,  # 获取endpoint
    TimeoutHandler,  # 获取timeout
    LogHandler,
    SignerHandler,  # 获取url和签名header
    RetryHandler,
    ServerErrorHandler,
    HttpHandler
]

DEFAULT_FORMAT = 'JSON'
DEFAULT_ENABLE_RETRY_POLICY = True
DEFAULT_MAX_RETRY_TIMES = 3
DEFAULT_CONNECTION_TIMEOUT = 5
DEFAULT_READ_TIMEOUT = 10
DEFAULT_ENABLE_HTTP_DEBUG = False
DEFAULT_ENABLE_HTTPS = False


class ClientConfig:
    """
    处理client级别的所有的参数
    """

    def __init__(self, access_key_id=None, access_key_secret=None, region_id=None,
                 enable_retry_policy=None, max_retry_times=None, user_agent=None,
                 extra_user_agent=None, enable_https=None, http_port=None, https_port=None,
                 connection_timeout=None, read_timeout=None, enable_http_debug=None,
                 http_proxy=None, https_proxy=None, enable_stream_logger=None):

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
        self._timeout = (self.connection_timeout, self.read_timeout)
        self.enable_http_debug = enable_http_debug
        self.http_proxy = http_proxy
        self.https_proxy = https_proxy
        self.enable_stream_logger = enable_stream_logger

    def read_from_env(self):

        def _set_env_to_config(config_name, env_name):

            env_value = os.environ.get(env_name)
            if env_value is not None:
                setattr(self, key, os.environ.get(env_value))

            if config_name == 'enable_http_debug':
                # FIXME recursive calls will be indefinite
                _set_env_to_config(config_name, 'HTTP_DEBUG')
                _set_env_to_config(config_name, 'http_debug')
            elif config_name == 'https_proxy':
                _set_env_to_config(config_name, 'HTTPS_PROXY')
                _set_env_to_config(config_name, 'https_proxy')
            elif config_name == 'http_proxy':
                _set_env_to_config(config_name, 'HTTP_PROXY')
                _set_env_to_config(config_name, 'http_proxy')

        for key in dir(self):
            # FIXME make sure we get only configuration members here, not functions & internal
            # variables
            if getattr(self, key) is None:
                env_name = 'ALIBABA_CLOUD_' + key.upper()
                _set_env_to_config(key, env_name)

    def read_from_profile(self):
        # TODO read from profile
        pass

    def read_from_default(self):
        pass


def get_merged_client_config(config):
    config.read_from_env()
    config.read_from_profile()
    config.read_from_default()
    return config


class AlibabaCloudClient:

    def __init__(self, client_config, credentials_provider):
        self.config = get_merged_client_config(client_config)
        self.credentials_provider = credentials_provider
        self.handlers = []
        self.endpoint_resolver = None  # TODO initialize
        self.logger = None  # TODO initialize

    def handle_request(self, api_request):
        # TODO handle different types of request
        context = RequestContext()
        context.api_equest = api_request
        context.config = self.config

        for handler in self.handlers:
            # 所有的一系列handler实际是组装参数,获取endpoint等等的数据
            handler.handle_request(context)

        # 应该返回原始的response，对error进行的处理
        try:
            response = http_request.get_response_object()
        except IOError as e:
            exception = ClientException(error_code.SDK_HTTP_ERROR, str(e))
            return None, None, None, exception

        response_flag = True
        # 对返回结果进行一层 exceptions 的校验
        for handler in reversed(self.handlers):
            if hasattr(handler, 'handle_exceptions'):
                result = handler.handle_exceptions(response)
                # TODO : result 有值，说明是ServerExceptions 下面的不走了
                if request is not None:
                    response_flag = False
                    return result

        # 对response 进行的一层处理,原本是response对象
        if response_flag:
            for handler in reversed(self.handlers):
                if hasattr(handler, 'handle_response'):
                    result = handler.handle_response(response)
                    return result


