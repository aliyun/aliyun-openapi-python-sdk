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

SDK_INVALID_REGION_ID = 'SDK.InvalidRegionId'
SDK_SERVER_UNREACHABLE = 'SDK.ServerUnreachable'
SDK_INVALID_REQUEST = 'SDK.InvalidRequest'
SDK_MISSING_ENDPOINTS_FILER = 'SDK.MissingEndpointsFiler'
SDK_UNKNOWN_SERVER_ERROR = 'SDK.UnknownServerError'
SDK_INVALID_CREDENTIAL = 'SDK.InvalidCredential'
SDK_INVALID_SESSION_EXPIRATION = 'SDK.InvalidSessionExpiration'
SDK_GET_SESSION_CREDENTIAL_FAILED = 'SDK.GetSessionCredentialFailed'
SDK_INVALID_PARAMS = 'SDK.InvalidParams'
SDK_NOT_SUPPORT = 'SDK.NotSupport'
SDK_ENDPOINT_RESOLVING_ERROR = 'SDK.EndpointResolvingError'
SDK_ENDPOINT_TESTABILITY = 'SDK.EndpointTestability'
SDK_HTTP_ERROR = 'SDK.HttpError'
SDK_INVALID_PARAMETER = "SDK.InvalidParameter"


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

    def __init__(self, error_code, error_message, endpoint=None,
                 http_status=None, request_id=None, service_name= None):
        self.error_code = error_code
        self.error_message = error_message
        self.endpoint = endpoint
        self.http_status = http_status
        self.request_id = request_id
        # TODO service_name
        self.service_name = service_name

    def __str__(self):
        return "HTTP Status: %s Error:%s %s RequestID: %s" % (
            str(self.http_status),
            self.error_code,
            self.error_message,
            self.request_id
        )

