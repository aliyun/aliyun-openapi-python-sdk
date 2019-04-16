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

import json
import time
from mock import MagicMock, patch
from base import SDKTestBase
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceHistoryEventsRequest import \
    DescribeInstanceHistoryEventsRequest
from aliyunsdkecs.request.v20140526.DescribeDisksRequest import DescribeDisksRequest
from aliyunsdkecs.request.v20140526.AttachDiskRequest import AttachDiskRequest
from aliyunsdkecs.request.v20140526.CreateDiskRequest import CreateDiskRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from alibabacloud.exceptions import ClientException, ServerException

import aliyunsdkcore.acs_exception.error_code as error_code
import alibabacloud.retry.retry_policy as retry_policy
from alibabacloud.retry.retry_condition import RetryCondition
from alibabacloud.retry.retry_policy_context import RetryPolicyContext


class RetryTest(SDKTestBase):

    def test_no_retry(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           auto_retry=False)

        request = DescribeInstancesRequest()
        request.set_endpoint("somewhere.you.will.never.get")
        config = client._get_new_style_config(request)
        with patch.object(client._get_new_style_client(request, config), "_handle_request",
                          wraps=client._get_new_style_client(request, config)._handle_request) as monkey:
            try:
                client.do_action_with_exception(request)
                assert False
            except ClientException as e:
                self.assertEqual(error_code.SDK_HTTP_ERROR, e.error_code)
        self.assertEqual(1, monkey.call_count)

    def test_default_retry_times(self):

        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)
        request = DescribeInstancesRequest()
        request.set_endpoint("somewhere.you.will.never.get")
        context = client._handle_request_in_new_style(request, raise_exception=False)

        self.assertEqual(3, context.http_request.retries)

    def test_no_retry_on_parameter_invalid(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)
        request = CreateInstanceRequest()
        context = client._handle_request_in_new_style(request, raise_exception=False)
        self.assertEqual(0, context.http_request.retries)
        self.assertTrue(isinstance(context.exception, ServerException))

    def test_retry_with_client_token(self):
        pass

    def test_retry_with_client_token_set(self):
        pass

    def test_invalid_max_retry_times(self):
        client = AcsClient(self.access_key_id,
                           self.access_key_secret,
                           self.region_id,
                           max_retry_time=-1)
        from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import \
            DescribeInstancesRequest
        request = DescribeInstancesRequest()
        request.set_endpoint("somewhere.you.will.never.get")

        try:
            response = client.do_action_with_exception(request)
            assert False
        except ClientException as e:
            self.assertEqual("SDK.InvalidParameter", e.error_code)
            self.assertEqual("max_retry_times should be a positive integer.",
                             e.error_message)

    def test_set_max_retry_times(self):
        client = AcsClient(self.access_key_id,
                           self.access_key_secret,
                           self.region_id,
                           max_retry_time=8)
        request = DescribeInstancesRequest()
        request.set_endpoint("somewhere.you.will.never.get")

        def no_sleep(delay):
            pass

        with patch.object(time, "sleep", no_sleep):
            context = client._handle_request_in_new_style(request, raise_exception=False)
            self.assertEqual(8, context.http_request.retries)

    def test_retry_conditions(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)

        default_retry_policy = retry_policy.get_default_retry_policy()

        def CE(code):
            return ClientException(code, "some error")

        def SE(code):
            return ServerException(code, "some error")

        def _get_retryable(*conditions):
            context = RetryPolicyContext(*conditions)
            return default_retry_policy.should_retry(context)

        def _assert_not_retryable(*conditions):
            retryable = _get_retryable(*conditions)
            self.assertTrue(retryable & RetryCondition.NO_RETRY)

        def _assert_retryable(*conditions):
            retryable = _get_retryable(*conditions)
            self.assertFalse(retryable & RetryCondition.NO_RETRY)

        def _assert_retryable_with_client_token(request):
            conditions = [request, SE("InternalError"), 0, 500]
            retryable = _get_retryable(*conditions)
            self.assertTrue(retryable &
                            RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF)

        def _assert_not_retryable_with_client_token(request):
            conditions = [request, SE("InternalError"), 0, 500]
            retryable = _get_retryable(*conditions)
            self.assertFalse(retryable & RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF)
        # retryable
        acs_request = DescribeInstancesRequest()
        retryable_request = client._get_new_style_request(acs_request)
        config = client._get_new_style_config(acs_request)
        retryable_client = client._get_new_style_client(acs_request, config)

        timeout_exception = CE(error_code.SDK_HTTP_ERROR)
        invalid_param_excpetion = SE("MissingParameter")
        unknown_error = SE(error_code.SDK_UNKNOWN_SERVER_ERROR)
        internal_error = SE("InternalError")
        product_code = retryable_client.product_code.lower()
        product_version = retryable_client.product_version
        _assert_retryable(retryable_request, timeout_exception, 0, 500, product_code, product_version)
        _assert_retryable(retryable_request, timeout_exception, 2, 500, product_code, product_version)
        _assert_retryable(retryable_request, unknown_error, 0, 500, product_code, product_version)
        _assert_retryable(retryable_request, unknown_error, 0, 502, product_code, product_version)
        _assert_retryable(retryable_request, unknown_error, 0, 503, product_code, product_version)
        _assert_retryable(retryable_request, unknown_error, 0, 504, product_code, product_version)
        _assert_retryable(retryable_request, internal_error, 0, 500, product_code, product_version)
        _assert_retryable(retryable_request, SE("Throttling"), 0, 400, product_code, product_version)
        _assert_retryable(retryable_request, SE("ServiceUnavailable"), 0, 503, product_code, product_version)
        _assert_not_retryable(retryable_request, invalid_param_excpetion, 0, 400, product_code, product_version)
        _assert_not_retryable(retryable_request, timeout_exception, 3, 500, product_code, product_version)
        _assert_not_retryable(retryable_request, SE("InvalidAccessKeyId.NotFound"), 0, 404, product_code, product_version)

        acs_request = DescribeInstanceHistoryEventsRequest()
        request1 = client._get_new_style_request(acs_request)

        config = self.client._get_new_style_config(acs_request)
        client1 = self.client._get_new_style_client(acs_request, config)
        product_code = client1.product_code.lower()
        product_version = client1.product_version
        _assert_retryable(request1, SE("ServiceUnavailable"), 0, 503, product_code, product_version)

        acs_request = DescribeDisksRequest()
        request2 = client._get_new_style_request(acs_request)

        config = self.client._get_new_style_config(acs_request)
        client2 = self.client._get_new_style_client(acs_request, config)
        product_code = client2.product_code.lower()
        product_version = client2.product_version

        _assert_retryable(request2, SE("ServiceUnavailable"), 0, 503, product_code, product_version)
        # no_retry
        acs_request = AttachDiskRequest()
        no_retry_request = client._get_new_style_request(acs_request)
        config = self.client._get_new_style_config(acs_request)
        no_retry_client = self.client._get_new_style_client(acs_request, config)

        product_code = no_retry_client.product_code.lower()
        product_version = no_retry_client.product_version

        _assert_not_retryable(no_retry_request, timeout_exception, 0, 500, product_code, product_version)
        _assert_not_retryable(no_retry_request, unknown_error, 0, 504, product_code, product_version)
        _assert_not_retryable(no_retry_request, invalid_param_excpetion, 0, 400, product_code, product_version)

        # _assert_retryable_with_client_token(CreateInstanceRequest())
        # _assert_retryable_with_client_token(CreateDiskRequest())
        # _assert_retryable_with_client_token(RunInstancesRequest())
        # _assert_not_retryable_with_client_token(AttachDiskRequest())
        # _assert_not_retryable_with_client_token(DescribeInstancesRequest())

    def test_normal_backoff(self):
        client = AcsClient(self.access_key_id,
                           self.access_key_secret,
                           self.region_id,
                           max_retry_time=10)
        request = DescribeInstancesRequest()
        request.set_endpoint("somewhere.you.will.never.get")

        globals()["_test_compute_delay"] = []

        def record_sleep(delay):
            global _test_compute_delay
            _test_compute_delay.append(delay)

        with patch.object(time, "sleep", wraps=record_sleep) as monkey:
            try:
                client.do_action_with_exception(request)
                assert False
            except ClientException as e:
                self.assertEqual(error_code.SDK_HTTP_ERROR, e.error_code)
        # self.assertEqual(10, monkey.call_count)
        self.assertEqual([0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4, 12.8, 20.0, 20.0],
                         _test_compute_delay)

    def test_throttled_backoff(self):
        # mock ServerErrorHandler的结果
        def _handle_response(context):
            context.exception = ServerException("Throttling", "some error")
        client = AcsClient(self.access_key_id,
                           self.access_key_secret,
                           self.region_id,
                           max_retry_time=10)
        acs_request = DescribeInstancesRequest()
        api_request = client._get_new_style_request(acs_request)
        config = client._get_new_style_config(acs_request)
        new_style_client = client._get_new_style_client(acs_request, config)
        globals()["_test_compute_delay"] = []
        def record_sleep(delay):
            global _test_compute_delay
            _test_compute_delay.append(delay)

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
            PrepareHandler(),
            CredentialsHandler(),
            SignerHandler(),
            TimeoutConfigReader(),
            LogHandler(),
            EndpointHandler(),
            RetryHandler(),
            ServerErrorHandler(),
            HttpHandler(),
        ]

        new_style_client.handlers = DEFAULT_HANDLERS

        with patch.object(time, "sleep", wraps=record_sleep) as monkey:
            with patch.object(ServerErrorHandler, "handle_response", wraps=_handle_response):
                try:
                    new_style_client._handle_request(api_request)
                    assert False
                except ServerException as e:
                    self.assertEqual("Throttling", e.error_code)
        self.assertEqual(10, monkey.call_count)
        self.assertEqual(10, len(_test_compute_delay))
