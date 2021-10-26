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

class EditEnvironmentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Workbench-ide', '2021-01-21', 'EditEnvironment')
		self.set_method('POST')

	def get_SupportComputeTypess(self): # RepeatList
		return self.get_query_params().get('SupportComputeTypes')

	def set_SupportComputeTypess(self, SupportComputeTypes):  # RepeatList
		for depth1 in range(len(SupportComputeTypes)):
			self.add_query_param('SupportComputeTypes.' + str(depth1 + 1), SupportComputeTypes[depth1])
	def get_EnvName(self): # String
		return self.get_query_params().get('EnvName')

	def set_EnvName(self, EnvName):  # String
		self.add_query_param('EnvName', EnvName)
	def get_IsOpenNatEip(self): # Boolean
		return self.get_query_params().get('IsOpenNatEip')

	def set_IsOpenNatEip(self, IsOpenNatEip):  # Boolean
		self.add_query_param('IsOpenNatEip', IsOpenNatEip)
	def get_CurrentOrgId(self): # String
		return self.get_query_params().get('CurrentOrgId')

	def set_CurrentOrgId(self, CurrentOrgId):  # String
		self.add_query_param('CurrentOrgId', CurrentOrgId)
	def get_EnvDescription(self): # String
		return self.get_query_params().get('EnvDescription')

	def set_EnvDescription(self, EnvDescription):  # String
		self.add_query_param('EnvDescription', EnvDescription)
	def get_EnvId(self): # Long
		return self.get_query_params().get('EnvId')

	def set_EnvId(self, EnvId):  # Long
		self.add_query_param('EnvId', EnvId)
