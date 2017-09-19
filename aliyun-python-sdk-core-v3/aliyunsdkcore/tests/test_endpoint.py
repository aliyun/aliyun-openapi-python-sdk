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
from aliyunsdkcore.request import RpcRequest
from aliyunsdkcore import client


class TestEndpoint(object):

    acs_client = None

    @classmethod
    def setup_class(cls):
        cf = configparser.ConfigParser()
        config_file = os.path.expanduser('~') + "/aliyun-sdk.ini"
        cf.read(config_file)

        cls.acs_client = client.AcsClient(cf.get("daily_access_key", "id"), cf.get("daily_access_key", "secret"), 'cn-zhangjiakou')
        client.region_provider.add_endpoint("Ecs", 'cn-zhangjiakou', 'ecs.cn-zhangjiakou.aliyuncs.com')

    def set_client(self, acs_client=client):
        self.acs_client = acs_client
        self.acs_client.set_region_id('cn-zhangjiakou')
        client.region_provider.add_endpoint("Ecs", 'cn-zhangjiakou', 'ecs.cn-zhangjiakou.aliyuncs.com')

    def test_resolve_endpoint1(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions')
        request.set_accept_format('JSON')
        endpoint = self.acs_client._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou.aliyuncs.com'

    def test_resolve_endpoint2(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions', 'ecs')
        request.set_accept_format('JSON')
        endpoint = self.acs_client._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou.aliyuncs.com'

    def test_resolve_endpoint3(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions', 'ecs')
        request.set_accept_format('JSON')
        client.region_provider.add_endpoint("Ecs", 'cn-zhangjiakou', 'ecs.cn-zhangjiakou123.aliyuncs.com')
        endpoint = self.acs_client._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou123.aliyuncs.com'

    def test_resolve_endpoint4(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions')
        request.set_accept_format('JSON')
        endpoint = self.acs_client._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou123.aliyuncs.com'

    def test_resolve_endpoint5(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions', 'ecs')
        request.set_accept_format('JSON')
        endpoint = self.acs_client._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou123.aliyuncs.com'
