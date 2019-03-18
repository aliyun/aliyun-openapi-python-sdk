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
from alibabacloud.http.http_response import HttpResponse
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode


class HttpHandler(RequestHandler):
    """
    获取参数，组装成request
    """
    def handle_request(self, context):
        http_request = HttpResponse(context)
        body_params = context.request.body_params
        if body_params:
            body = urlencode(body_params)
            http_request.set_content(body, "utf-8", 'application/x-www-form-urlencoded')
        context.http_request = http_request

    def handle_response(self, request, response):
        pass

