# coding:utf-8

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import time
import logging
import json

from aliyunsdkcore.vendored.six.moves.urllib.request import urlopen
from aliyunsdkcore.auth.signers.signer import Signer
from aliyunsdkcore.acs_exception.exceptions import ServerException

logger = logging.getLogger(__name__)


class BearTokenSigner(Signer):
    # bear token
    # https://help.aliyun.com/document_detail/69962.html?spm=a2c4g.11186623.2.15.5dad35f6MtkJkX
    # TODO  not sure
    def __init__(self, bear_token_credential, region_id=None, do_action_api=None, debug=None):
        self._credential = bear_token_credential

    def sign(self, region_id, request):
        self._check_session_credential()
        token = self._session_credential
        # which token
        if request.get_style() == 'RPC':
            request.add_query_param("BearerToken", token)
        else:
            request.add_header("x-acs-bearer-token", token)
        header = request.get_signed_header(region_id, None, None)
        url = request.get_url(region_id, None, None)
        return header, url

    def _check_session_credential(self):
        now = int(time.time())
        if now - self._last_update_time > (self._expiration * self._REFRESH_SCALE):
            self._refresh_session_ak_and_sk()

    def _refresh_session_ak_and_sk(self):
        import requests
        payload = {
            'refresh_token': self._credential.bear_token,
            'client_id': 'client_id',  # 应用的Identifier
            'grant_type': 'refresh_token'
        }
        content = requests.post("https://oauth.aliyun.com/v1/token", data=payload)
        response = json.loads(content.text.decode('utf-8'))
        if response.get("status_code") != "200":
            message = 'refresh bear token err, code is ' + \
                response.get("Code")
            raise ServerException(
                response.get("Code"), message, None)

        self._session_credential = response.get("access_token")
        self._expiration = response.get("expires_in")
        self._last_update_time = int(time.time())
