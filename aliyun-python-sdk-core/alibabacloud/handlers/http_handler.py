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
    def handle_request(self, context):
        self.do_request(context)

    def handle_response(self, context):
        pass

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

            try:
                response = s.send(prepped, proxies=http_request.proxy,
                                  timeout=http_request.timeout,
                                  allow_redirects=False, verify=None, cert=None)
            except IOError as e:
                from aliyunsdkcore.acs_exception.exceptions import ClientException
                from aliyunsdkcore.acs_exception import error_code
                exception = ClientException(error_code.SDK_HTTP_ERROR, str(e))

                context.exception = exception
                from alibabacloud.request import HTTPResponse
                context.http_response = HTTPResponse()
            else:
                context.http_response = response
