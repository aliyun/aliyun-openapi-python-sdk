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
from alibabacloud.handlers.credentials_handler import CredentialsHandler
from alibabacloud.handlers.signer_handler import SignerHandler

from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader
from alibabacloud.handlers.endpoint_handler import EndpointHandler
from alibabacloud.handlers.log_handler import LogHandler
from alibabacloud.handlers.retry_handler import RetryHandler
from alibabacloud.handlers.server_error_handler import ServerErrorHandler
from alibabacloud.handlers.http_handler import HttpHandler


DEFAULT_HANDLERS = [
    PrepareHandler,

    CredentialsHandler,
    SignerHandler,
    TimeoutConfigReader,
    LogHandler,
    EndpointHandler,

    RetryHandler,
    ServerErrorHandler,
    HttpHandler,
]

DEFAULT_FORMAT = 'JSON'
DEFAULT_ENABLE_RETRY_POLICY = True
DEFAULT_MAX_RETRY_TIMES = 3
DEFAULT_CONNECTION_TIMEOUT = 5
DEFAULT_READ_TIMEOUT = 10
DEFAULT_ENABLE_HTTP_DEBUG = False
DEFAULT_ENABLE_HTTPS = False
HTTP_PORT = 80
HTTPS_PORT = 443


class ClientConfig:
    """
    处理client级别的所有的参数
    """

    ENV_NAME_FOR_CONFIG_FILE = 'ALIBABA_CLOUD_CONFIG_FILE'
    DEFAULT_NAME_FOR_CONFIG_FILE = '~/.alibabacloud/config'

    def __init__(self, access_key_id=None, access_key_secret=None, region_id=None,
                 max_retry_times=None, user_agent=None, extra_user_agent=None,
                 enable_https=None, http_port=HTTP_PORT, https_port=HTTPS_PORT,
                 connection_timeout=None, read_timeout=None, enable_http_debug=None,
                 http_proxy=None, https_proxy=None, enable_stream_logger=None,
                 profile_name=None, config_file=None, enable_retry=True, endpoint=None):

        # credentials部分会用到
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.region_id = region_id
        self.enable_retry = enable_retry
        self.max_retry_times = max_retry_times
        self.endpoint = endpoint

        # user-agent
        self.user_agent = user_agent
        self.extra_user_agent = extra_user_agent
        # https
        self.enable_https = enable_https
        self.http_port = http_port
        self.https_port = https_port
        # timeout
        self.connection_timeout = connection_timeout
        self.read_timeout = read_timeout
        # logger
        self.enable_stream_logger = enable_stream_logger
        # credentials 的profile
        self.profile_name = profile_name
        # 读取配置文件
        self.config_file = config_file
        self.enable_http_debug = enable_http_debug  # http-debug 只从环境变量获取，不设置开关
        # proxy provider两个： client  env
        self.http_proxy = http_proxy
        self.https_proxy = https_proxy
        self._proxy = {
            'http': self.http_proxy,
            'https': self.https_proxy,
        }

    @property
    def proxy(self):
        return self._proxy

    def read_from_env(self):
        # 从环境变量读取一定量的数据
        env_vars = ['HTTPS_PROXY', 'HTTP_PROXY']
        for item in env_vars:
            if getattr(self, item.lower()) is None:
                setattr(self, item.lower(), os.environ.get(item) or os.environ.get(item.lower()))

        self.enable_http_debug = os.environ.get('DEBUG') == 'sdk' or 'SDK'

    def read_from_profile(self):
        profile = {}
        # TODO read from profile
        from alibabacloud.utils.ini_helper import load_config
        if self.config_file is None:
            # 没有指定file
            if self.ENV_NAME_FOR_CONFIG_FILE in os.environ:
                env_config_file_path = os.environ.get(self.ENV_NAME_FOR_CONFIG_FILE)
                if env_config_file_path is not None:
                    full_path = os.path.expanduser(env_config_file_path)
                    loaded_config = load_config(full_path)
                    profile = loaded_config.get(self.profile_name, {})
                else:
                    # 默认配置不存在
                    filename = self.DEFAULT_NAME_FOR_CONFIG_FILE
                    loaded_config = load_config(filename)
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

    def _update_config(self, new_config):
        # request 的config 更新client的config
        request_settings = ['enable_https', 'connection_timeout', 'read_timeout', 'endpoint']
        for attr in request_settings:
            if getattr(new_config, attr) is not None:
                setattr(self, attr, getattr(new_config, attr))


def get_merged_client_config(config):
    config.read_from_env()
    config.read_from_profile()
    # config.read_from_default()

    return config


class AlibabaCloudClient:

    def __init__(self, client_config, credentials_provider):
        # client_config:传入的ClientConfig

        self.config = get_merged_client_config(client_config)

        if credentials_provider is not None:
            self.credentials_provider = credentials_provider
        else:
            from alibabacloud.credentials.provider import DefaultChainedCredentialsProvider

            self.credentials_provider = DefaultChainedCredentialsProvider(self.config)
        self.handlers = DEFAULT_HANDLERS
        self.logger = None  # TODO initialize
        from alibabacloud.endpoint.default_endpoint_resolver import DefaultEndpointResolver

        self.endpoint_resolver = DefaultEndpointResolver(self.config)  # TODO initialize
        self.product_code = None
        self.location_service_code = None
        self.product_version = None
        self.location_endpoint_type = None

        import alibabacloud.retry.retry_policy as retry_policy
        # retry
        if self.config.enable_retry:
            self.retry_policy = retry_policy.get_default_retry_policy(
                max_retry_times=self.config.max_retry_times)
        else:
            self.retry_policy = retry_policy.NO_RETRY_POLICY

    def _handle_request(self, api_request, _raise_exception=True):
        # handle context
        context = RequestContext()
        context.api_request = api_request
        from .request import HTTPRequest
        context.http_request = HTTPRequest()
        context.config = self.config

        context.client = self

        handler_index = 0

        while True:
            for i in range(len(self.handlers[handler_index:])):
                self.handlers[i]().handle_request(context)

            for i in reversed(range(len(self.handlers[handler_index:]))):
                self.handlers[i]().handle_response(context)
                if context.retry_flag:
                    time.sleep(context.retry_backoff / 1000)
                    handler_index = i
                    break

        if context.exception and _raise_exception:
            raise context.exception

        return context


class ECSClient(AlibabaCloudClient):

    def __init__(self):
        self.product = 'Ecs'
        self.location_service_code = 'ecs'
        self.location_endpoint_type = 'OpenAPI'

    def create_instance(self, instance_name=None, instance_id=None):
        api_request = APIRequest(action_name, method, protocol, style)
        api_request._params['InstanceName'] = instance_name
        return self._handle_request(api_request).result

    def delete_instance(self, **params):
        api_request = APIRequest(**params)
        return self._handle_request(api_request).result


class OTSClient(AlibabaCloudClient):

    def create_table(self, **params):
        api_request = APIRequest(**params)
        return self._handle_request(api_request).result


class STSClient(AlibabaCloudClient):
    def __init__(self):
        self.product = 'Sts'
        self.location_service_code = 'sts'
        self.location_endpoint_type = 'OpenAPI'
        # AlibabaCloudClient.__init__(self)

    def handle_request(self, request, config):
        self._handle_request(request, _config=config, _raise_exception=True)
