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
import json

from alibabacloud.handlers import RequestHandler
from alibabacloud.http.http_response import HttpResponse
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode


class ServerErrorHandler(RequestHandler):
    def handle_exceptions(self, context):
        response = context.response
        request_id = None

        try:
            body_obj = json.loads(response.text.decode('utf-8'))
            request_id = body_obj.get('RequestId')
        except (ValueError, TypeError, AttributeError):
            # in case the response body is not a json string, return the raw
            # data instead
            logger.warning('Failed to parse response as json format. Response:%s', response.text)

        if response.codes < codes.OK or response.codes >= codes.MULTIPLE_CHOICES:

            server_error_code, server_error_message = self._parse_error_info_from_response_body(
                response.text.decode('utf-8'))
            if response.codes == codes.BAD_REQUEST and server_error_code == 'SignatureDoesNotMatch':
                if string_to_sign == server_error_message.split(':')[1]:
                    server_error_code = 'InvalidAccessKeySecret'
                    server_error_message = 'The AccessKeySecret is incorrect. ' \
                                           'Please check your AccessKeyId and AccessKeySecret.'
            exception = ServerException(
                server_error_code,
                server_error_message,
                http_status=http_status,
                request_id=request_id)

            logger.error("ServerException occurred. Host:%s SDK-Version:%s ServerException:%s",
                         endpoint, aliyunsdkcore.__version__, str(exception))

            return exception
