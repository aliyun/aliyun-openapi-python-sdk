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

# coding:utf-8

import os
import ConfigParser
import ssl

from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import RamRoleArnCredential
from .test_roa_api import TestRoaApi
from .test_rpc_api import TestRpcApi
from .test_endpoint import TestEndpoint

headerParam = "hdParam"
queryParam = "queryParam"
bodyParam = "bodyContent"


class TestStsTokenSigner(object):
    acs_client = None
    public_key_id = None
    private_key = None

    @classmethod
    def setup_class(cls):
        # ignore https credential
        ssl._DEFAULT_CIPHERS = 'ALL'
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

        cf = ConfigParser.ConfigParser()
        config_file = os.path.expanduser('~') + "/aliyun-sdk.ini"
        cf.read(config_file)

        access_key_id = cf.get('sdk_test_auth_ram_role_arn_credential', 'access_key_id')
        access_key_secret = cf.get('sdk_test_auth_ram_role_arn_credential', 'access_key_secret')
        role_arn = cf.get('sdk_test_auth_ram_role_arn_credential', 'role_arn')
        session_role_name = 'python-sdk-test'

        region_provider.modify_point('Sts', 'cn-hangzhou', 'sts.aliyuncs.com')

        ram_role_arn_credential = RamRoleArnCredential(access_key_id, access_key_secret, role_arn, session_role_name)
        cls.acs_client = AcsClient(region_id='cn-hangzhou', credential=ram_role_arn_credential)
        assert cls.acs_client

    def test_roa_request(self):
        roa_test_cases = TestRoaApi()
        roa_test_cases.set_client(acs_client=TestStsTokenSigner.acs_client)
        attributes = dir(roa_test_cases)
        for attr in attributes:
            if attr.startswith('test_'):
                test_method = getattr(roa_test_cases, attr)
                test_method()

    def test_rpc_request(self):
        rpc_test_cases = TestRpcApi()
        rpc_test_cases.set_client(acs_client=TestStsTokenSigner.acs_client)
        attributes = dir(rpc_test_cases)
        for attr in attributes:
            if attr.startswith('test_'):
                test_method = getattr(rpc_test_cases, attr)
                test_method()

    def test_endpoint(self):
        endpoint_test_cases = TestEndpoint()
        endpoint_test_cases.set_client(acs_client=TestStsTokenSigner.acs_client)
        attributes = sorted(dir(endpoint_test_cases))
        tests = [attr for attr in attributes if attr.startswith('test_')]
        print( tests)
        for test in tests:
            test_method = getattr(endpoint_test_cases, test)
            test_method()

