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
from aliyunsdkcore.http import format_type
from .ft import TestRoaApiRequest

headerParam = "hdParam"
queryParam = "queryParam"
bodyParam = "bodyContent"

cf = configparser.ConfigParser()
config_file = os.path.expanduser('~') + "/aliyun-sdk.ini"
cf.read(config_file)

region_provider.modify_point('Ft', 'cn-hangzhou', 'ft.aliyuncs.com')
client = AcsClient(cf.get("daily_access_key", "id"), cf.get("daily_access_key", "secret"), 'cn-hangzhou')
assert client


class TestRoaApi(object):
    acs_client = client

    def set_client(self, acs_client=client):
        self.acs_client = acs_client

    @staticmethod
    def get_base_request():
        request = TestRoaApiRequest.TestRoaApiRequest()
        request.set_header_param(headerParam)
        request.set_query_param(queryParam)
        return request

    def test_get(self):
        request = TestRoaApi.get_base_request()
        request.set_method("GET")
        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Headers").get("HeaderParam") == headerParam
        assert response.get("Headers").get("x-sdk-invoke-type") == 'normal'

    def test_post(self):
        request = TestRoaApi.get_base_request()
        request.set_method("POST")
        request.set_body_param(bodyParam)
        request.set_content_type(format_type.APPLICATION_FORM)
        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Headers").get("HeaderParam") == headerParam
        assert response.get("Params").get("BodyParam") == bodyParam

    def test_post_reuse(self):
        request = TestRoaApi.get_base_request()
        request.set_method("POST")
        request.set_body_param(bodyParam)
        request.set_content_type(format_type.APPLICATION_FORM)
        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Headers").get("HeaderParam") == headerParam
        assert response.get("Params").get("BodyParam") == bodyParam

        request.set_body_param(bodyParam + "1")
        request.set_content_type(format_type.APPLICATION_FORM)
        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Headers").get("HeaderParam") == headerParam
        assert response.get("Params").get("BodyParam") == bodyParam + "1"

    def test_post_with_stream(self):
        request = TestRoaApi.get_base_request()
        request.set_method("POST")
        request.set_content("test_content")
        request.set_content_type(format_type.APPLICATION_OCTET_STREAM)

        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Headers").get("HeaderParam") == headerParam
        assert response.get("Body") == 'test_content'

    def test_post_with_json(self):
        request = TestRoaApi.get_base_request()
        request.set_method("POST")
        dict_data = {'data': 1}
        request.set_content(json.dumps(dict_data))
        request.set_content_type(format_type.APPLICATION_JSON)

        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Headers").get("HeaderParam") == headerParam
        assert response.get("Headers").get("Content-Type") == 'application/json'
        assert response.get("Body") == '{"data": 1}'

    def test_head(self):
        request = TestRoaApi.get_base_request()
        request.set_method("HEAD")
        body = self.acs_client.do_action_with_exception(request)
        assert len(body) == 0

    def test_put(self):
        request = TestRoaApi.get_base_request()
        request.set_method("PUT")
        request.set_body_param(bodyParam)
        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Headers").get("HeaderParam") == headerParam
        assert response.get("Params").get("BodyParam") == bodyParam

    def test_delete(self):
        request = TestRoaApi.get_base_request()
        request.set_method("DELETE")
        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == queryParam
        assert response.get("Headers").get("HeaderParam") == headerParam
