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
import sys

from .http import protocol_type
from .http import method_type as mt
from .http import format_type as ft
from .auth.composer import rpc_signature_composer as rpc_signer
from .auth.composer import roa_signature_composer as roa_signer
from .auth.composer import oss_signature_composer as oss_signer
from .auth.utils import md5_tool
from aliyunsdkcore.auth.algorithm import sha_hmac1
from aliyunsdkcore.acs_exception import exceptions
from aliyunsdkcore.acs_exception import error_code
import abc

"""
Acs request model.

Created on 6/15/2015

@author: alex jiang
"""

STYLE_RPC = 'RPC'
STYLE_ROA = 'ROA'
STYLE_OSS = 'OSS'

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


class AcsRequest:
    """
    Acs request base class. This class wraps up common parameters for a request.
    """
    __metaclass__ = abc.ABCMeta

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

    def add_query_param(self, k, v):
        self._params[k] = v

    def add_body_params(self, k, v):
        self._body_params[k] = v

    def get_body_params(self):
        return self._body_params

    def get_uri_pattern(self):
        return self._uri_pattern

    def get_uri_params(self):
        return self._uri_params

    def get_product(self):
        return self._product

    def get_version(self):
        return self._version

    def get_action_name(self):
        return self._action_name

    def get_accept_format(self):
        return self._accept_format

    def get_protocol_type(self):
        return self._protocol_type

    def get_query_params(self):
        return self._params

    def get_method(self):
        return self._method

    def set_uri_pattern(self, pattern):
        self._uri_pattern = pattern

    def set_uri_params(self, params):
        self._uri_params = params

    def set_method(self, method):
        self._method = method

    def set_product(self, product):
        self._product = product

    def set_version(self, version):
        self._version = version

    def set_action_name(self, action_name):
        self._action_name = action_name

    def set_accept_format(self, accept_format):
        self._accept_format = accept_format

    def set_protocol_type(self, protocol_type):
        self._protocol_type = protocol_type

    def set_query_params(self, params):
        self._params = params

    def set_body_params(self, body_params):
        self._body_params = body_params

    def set_content(self, content):
        """

        :param content: ByteArray
        :return:
        """
        self._content = content

    def get_content(self):
        """

        :return: ByteArray
        """
        return self._content

    def get_headers(self):
        """

        :return: Dict
        """
        return self._header

    def set_headers(self, headers):
        """

        :param headers: Dict
        :return:
        """
        self._header = headers

    def add_header(self, k, v):
        self._header[k] = v

    def set_user_agent(self, agent):
        self.add_header('User-Agent', agent)

    def set_location_service_code(self, location_service_code):
        self._location_service_code = location_service_code

    def get_location_service_code(self):
        return self._location_service_code

    def get_location_endpoint_type(self):
        return self._location_endpoint_type

    def set_content_type(self, content_type):
        self.add_header("Content-Type", content_type)

    @abc.abstractmethod
    def get_style(self):
        pass

    @abc.abstractmethod
    def get_url(self, region_id, ak, secret):
        pass

    @abc.abstractmethod
    def get_signed_header(self, region_id, ak, secret):
        pass

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint


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
            signer=sha_hmac1):
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
        self._signer = signer

    def get_style(self):
        return self._style

    def _get_sign_params(self):
        req_params = self.get_query_params()
        if req_params is None:
            req_params = {}
        req_params['Version'] = self.get_version()
        req_params['Action'] = self.get_action_name()
        req_params['Format'] = self.get_accept_format()

        return req_params

    def get_url(self, region_id, ak, secret):
        sign_params = self._get_sign_params()
        if 'RegionId' not in sign_params.keys():
            sign_params['RegionId'] = region_id
        url = rpc_signer.get_signed_url(
            sign_params,
            ak,
            secret,
            self.get_accept_format(),
            self.get_method(),
            self.get_body_params(),
            self._signer)
        return url

    def get_signed_header(self, region_id=None, ak=None, secret=None):
        headers = {}
        for headerKey, headerValue in self.get_headers().items():
            if headerKey.startswith("x-acs-") or headerKey.startswith("x-sdk-"):
                headers[headerKey] = headerValue
        return headers


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
        if headers:
            self._header = headers
        self._uri_pattern = uri_pattern
        self._path_params = path_params

    def get_style(self):
        """

        :return: String
        """
        return self._style

    def get_path_params(self):
        return self._path_params

    def set_path_params(self, path_params):
        self._path_params = path_params

    def add_path_param(self, k, v):
        if self._path_params is None:
            self._path_params = {}
        self._path_params[k] = v

    def _get_sign_params(self):
        req_params = self.get_query_params()
        if req_params is None:
            req_params = {}
        self.add_header("x-acs-version", self.get_version())
        # req_params['Version'] = self.get_version()
        # req_params['Action'] = self.get_action_name()
        # req_params['Format'] = self.get_accept_format()
        return req_params

    def get_signed_header(self, region_id, ak, secret):
        """
        Generate signed header
        :param region_id: String
        :param ak: String
        :param secret: String
        :return: Dict
        """
        sign_params = self._get_sign_params()
        if self.get_content() is not None:
            md5_str = md5_tool.get_md5_base64_str(self.get_content())
            self.add_header('Content-MD5', md5_str)
        if 'RegionId' not in sign_params.keys():
            sign_params['RegionId'] = region_id
            self.add_header('x-acs-region-id', region_id)

        signed_headers = roa_signer.get_signature_headers(
            sign_params,
            ak,
            secret,
            self.get_accept_format(),
            self.get_headers(),
            self.get_uri_pattern(),
            self.get_path_params(),
            self.get_method())
        return signed_headers

    def get_url(self, region_id, ak=None, secret=None):
        """
        Compose request url without domain
        :param region_id: String
        :return: String
        """
        sign_params = self.get_query_params()
        # if region_id not in sign_params.keys():
        #     sign_params['RegionId'] = region_id
        url = roa_signer.get_url(
            self.get_uri_pattern(),
            sign_params,
            self.get_path_params())
        return url


class OssRequest(AcsRequest):
    def __init__(
            self,
            product,
            version,
            action_name,
            location_service_code,
            bucket=None,
            method=None,
            headers=None,
            uri_pattern=None,
            path_params=None,
            protocol=None):
        """

        :param product: String, mandatory
        :param version: String, mandatory
        :param action_name: String, mandatory
        :param bucket: String
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
            'openAPI',
            ft.XML,
            protocol,
            method)
        self.__style = STYLE_OSS
        self.__bucket = bucket
        self.__method = method
        self.__header = headers
        self.__uri_pattern = uri_pattern
        self.__path_params = path_params

    def get_style(self):
        return self.__style

    def get_path_params(self):
        """

        :return: dict
        """
        return self.__path_params

    def set_path_params(self, path_params):
        self.__path_params = path_params

    def add_path_param(self, k, v):
        if self.__path_params is None:
            self.__path_params = {}
        self.__path_params[k] = v

    def __get_sign_params(self):
        req_params = self.get_query_params()
        if req_params is None:
            req_params = {}
        req_params['Version'] = self.get_version()
        req_params['Action'] = self.get_action_name()
        req_params['Format'] = self.get_accept_format()
        return req_params

    def get_signed_header(self, region_id, ak, secret, ):
        """
        Compose signed headers.
        :param region_id: String
        :param ak: String
        :param secret: String
        :return:
        """
        sign_params = self.get_query_params()
        if 'RegionId' not in sign_params.keys():
            sign_params['RegionId'] = region_id
        signed_headers = oss_signer.get_signature_headers(
            sign_params,
            ak,
            secret,
            self.get_accept_format(),
            self.get_headers(),
            self.get_uri_pattern(),
            self.get_path_params(),
            self.get_method(),
            self.__bucket)
        return signed_headers

    def get_url(self, region_id, ak=None, secret=None):
        """
        Generate request url without domain
        :param region_id: String
        :return: String
        """
        sign_params = self.get_query_params()
        if 'RegionId' not in sign_params.keys():
            sign_params['RegionId'] = region_id
        url = oss_signer.get_url(
            sign_params,
            self.get_uri_pattern(),
            self.get_path_params())
        return url


class CommonRequest(AcsRequest):
    def __init__(self, domain=None, version=None, action_name=None, uri_pattern=None, product=None, location_endpoint_type='openAPI'):
        super(CommonRequest, self).__init__(product)

        self.request = None
        self.endpoint = domain
        self._version = version
        self._action_name = action_name
        self._uri_pattern = uri_pattern
        self._product = product
        self._location_endpoint_type = location_endpoint_type,
        self._signer = sha_hmac1
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
            raise exceptions.ClientException(error_code.SDK_INVALID_PARAMS,
                                             'common params [version] is required, cannot be empty')
        if not self._action_name and not self._uri_pattern:
            raise exceptions.ClientException(error_code.SDK_INVALID_PARAMS,
                                             'At least one of [action] and [uri_pattern] has a value')
        if not self.endpoint and not self._product:
            raise exceptions.ClientException(error_code.SDK_INVALID_PARAMS,
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

    def get_url(self, region_id, ak, secret):
        return self.request.get_url(region_id, ak, secret)

    def get_signed_header(self, region_id, ak, secret):
        return self.request.get_signed_header(region_id, ak, secret)

    def fill_params(self):

        self.request.set_uri_pattern(self.get_uri_pattern())

        self.request.set_uri_params(self.get_uri_params())

        self.request.set_method(self.get_method())

        self.request.set_product(self.get_product())

        self.request.set_version(self.get_version())

        self.request.set_action_name(self.get_action_name())

        self.request.set_accept_format(self.get_accept_format())

        self.request.set_protocol_type(self.get_protocol_type())

        self.request.set_query_params(self.get_query_params())

        self.request.set_content(self.get_content())

        self.request.set_headers(self.get_headers())

        self.request.set_location_service_code(self.get_location_service_code())

        self.request.set_body_params(self.get_body_params())

