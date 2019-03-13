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

import logging

from alibabacloud.signer.signer import Signer

logger = logging.getLogger(__name__)


class BearTokenSigner(Signer):
    # bear token
    # https://help.aliyun.com/document_detail/69962.html?spm=a2c4g.11186623.2.15.5dad35f6MtkJkX
    # TODO  not sure
    def __init__(self, bear_token_credential):
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
