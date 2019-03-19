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
import time
from alibabacloud.handlers import RequestContext

DEFAULT_HANDLERS = [
    PrepareHandler,
    SignerHandler,  # 获取Signature
    URLHandler,  # 获取url
    HttpHeaderHandler,  # 获取签名的header
    TimeoutHandler,  # 获取timeout
    EndpointHandler,  # 获取endpoint
    LogHandler,
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
    ENV_NAME_FOR_CONFIG_FILE = 'ALIBABA_CLOUD_CONFIG_FILE'
    DEFAULT_NAME_FOR_CONFIG_FILE = ['/etc/.alibabacloud/config',
                                         '~/.alibabacloud/config']

    def __init__(self, access_key_id=None, access_key_secret=None, region_id=None,
                 enable_retry_policy=None, max_retry_times=None, user_agent=None,
                 extra_user_agent=None, enable_https=None, http_port=None, https_port=None,
                 connection_timeout=None, read_timeout=None, enable_http_debug=None,
                 http_proxy=None, https_proxy=None, enable_stream_logger=None,
                 profile_name=None, config_file=None):

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
        self.enable_http_debug = enable_http_debug
        # proxy provider两个： client  env
        self.http_proxy = http_proxy
        self.https_proxy = https_proxy
        self.proxy = {
            'http': self.http_proxy,
            'https': self.https_proxy,
        }
        self.enable_stream_logger = enable_stream_logger
        self.profile_name = profile_name
        self.config_file = config_file

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
        from alibabacloud.utils.ini_helper import load_config
        profile = {}
        if self.config_file is None:
            if self.ENV_NAME_FOR_CONFIG_FILE in os.environ:

                env_config_file_path = os.environ.get(self.ENV_NAME_FOR_CONFIG_FILE)
                if env_config_file_path is None or len(env_config_file_path) == 0:
                    # 默认配置不存在
                    return None
                full_path = os.path.expanduser(env_config_file_path)
                self._loaded_config = load_config(full_path)
                profile = self._loaded_config.get(self.profile_name, {})
            else:
                potential_locations = self.DEFAULT_NAME_FOR_CONFIG_FILE
                for filename in potential_locations:
                    try:
                        self._loaded_config = load_config(filename)
                        break
                    except Exception:
                        continue
                profile = self._loaded_config.get(self.profile_name, {})
        else:
            profile = load_config(self.config_file)
        
        for key in dir(self):
            if profile.get(key)is not None and getattr(self, key) is None:
                # 不存在config当中的值 pass
                setattr(self, key, profile.get(key))

        return None

    def read_from_default(self):
        # some config DEFAULT
        # 用户实例化的时候，就进行了覆盖
        pass

    def handle_timeout(self):
        pass


def get_merged_client_config(config):
    config.read_from_env()
    config.read_from_profile()
    config.read_from_default()
    return config


class AlibabaCloudClient:

    def __init__(self, client_config, credentials_provider=DefaultCredentialsProvider):
        self.config = get_merged_client_config(client_config)
        self.credentials_provider = credentials_provider
        self.handlers = DEFAULT_HANDLERS
        self.logger = None  # TODO initialize
        # endpoint_resolver阶段需要
        self.endpoint_resolver = DefaultEndpointResolver(self)  # TODO initialize
        self.product_code = product_code
        self.location_service_code = location_service_code
        self.location_service_type = location_service_type

    def handle_request(self, api_request, request_handlers=None, context=None):
        # TODO handle different types of request
        if not context:
            context = RequestContext()
            context.api_request = api_request
            from .request import HTTPRequest
            context.http_request = HTTPRequest()
            context.config = self.config

        if not request_handlers:
            request_handlers = self.handlers

        for i in range(len(request_handlers)):
            request_handlers[i].handle_request(context)

        for i in reversed(range(len(request_handlers))):
            request_handlers[i].handle_response(context)
            if context.retry_flag:
                time.sleep(context.retry_backoff)
                self.handle_request(api_request,
                                    request_handlers=request_handlers[i:],
                                    context=context)

        return context.result
