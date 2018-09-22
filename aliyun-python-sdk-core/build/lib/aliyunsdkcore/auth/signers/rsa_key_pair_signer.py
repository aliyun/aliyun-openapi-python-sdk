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

import sched
import time
import threading
import json
import logging
import socket

from aliyunsdkcore.auth.signers.signer import Signer
from aliyunsdkcore.acs_exception import error_code
from aliyunsdkcore.acs_exception import error_msg
from aliyunsdkcore.acs_exception import exceptions
from aliyunsdkcore.request import RpcRequest
from aliyunsdkcore.auth.algorithm import sha_hmac256


class RsaKeyPairSigner(Signer):
    _MIN_SESSION_PERIOD = 900
    _MAX_SESSION_PERIOD = 3600
    _RETRY_DELAY_FAST = 3
    _PRIORITY = 1

    def __init__(self, rsa_key_pair_credential, region_id, debug=False):
        if not debug and rsa_key_pair_credential.session_period < self._MIN_SESSION_PERIOD \
                or rsa_key_pair_credential.session_period > self._MAX_SESSION_PERIOD:
            raise exceptions.ClientException(
                error_code.SDK_INVALID_SESSION_EXPIRATION,
                error_msg.get_msg('SDK_INVALID_SESSION_EXPIRATION').format(self._MIN_SESSION_PERIOD,
                                                                           self._MAX_SESSION_PERIOD))
        rsa_key_pair_credential.region_id = region_id
        self._public_key_id = rsa_key_pair_credential.public_key_id
        self._private_key = rsa_key_pair_credential.private_key
        self._session_period = rsa_key_pair_credential.session_period
        self._schedule_interval = rsa_key_pair_credential.session_period if debug \
            else max(rsa_key_pair_credential.session_period * 0.8, 5)
        from aliyunsdkcore.client import AcsClient
        self._sts_client = AcsClient(self._public_key_id, self._private_key, rsa_key_pair_credential.region_id)
        self._session_credential = None
        self._get_session_ak_and_sk()
        self._scheduler = sched.scheduler(time.time, time.sleep)
        self._daemon_thread = threading.Thread(target=self._refresh_session_ak_and_sk, args=[True, 0])
        self._daemon_thread.setDaemon(True)
        self._daemon_thread.start()

    def sign(self, region_id, request):
        session_ak, session_sk = self._session_credential
        header = request.get_signed_header(region_id, session_ak, session_sk)
        url = request.get_url(region_id, session_ak, session_sk)
        return header, url

    def _get_session_ak_and_sk(self):

        request = GetSessionAkRequest()
        request.set_method("GET")
        request.set_duration_seconds(self._session_period)

        try:
            response_str = self._sts_client.do_action_with_exception(request)
            response = json.loads(response_str)
            session_ak = str(response.get("SessionAccessKey").get("SessionAccessKeyId"))
            session_sk = str(response.get("SessionAccessKey").get("SessionAccessKeySecret"))

            self._session_credential = session_ak, session_sk
        except exceptions.ServerException as srv_ex:
            if srv_ex.error_code == 'InvalidAccessKeyId.NotFound' or srv_ex.error_code == 'SignatureDoesNotMatch':
                raise exceptions.ClientException(error_code.SDK_INVALID_CREDENTIAL,
                                                 error_msg.get_msg('SDK_INVALID_CREDENTIAL'))
            else:
                raise

    # no-limit-retry if failed with any conditions.
    # fast retry in first 3 times, then the interval becomes incremental.
    # the max interval is 10 minutes.
    def _refresh_session_ak_and_sk(self, is_init, retry_times=0):
        delay = self._schedule_interval
        next_retry_time = 0
        try:
            if not is_init:
                self._get_session_ak_and_sk()
        except (Exception, socket.error) as ex:
            if retry_times <= 3:
                delay = self._RETRY_DELAY_FAST
            else:
                delay = 60 * min(10, retry_times)
            next_retry_time = retry_times + 1
            logging.warn(
                'refresh session ak failed, auto retry after {} seconds. message = {}'.format(delay, ex))
        finally:
            self._scheduler.enter(delay, self._PRIORITY, self._refresh_session_ak_and_sk, [False, next_retry_time])
            self._scheduler.run()


class GetSessionAkRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, product='Sts', version='2015-04-01', action_name='GenerateSessionAccessKey',
                            signer=sha_hmac256)
        self.set_protocol_type('https')

    def get_duration_seconds(self):
        return self.get_query_params().get("DurationSeconds")

    def set_duration_seconds(self, duration_seconds):
        self.add_query_param('DurationSeconds', duration_seconds)

    def get_public_key_id(self):
        return self.get_query_params().get('PublicKeyId')

    def set_public_key_id(self, public_key_id):
        self.add_query_param('PublicKeyId', public_key_id)

