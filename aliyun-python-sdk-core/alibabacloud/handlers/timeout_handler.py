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


class TimeoutHandler(RequestHandler):
    """
    timeout:
        connect_timeout ,必须给用户接口实现
            client的，
        read_timeout:用户实现没意义
    """
    def handle_request(self, context):
        request = context.request
        if request.connect_timeout:
            pass
        context.timeout = (connect_timeout, read_timeout)
        return context

    def handle_response(self, request, response):
        # context 实际是request
        pass

