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

from base import SDKTestBase
from mock import MagicMock, patch
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.http.http_response import HttpResponse

from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceHistoryEventsRequest import \
    DescribeInstanceHistoryEventsRequest
from aliyunsdkecs.request.v20140526.DescribeDisksRequest import DescribeDisksRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkram.request.v20150501.ListUsersRequest import ListUsersRequest

from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException


class TimeoutTest(SDKTestBase):

    def setUp(self):
        globals()['_test_patch_client_timeout'] = None

    def _patch_client(self, client):

        original_make_http_response = client._make_http_response

        def _make_http_response(endpoint, request, timeout, specific_signer=None):
            global _test_patch_client_timeout
            _test_patch_client_timeout = timeout
            timeout = 0.01
            return original_make_http_response(endpoint, request, timeout,
                                               specific_signer=None)

        client._make_http_response = _make_http_response

    def _test_timeout(self, client, request, expected_timeout):
        global _test_patch_client_timeout
        _test_patch_client_timeout = 0
        request.set_endpoint("somewhere.you.will.never.get")
        with self.assertRaises(ClientException):
            client.do_action_with_exception(request)
        self.assertEqual(expected_timeout, _test_patch_client_timeout)

    def test_default_time_out(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           auto_retry=False)
        self._patch_client(client)
        self._test_timeout(client, DescribeInstancesRequest(), 10)
        self._test_timeout(client, CreateInstanceRequest(), 86)
        self._test_timeout(client, DescribeInstanceHistoryEventsRequest(), 19)
        self._test_timeout(client, DescribeDisksRequest(), 19)
        self._test_timeout(client, RunInstancesRequest(), 86)
        self._test_timeout(client, ListUsersRequest(), 10)  # not configured, using default

    def test_user_set_time_out(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           timeout=20, auto_retry=False)
        self._patch_client(client)
        self._test_timeout(client, DescribeInstancesRequest(), 20)
        self._test_timeout(client, CreateInstanceRequest(), 20)
        self._test_timeout(client, DescribeInstanceHistoryEventsRequest(), 20)
        self._test_timeout(client, DescribeDisksRequest(), 20)
        self._test_timeout(client, RunInstancesRequest(), 20)
        self._test_timeout(client, ListUsersRequest(), 20)
