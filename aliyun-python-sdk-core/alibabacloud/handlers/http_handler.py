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

from alibabacloud.vendored.requests import Request, Session
from alibabacloud.vendored.requests.packages import urllib3
from alibabacloud.exceptions import ClientException


class HttpHandler(RequestHandler):

    def handle_request(self, context):
        self._do_request(context)

    def handle_response(self, context):
        pass

    def _do_request(self, context):
        http_request = context.http_request
        # modify retry flag
        context.retry_flag = False

        with Session() as s:
            current_protocol = 'http://' if http_request.protocol.lower() == 'http' else 'https://'
            url = current_protocol + context.endpoint + http_request.params
            if http_request.port != 80 or http_request.port != 443:
                url = current_protocol + context.endpoint + ":" + \
                      str(http_request.port) + http_request.params

            http_request.url = url
            req = Request(method=http_request.method, url=http_request.url,
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

                # requests.adapters.DEFAULT_RETRIES = 0
            except IOError as e:
                exception = ClientException(str(e))

                context.exception = exception
                from alibabacloud.request import HTTPResponse
                context.http_response = HTTPResponse()
            else:

                if context.config.enable_http_debug is not None:
                    # http debug information
                    self._do_http_debug(context, response)
                context.http_response = response

    @staticmethod
    def _prepare_http_debug(request, symbol):
        base = ''
        for key, value in request.headers.items():
            base += '\n%s %s : %s' % (symbol, key, value)
        return base

    @staticmethod
    def _do_http_debug(context, response):
        # logger the request
        http_request = context.http_request
        request_base = '\n> %s %s HTTP/1.1' % (http_request.method.upper(), http_request.url)
        request_base += '\n> Host : %s' % http_request.endpoint
        # logger.debug(request_base + self._prepare_http_debug(request, '>'))

        # logger the response
        from alibabacloud.vendored.requests import status_codes
        response_base = '\n< HTTP/1.1 %s %s' % (
            response.status_code, status_codes._codes.get(response.status_code)[0].upper())
        # logger.debug(response_base + self.prepare_http_debug(response, '<'))
