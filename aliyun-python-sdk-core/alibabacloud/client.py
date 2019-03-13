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

from alibabacloud.handlers import RequestContext


class ClientConfig:

    def __init__(self, access_key_id=None, access_key_secret=None, region_id=None,
                 enable_retry_policy=True, max_retry_times=None, user_agent=None,
                 extra_user_agent=None, enable_https=True, http_port=None, https_port=None,
                 connection_timeout=None, read_timeout=None):

        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        # TODO assign more attributes


class AlibabaCloudClient:

    def __init__(self, client_config, credentials_provider):
        self.config = client_config
        self.credentials_provider = credentials_provider
        self.handlers = []

    def _handle_request(self, request):
        # TODO handle different types of request
        context = RequestContext()
        context.request = request

        for handler in self.handlers:
            handler.handl_request(context)

        for handler in reversed(self.handlers):
            handler.handl_response(context)
