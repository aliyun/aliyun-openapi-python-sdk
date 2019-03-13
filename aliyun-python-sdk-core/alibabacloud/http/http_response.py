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
from aliyunsdkcore.http.http_request import HttpRequest
from aliyunsdkcore.http import protocol_type as PT

from aliyunsdkcore.vendored.requests import status_codes
from aliyunsdkcore.utils import parameter_helper as helper

GET = "GET"
PUT = "PUT"
POST = "POST"
DELETE = "DELETE"
HEAD = "HEAD"
OPTIONS = "OPTIONS"

HTTP = "http"
HTTPS = "https"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
logger.addHandler(ch)

XML = 'XML'
JSON = 'JSON'
RAW = 'RAW'
APPLICATION_FORM = 'application/x-www-form-urlencoded'
APPLICATION_XML = 'application/xml'
APPLICATION_JSON = 'application/json'
APPLICATION_OCTET_STREAM = 'application/octet-stream'
TEXT_XML = 'text/xml'


def map_format_to_accept(format):
    if format == XML:
        return APPLICATION_XML
    if format == JSON:
        return APPLICATION_JSON
    return APPLICATION_OCTET_STREAM


def map_accept_to_format(accept):
    if accept.lower() == APPLICATION_XML or accept.lower() == TEXT_XML:
        return XML
    if accept.lower() == APPLICATION_JSON:
        return JSON
    return RAW


class HttpResponse(HttpRequest):
    content_md5 = "Content-MD5"
    content_length = "Content-Length"
    content_type = "Content-Type"

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
        self.host = host,
        self.url = url,
        self.method = method
        self.headers = headers
        self.ssl_enable = False
        if protocol is PT.HTTPS:
            self.ssl_enable = True
        self.key_file = key_file
        self.cert_file = cert_file
        self.port = port
        self.connection = None
        self.timeout = timeout
        self.content = content

    def remove_header_parameter(self, key):
        if key is not None:
            if key in self.__headers:
                self.__headers.pop(key)

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
            current_protocol = 'https://' if self.get_ssl_enabled() else 'http://'

            url = current_protocol + self.get_host() + self.get_url()

            if self.__port != 80:
                url = current_protocol + self.get_host() + ":" + str(self.__port) + self.get_url()

            req = Request(method=self.get_method(), url=url,
                          data=self.content,
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
                              timeout=self.timeout,
                              allow_redirects=False, verify=None, cert=None)

            http_debug = os.environ.get('DEBUG')

            if http_debug is not None and http_debug.lower() == 'sdk':
                # http debug information
                self.do_http_debug(prepped, response)

            return response.status_code, response.headers, response.content
