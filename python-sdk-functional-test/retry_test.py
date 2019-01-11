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

from mock import MagicMock, patch
from base import SDKTestBase
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkcore.acs_exception.exceptions import ClientException
import aliyunsdkcore.acs_exception.error_code as error_code


class RetryTest(SDKTestBase):

    def test_no_retry(self):

        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           auto_retry=False)
        request = DescribeInstancesRequest()
        request.set_endpoint("somewhere.you.will.never.get")
        with patch.object(client, "_handle_single_request") as monkey:
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
        with patch.object(client, "_handle_single_request") as monkey:
            try:
                client.do_action_with_exception(request)
                assert False
            except ClientException as e:
                self.assertEqual(error_code.SDK_HTTP_ERROR, e.get_error_code())
        self.assertEqual(4, monkey.call_count)
