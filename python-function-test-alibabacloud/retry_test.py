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
                self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
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

        with patch.object(time, "sleep", no_sleep):
            context = client._handle_request_in_new_style(request, raise_exception=False)
            self.assertEqual(8, context.http_request.retries)

    def test_retry_conditions(self):
        pass

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
        # self.assertEqual(10, monkey.call_count)
        self.assertEqual([0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4, 12.8, 20.0, 20.0],
                         _test_compute_delay)

    def test_throttled_backoff(self):
        pass
