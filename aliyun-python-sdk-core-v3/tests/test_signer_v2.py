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

import os
import configparser
import pytest
import ssl
import time

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.acs_exception.exceptions import ClientException
from .test_roa_api import TestRoaApi
from .test_rpc_api import TestRpcApi
from .test_endpoint import TestEndpoint

headerParam = "hdParam"
queryParam = "queryParam"
bodyParam = "bodyContent"


class TestSignerV2(object):
    acs_client = None
    public_key_id = None
    private_key = None

    @classmethod
    def setup_class(cls):
        # ignore https credential
        ssl._DEFAULT_CIPHERS = 'ALL'
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

        cf = configparser.ConfigParser()
        config_file = os.path.expanduser('~') + "/aliyun-sdk.ini"
        cf.read(config_file)

        public_key_id = cf.get('sdk_test_auth_v2_credential', 'public_key_id')
        private_key = cf.get('sdk_test_auth_v2_credential', 'private_key')

        region_provider.modify_point('Sts', 'cn-hangzhou', 'sts.aliyuncs.com')
        cls.public_key_id = public_key_id
        cls.private_key = private_key
        cls.acs_client = AcsClient(region_id='cn-hangzhou', public_key_id=public_key_id, private_key=private_key)
        assert cls.acs_client

    def test_session_period_check(self):
        with pytest.raises(ClientException):
            AcsClient(region_id='cn-hangzhou', public_key_id="", private_key="", session_period=899)
        with pytest.raises(ClientException):
            AcsClient(region_id='cn-hangzhou', public_key_id="", private_key="", session_period=3601)

    def test_credential_check(self):
        with pytest.raises(ClientException):
            AcsClient(region_id='cn-hangzhou')
        with pytest.raises(ClientException):
            AcsClient(region_id='cn-hangzhou', public_key_id="")
        with pytest.raises(ClientException):
            AcsClient(region_id='cn-hangzhou', private_key="")
        with pytest.raises(ClientException):
            AcsClient(region_id='cn-hangzhou', ak="")
        with pytest.raises(ClientException):
            AcsClient(region_id='cn-hangzhou', secret="")
        with pytest.raises(ClientException):
            AcsClient(region_id='cn-hangzhou', public_key_id=self.public_key_id + "1", private_key=self.private_key)
        assert AcsClient(region_id='cn-hangzhou', ak="ak", secret="secret")

    def test_schedule_task(self):
        test_client = AcsClient(region_id='cn-hangzhou',
                                public_key_id=self.public_key_id,
                                private_key=self.private_key,
                                session_period=1,
                                debug=True)
        signer = getattr(test_client, '_signer')
        session_credential_before = None
        for i in range(3):
            session_credential_now = getattr(signer, '_session_credential')
            assert session_credential_now and session_credential_now != session_credential_before
            time.sleep(2)
            session_credential_before = session_credential_now

    def test_retry(self, capsys):
        test_client = AcsClient(region_id='cn-hangzhou',
                                public_key_id=self.public_key_id,
                                private_key=self.private_key,
                                session_period=1,
                                debug=True)
        signer = getattr(test_client, '_signer')
        setattr(signer, '_RETRY_DELAY_FAST', 1)

        inner_signer = getattr(getattr(signer, '_sts_client'), '_signer')
        setattr(inner_signer, '_access_key', 'wrong_access_key')

        time.sleep(10)
        out, err = capsys.readouterr()
        keywords = 'refresh session ak failed, auto retry'
        assert err.count(keywords) >= 3

    def test_roa_request(self):
        roa_test_cases = TestRoaApi()
        roa_test_cases.set_client(acs_client=TestSignerV2.acs_client)
        attributes = dir(roa_test_cases)
        for attr in attributes:
            if attr.startswith('test_'):
                test_method = getattr(roa_test_cases, attr)
                test_method()

    def test_rpc_request(self):
        rpc_test_cases = TestRpcApi()
        rpc_test_cases.set_client(acs_client=TestSignerV2.acs_client)
        attributes = dir(rpc_test_cases)
        for attr in attributes:
            if attr.startswith('test_'):
                test_method = getattr(rpc_test_cases, attr)
                test_method()

    def test_endpoint(self):
        endpoint_test_cases = TestEndpoint()
        endpoint_test_cases.set_client(acs_client=TestSignerV2.acs_client)
        attributes = sorted(dir(endpoint_test_cases))
        tests = [attr for attr in attributes if attr.startswith('test_')]
        print(tests)
        for test in tests:
            test_method = getattr(endpoint_test_cases, test)
            test_method()
