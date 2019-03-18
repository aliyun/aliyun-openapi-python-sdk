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
import logging

from aliyunsdkcore.vendored.requests import Request, Session
from aliyunsdkcore.vendored.requests.packages import urllib3
from aliyunsdkcore.http import protocol_type as PT

from aliyunsdkcore.vendored.requests import status_codes
from aliyunsdkcore.http import format_type
from aliyunsdkcore.utils import parameter_helper as helper


class HttpResponse:
    content_md5 = "Content-MD5"
    content_length = "Content-Length"
    content_type = "Content-Type"

    def __init__(
            self,
            host="",
            url="/",
            method="GET",
            headers={},
            protocol='http',
            content=None,
            port=None,
            key_file=None,
            cert_file=None,
            timeout=None):
        self.host = host,
        self.url = url,
        self.method = method
        self.headers = headers
        self.ssl_enable = False
        if protocol is 'https':
            self.ssl_enable = True
        self.key_file = key_file
        self.cert_file = cert_file
        self.port = port
        self.connection = None
        self.timeout = timeout
        self.content = content

    def remove_header_parameter(self, key):
        if key is not None:
            if key in self.headers:
                self.headers.pop(key)

    def set_content(self, content, encoding, format=RAW):
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

    def get_response_object(self):
        with Session() as s:
            current_protocol = 'https://' if self.ssl_enable else 'http://'
            # TODO : 最终拼接的是啥，还需要调查下
            url = current_protocol + self.host + self.url

            if self.port != 80:
                url = current_protocol + self.host + ":" + str(self.port) + self.url

            req = Request(method=self.method, url=url,
                          data=self.content,
                          headers=self.headers,
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
                              timeout=self.timeout,
                              allow_redirects=False, verify=None, cert=None)
            return response.status_code, response.headers, response.content
