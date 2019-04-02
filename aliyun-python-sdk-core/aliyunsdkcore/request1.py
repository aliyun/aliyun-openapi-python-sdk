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
import abc
from aliyunsdkcore.vendored.six import add_metaclass

from aliyunsdkcore.http import protocol_type
from aliyunsdkcore.http import method_type as mt
from aliyunsdkcore.http import format_type as ft
# from aliyunsdkcore.auth.composer import rpc_signature_composer as rpc_signer
# from aliyunsdkcore.auth.composer import composer as roa_signer
# from aliyunsdkcore.auth.algorithm import sha_hmac1
from aliyunsdkcore.acs_exception import exceptions
from aliyunsdkcore.acs_exception import error_code
from aliyunsdkcore.vendored.requests.structures import CaseInsensitiveDict


"""
Acs request model.
"""

STYLE_RPC = 'RPC'
STYLE_ROA = 'ROA'

_default_protocol_type = protocol_type.HTTP


def set_default_protocol_type(user_protocol_type):
    global _default_protocol_type

    if user_protocol_type == protocol_type.HTTP or user_protocol_type == protocol_type.HTTPS:
        _default_protocol_type = user_protocol_type
    else:
        raise exceptions.ClientException(
            error_code.SDK_INVALID_PARAMS,
            "Invalid 'protocol_type', should be 'http' or 'https'"
        )


def get_default_protocol_type():
    return _default_protocol_type


@add_metaclass(abc.ABCMeta)
class AcsRequest:
    """
    Acs request base class. This class wraps up common parameters for a request.
    """

    def __init__(self, product, version=None,
                 action_name=None,
                 location_service_code=None,
                 location_endpoint_type='openAPI',
                 accept_format=None,
                 protocol_type=None,
                 method=None):
        """

        :param product:
        :param version:
        :param action_name:
        :param params:
        :param resource_owner_account:
        :param protocol_type:
        :param accept_format:
        :return:
        """
        self._version = version
        self._product = product
        self._action_name = action_name
        self._protocol_type = protocol_type
        if self._protocol_type is None:
            self._protocol_type = _default_protocol_type

        self._accept_format = accept_format
        self._params = {}
        self._method = method
        self._header = {}
        self._body_params = {}
        self._uri_pattern = None
        self._uri_params = None
        self._content = None
        self._location_service_code = location_service_code
        self._location_endpoint_type = location_endpoint_type
        self.add_header('x-sdk-invoke-type', 'normal')
        self.endpoint = None
        self._extra_user_agent = {}
        self.string_to_sign = ''
        self._request_connect_timeout = None
        self._request_read_timeout = None

        from alibabacloud.client import ClientConfig

        self._new_style_config = ClientConfig()
        if self._protocol_type == 'https':
            self._new_style_config.enable_https = True

    def add_query_param(self, k, v):
        self._params[k] = v

    def add_body_params(self, k, v):
        self._body_params[k] = v

    def add_header(self, k, v):
        self._header[k] = v

    def set_user_agent(self, agent):
        self.add_header('User-Agent', agent)

    def append_user_agent(self, key, value):
        self._extra_user_agent.update({key: value})

    def request_user_agent(self):
        request_user_agent = {}
        if 'User-Agent' in self.get_headers():
            request_user_agent.update({
                'request': self.get_headers().get('User-Agent')
            })

        else:
            request_user_agent.update(self._extra_user_agent)

        return CaseInsensitiveDict(request_user_agent)

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint
        self._new_style_config.endpoint = self.endpoint

    def get_connect_timeout(self):
        return self._new_style_config.connection_timeout

    def set_connect_timeout(self, connect_timeout):
        self._new_style_config.connection_timeout = connect_timeout

    def get_read_timeout(self):
        return self._new_style_config.read_timeout

    def set_read_timeout(self, read_timeout):
        self._new_style_config.read_timeout = read_timeout

    # TODO add some
    @property
    def version(self):
        return self._version

    @property
    def product(self):
        return self._product

    @property
    def action_name(self):
        return self._action_name

    @property
    def protocol_type(self):
        return self._protocol_type

    # self._action_name = action_name
    # self._protocol_type = protocol_type
    # if self._protocol_type is None:
    #     self._protocol_type = _default_protocol_type
    #
    # self._accept_format = accept_format
    # self._params = {}
    # self._method = method
    # self._header = {}
    # self._body_params = {}
    # self._uri_pattern = None
    # self._uri_params = None
    # self._content = None
    # self._location_service_code = location_service_code
    # self._location_endpoint_type = location_endpoint_type
    # self.add_header('x-sdk-invoke-type', 'normal')
    # self.endpoint = None
    # self._extra_user_agent = {}


class RpcRequest(AcsRequest):
    """
    Class to compose an RPC style request with.
    """

    def __init__(
            self,
            product,
            version,
            action_name,
            location_service_code=None,
            location_endpoint_type='openAPI',
            format=None,
            protocol=None,
            # signer=sha_hmac1
    ):
        AcsRequest.__init__(
            self,
            product,
            version,
            action_name,
            location_service_code,
            location_endpoint_type,
            format,
            protocol,
            mt.GET)
        self._style = STYLE_RPC


class RoaRequest(AcsRequest):
    """
    Class to compose an ROA style request with.
    """

    def __init__(
            self,
            product,
            version,
            action_name,
            location_service_code=None,
            location_endpoint_type='openAPI',
            method=None,
            headers=None,
            uri_pattern=None,
            path_params=None,
            protocol=None):
        """

        :param product: String, mandatory
        :param version: String, mandatory
        :param action_name: String, mandatory
        :param method: String
        :param headers: Dict
        :param uri_pattern: String
        :param path_params: Dict
        :param protocol: String
        :return:
        """
        AcsRequest.__init__(
            self,
            product,
            version,
            action_name,
            location_service_code,
            location_endpoint_type,
            ft.RAW,
            protocol,
            method)
        self._style = STYLE_ROA
        self._method = method
        if headers is not None:
            self._header = headers
        self._uri_pattern = uri_pattern
        self._path_params = path_params

    def add_path_param(self, k, v):
        if self._path_params is None:
            self._path_params = {}
        self._path_params[k] = v


class CommonRequest(AcsRequest):
    def __init__(self, domain=None, version=None, action_name=None, uri_pattern=None, product=None,
                 location_endpoint_type='openAPI'):
        super(CommonRequest, self).__init__(product)

        self.request = None
        self.endpoint = domain
        self._version = version
        self._action_name = action_name
        self._uri_pattern = uri_pattern
        self._product = product
        self._location_endpoint_type = location_endpoint_type
        # self._signer = sha_hmac1
        self.add_header('x-sdk-invoke-type', 'common')
        self._path_params = None
        self._method = "GET"

    def get_path_params(self):
        return self._path_params

    def set_path_params(self, path_params):
        self._path_params = path_params

    def add_path_param(self, k, v):
        if self._path_params is None:
            self._path_params = {}
        self._path_params[k] = v

    def set_domain(self, domain):
        self.endpoint = domain

    def get_domain(self):
        return self.endpoint

    def set_version(self, version):
        self._version = version

    def get_version(self):
        return self._version

    def set_action_name(self, action_name):
        self._action_name = action_name

    def get_action_name(self):
        return self._action_name

    def set_uri_pattern(self, uri_pattern):
        self._uri_pattern = uri_pattern

    def get_uri_pattern(self):
        return self._uri_pattern

    def set_product(self, product):
        self._product = product

    def get_product(self):
        return self._product

    def trans_to_acs_request(self):
        if not self._version:
            raise exceptions.ClientException(
                error_code.SDK_INVALID_PARAMS,
                'common params [version] is required, cannot be empty')
        if not self._action_name and not self._uri_pattern:
            raise exceptions.ClientException(
                error_code.SDK_INVALID_PARAMS,
                'At least one of [action] and [uri_pattern] has a value')
        if not self.endpoint and not self._product:
            raise exceptions.ClientException(
                error_code.SDK_INVALID_PARAMS,
                'At least one of [domain] and [product_name] has a value')

        if self._uri_pattern:
            self._style = STYLE_ROA
            self.request = RoaRequest(product=self.get_product(), version=self.get_version(),
                                      action_name=self.get_action_name(),
                                      location_endpoint_type=self.get_location_endpoint_type()
                                      )
            self.fill_params()
        else:
            self._style = STYLE_RPC
            self.request = RpcRequest(product=self.get_product(), version=self.get_version(),
                                      action_name=self.get_action_name(),
                                      location_endpoint_type=self.get_location_endpoint_type(),
                                      )
            self.fill_params()

    def get_style(self):
        return self._style

    def fill_params(self):

        self.request._uri_pattern = self._uri_pattern

        self.request._uri_params = self._uri_params

        if self.get_style() == STYLE_ROA:
            self.request._path_params = self._path_params

        self.request._method = self._method

        self.request._product = self._product

        self.request._version = self._version

        self.request._action_name = self._action_name

        self.request._accept_format = self._accept_format

        self.request._protocol_type = self._protocol_type

        self.request._query_params = self._query_params

        self.request._content = self._content

        self.request._headers = self._headers

        self.request._location_service_code = self._location_service_code

        self.request._body_params = self._body_params

        self.request._endpoint = self.endpoint
