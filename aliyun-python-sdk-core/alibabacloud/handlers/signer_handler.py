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


class SignerHandler(RequestHandler):
    # 源代码实现了获取header和url
    def handle_request(self, context):
        request = context.request
        signer_cls = self.get_signer_cls(context)
        context.header, context.url = signer_cls.sign(self._region_id, request)

    def handle_response(self, request, response):
        # context 实际是request
        pass

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
