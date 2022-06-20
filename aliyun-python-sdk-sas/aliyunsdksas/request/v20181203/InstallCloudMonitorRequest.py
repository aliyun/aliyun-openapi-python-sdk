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
from aliyunsdksas.endpoint import endpoint_data

class InstallCloudMonitorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'InstallCloudMonitor')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AgentAccessKey(self): # String
		return self.get_query_params().get('AgentAccessKey')

	def set_AgentAccessKey(self, AgentAccessKey):  # String
		self.add_query_param('AgentAccessKey', AgentAccessKey)
	def get_AgentSecretKey(self): # String
		return self.get_query_params().get('AgentSecretKey')

	def set_AgentSecretKey(self, AgentSecretKey):  # String
		self.add_query_param('AgentSecretKey', AgentSecretKey)
	def get_UuidLists(self): # RepeatList
		return self.get_query_params().get('UuidList')

	def set_UuidLists(self, UuidList):  # RepeatList
		for depth1 in range(len(UuidList)):
			self.add_query_param('UuidList.' + str(depth1 + 1), UuidList[depth1])
	def get_ArgusVersion(self): # String
		return self.get_query_params().get('ArgusVersion')

	def set_ArgusVersion(self, ArgusVersion):  # String
		self.add_query_param('ArgusVersion', ArgusVersion)
	def get_InstanceIdLists(self): # RepeatList
		return self.get_query_params().get('InstanceIdList')

	def set_InstanceIdLists(self, InstanceIdList):  # RepeatList
		for depth1 in range(len(InstanceIdList)):
			self.add_query_param('InstanceIdList.' + str(depth1 + 1), InstanceIdList[depth1])
