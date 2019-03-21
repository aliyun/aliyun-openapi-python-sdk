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
from alibabacloud.handlers.prepare_handler import PrepareHandler
from alibabacloud.handlers.signer_handler import SignerHandler
from alibabacloud.handlers.url_handler import URLHandler
from alibabacloud.handlers.http_header_handler import HttpHeaderHandler
from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader
from alibabacloud.handlers.endpoint_handler import EndpointHandler
from alibabacloud.handlers.log_handler import LogHandler
from alibabacloud.handlers.retry_handler import RetryHandler
from alibabacloud.handlers.server_error_handler import ServerErrorHandler
from alibabacloud.handlers.http_handler import HttpHandler
from alibabacloud.credentials.credentials_provider import DefaultCredentialsProvider
from alibabacloud.endpoint.default_endpoint_resolver import DefaultEndpointResolver
DEFAULT_HANDLERS = [
    PrepareHandler,
    SignerHandler,  # 获取Signature
    URLHandler,  # 获取url
    HttpHeaderHandler,  # 获取签名的header
    TimeoutConfigReader,  # 获取timeout
    EndpointHandler,  # 获取endpoint
    LogHandler,
    # RetryHandler,
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

    def __init__(self, access_key_id=None, access_key_secret=None, bearer_token=None,
                 secret_token=None, region_id=None,
                 enable_retry_policy=None, max_retry_times=None, user_agent=None,
                 extra_user_agent=None, enable_https=None, http_port=None, https_port=None,
                 connection_timeout=None, read_timeout=None, enable_http_debug=None,
                 http_proxy=None, https_proxy=None, enable_stream_logger=None,
                 profile_name=None, config_file=None):

        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.secret_token = secret_token
        self.bearer_token = bearer_token

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
        # self.http_proxy = http_proxy
        # self.https_proxy = https_proxy
        self.proxy = {
            'http': http_proxy,
            'https': https_proxy,
        }
        self.enable_stream_logger = enable_stream_logger
        self.profile_name = profile_name
        self.config_file = config_file

    def read_from_env(self):
        # 从环境变量读取一定量的数据
        pass
        # env_vars = ['HTTP_DEBUG', 'HTTPS_PROXY', 'HTTP_PROXY']
        # for item in env_vars:
        #     if getattr(self, item.lower()) is None:
        #         setattr(self, item.lower(), os.environ.get(item) or os.environ.get(item.lower()))

    def read_from_profile(self):
        ENV_NAME_FOR_CONFIG_FILE = 'ALIBABA_CLOUD_CONFIG_FILE'
        DEFAULT_NAME_FOR_CONFIG_FILE = ['/etc/.alibabacloud/config',
                                        '~/.alibabacloud/config']
        # TODO read from profile
        from alibabacloud.utils.ini_helper import load_config
        profile = {}
        loaded_config = {}
        if self.config_file is None:
            if ENV_NAME_FOR_CONFIG_FILE in os.environ:

                env_config_file_path = os.environ.get(ENV_NAME_FOR_CONFIG_FILE)
                if env_config_file_path is None or len(env_config_file_path) == 0:
                    # 默认配置不存在
                    return None
                full_path = os.path.expanduser(env_config_file_path)
                loaded_config = load_config(full_path)
                profile = loaded_config.get(self.profile_name, {})
            else:
                potential_locations = DEFAULT_NAME_FOR_CONFIG_FILE
                for filename in potential_locations:
                    try:
                        loaded_config = load_config(filename)
                        break
                    except Exception:
                        continue
                profile = loaded_config.get(self.profile_name, {})
        else:
            profile = load_config(self.config_file)
        
        for key in dir(self):
            if profile.get(key)is not None and getattr(self, key) is None:
                # 不存在config当中的值 pass
                setattr(self, key, profile.get(key))
            # print('不存在config当中的值', key)

    def read_from_default(self):
        # some config DEFAULT
        # 用户实例化的时候，就进行了覆盖
        pass


def get_merged_client_config(config):
    # config.read_from_env()
    # config.read_from_profile()
    # config.read_from_default()
    return config


class AlibabaCloudClient:

    def __init__(self, client_config, credentials_provider=DefaultCredentialsProvider):
        self.config = get_merged_client_config(client_config)
        self.credentials_provider = DefaultCredentialsProvider
        self.handlers = DEFAULT_HANDLERS
        self.logger = None  # TODO initialize
        # endpoint_resolver阶段需要
        self.endpoint_resolver = DefaultEndpointResolver(self)  # TODO initialize
        self.product_code = None
        self.location_service_code = None
        self.location_service_type = None
        self.location_endpoint_type = None

    def handle_request(self, api_request, request_handlers=None, context=None):
        # TODO handle different types of request
        from aliyunsdkcore.request import CommonRequest
        if isinstance(api_request, CommonRequest):
            api_request.trans_to_acs_request()
        self.product_code = api_request.get_product()
        self.location_service_code = api_request.get_location_service_code()
        self.location_endpoint_type = api_request.get_location_endpoint_type()
        if not context:
            context = RequestContext()
            context.api_request = api_request
            from .request import HTTPRequest
            context.http_request = HTTPRequest()
            context.config = self.config
            context.credentials_provider = self.credentials_provider
            context.product_code = self.product_code
            context.location_service_code = self.location_service_code
            context.location_endpoint_type = self.location_endpoint_type
            context.endpoint_resolver = self.endpoint_resolver
            # credentials 是和请求解耦的，从请求的流程来看，不应该放在handle当中
            context.credentials = self.get_credentials()

        if not request_handlers:
            request_handlers = self.handlers

        for i in range(len(request_handlers)):
            request_handlers[i]().handle_request(context)

        for i in reversed(range(len(request_handlers))):
            request_handlers[i]().handle_response(context)
            # if context.retry_flag:
            #     time.sleep(context.retry_backoff)
            #     self.handle_request(api_request,
            #                         request_handlers=request_handlers[i:],
            #                         context=context)

        return context.response

    def get_credentials(self):
        credentials_provider = self.credentials_provider({
            'access_key_id': self.config.access_key_id,
            'access_key_secret': self.config.access_key_secret,
            'secret_token': self.config.secret_token,
            'bearer_token': self.config.bearer_token,
            'profile_name': 'client5'
        })
        credentials = credentials_provider.load_credentials()
        if credentials is None:
            from aliyunsdkcore.acs_exception.exceptions import ClientException
            raise ClientException(
                'Credentials',
                'Unable to locate credentials.'
            )
        return credentials


