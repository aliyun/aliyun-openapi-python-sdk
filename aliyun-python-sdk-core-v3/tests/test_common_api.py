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
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import format_type
from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.acs_exception import exceptions


class TestCommonApi(object):
    acs_client = None

    @classmethod
    def setup_class(cls):
        cf = configparser.ConfigParser()
        config_file = os.path.expanduser('~') + "/aliyun-sdk.ini"
        cf.read(config_file)
        cls.acs_client = AcsClient(cf.get("daily_access_key", "id"), cf.get("daily_access_key", "secret"), 'cn-hangzhou')

    def set_client(self, acs_client):
        self.acs_client = acs_client

    def test_roa_form_with_init(self):
        request = CommonRequest(domain='ft.aliyuncs.com', version='2016-01-02', action_name='TestRoaApi', uri_pattern='/web/cloudapi')
        request.set_method('POST')
        request.add_header('HeaderParam', 'headerValue')
        request.add_query_param('QueryParam', 'queryValue')
        request.add_body_params('BodyParam', 'bodyValue')

        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == 'queryValue'
        assert response.get("Headers").get("HeaderParam") == 'headerValue'
        assert response.get("Params").get("BodyParam") == 'bodyValue'

    def test_roa_form_with_setup(self):
        request = CommonRequest()
        request.set_domain('ft.aliyuncs.com')
        request.set_version('2016-01-02')
        request.set_action_name('TestRoaApi')
        request.set_uri_pattern('/web/cloudapi')
        request.set_method('POST')
        request.add_header('HeaderParam', 'headerValue')
        request.add_query_param('QueryParam', 'queryValue')
        request.add_body_params('BodyParam', 'bodyValue')

        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == 'queryValue'
        assert response.get("Headers").get("HeaderParam") == 'headerValue'
        assert response.get("Params").get("BodyParam") == 'bodyValue'

    def test_resolve_endpoint(self):
        region_provider.modify_point('Ft', 'cn-hangzhou', 'ft.aliyuncs.com')
        request = CommonRequest()
        request.set_product('Ft')
        request.set_version('2016-01-02')
        request.set_action_name('TestRoaApi')
        request.set_uri_pattern('/web/cloudapi')
        request.set_method('POST')
        request.add_header('HeaderParam', 'headerValue')
        request.add_query_param('QueryParam', 'queryValue')
        request.add_body_params('BodyParam', 'bodyValue')

        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == 'queryValue'
        assert response.get("Headers").get("HeaderParam") == 'headerValue'
        assert response.get("Params").get("BodyParam") == 'bodyValue'

    def test_resolve_endpoint_from_location(self):
        request = CommonRequest()
        request.set_product('Ecs')
        request.set_version('2014-05-26')
        request.set_action_name('DescribeRegions')
        request.set_method('GET')

        try:
            self.acs_client.do_action_with_exception(request)
        except exceptions.ServerException as e:
            assert e.get_error_code() == 'InvalidAccessKeyId.NotFound'

    def test_roa_stream(self):
        request = CommonRequest(domain='ft.aliyuncs.com', version='2016-01-02', action_name='TestRoaApi', uri_pattern='/web/cloudapi')
        request.set_method('POST')
        request.add_header('HeaderParam', 'headerValue')
        request.add_query_param('QueryParam', 'queryValue')
        request.set_content("test_content")

        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == 'queryValue'
        assert response.get("Headers").get("HeaderParam") == 'headerValue'
        assert response.get("Body") == 'test_content'

    def test_roa_json(self):
        request = CommonRequest(domain='ft.aliyuncs.com', version='2016-01-02', action_name='TestRoaApi', uri_pattern='/web/cloudapi')
        request.set_method('POST')
        request.add_header('HeaderParam', 'headerValue')
        request.add_query_param('QueryParam', 'queryValue')
        dict_data = {'data': 1}
        request.set_content(json.dumps(dict_data))
        request.set_content_type(format_type.APPLICATION_JSON)

        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("RegionId") == 'cn-hangzhou'
        assert response.get("Params").get("QueryParam") == 'queryValue'
        assert response.get("Headers").get("HeaderParam") == 'headerValue'
        assert response.get("Headers").get("Content-Type") == 'application/json'
        assert response.get("Body") == '{"data": 1}'

    def test_rpc_post_with_init(self):
        request = CommonRequest(domain='ft.aliyuncs.com', version='2016-01-01', action_name='TestRpcApi')
        request.set_method('POST')
        request.add_query_param('QueryParam', 'queryValue')
        request.add_body_params('BodyParam', 'bodyValue')

        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == 'queryValue'
        assert response.get("Params").get("BodyParam") == 'bodyValue'

    def test_rpc_post_with_setup(self):
        request = CommonRequest()
        request.set_domain('ft.aliyuncs.com')
        request.set_version('2016-01-01')
        request.set_action_name('TestRpcApi')
        request.set_method('POST')
        request.add_query_param('QueryParam', 'queryValue')
        request.add_body_params('BodyParam', 'bodyValue')

        body = self.acs_client.do_action_with_exception(request)
        assert body

        response = json.loads(body)
        assert response

        assert response.get("Params").get("QueryParam") == 'queryValue'
        assert response.get("Params").get("BodyParam") == 'bodyValue'

