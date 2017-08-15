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
import json
import configparser

from aliyunsdkcore.client import AcsClient
from aliyunsdkft.request.v20160101 import TestRpcApiRequest
from aliyunsdkcore.profile import region_provider

queryParam = "queryParam"
bodyParam = "bodyContent"

cf = configparser.ConfigParser()
config_file = os.path.expanduser('~') + "/aliyun-sdk.ini"
cf.read(config_file)

region_provider.modify_point('Ft', 'cn-hangzhou', 'ft.aliyuncs.com')
client = AcsClient(cf.get("daily_access_key", "id"), cf.get("daily_access_key", "secret"), 'cn-hangzhou')
assert client


class TestRpcApi(object):

    def get_base_request(self):
        request = TestRpcApiRequest.TestRpcApiRequest()
        request.set_QueryParam(queryParam)
        return request

    def test_get(self):
        request = self.get_base_request()
        request.set_method("GET")
        body = client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam

    def test_post(self):
        request = self.get_base_request()
        request.set_method("POST")
        request.set_BodyParam(bodyParam)
        body = client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Params").get("BodyParam") == bodyParam

    def test_head(self):
        request = self.get_base_request()
        request.set_method("HEAD")
        body = client.do_action_with_exception(request)
        assert body == b''

    def test_put(self):
        request = self.get_base_request()
        request.set_method("PUT")
        request.set_BodyParam(bodyParam)
        body = client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Params").get("BodyParam") == bodyParam

    def test_delete(self):
        request = self.get_base_request()
        request.set_method("DELETE")
        body = client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
