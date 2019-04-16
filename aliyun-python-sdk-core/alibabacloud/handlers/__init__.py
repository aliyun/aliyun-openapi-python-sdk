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


class RequestContext:

    def __init__(self, api_request=None, http_request=None, api_response=None, http_response=None,
                 exception=None, retry_flag=True, retry_backoff=0, config=None, client=None):
        self.api_request = api_request
        self.http_request = http_request
        self.api_response = api_response
        self.http_response = http_response
        self.exception = exception

        self.config = config
        self.client = client
        self.retry_flag = retry_flag
        self.retry_backoff = retry_backoff


class RequestHandler:

    def handle_request(self, context):
        pass

    def handle_response(self, context):
        pass
