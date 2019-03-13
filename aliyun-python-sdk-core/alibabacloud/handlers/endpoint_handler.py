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

    resolve_request_cls = ResolveEndpointRequest
    # TODO client 内部仅仅是再次发送了一次请求，可以再次的优化这个方法
    resolve_endpoint_cls = DefaultEndpointResolver(client)

    def handle_request(self, context):
        request = context.request
        if request.endpoint:
            context.endpoint = request.endpoint
        else:
            context.endpoint = self.resolve_endpoint(context.confi8g.region_id, request)

    def handle_response(self, response):
        pass

    def resolve_endpoint(self, region_id, request):
        resolve_request = self.resolve_request_cls(
            region_id,
            request.get_product(),
            request.get_location_service_code(),
            request.get_location_endpoint_type(),
        )
        return self.resolve_endpoint_cls.resolve(resolve_request)
