# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8
import os
import warnings
import logging
import platform

# from aliyunsdkcore.endpoint.default_endpoint_resolver import DefaultEndpointResolver
import aliyunsdkcore.utils
import alibabacloud.utils.validation
from aliyunsdkcore.vendored.requests.structures import CaseInsensitiveDict
from aliyunsdkcore.vendored.requests.structures import OrderedDict

from aliyunsdkcore.auth.credentials import AccessKeyCredential, StsTokenCredential
from aliyunsdkcore.auth.credentials import RamRoleArnCredential, EcsRamRoleCredential
from aliyunsdkcore.auth.credentials import RsaKeyPairCredential

# from alibabacloud.exception import ClientException

from alibabacloud.endpoint.default_endpoint_resolver import DefaultEndpointResolver
from alibabacloud.credentials import AccessKeyCredentials, SecurityCredentials
from alibabacloud.credentials.provider import StaticCredentialsProvider
from alibabacloud.credentials.provider import RamRoleCredentialsProvider
from alibabacloud.credentials.provider import InstanceProfileCredentialsProvider
from alibabacloud.client import ClientConfig
from alibabacloud.client import AlibabaCloudClient  # New Style Client

"""
Acs default client module.
"""

DEFAULT_READ_TIMEOUT = 10
DEFAULT_CONNECTION_TIMEOUT = 5

# TODO: replace it with TimeoutHandler
_api_timeout_config_data = aliyunsdkcore.utils._load_json_from_data_dir("timeout_config.json")

logger = logging.getLogger(__name__)


class AcsClient:
    LOG_FORMAT = '%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s'

    def __init__(
            self,
            ak=None,
            secret=None,
            region_id="cn-hangzhou",
            auto_retry=True,
            max_retry_time=None,
            user_agent=None,
            port=80,
            connect_timeout=None,
            timeout=None,
            public_key_id=None,
            private_key=None,
            session_period=3600,
            credential=None,
            debug=False,
            profile_name='default'):
        """
        constructor for AcsClient
        :param ak: String, access key id
        :param secret: String, access key secret
        :param region_id: String, region id
        :param auto_retry: Boolean
        :param max_retry_time: Number
        :return:
        """

        self._new_style_config = ClientConfig(
            max_retry_times=max_retry_time,
            enable_retry=auto_retry,
            access_key_id=ak,
            access_key_secret=secret,
            region_id=region_id,
            user_agent=user_agent,
            http_port=port,
            connection_timeout=connect_timeout,
            read_timeout=timeout,
            # add
            profile_name=profile_name
        )

        self._loaded_new_clients = {}
        self._endpoint_resolver = DefaultEndpointResolver(self)
        self._credentials_provider = self._init_credentials_provider(ak, secret, credential)

    def _init_credentials_provider(self, access_key_id, access_key_secret, legacy_credentials):

        # get credentials provider
        access_key_id = os.environ.get('ALIYUN_ACCESS_KEY_ID') or access_key_id
        access_key_secret = os.environ.get('ALIYUN_ACCESS_KEY_SECRET') or access_key_secret

        if access_key_id and access_key_secret:
            credentials = AccessKeyCredentials(access_key_id, access_key_secret)
            return StaticCredentialsProvider(credentials)

        elif legacy_credentials:
            if isinstance(legacy_credentials, AccessKeyCredential):
                return StaticCredentialsProvider(AccessKeyCredentials(
                    legacy_credentials.access_key_id,
                    legacy_credentials.access_key_secret,
                ))
            elif isinstance(legacy_credentials, StsTokenCredential):
                return StaticCredentialsProvider(SecurityCredentials(
                    legacy_credentials.sts_access_key_id,
                    legacy_credentials.sts_access_key_secret,
                    legacy_credentials.sts_token,
                ))
            elif isinstance(legacy_credentials, RamRoleArnCredential):
                return RamRoleCredentialsProvider(
                    AccessKeyCredentials(
                        legacy_credentials.sts_access_key_id,
                        legacy_credentials.sts_access_key_secret,
                    ),
                    legacy_credentials.role_arn,
                    legacy_credentials.session_role_name,
                )
            elif isinstance(legacy_credentials, EcsRamRoleCredential):
                return InstanceProfileCredentialsProvider(legacy_credentials.role_name)
            elif isinstance(legacy_credentials, RsaKeyPairCredential):
                raise ClientException("Sorry, RsaKeyPairCredential are no longer supported.")
            else:
                raise ClientException("{0} is not a valid credentials type.".format(
                    legacy_credentials.__class__.__name__))

    def get_region_id(self):
        return self._new_style_config.region_id

    def get_access_key(self):
        return self._new_style_config.access_key_id

    def get_access_secret(self):
        return self._new_style_config.access_key_secret

    def is_auto_retry(self):
        return self._new_style_config.enable_retry

    def get_max_retry_num(self):
        return self._new_style_config.max_retry_times

    def get_user_agent(self):
        return self._new_style_config.user_agent

    def set_region_id(self, region):
        return self._new_style_config.region_id

    def set_max_retry_num(self, num):
        self._new_style_config.max_retry_times = num

    def set_auto_retry(self, flag):
        """
        set whether or not the client perform auto-retry
        :param flag: Booleans
        :return: None
        """
        self._new_style_config.enable_retry = flag

    def set_user_agent(self, agent):
        """
        User agent set to client will overwrite the request setting.
        :param agent:
        :return:
        """
        self._new_style_config.user_agent = agent

    def append_user_agent(self, key, value):
        # TODO fix user agent
        pass
        # self._extra_user_agent.update({key: value})

    @staticmethod
    def user_agent_header():
        base = '%s (%s %s;%s)' \
               % ('AlibabaCloud',
                  platform.system(),
                  platform.release(),
                  platform.machine()
                  )
        return base

    @staticmethod
    def default_user_agent():
        default_agent = OrderedDict()
        default_agent['Python'] = platform.python_version()
        default_agent['Core'] = __import__('aliyunsdkcore').__version__
        default_agent['python-requests'] = __import__(
            'aliyunsdkcore.vendored.requests.__version__', globals(), locals(),
            ['vendored', 'requests', '__version__'], 0).__version__

        return CaseInsensitiveDict(default_agent)

    def client_user_agent(self):
        client_user_agent = {}
        if self.get_user_agent() is not None:
            client_user_agent.update({'client': self.get_user_agent()})
        else:
            client_user_agent.update(self._extra_user_agent)

        return CaseInsensitiveDict(client_user_agent)

    def get_port(self):
        return self._new_style_config.http_port

    def get_location_service(self):
        return None

    @staticmethod
    def merge_user_agent(default_agent, extra_agent):
        if default_agent is None:
            return extra_agent

        if extra_agent is None:
            return default_agent
        user_agent = default_agent.copy()
        for key, value in extra_agent.items():
            if key not in default_agent:
                user_agent[key] = value
        return user_agent

    def handle_extra_agent(self, request):
        client_agent = self.client_user_agent()
        request_agent = request.request_user_agent()

        if client_agent is None:
            return request_agent

        if request_agent is None:
            return client_agent
        for key in request_agent:
            if key in client_agent:
                client_agent.pop(key)
        client_agent.update(request_agent)
        return client_agent

    def implementation_of_do_action(self, request, signer=None):
        # keep compatible
        warnings.warn(
            "implementation_of_do_action() method is deprecated",
            DeprecationWarning)

        context = self._handle_request_in_new_style(request, raise_exception=False)
        return (context.http_response.status, context.http_response.headers,
                context.http_response.content)

    def _get_new_style_request(self, acs_request):
        return acs_request

    def _get_new_style_config(self, acs_request):
        self._new_style_config._update_config(acs_request._new_style_config)

        return self._new_style_config

        # return alibabacloud.client.get_merged_client_config([
        #     self._new_style_config,
        #     acs_request._new_style_config,
        # ])

    def _get_new_style_client(self, acs_request):
        key = acs_request.get_product()
        key += '@' + acs_request.get_version()
        key += '@' + acs_request.get_location_service_code()
        key += '@' + acs_request.get_location_endpoint_type()
        if key not in self._loaded_new_clients:
            config = ClientConfig()
            client = AlibabaCloudClient(
                config,
                credentials_provider=self._credentials_provider
            )
            client.location_service_code = acs_request.get_location_service_code()
            client.location_endpoint_type = acs_request.get_location_service_code()
            client.location_endpoint_type = acs_request.get_location_endpoint_type()
            client.product_code = acs_request.get_product()

            self._loaded_new_clients[key] = client
            self._loaded_new_clients[key].endpoint_resolver = self._endpoint_resolver

        return self._loaded_new_clients[key]

    def _handle_request_in_new_style(self, acs_request, raise_exception=True):
        api_request = self._get_new_style_request(acs_request)
        config = self._get_new_style_config(acs_request)
        new_style_client = self._get_new_style_client(acs_request)
        context = new_style_client._handle_request(api_request, _config=config,
                                                   _raise_exception=raise_exception)
        return context

    def do_action_with_exception(self, acs_request):
        context = self._handle_request_in_new_style(acs_request)
        return context.http_response.content

    def do_action(self, acs_request):
        warnings.warn(
            "do_action() method is deprecated, please use do_action_with_exception() instead.",
            DeprecationWarning)
        context = self._handle_request_in_new_style(acs_request, raise_exception=False)
        return context.http_response.content

    def get_response(self, acs_request):
        return self.implementation_of_do_action(acs_request)

    def add_endpoint(self, region_id, product_code, endpoint):
        self._endpoint_resolver.put_endpoint_entry(
            region_id, product_code, endpoint)
