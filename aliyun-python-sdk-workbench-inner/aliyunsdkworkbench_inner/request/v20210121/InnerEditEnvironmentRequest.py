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

class InnerEditEnvironmentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Workbench-inner', '2021-01-21', 'InnerEditEnvironment')
		self.set_method('POST')

	def get_EnvName(self):
		return self.get_query_params().get('EnvName')

	def set_EnvName(self,EnvName):
		self.add_query_param('EnvName',EnvName)

	def get_EnvDesc(self):
		return self.get_query_params().get('EnvDesc')

	def set_EnvDesc(self,EnvDesc):
		self.add_query_param('EnvDesc',EnvDesc)

	def get_CurrentOrgId(self):
		return self.get_query_params().get('CurrentOrgId')

	def set_CurrentOrgId(self,CurrentOrgId):
		self.add_query_param('CurrentOrgId',CurrentOrgId)

	def get_EnvId(self):
		return self.get_query_params().get('EnvId')

	def set_EnvId(self,EnvId):
		self.add_query_param('EnvId',EnvId)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_SupportComputeTypess(self):
		return self.get_query_params().get('SupportComputeTypes')

	def set_SupportComputeTypess(self, SupportComputeTypess):
		for depth1 in range(len(SupportComputeTypess)):
			if SupportComputeTypess[depth1] is not None:
				self.add_query_param('SupportComputeTypes.' + str(depth1 + 1) , SupportComputeTypess[depth1])

	def get_IsOpenNateip(self):
		return self.get_query_params().get('IsOpenNateip')

	def set_IsOpenNateip(self,IsOpenNateip):
		self.add_query_param('IsOpenNateip',IsOpenNateip)