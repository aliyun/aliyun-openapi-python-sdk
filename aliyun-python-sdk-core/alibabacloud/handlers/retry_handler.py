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

from alibabacloud.handlers import RequestHandler
import aliyunsdkcore.retry.retry_policy as retry_policy
from aliyunsdkcore.retry.retry_condition import RetryCondition
from aliyunsdkcore.retry.retry_policy_context import RetryPolicyContext
import aliyunsdkcore.utils
import aliyunsdkcore.utils.parameter_helper
import aliyunsdkcore.utils.validation

class RetryHandler(RequestHandler):
    def handle_request(self):
        retry_policy_context = RetryPolicyContext(request, None, 0, None)
        if self._retry_policy.should_retry(retry_policy_context) & \
                RetryCondition.SHOULD_RETRY_WITH_CLIENT_TOKEN:
            self._add_request_client_token(request)

        retries = 0
