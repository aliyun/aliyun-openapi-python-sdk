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

# coding=utf-8

import os
import sys
import json
import configparser

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider
from .ft import TestRpcApiRequest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

queryParam = "queryParam"
bodyParam = "bodyContent"

cf = configparser.ConfigParser()
config_file = os.path.expanduser('~') + "/aliyun-sdk.ini"
cf.read(config_file)

region_provider.modify_point('Ft', 'cn-hangzhou', 'ft.aliyuncs.com')
client = AcsClient(cf.get("daily_access_key", "id"), cf.get("daily_access_key", "secret"), 'cn-hangzhou')
assert client


class TestRpcApi(object):

    acs_client = client

    def set_client(self, acs_client=client):
        self.acs_client = acs_client

    def get_base_request(self):
        request = TestRpcApiRequest.TestRpcApiRequest()
        request.set_query_param(queryParam)
        return request

    def test_get(self):
        request = self.get_base_request()
        request.set_method("GET")
        body = self.acs_client.do_action_with_exception(request)
        print(body)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam

    def test_post(self):
        request = self.get_base_request()
        request.set_method("POST")
        request.set_body_param(bodyParam)
        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Params").get("BodyParam") == bodyParam

    def test_head(self):
        request = self.get_base_request()
        request.set_method("HEAD")
        body = self.acs_client.do_action_with_exception(request)
        assert len(body) == 0

    def test_put(self):
        request = self.get_base_request()
        request.set_method("PUT")
        request.set_body_param(bodyParam)
        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Params").get("BodyParam") == bodyParam

    def test_delete(self):
        request = self.get_base_request()
        request.set_method("DELETE")
        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
