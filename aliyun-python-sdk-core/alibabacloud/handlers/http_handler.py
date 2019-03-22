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
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode
import os
import logging

from aliyunsdkcore.vendored.requests import Request, Session
from aliyunsdkcore.vendored.requests.packages import urllib3
from aliyunsdkcore.http.http_request import HttpRequest
from aliyunsdkcore.http import protocol_type as PT

from aliyunsdkcore.vendored.requests import status_codes

class HttpHandler(RequestHandler):
    """
    获取参数，组装成request
    """
    def set_content(self, content, encoding, format='RAW'):
        # 有body_params ，就是 urlencode 结果的值
        # 没有，就是request的
        self.content = content
        if content is None:
            self.remove_header_parameter(self.content_md5)
            self.remove_header_parameter(self.content_type)
            self.remove_header_parameter(self.content_length)
            self.content_type = None
            self.encoding = None
        else:
            str_md5 = helper.md5_sum(content)
            content_length = len(content)
            self.headers[self.content_md5] = str_md5
            self.headers[self.content_length] = str(content_length)
            self.headers[self.content_type] = format
            self.encoding = encoding
    def handle_request(self, context):
        http_request = context.http_request
        body_params = context.api_request.get_body_params()
        if body_params:
            body = urlencode(body_params)
            http_request.set_content(body, "utf-8", 'application/x-www-form-urlencoded')
        context.http_request = http_request

    def handle_response(self, context):
        self.do_request(context)

    @staticmethod
    def do_request(context):
        http_request = context.http_request
        with Session() as s:
            current_protocol = 'http://' if http_request.protocol.lower() == 'http' else 'https://'
            # TODO : 最终拼接的是啥，还需要调查下
            url = current_protocol + context.endpoint + http_request.url

            if http_request.port != 80 or http_request.port != 443:
                url = current_protocol + context.endpoint + ":" + \
                      str(http_request.port) + http_request.url

            req = Request(method=http_request.method, url=url,
                          data=http_request.body,
                          headers=http_request.headers,
                          )
            prepped = s.prepare_request(req)

            # ignore the warning-InsecureRequestWarning
            urllib3.disable_warnings()

            response = s.send(prepped, proxies=http_request.proxy,
                              timeout=http_request.timeout,
                              allow_redirects=False, verify=None, cert=None)
            context.http_response = response

