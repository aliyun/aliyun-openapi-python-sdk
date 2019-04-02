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
from alibabacloud.utils import format_type
from aliyunsdkcore.compat import urlencode


class APIRequest:

    def __init__(self, request):
        self.accept_format = 'Json'

        self.style = request._style
        self.action_name = request._action_name

        self.query_params = request._params
        self.protocol = request._protocol_type  # http|https
        self.method = request._method
        self.headers = request._header  # 原本为空，都是组装的
        self.endpoint = request.endpoint
        self.body_params = request._body_params
        self.content = request._content

        # Roa特有的
        if self.style == 'ROA':
            self.uri_pattern = request._uri_pattern
            self.path_params = request._path_params

        body_params = request._body_params
        if body_params:
            # TODO， request.body 必须是json，application/x-www-form-urlencoded,原 SDK是以下的操作

            # FIXME  修正后的操作.APPLICATION_FORM 其实本就应该是get请求的urlencode编码的形式，post还是应该采取json
            # 这里明确几点：
            # 1.body只对post 和put 有效
            # 2.
            allow_methods = ['POST', 'PUT']
            # if self.style == 'ROA' and self.method.upper() in allow_methods:
            if self.method.upper() in allow_methods:
                import json
                body = json.dumps(body_params)
                self.content = body
                self.headers["Content-Type"] = format_type.APPLICATION_JSON

            else:
                body = urlencode(body_params, doseq=True)
                self.content = body
                self.headers["Content-Type"] = format_type.APPLICATION_FORM

            # 把这个URL编码的值赋给content，设置content-type
            # FIXME body is the final bytes to be sent to the server via HTTP
            # content is an application level concept
        elif self.content and "Content-Type" not in self.headers:

            self.headers["Content-Type"] = format_type.APPLICATION_OCTET_STREAM


class APIResponse:
    pass


class HTTPRequest:
    def __init__(self, accept_format=None, method=None, protocol=None, proxy=None,
                 signature=None,
                 headers=None, url=None, endpoint=None, timeout=None,
                 body="", enable_retry=None, max_retry_times=None, retries=0, credentials=None):

        self.accept_format = accept_format
        # TODO， request.body 必须是json
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


class _APIRequest:

    def __init__(self, action_name, http_method, **params):
        self.action_name = action_name
        self.protocol = "https"
        # method 和protocol 是正交的
        # self.http_method = http_method
        self.method = http_method

        self._params = params

    def __getattr__(self, item):
        return self._params[item]
