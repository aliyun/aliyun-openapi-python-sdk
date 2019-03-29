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


class ClientException(Exception):
    pass


class ServerException(Exception):

    def __init__(self, service_name, endpoint, http_status, error_code, error_message, request_id):
        self.service_name = service_name
        self.endpoint = endpoint
        self.http_status = http_status
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
