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

import sys
from aliyunsdkcore.client import AcsClient


# The unittest module got a significant overhaul
# in 2.7, so if we're in 2.6 we can use the backported
# version unittest2.
if sys.version_info[:2] == (2, 6):
    from unittest2 import TestCase
else:
    from unittest import TestCase


class SDKTestBase(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        # if sys.version_info[0] == 2:
        #     self.assertRegex = self.assertRegexpMatches
        self._init_env()

    def test_env_available(self):
        # To let test script know whether env is available, to continue the tests
        self._init_env()

    def _init_env(self):
        self._sdk_config = self._init_sdk_config()
        self.access_key_id = self._read_key_from_env_or_config("ACCESS_KEY_ID")
        self.access_key_secret = self._read_key_from_env_or_config("ACCESS_KEY_SECRET")
        self.sub_access_key_id = self._read_key_from_env_or_config("SUB_ACCESS_KEY_ID")
        self.sub_access_key_secret = self._read_key_from_env_or_config("SUB_ACCESS_KEY_SECRET")
        self.region_id = self._read_key_from_env_or_config("REGION_ID")

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
        self.client = self.init_client()

    def init_client(self, region_id=None):
        if not region_id:
            region_id = self.region_id
        return AcsClient(self.access_key_id, self.access_key_secret, region_id)

    def init_sub_client(self):
        return AcsClient(self.sub_access_key_id, self.sub_access_key_secret, self.region_id)

    @staticmethod
    def get_dict_response(string):
        return json.loads(string.decode('utf-8'), encoding="utf-8")


def disabled(func):
    def _decorator(func):
        pass
    return _decorator



