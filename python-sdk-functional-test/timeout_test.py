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
        globals()['_test_patch_client_read_timeout'] = None
        globals()['_test_patch_client_connect_timeout'] = None

    def _patch_client(self, client):

        original_make_http_response = client._make_http_response

        def _make_http_response(endpoint, request, read_timeout, connect_timeout,
                                specific_signer=None):
            global _test_patch_client_read_timeout, _test_patch_client_connect_timeout
            _test_patch_client_read_timeout = read_timeout
            _test_patch_client_connect_timeout = connect_timeout
            read_timeout = 0.01
            connect_timeout = 0.01
            return original_make_http_response(endpoint, request, read_timeout, connect_timeout,
                                               specific_signer=None)

        client._make_http_response = _make_http_response

    def _test_timeout(self, client, request, expected_read_timeout, expected_connect_timeout):
        global _test_patch_client_read_timeout, _test_patch_client_connect_timeout
        _test_patch_client_read_timeout = 0
        _test_patch_client_connect_timeout = 0
        request.set_endpoint("somewhere.you.will.never.get")
        with self.assertRaises(ClientException):
            client.do_action_with_exception(request)
        self.assertEqual(expected_read_timeout, _test_patch_client_read_timeout)
        self.assertEqual(expected_connect_timeout, _test_patch_client_connect_timeout)

    def test_request_customized_timeout(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           auto_retry=False)
        descrbe_instance = DescribeInstancesRequest()
        descrbe_instance.set_read_timeout(3)
        descrbe_instance.set_connect_timeout(3)
        self._patch_client(client)
        self._test_timeout(client, descrbe_instance, 3, 3)

    def test_client_customized_timeout(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           timeout=7, connect_timeout=7, auto_retry=False)
        self._patch_client(client)
        self._test_timeout(client, DescribeInstancesRequest(), 7, 7)

    def test_default_request_timeout(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           timeout=96, connect_timeout=96, auto_retry=False)
        self._patch_client(client)
        self._test_timeout(client, CreateInstanceRequest(), 96, 96)

    def test_default_client_timeout(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           auto_retry=False)
        self._patch_client(client)
        self._test_timeout(client, DescribeInstancesRequest(), 10, 5)

    def test_read_timeout_priority(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           timeout=5, auto_retry=False)
        self._patch_client(client)
        create_instance = CreateInstanceRequest()
        create_instance.set_read_timeout(7)
        self._test_timeout(client, create_instance, 7, 5)

    def test_connect_timeout_priority(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           connect_timeout=5, auto_retry=False)
        self._patch_client(client)
        create_instance = CreateInstanceRequest()
        create_instance.set_connect_timeout(7)
        self._test_timeout(client, create_instance, 86, 7)

