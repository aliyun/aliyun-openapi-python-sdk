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

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import RpcRequest

client = AcsClient('your_access_key', 'your_access_secret', 'cn-hangzhou')
location_service = client.get_location_service()
location_service.set_location_service_attr(region='cn-beijing',
                                           product_name="Location",
                                           domain="location.aliyuncs.com")
domain = location_service.find_product_domain(client.get_region_id(), 'oss');
print domain
domain = location_service.find_product_domain(client.get_region_id(), 'oss');
print domain


class DescribeRegionsRequest(RpcRequest):

    def __init__(self, OwnerId = None, ResourceOwnerAccount = None,
                 ResourceOwnerId = None, OwnerAccount = None):
        RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeRegions', 'oss')
        self.add_query_param('OwnerId',OwnerId)
        self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)
        self.add_query_param('ResourceOwnerId',ResourceOwnerId)
        self.add_query_param('OwnerAccount',OwnerAccount)

request = DescribeRegionsRequest()
status, headers, body = client.get_response(request)
print status
print body
