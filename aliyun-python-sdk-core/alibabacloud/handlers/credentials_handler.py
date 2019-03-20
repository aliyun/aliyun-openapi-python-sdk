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


class CredentialsHandler(RequestHandler):

    def handle_request(self, context):
        http_request = context.http_request
        api_request = context.api_request

        credentials = context.client.credentials_provider(context)
        context.http_request.credentials = credentials

    def handle_response(self, response):
        pass

    @staticmethod
    def get_credentials(context):
        credentials_provider = context.client.credentials_provider({
            'access_key_id': context.config.access_key_id,
            'access_key_secret': context.config.access_key_secret,
        })
        credentials = credentials_provider.load_credentials()
        if credentials is None:
            raise ClientException(
                'Credentials',
                'Unable to locate credentials.'
            )
        return credentials
