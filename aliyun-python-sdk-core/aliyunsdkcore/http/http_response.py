# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

import os
from aliyunsdkcore.vendored.requests import Request, Session
from aliyunsdkcore.vendored.requests.packages import urllib3
from aliyunsdkcore.http.http_request import HttpRequest
from aliyunsdkcore.http import protocol_type as PT

DEFAULT_CONNECT_TIMEOUT = 5


class HttpResponse(HttpRequest):
    def __init__(
            self,
            host="",
            url="/",
            method="GET",
            headers={},
            protocol=PT.HTTP,
            content=None,
            port=None,
            key_file=None,
            cert_file=None,
            timeout=None):
        HttpRequest.__init__(
            self,
            host=host,
            url=url,
            method=method,
            headers=headers)
        self.__ssl_enable = False
        if protocol is PT.HTTPS:
            self.__ssl_enable = True
        self.__key_file = key_file
        self.__cert_file = cert_file
        self.__port = port
        self.__connection = None
        self._timeout = timeout
        self.set_body(content)

    def set_ssl_enable(self, enable):
        self.__ssl_enable = enable

    def get_ssl_enabled(self):
        return self.__ssl_enable

    def get_response_object(self):
        with Session() as s:
            current_protocol = 'https://' if self.get_ssl_enabled() else 'http://'

            url = current_protocol + self.get_host() + self.get_url()

            if self.__port != 80:
                url = current_protocol + self.get_host() + ":" + str(self.__port) + self.get_url()

            req = Request(method=self.get_method(), url=url,
                          data=self.get_body(),
                          headers=self.get_headers(),
                          )
            prepped = s.prepare_request(req)

            proxy_https = os.environ.get('HTTPS_PROXY') or os.environ.get(
                'https_proxy')
            proxy_http = os.environ.get(
                'HTTP_PROXY') or os.environ.get('http_proxy')

            proxies = {
                "http": proxy_http,
                "https": proxy_https,
            }
            # ignore the warning-InsecureRequestWarning
            urllib3.disable_warnings()
            response = s.send(prepped, proxies=proxies,
                              timeout=(DEFAULT_CONNECT_TIMEOUT, self._timeout),
                              allow_redirects=False, verify=None, cert=None)
            return response.status_code, response.headers, response.content
