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

from aliyunsdkcore.request import RpcRequest


class DescribeContainerGroupStatusRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, 'Eci', '2018-08-08', 'DescribeContainerGroupStatus', 'eci')
        self.set_method('POST')

    def get_ZoneId(self):
        return self.get_query_params().get('ZoneId')

    def set_ZoneId(self, ZoneId):
        self.add_query_param('ZoneId', ZoneId)

    def get_VSwitchId(self):
        return self.get_query_params().get('VSwitchId')

    def set_VSwitchId(self, VSwitchId):
        self.add_query_param('VSwitchId', VSwitchId)

    def get_ResourceGroupId(self):
        return self.get_query_params().get('ResourceGroupId')

    def set_ResourceGroupId(self, ResourceGroupId):
        self.add_query_param('ResourceGroupId', ResourceGroupId)

    def get_Tags(self):
        return self.get_query_params().get('Tags')

    def set_Tags(self, Tags):
        for i in range(len(Tags)):
            if Tags[i].get('Key') is not None:
                self.add_query_param('Tag.' + str(i + 1) + '.Key', Tags[i].get('Key'))
            if Tags[i].get('Value') is not None:
                self.add_query_param('Tag.' + str(i + 1) + '.Value', Tags[i].get('Value'))

    def get_Condition(self):
        return self.get_query_params().get('Condition')

    def set_Condition(self, Condition):
        for con in range(len(Condition)):
            if Condition[con].get('Type') is not None:
                self.add_query_param(f'Condition.{str(con + 1)}.Type', Condition[con].get('Type'))
            if Condition[con].get('Status') is not None:
                self.add_query_param(f'Condition.{str(con + 1)}.Status', Condition[con].get('Status'))

    def get_ContainerGroupIds(self):
        return self.get_query_params().get('ContainerGroupIds')

    def set_ContainerGroupIds(self, ContainerGroupIds):
        self.add_query_param('ContainerGroupIds', ContainerGroupIds)

    def get_SinceSecond(self):
        return self.get_query_params().get('SinceSecond')

    def set_SinceSecond(self, SinceSecond):
        self.add_query_param('SinceSecond', SinceSecond)

    def get_NextToken(self):
        return self.get_query_params().get('NextToken')

    def set_NextToken(self, NextToken):
        self.add_query_param('NextToken', NextToken)

    def get_Limit(self):
        return self.get_query_params().get('Limit')

    def set_Limit(self, Limit):
        self.add_query_param('Limit', Limit)

