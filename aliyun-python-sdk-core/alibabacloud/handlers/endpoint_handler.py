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
from alibabacloud.endpoint.resolver_endpoint_request import ResolveEndpointRequest


class EndpointHandler(RequestHandler):

    def handle_request(self, context):
        resolve_request = ResolveEndpointRequest(
            context.config.region_id,
            context.client.product_code,
            context.client.location_service_code,
            context.client.location_endpoint_type,
        )
        context.endpoint = context.client.endpoint_resolver.resolve(resolve_request)

    def handle_response(self, response):
        pass
