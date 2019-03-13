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


class EndpointHandler(RequestHandler):
    """
    region+产品，必须是request的范畴
    """
    def handle_request(self, context):
        request = context.request
        if request.endpoint is None:
            endpoint = context.config.resolve_endpoint_cls(request)
        context.endpoint = request.endpoint or endpoint

    def handle_response(self, response):
        pass
