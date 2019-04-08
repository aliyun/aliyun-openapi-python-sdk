# Copyright 2018 Alibaba Cloud Inc. All rights reserved.
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

import os.path
import json
import os
from unittest import TestCase

from aliyunsdkcore.client import AcsClient


class SDKTestBase(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        # if sys.version_info[0] == 2:
        #     self.assertRegex = self.assertRegexpMatches
        self._init_env()

    def _init_env(self):
        self._sdk_config = self._init_sdk_config()
        self.access_key_id = self._read_key_from_env_or_config("ACCESS_KEY_ID")
        self.access_key_secret = self._read_key_from_env_or_config("ACCESS_KEY_SECRET")
        self.region_id = self._read_key_from_env_or_config("REGION_ID")
        self.user_id = self._read_key_from_env_or_config("USER_ID")
        if 'TRAVIS_JOB_NUMBER' in os.environ:
            self.travis_concurrent = os.environ.get('TRAVIS_JOB_NUMBER').split(".")[-1]
        else:
            self.travis_concurrent = "0"
        self.default_ram_user_name = "RamUserForSDKCredentialsTest" + self.travis_concurrent
        self.default_ram_role_name = "RamROleForSDKTest" + self.travis_concurrent
        self.default_role_session_name = "RoleSession" + self.travis_concurrent
        self.ram_user_id = None
        self.ram_policy_attched = False
        self.ram_user_access_key_id = None
        self.ram_user_access_key_secret = None
        self.ram_role_arn = None

    def _init_sdk_config(self):
        sdk_config_path = os.path.join(os.path.expanduser("~"), "aliyun_sdk_config.json")
        if os.path.isfile(sdk_config_path):
            with open(sdk_config_path) as fp:
                return json.loads(fp.read())

    def _read_key_from_env_or_config(self, key_name):
        if key_name.upper() in os.environ:
            return os.environ.get(key_name.upper())
        if key_name.lower() in self._sdk_config:
            return self._sdk_config[key_name.lower()]

        raise Exception("Failed to find sdk config: " + key_name)

    def setUp(self):
        TestCase.setUp(self)
        self.client = self.init_client()

    def tearDown(self):
        pass

    def init_client(self, region_id=None):
        if not region_id:
            region_id = self.region_id
        client = AcsClient(self.access_key_id, self.access_key_secret, region_id, timeout=120)
        return client

    @staticmethod
    def get_dict_response(string):
        return json.loads(string.decode('utf-8'), encoding="utf-8")
