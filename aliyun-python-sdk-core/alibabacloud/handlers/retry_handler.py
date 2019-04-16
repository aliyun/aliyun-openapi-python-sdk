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
from alibabacloud.retry.retry_condition import RetryCondition
from alibabacloud.retry.retry_policy_context import RetryPolicyContext
import alibabacloud.utils.parameter_helper


class RetryHandler(RequestHandler):

    def handle_request(self, context):

        client = context.client
        product_code = client.product_code.lower() if client.product_code else None

        if context.http_request.retries == 0:
            retry_policy_context = RetryPolicyContext(context.api_request, None, 0, None, product_code, client.product_version)
            if context.client.retry_policy.should_retry(retry_policy_context) & \
                    RetryCondition.SHOULD_RETRY_WITH_CLIENT_TOKEN:
                self._add_request_client_token(context.api_request)

    def handle_response(self, context):
        client = context.client
        api_request = context.api_request
        product_code = client.product_code.lower() if client.product_code else None

        retry_policy_context = RetryPolicyContext(api_request, context.exception,
                                                  context.http_request.retries,
                                                  context.http_response.status_code,
                                                  product_code, client.product_version)

        should_retry = context.client.retry_policy.should_retry(retry_policy_context)
        if should_retry & RetryCondition.NO_RETRY:
            context.retry_flag = False
        else:
            retry_policy_context.retryable = should_retry
            context.http_request.retries += 1
            context.retry_flag = True
            context.retry_backoff = context.client.retry_policy.compute_delay_before_next_retry(
                retry_policy_context
            )

    @staticmethod
    def _add_request_client_token(request):
        # TODO implement: add a ClientToken parameter on api_request
        # 新的接口不确定body还是query获取到ClientToken
        client_token = request.params.get('ClientToken')
        if not client_token:
            # ClientToken has not been set
            client_token = alibabacloud.utils.parameter_helper.get_uuid()  # up to 60 chars
            request.set_ClientToken(client_token)