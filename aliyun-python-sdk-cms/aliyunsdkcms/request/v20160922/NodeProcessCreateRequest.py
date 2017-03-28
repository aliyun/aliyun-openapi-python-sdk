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


class NodeProcessCreateRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, 'Cms', '2016-09-22', 'NodeProcessCreate', 'cms')
        self.set_accept_format('json')

    def get_InstanceId(self):
        return self.get_query_params().get('InstanceId')

    def set_InstanceId(self, InstanceId):
        self.add_query_param('InstanceId', InstanceId)

    def get_Name(self):
        return self.get_query_params().get('Name')

    def set_Name(self, Name):
        self.add_query_param('Name', Name)

    def get_ProcessName(self):
        return self.get_query_params().get('ProcessName')

    def set_ProcessName(self, ProcessName):
        self.add_query_param('ProcessName', ProcessName)

    def get_ProcessUser(self):
        return self.get_query_params().get('ProcessUser')

    def set_ProcessUser(self, ProcessUser):
        self.add_query_param('ProcessUser', ProcessUser)

    def get_Command(self):
        return self.get_query_params().get('Command')

    def set_Command(self, Command):
        self.add_query_param('Command', Command)
