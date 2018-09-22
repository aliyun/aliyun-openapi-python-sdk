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
import json
import urllib2
import logging

from aliyunsdkcore.auth.signers.signer import Signer


class EcsRamRoleSigner(Signer):
    _REFRESH_SCALE = 0.8

    def __init__(self, ecs_ram_role_credential):
        self._credential = ecs_ram_role_credential
        self._last_update_time = 0
        self._expiration = 0

    def sign(self, region_id, request):
        self._check_session_credential()
        session_ak, session_sk, token = self._session_credential
        if request.get_style() == 'RPC':
            request.add_query_param("SecurityToken", token)
        else:
            request.add_header("x-acs-security-token", token)
        header = request.get_signed_header(region_id, session_ak, session_sk)
        url = request.get_url(region_id, session_ak, session_sk)
        return header, url

    def _check_session_credential(self):
        now = int(time.time())
        if now - self._last_update_time > (self._expiration * self._REFRESH_SCALE):
            self._refresh_session_ak_and_sk()

    def _refresh_session_ak_and_sk(self):
        try:
            request_url = "http://100.100.100.200/latest/meta-data/ram/security-credentials/" + self._credential.role_name
            content = urllib2.urlopen(request_url).read()
            response = json.loads(content)
            if response.get("Code") != "Success":
                logging.error('refresh Ecs sts token err, code is ' + response.get("Code"))
                return
            session_ak = response.get("AccessKeyId")
            session_sk = response.get("AccessKeySecret")
            token = response.get("SecurityToken")
            self._session_credential = session_ak, session_sk, token
            self._expiration = response.get("Expiration")
        except IOError as e:
            logging.error('refresh Ecs sts token err', e)
