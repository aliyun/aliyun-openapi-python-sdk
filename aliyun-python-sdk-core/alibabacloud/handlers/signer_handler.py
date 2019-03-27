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
from alibabacloud.signer import Signer

from alibabacloud.utils import parameter_helper as helper
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode


class SignerHandler(RequestHandler):
    content_md5 = "Content-MD5"
    content_length = "Content-Length"
    content_type = "Content-Type"
    """
    处理signature，headers,params
    """

    def handle_request(self, context):
        http_request = context.http_request
        api_request = context.api_request

        credentials = http_request.credentials

        signature, headers, params = Signer().sign(credentials, context)
        # TODO fix other headers
        http_request.signature = signature
        http_request.params = params
        # modify headers
        body_params = api_request.get_body_params()
        if body_params:
            body = urlencode(body_params)
            headers = self._modify_http_body(headers, body, "utf-8",
                                            'application/x-www-form-urlencoded')
        context.http_request.headers = headers

        http_request.headers = headers

    def handle_response(self, context):
        pass

    def _modify_http_body(self, headers, body, encoding, format='RAW'):
        # 有body_params ，就是 urlencode 结果的值
        # 没有，就是request的
        if body is None:
            headers.pop(self.content_md5, None)
            headers.pop(self.content_type, None)
            headers.pop(self.content_length, None)
        else:

            str_md5 = helper.md5_sum(body)
            content_length = len(body)
            headers[self.content_md5] = str_md5
            headers[self.content_length] = str(content_length)
            headers[self.content_type] = format
        return headers

