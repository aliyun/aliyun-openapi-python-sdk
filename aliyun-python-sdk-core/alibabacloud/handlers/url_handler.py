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
        http_request = context.http_request
        api_request = context.api_request
        signed_url = api_request.get_url(context.config.region_id,
                                         context.config.access_key_id,
                                         context.config.access_key_secret)
        http_request.url = signed_url
        context.http_request = http_request

    def handle_response(self, context):
        # context 实际是http_request
        pass
