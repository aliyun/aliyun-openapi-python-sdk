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

from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceHistoryEventsRequest import \
    DescribeInstanceHistoryEventsRequest
from aliyunsdkecs.request.v20140526.DescribeDisksRequest import DescribeDisksRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkram.request.v20150501.ListUsersRequest import ListUsersRequest

from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException

from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader


class TimeoutTest(SDKTestBase):

    def _patch_context(self, client, acs_request):
        api_request = client._get_new_style_request(acs_request)
        config = client._get_new_style_config(acs_request)
        new_style_client = client._get_new_style_client(acs_request, config)

        from alibabacloud.handlers import RequestContext
        from alibabacloud.request import HTTPRequest

        context = RequestContext(api_request=api_request, http_request=HTTPRequest(),
                                 config=new_style_client.config, client=new_style_client,
                                 retry_flag=False)
        return context

    def test_default_timeout(self):
        client = AcsClient(self.access_key_id,
                           self.access_key_secret,
                           self.region_id,
                           auto_retry=False)
        acs_request = DescribeInstancesRequest()

        context = self._patch_context(client, acs_request)

        timeout_handler = TimeoutConfigReader()
        timeout_handler.handle_request(context)

        self.assertEqual((5, 10), context.http_request.timeout)

    def test_client_customized_timeout(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           timeout=7, connect_timeout=8, auto_retry=False)
        acs_request = DescribeInstancesRequest()

        context = self._patch_context(client, acs_request)

        timeout_handler = TimeoutConfigReader()
        timeout_handler.handle_request(context)

        self.assertEqual((8, 7), context.http_request.timeout)

    def test_read_timeout_priority(self):
        # read config
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           timeout=20, auto_retry=False)
        acs_request = RunInstancesRequest()
        context = self._patch_context(client, acs_request)
        timeout_handler = TimeoutConfigReader()
        timeout_handler.handle_request(context)
        self.assertEqual((5, 20), context.http_request.timeout)
        # read file
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           auto_retry=False)
        acs_request = RunInstancesRequest()
        context = self._patch_context(client, acs_request)
        timeout_handler = TimeoutConfigReader()
        timeout_handler.handle_request(context)
        self.assertEqual((5, 86), context.http_request.timeout)

    def test_connect_timeout_priority(self):
        # read config
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           connect_timeout=20, auto_retry=False)
        acs_request = RunInstancesRequest()
        context = self._patch_context(client, acs_request)
        timeout_handler = TimeoutConfigReader()
        timeout_handler.handle_request(context)
        self.assertEqual((20, 86), context.http_request.timeout)
        # read file
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           auto_retry=False)
        acs_request = RunInstancesRequest()
        context = self._patch_context(client, acs_request)
        timeout_handler = TimeoutConfigReader()
        timeout_handler.handle_request(context)
        self.assertEqual((5, 86), context.http_request.timeout)
