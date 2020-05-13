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
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
import aliyunsdkcore.acs_exception.error_code as error_code
import aliyunsdkcore.retry.retry_policy as retry_policy
from aliyunsdkcore.retry.retry_condition import RetryCondition
from aliyunsdkcore.retry.retry_policy_context import RetryPolicyContext


class RetryTest(SDKTestBase):

    def test_no_retry(self):

        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           auto_retry=False)
        request = DescribeInstancesRequest()
        request.set_endpoint("somewhere.you.will.never.get")
        with patch.object(client, "_handle_single_request",
                          wraps=client._handle_single_request) as monkey:
            try:
                client.do_action_with_exception(request)
                assert False
            except ClientException as e:
                self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
        self.assertEqual(1, monkey.call_count)

    def test_default_retry(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)
        request = DescribeInstancesRequest()
        request.set_endpoint("somewhere.you.will.never.get")

        def no_sleep(delay):
            pass

        with patch.object(time, "sleep", no_sleep):

            with patch.object(client, "_handle_single_request",
                              wraps=client._handle_single_request) as monkey:
                try:
                    client.do_action_with_exception(request)
                    assert False
                except ClientException as e:
                    self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
            self.assertEqual(4, monkey.call_count)

    def test_default_retry_times(self):

        def no_sleep(delay):
            pass

        with patch.object(time, "sleep", no_sleep):

            # test 3 retries
            globals()['_test_retry_times'] = 0
            client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)
            orginal_func = client._handle_single_request

            def _handle_single_request(*args, **kwargs):
                global _test_retry_times
                if _test_retry_times < 3:
                    _test_retry_times += 1
                    return (
                        None,
                        None,
                        None,
                        ClientException(error_code.SDK_HTTP_ERROR, "some error"),
                    )
                else:
                    return orginal_func(*args, **kwargs)

            request = DescribeInstancesRequest()
            with patch.object(client, "_handle_single_request",
                              wraps=_handle_single_request) as monkey:
                client.do_action_with_exception(request)
            self.assertEqual(4, monkey.call_count)

            # test 2 retries
            globals()['_test_retry_times'] = 0
            client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)
            orginal_func = client._handle_single_request

            def _handle_single_request(*args, **kwargs):
                global _test_retry_times
                if _test_retry_times < 2:
                    _test_retry_times += 1
                    return (
                        None,
                        None,
                        None,
                        ClientException(error_code.SDK_HTTP_ERROR, "some error"),
                    )
                else:
                    return orginal_func(*args, **kwargs)

            request = DescribeInstancesRequest()
            with patch.object(client, "_handle_single_request",
                              wraps=_handle_single_request) as monkey:
                client.do_action_with_exception(request)
            self.assertEqual(3, monkey.call_count)

            # test 1 retries
            globals()['_test_retry_times'] = 0
            client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)
            orginal_func = client._handle_single_request

            def _handle_single_request(*args, **kwargs):
                global _test_retry_times
                if _test_retry_times < 1:
                    _test_retry_times += 1
                    return (
                        None,
                        None,
                        None,
                        ClientException(error_code.SDK_HTTP_ERROR, "some error"),
                    )
                else:
                    return orginal_func(*args, **kwargs)

            request = DescribeInstancesRequest()
            with patch.object(client, "_handle_single_request",
                              wraps=_handle_single_request) as monkey:
                response = client.do_action_with_exception(request)
                obj = json.loads(response.decode('utf8'))
                self.assertTrue('PageNumber' in obj)
                self.assertTrue('Instances' in obj)
        self.assertEqual(2, monkey.call_count)

    def test_no_retry_on_parameter_invalid(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)
        request = CreateInstanceRequest()
        with patch.object(client, "_handle_single_request",
                          wraps=client._handle_single_request) as monkey:
            try:
                client.do_action_with_exception(request)
                assert False
            except ServerException as e:
                self.assertEqual("MissingParameter", e.get_error_code())
        self.assertEqual(1, monkey.call_count)

    def test_retry_with_client_token(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)
        orginal_func = client._handle_single_request

        request = CreateInstanceRequest()
        request.set_ImageId("coreos_1745_7_0_64_30G_alibase_20180705.vhd")
        request.set_InstanceType("ecs.n2.small")

        globals()['_test_client_token'] = None
        globals()['_test_retry_times'] = 0

        def _handle_single_request(endpoint, request, request_timeout, request_connect_timeout,
                                   signer=None):
            global _test_client_token
            global _test_retry_times

            if _test_retry_times > 0:
                assert _test_client_token == request.get_ClientToken()
            _test_retry_times += 0
            _test_client_token = request.get_ClientToken()
            return (
                None,
                None,
                None,
                ClientException(error_code.SDK_HTTP_ERROR, "some error"),
            )

        def no_sleep(delay):
            pass

        with patch.object(time, "sleep", no_sleep):
            with patch.object(client, "_handle_single_request",
                              wraps=_handle_single_request) as monkey:
                try:
                    client.do_action_with_exception(request)
                    assert False
                except ClientException as e:
                    self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
            self.assertEqual(4, monkey.call_count)

    def test_retry_with_client_token_set(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id)
        orginal_func = client._handle_single_request

        request = CreateInstanceRequest()
        request.set_ImageId("coreos_1745_7_0_64_30G_alibase_20180705.vhd")
        request.set_InstanceType("ecs.n2.small")
        request.set_ClientToken("ABCDEFGHIJKLMN")

        globals()['_test_retry_times'] = 0

        def _handle_single_request(endpoint, request, request_timeout, request_connect_timeout,
                                   signer=None):
            global _test_retry_times

            assert "ABCDEFGHIJKLMN" == request.get_ClientToken()
            _test_retry_times += 0
            return (
                None,
                None,
                None,
                ClientException(error_code.SDK_HTTP_ERROR, "some error"),
            )

        def no_sleep(delay):
            pass

        with patch.object(time, "sleep", no_sleep):
            with patch.object(client, "_handle_single_request",
                              wraps=_handle_single_request) as monkey:
                try:
                    client.do_action_with_exception(request)
                    assert False
                except ClientException as e:
                    self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
            self.assertEqual(4, monkey.call_count)

    def test_invalid_max_retry_times(self):
        try:
            client = AcsClient(self.access_key_id,
                               self.access_key_secret,
                               self.region_id,
                               max_retry_time=-1)
            assert False
        except ClientException as e:
            self.assertEqual("SDK.InvalidParameter", e.get_error_code())
            self.assertEqual("max_retry_times should be a positive integer.",
                             e.get_error_msg())

    def test_set_max_retry_times(self):
        client = AcsClient(self.access_key_id,
                           self.access_key_secret,
                           self.region_id,
                           max_retry_time=8)
        request = DescribeInstancesRequest()
        request.set_endpoint("somewhere.you.will.never.get")

        def no_sleep(delay):
            pass

        with patch.object(client, "_handle_single_request",
                          wraps=client._handle_single_request) as monkey:
            with patch.object(time, "sleep", no_sleep):
                try:
                    client.do_action_with_exception(request)
                    assert False
                except ClientException as e:
                    self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
        self.assertEqual(9, monkey.call_count)

    def test_retry_conditions(self):

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

        no_retry_request = AttachDiskRequest()
        retryable_request = DescribeInstancesRequest()

        timeout_exception = CE(error_code.SDK_HTTP_ERROR)
        invalid_param_excpetion = SE("MissingParameter")
        unknown_error = SE(error_code.SDK_UNKNOWN_SERVER_ERROR)
        internal_error = SE("InternalError")

        _assert_retryable(retryable_request, timeout_exception, 0, 500)
        _assert_retryable(retryable_request, timeout_exception, 2, 500)
        _assert_retryable(retryable_request, unknown_error, 0, 500)
        _assert_retryable(retryable_request, unknown_error, 0, 502)
        _assert_retryable(retryable_request, unknown_error, 0, 503)
        _assert_retryable(retryable_request, unknown_error, 0, 504)
        _assert_retryable(retryable_request, internal_error, 0, 500)
        _assert_retryable(retryable_request, SE("Throttling"), 0, 400)
        _assert_retryable(retryable_request, SE("ServiceUnavailable"), 0, 503)
        _assert_retryable(DescribeInstanceHistoryEventsRequest(),
                          SE("ServiceUnavailable"), 0, 503)
        _assert_retryable(DescribeDisksRequest(), SE("ServiceUnavailable"), 0, 503)

        _assert_not_retryable(no_retry_request, timeout_exception, 0, 500)
        _assert_not_retryable(no_retry_request, unknown_error, 0, 504)
        _assert_not_retryable(no_retry_request, invalid_param_excpetion, 0, 400)
        _assert_not_retryable(retryable_request, invalid_param_excpetion, 0, 400)
        _assert_not_retryable(retryable_request, timeout_exception, 3, 500)
        _assert_not_retryable(retryable_request, SE("InvalidAccessKeyId.NotFound"), 0, 404)

        _assert_retryable_with_client_token(CreateInstanceRequest())
        _assert_retryable_with_client_token(CreateDiskRequest())
        _assert_retryable_with_client_token(RunInstancesRequest())
        _assert_not_retryable_with_client_token(AttachDiskRequest())
        _assert_not_retryable_with_client_token(DescribeInstancesRequest())

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
                self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
        self.assertEqual(10, monkey.call_count)
        self.assertEqual([0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4, 12.8, 20.0, 20.0],
                         _test_compute_delay)

    def test_throttled_backoff(self):
        client = AcsClient(self.access_key_id,
                           self.access_key_secret,
                           self.region_id,
                           max_retry_time=10)
        request = DescribeInstancesRequest()

        globals()["_test_compute_delay"] = []

        def record_sleep(delay):
            global _test_compute_delay
            _test_compute_delay.append(delay)

        def _handle_single_request(endpoint, request, request_timeout, request_connect_timeout,
                                   signer=None):
            return 400, {}, None, ServerException("Throttling", "some error")

        client._handle_single_request = _handle_single_request

        with patch.object(time, "sleep", wraps=record_sleep) as monkey:
            try:
                client.do_action_with_exception(request)
                assert False
            except ServerException as e:
                self.assertEqual("Throttling", e.get_error_code())
        self.assertEqual(10, monkey.call_count)
        self.assertEqual(10, len(_test_compute_delay))

        base = 0.5
        for i in range(10):
            min_delay = base / 2.0
            max_delay = base
            self.assertTrue(min_delay < _test_compute_delay[i] < max_delay)
            base *= 2
            if base >= 20:
                base = 20
