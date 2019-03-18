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
from alibabacloud.signer.bearer_token_signer import BearTokenSigner  # FIXME: bear -> bearer


class SignerHandler(RequestHandler):

    _signer_map = {
        "AccessKeyCredentials": AccessKeySigner(),
        "SecurityCredentials": SecuritySigner(),
        "BearTokenCredentials": BearTokenSigner()
    }

    # 源代码实现了获取header和url
    def handle_request(self, context):
        http_request = context.http_request
        credentials = context.client.credentials_provider.load_credentials()
        signer = self._signer_map[credentials.__class__.__name__]
        signature = signer.sign(credentials, context)
        http_request.headers['Signature'] = signature
        # TODO fix other headers

    def get_signer_cls(self, context):
        # 原本AK组装的static_provider
        # using CredentialsProvider
        if context.config.credentials_provider_chain:
            self.credentials = context.config.credentials_provider_chain()
        else:
            _credentials_provider = DefaultCredentialsProvider(_credential)
            self.credentials = _credentials_provider.load_credentials()
        if self.credentials is None:
            raise ClientException(
                'Credentials',
                'Unable to locate credentials.'
            )
        return SignerFactory.get_signer(
            credentials=self.credentials, region_id=self._region_id,
            do_action_api=self._implementation_of_do_action, debug=self.debug)
