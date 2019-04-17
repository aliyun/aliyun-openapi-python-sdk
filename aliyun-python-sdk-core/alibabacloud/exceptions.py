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
    """client exception"""

    def __init__(self, error_message):
        """

        :param error_message: error message
        :return:
        """
        Exception.__init__(self)
        self.__error_type = 'Client'
        self.error_message = error_message

    def __str__(self):
        return "%s" % (
            self.error_message,
        )


class ServerException(Exception):

    def __init__(self, error_code, error_message, endpoint=None, service_name=None,
                 http_status=None, request_id=None):
        self.error_code = error_code
        self.error_message = error_message
        self.endpoint = endpoint
        # TODO service_name
        self.service_name = service_name
        self.http_status = http_status
        self.request_id = request_id

    def __str__(self):
        return "HTTP Status: %s Product:%s Endpoint:%s Error:%s %s RequestID: %s" % (
            str(self.http_status),
            self.service_name,
            self.endpoint,
            self.error_code,
            self.error_message,
            self.request_id
        )

