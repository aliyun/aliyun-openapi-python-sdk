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
from alibabacloud.credentials.credentials import AccessKeyCredentials
from alibabacloud.credentials.credentials import SecurityCredentials
from alibabacloud.credentials.credentials import BearTokenCredentials
from alibabacloud.signer.access_key_signer import AccessKeySigner
from alibabacloud.signer.security_signer import SecuritySigner
from alibabacloud.signer.bearer_token_signer import BearerTokenSigner  # FIXME: bear -> bearer


class SignerHandler(RequestHandler):

    _signer_map = {
        "AccessKeyCredentials": AccessKeySigner(),
        "SecurityCredentials": SecuritySigner(),
        "BearTokenCredentials": BearerTokenSigner()
    }

    # 只实现了signature
    def handle_request(self, context):
        http_request = context.http_request

        credentials = context.credentials
        signer = self._signer_map[credentials.__class__.__name__]

        signature = signer.sign(credentials, context)
        # TODO fix other headers
        http_request.signature = signature
        ############
        # parameters = signer.sign(credentials, context)
        # # 获取请求参数parameters
        # signature = parameters['Signature']
        # # TODO fix other headers
        # http_request.signature = signature
        #
        # context.http_request.parameters = parameters
