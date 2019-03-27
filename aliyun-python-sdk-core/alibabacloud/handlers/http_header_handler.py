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
from alibabacloud.utils import parameter_helper as helper
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode


class HttpHeaderHandler(RequestHandler):
    """
    处理http_request的header的内容,便于后续
    """
    content_md5 = "Content-MD5"
    content_length = "Content-Length"
    content_type = "Content-Type"

    def handle_request(self, context):
        api_request = context.api_request
        # access_key_id = context.credentials.access_key_id if context.credentials.access_key_id \
        #     else ''
        # access_key_secret = context.credentials.access_key_secret \
        #     if context.credentials.access_key_secret else ''
        #
        # signed_header = api_request.get_signed_header(context.config.region_id,
        #                                               access_key_id,
        #                                               access_key_secret)
        headers = context.http_request.headers
        body_params = api_request.get_body_params()
        if body_params:
            body = urlencode(body_params)
            headers = self.modify_http_body(headers, body, "utf-8",
                                            'application/x-www-form-urlencoded')
        context.http_request.headers = headers

    def handle_response(self, context):
        # context 实际是http_request
        pass

    def modify_http_body(self, headers, body, encoding, format='RAW'):
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
