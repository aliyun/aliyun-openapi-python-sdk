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


class LogHandler(RequestHandler):

    def handle_request(self, context):
        # log_string = self._get_request_log_string(context.request)
        # context.client.logger.debug(log_string)
        pass

    def handle_response(self, context):
        # log_string = self._get_response_log_string(context.response)
        # context.client.logger.debug(log_string)
        pass

    def _get_request_log_string(self, request):
        pass

    def _get_response_log_string(self, response):
        pass
