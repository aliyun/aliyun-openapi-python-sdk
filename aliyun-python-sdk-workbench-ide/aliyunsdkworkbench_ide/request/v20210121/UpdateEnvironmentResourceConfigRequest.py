# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class UpdateEnvironmentResourceConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Workbench-ide', '2021-01-21', 'UpdateEnvironmentResourceConfig')
		self.set_method('POST')

	def get_CurrentOrgId(self):
		return self.get_query_params().get('CurrentOrgId')

	def set_CurrentOrgId(self,CurrentOrgId):
		self.add_query_param('CurrentOrgId',CurrentOrgId)

	def get_ConfigLists(self):
		return self.get_query_params().get('ConfigList')

	def set_ConfigLists(self, ConfigLists):
		for depth1 in range(len(ConfigLists)):
			if ConfigLists[depth1].get('InstanceId') is not None:
				self.add_query_param('ConfigList.' + str(depth1 + 1) + '.InstanceId', ConfigLists[depth1].get('InstanceId'))
			if ConfigLists[depth1].get('ConfigName') is not None:
				self.add_query_param('ConfigList.' + str(depth1 + 1) + '.ConfigName', ConfigLists[depth1].get('ConfigName'))
			if ConfigLists[depth1].get('ConfigDescription') is not None:
				self.add_query_param('ConfigList.' + str(depth1 + 1) + '.ConfigDescription', ConfigLists[depth1].get('ConfigDescription'))
			if ConfigLists[depth1].get('ConfigValue') is not None:
				self.add_query_param('ConfigList.' + str(depth1 + 1) + '.ConfigValue', ConfigLists[depth1].get('ConfigValue'))

	def get_EnvId(self):
		return self.get_query_params().get('EnvId')

	def set_EnvId(self,EnvId):
		self.add_query_param('EnvId',EnvId)

	def get_CloudServiceName(self):
		return self.get_query_params().get('CloudServiceName')

	def set_CloudServiceName(self,CloudServiceName):
		self.add_query_param('CloudServiceName',CloudServiceName)