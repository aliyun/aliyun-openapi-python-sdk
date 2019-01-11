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
import time
import warnings
import json
import aliyunsdkcore
import jmespath
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
import aliyunsdkcore.retry.retry_policy as retry_policy
from aliyunsdkcore.retry.retry_condition import RetryCondition
from aliyunsdkcore.retry.retry_policy_context import RetryPolicyContext
import aliyunsdkcore.utils
import aliyunsdkcore.utils.parameter_helper
import aliyunsdkcore.utils.validation

"""
Acs default client module.
"""

DEFAULT_SDK_CONNECTION_TIMEOUT_IN_SECONDS = 10

# TODO: replace it with TimeoutHandler
_api_timeout_config_data = aliyunsdkcore.utils._load_json_from_data_dir("timeout_config.json")


class AcsClient:

    def __init__(
            self,
            ak=None,
            secret=None,
            region_id="cn-hangzhou",
            auto_retry=True,
            max_retry_time=None,
            user_agent=None,
            port=80,
            timeout=None,
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

        self._max_retry_num = max_retry_time
        self._auto_retry = auto_retry
        self._ak = ak
        self._secret = secret
        self._region_id = region_id
        self._user_agent = user_agent
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
            credential, region_id, self._implementation_of_do_action, debug)
        self._endpoint_resolver = DefaultEndpointResolver(self)

        if self._auto_retry:
            self._retry_policy = retry_policy.get_default_retry_policy(
                max_retry_times=self._max_retry_num)
        else:
            self._retry_policy = retry_policy.NO_RETRY_POLICY

    def get_region_id(self):
        return self._region_id

    def get_access_key(self):
        return self._ak

    def get_access_secret(self):
        return self._secret

    def is_auto_retry(self):
        return self._auto_retry

    def get_max_retry_num(self):
        return self._max_retry_num

    def get_user_agent(self):
        return self._user_agent

    def set_region_id(self, region):
        self._region_id = region

    def set_max_retry_num(self, num):
        self._max_retry_num = num

    def set_auto_retry(self, flag):
        """
        set whether or not the client perform auto-retry
        :param flag: Booleans
        :return: None
        """
        self._auto_retry = flag

    def set_user_agent(self, agent):
        """
        User agent set to client will overwrite the request setting.
        :param agent:
        :return:
        """
        self._user_agent = agent

    def get_port(self):
        return self._port

    def get_location_service(self):
        return None

    def _make_http_response(self, endpoint, request, timeout, specific_signer=None):
        body_params = request.get_body_params()
        if body_params:
            body = urlencode(body_params)
            request.set_content(body)
            request.set_content_type(format_type.APPLICATION_FORM)
        elif request.get_content() and "Content-Type" not in request.get_headers():
            request.set_content_type(format_type.APPLICATION_OCTET_STREAM)
        method = request.get_method()

        signer = self._signer if specific_signer is None else specific_signer
        header, url = signer.sign(self._region_id, request)

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
            timeout=timeout)
        if body_params:
            body = urlencode(request.get_body_params())
            response.set_content(body, "utf-8", format_type.APPLICATION_FORM)
        return response

    def _implementation_of_do_action(self, request, signer=None):
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

        return self._handle_retry_and_timeout(endpoint, request, signer)

    def implementation_of_do_action(self, request, signer=None):
        # keep compatible
        warnings.warn(
            "implementation_of_do_action() method is deprecated",
            DeprecationWarning)

        status, headers, body, exception = self._implementation_of_do_action(request, signer)
        return status, headers, body

    def _add_request_client_token(self, request):
        if hasattr(request, "set_ClientToken") and hasattr(request, "get_ClientToken"):
            client_token = request.get_ClientToken()
            if not client_token:
                # ClientToken has not been set
                client_token = aliyunsdkcore.utils.parameter_helper.get_uuid()  # up to 60 chars
                request.set_ClientToken(client_token)

    def _get_request_timeout(self, request):
        # TODO: replace it with a timeout_handler
        if self._timeout:
            return self._timeout

        if request.get_product() is None:
            return DEFAULT_SDK_CONNECTION_TIMEOUT_IN_SECONDS
        path = '"{0}"."{1}"."{2}"'.format(request.get_product().lower(), request.get_version(),
                                          request.get_action_name())
        timeout = jmespath.search(path, _api_timeout_config_data)
        if timeout is None:
            return DEFAULT_SDK_CONNECTION_TIMEOUT_IN_SECONDS
        else:
            aliyunsdkcore.utils.validation.assert_integer_positive(timeout, "timeout")
            return max(timeout, DEFAULT_SDK_CONNECTION_TIMEOUT_IN_SECONDS)

    def _handle_retry_and_timeout(self, endpoint, request, signer):
        # TODO: replace it with a retry_handler
        # it's a temporary implementation. the long-term plan will be a group a normalized handlers
        # which contains retry_handler and timeout_handler

        # decide whether we should initialize a ClientToken for the request
        retry_policy_context = RetryPolicyContext(request, None, 0, None)
        if self._retry_policy.should_retry(retry_policy_context) & \
                RetryCondition.SHOULD_RETRY_WITH_CLIENT_TOKEN:
            self._add_request_client_token(request)

        request_timeout = self._get_request_timeout(request)

        retryable = RetryCondition.SHOULD_RETRY
        retries = 0

        while True:

            status, headers, body, exception = self._handle_single_request(endpoint,
                                                                           request,
                                                                           request_timeout,
                                                                           signer)
            retry_policy_context = RetryPolicyContext(request, exception, retries, status)
            retryable = self._retry_policy.should_retry(retry_policy_context)
            if retryable & RetryCondition.NO_RETRY:
                break
            retry_policy_context.retryable = retryable
            time_to_sleep = self._retry_policy.compute_delay_before_next_retry(retry_policy_context)
            time.sleep(time_to_sleep / 1000.0)
            retries += 1

        if isinstance(exception, ClientException):
            raise exception

        return status, headers, body, exception

    def _handle_single_request(self, endpoint, request, timeout, signer):
        http_response = self._make_http_response(endpoint, request, timeout, signer)

        exception = None

        # Do the actual network thing
        try:
            status, headers, body = http_response.get_response_object()
        except IOError as e:
            error_message = str(e)
            error_message += "\nEndpoint: " + endpoint
            error_message += "\nProduct: " + str(request.get_product())
            error_message += "\nSdkCoreVersion: " + aliyunsdkcore.__version__
            error_message += "\nHttpUrl: " + str(http_response.get_url())
            error_message += "\nHttpHeaders: " + \
                str(http_response.get_headers())

            exception = ClientException(error_code.SDK_HTTP_ERROR, error_message)
            return None, None, None, exception

        exception = self._get_server_exception(status, body)
        return status, headers, body, exception

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

    def _get_server_exception(self, http_status, response_body):
        request_id = None

        try:
            body_obj = json.loads(response_body.decode('utf-8'))
            request_id = body_obj.get('RequestId')
        except (ValueError, TypeError, AttributeError):
            # in case the response body is not a json string, return the raw
            # data instead
            pass

        if http_status < http_client.OK or http_status >= http_client.MULTIPLE_CHOICES:

            server_error_code, server_error_message = self._parse_error_info_from_response_body(
                response_body.decode('utf-8'))
            return ServerException(
                server_error_code,
                server_error_message,
                http_status=http_status,
                request_id=request_id)

    def do_action_with_exception(self, acs_request):

        # set server response format as json, because this function will
        # parse the response so which format doesn't matter
        acs_request.set_accept_format('JSON')

        status, headers, body, exception = self._implementation_of_do_action(acs_request)

        if exception:
            raise exception

        return body

    def _resolve_endpoint(self, request):
        resolve_request = ResolveEndpointRequest(
            self._region_id,
            request.get_product(),
            request.get_location_service_code(),
            request.get_location_endpoint_type(),
        )
        return self._endpoint_resolver.resolve(resolve_request)

    def do_action(self, acs_request):
        warnings.warn(
            "do_action() method is deprecated, please use do_action_with_exception() instead.",
            DeprecationWarning)
        status, headers, body, exception = self._implementation_of_do_action(acs_request)
        return body

    def get_response(self, acs_request):
        return self.implementation_of_do_action(acs_request)

    def add_endpoint(self, region_id, product_code, endpoint):
        self._endpoint_resolver.put_endpoint_entry(
            region_id, product_code, endpoint)
