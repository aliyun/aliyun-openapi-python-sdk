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


class APIRequest:
    pass


class APIResponse:
    pass


class HTTPRequest:
    def __init__(self, accept_format=None, method=None, protocol=None, proxy=None,
                 signature=None,
                 headers=None, url=None, endpoint=None, timeout=None,
                 body=None, enable_retry=None, max_retry_times=None, retries=0, credentials=None):

        self.accept_format = accept_format
        self.body = body
        self.method = method
        self.protocol = protocol
        self.proxy = proxy
        self.port = 80
        self.signature = signature
        self.headers = headers
        self.url = url
        self.timeout = timeout
        self.endpoint = endpoint
        self.enable_retry = enable_retry
        self.max_retry_times = max_retry_times
        self.retries = retries

        self.credentials = credentials


class HTTPResponse:
    def __init__(self, status_code=None, headers=None, content=None):
        self.status_code = status_code
        self.headers = headers
        self.content = content

http_request = HTTPRequest()
