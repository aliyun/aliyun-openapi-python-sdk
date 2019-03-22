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

    def __init__(self):
        self.api_request = None
        self.http_request = None
        self.api_response = None
        self.http_response = None
        self.exception = None
        self.retry_flag = False
        self.retry_backoff = 0


class RequestHandler:

    def handle_request(self, context):
        pass

    def handle_response(self, context):
        pass
