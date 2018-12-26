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
import sys
import os

from unittest import TestCase
from aliyunsdkcore.client import AcsClient


class SDKTestBase(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        if sys.version_info[0] == 2:
            self.assertRegex = self.assertRegexpMatches

    def setUp(self):

        if os.environ.get('ACCESS_KEY_ID') and os.environ.get('ACCESS_KEY_SECRET'):
            self.access_key_id = os.environ.get('ACCESS_KEY_ID')
            self.access_key_secret = os.environ.get('ACCESS_KEY_SECRET')
        else:
            sdk_config_path = os.path.join(os.path.expanduser("~"), "aliyun_sdk_config.json")
            with open(sdk_config_path) as fp:
                config = json.loads(fp.read())
                self.access_key_id = config['access_key_id']
                self.access_key_secret = config['access_key_secret']

        self.client = self.init_client()

    def init_client(self, region_id=None):
        if not region_id:
            region_id = 'cn-hangzhou'
        return AcsClient(self.access_key_id, self.access_key_secret, region_id)

    @staticmethod
    def get_dict_response(string):
        return json.loads(string, encoding="utf-8")


