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
import platform

from alibabacloud.handlers import RequestHandler


class URLHandler(RequestHandler):
    """
    处理http_request的url的内容,便于后续
    """
    def handle_request(self, context):
        # pass
        http_request = context.http_request
        api_request = context.api_request
        access_key_id = context.credentials.access_key_id if context.credentials.access_key_id else ''
        access_key_secret = context.credentials.access_key_secret \
            if context.credentials.access_key_secret else ''
        signed_url = api_request.get_url(context.config.region_id,
                                         access_key_id,
                                         access_key_secret)
        print(2222222222, signed_url)
        http_request.url = signed_url
        context.http_request = http_request

        # params = urlencode(context.http_request.parameters)
        # url = '%s?%s' % (url, params)
        # print(url)

    def handle_response(self, context):
        # context 实际是http_request
        pass
