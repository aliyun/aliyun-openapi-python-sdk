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
import warnings
import json
import aliyunsdkcore
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode
from aliyunsdkcore.vendored.six.moves import http_client

from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.acs_exception import error_code, error_msg
from aliyunsdkcore.http.http_response import HttpResponse
from aliyunsdkcore.request import AcsRequest
from aliyunsdkcore.http import format_type
from aliyunsdkcore.auth.signers.signer_factory import SignerFactory
from aliyunsdkcore.request import CommonRequest

from aliyunsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from aliyunsdkcore.endpoint.default_endpoint_resolver import DefaultEndpointResolver


"""
Acs default client module.
"""

DEFAULT_SDK_CONNECTION_TIMEOUT_IN_SECONDS = 10


class AcsClient:

    def __init__(
            self,
            ak=None,
            secret=None,
            region_id="cn-hangzhou",
            auto_retry=True,
            max_retry_time=3,
            user_agent=None,
            port=80,
            timeout=DEFAULT_SDK_CONNECTION_TIMEOUT_IN_SECONDS,
            public_key_id=None,
            private_key=None,
            session_period=3600,
            credential=None,
            debug=False):
        """
        constructor for AcsClient
        :param ak: String, access key id
        :param secret: String, access key secret
        :param region_id: String, region id
        :param auto_retry: Boolean
        :param max_retry_time: Number
        :return:
        """

        self.__max_retry_num = max_retry_time
        self.__auto_retry = auto_retry
        self.__ak = ak
        self.__secret = secret
        self.__region_id = region_id
        self.__user_agent = user_agent
        self._port = port
        self._timeout = timeout
        credential = {
            'ak': ak,
            'secret': secret,
            'public_key_id': public_key_id,
            'private_key': private_key,
            'session_period': session_period,
            'credential': credential,
        }
        self._signer = SignerFactory.get_signer(
            credential, region_id, self.implementation_of_do_action, debug)
        self._endpoint_resolver = DefaultEndpointResolver(self)

    def get_region_id(self):
        """

        :return: String
        """
        return self.__region_id

    def get_access_key(self):
        """

        :return: String
        """
        return self.__ak

    def get_access_secret(self):
        """

        :return: String
        """
        return self.__secret

    def is_auto_retry(self):
        """

        :return:Boolean
        """
        return self.__auto_retry

    def get_max_retry_num(self):
        """

        :return: Number
        """
        return self.__max_retry_num

    def get_user_agent(self):
        return self.__user_agent

    def set_region_id(self, region):
        self.__region_id = region

    def set_max_retry_num(self, num):
        """
        set auto retry number
        :param num: Numbers
        :return: None
        """
        self.__max_retry_num = num

    def set_auto_retry(self, flag):
        """
        set whether or not the client perform auto-retry
        :param flag: Booleans
        :return: None
        """
        self.__auto_retry = flag

    def set_user_agent(self, agent):
        """
        User agent set to client will overwrite the request setting.
        :param agent:
        :return:
        """
        self.__user_agent = agent

    def get_port(self):
        return self._port

    def get_location_service(self):
        return None

    def _make_http_response(self, endpoint, request, specific_signer=None):
        body_params = request.get_body_params()
        if body_params:
            body = urlencode(body_params)
            request.set_content(body)
            request.set_content_type(format_type.APPLICATION_FORM)
        elif request.get_content() and "Content-Type" not in request.get_headers():
            request.set_content_type(format_type.APPLICATION_OCTET_STREAM)
        method = request.get_method()

        signer = self._signer if specific_signer is None else specific_signer
        header, url = signer.sign(self.__region_id, request)

        if self.get_user_agent() is not None:
            header['User-Agent'] = self.get_user_agent()
        if header is None:
            header = {}
        header['x-sdk-client'] = 'python/2.0.0'

        protocol = request.get_protocol_type()
        response = HttpResponse(
            endpoint,
            url,
            method,
            header,
            protocol,
            request.get_content(),
            self._port,
            timeout=self._timeout)
        if body_params:
            body = urlencode(request.get_body_params())
            response.set_content(body, "utf-8", format_type.APPLICATION_FORM)
        return response

    def implementation_of_do_action(self, request, signer=None):
        if not isinstance(request, AcsRequest):
            raise ClientException(
                error_code.SDK_INVALID_REQUEST,
                error_msg.get_msg('SDK_INVALID_REQUEST'))

        # add core version
        core_version = __import__('aliyunsdkcore').__version__
        request.add_header('x-sdk-core-version', core_version)

        if isinstance(request, CommonRequest):
            request.trans_to_acs_request()

        if request.endpoint:
            endpoint = request.endpoint
        else:
            endpoint = self._resolve_endpoint(request)

        http_response = self._make_http_response(endpoint, request, signer)

        # Do the actual network thing
        try:
            status, headers, body = http_response.get_response_object()
            return status, headers, body
        except IOError as e:
            error_message = str(e)
            error_message += "\nEndpoint: " + endpoint
            error_message += "\nProduct: " + str(request.get_product())
            error_message += "\nSdkCoreVersion: " + aliyunsdkcore.__version__
            error_message += "\nHttpUrl: " + str(http_response.get_url())
            error_message += "\nHttpHeaders: " + \
                str(http_response.get_headers())

            raise ClientException(error_code.SDK_HTTP_ERROR, error_message)

    @staticmethod
    def _parse_error_info_from_response_body(response_body):
        error_code_to_return = error_code.SDK_UNKNOWN_SERVER_ERROR
        # TODO handle if response_body is too big
        error_message_to_return = "ServerResponseBody: " + str(response_body)
        try:
            body_obj = json.loads(response_body)
            if 'Code' in body_obj:
                error_code_to_return = body_obj['Code']
            if 'Message' in body_obj:
                error_message_to_return = body_obj['Message']
        except ValueError:
            # failed to parse body as json format
            pass

        return error_code_to_return, error_message_to_return

    def do_action_with_exception(self, acs_request):

        # set server response format as json, because thie function will
        # parse the response so which format doesn't matter
        acs_request.set_accept_format('JSON')

        status, headers, body = self.implementation_of_do_action(acs_request)

        request_id = None

        try:
            body_obj = json.loads(body.decode('utf-8'))
            request_id = body_obj.get('RequestId')
        except (ValueError, TypeError, AttributeError):
            # in case the response body is not a json string, return the raw
            # data instead
            pass

        if status < http_client.OK or status >= http_client.MULTIPLE_CHOICES:

            server_error_code, server_error_message = self._parse_error_info_from_response_body(
                body.decode('utf-8'))
            raise ServerException(
                server_error_code,
                server_error_message,
                http_status=status,
                request_id=request_id)

        return body

    def _resolve_endpoint(self, request):
        resolve_request = ResolveEndpointRequest(
            self.__region_id,
            request.get_product(),
            request.get_location_service_code(),
            request.get_location_endpoint_type(),
        )
        return self._endpoint_resolver.resolve(resolve_request)

    def do_action(self, acs_request):
        warnings.warn(
            "do_action() method is deprecated, please use do_action_with_exception() instead.",
            DeprecationWarning)
        status, headers, body = self.implementation_of_do_action(acs_request)
        return body

    def get_response(self, acs_request):
        return self.implementation_of_do_action(acs_request)

    def add_endpoint(self, region_id, product_code, endpoint):
        self._endpoint_resolver.put_endpoint_entry(
            region_id, product_code, endpoint)
