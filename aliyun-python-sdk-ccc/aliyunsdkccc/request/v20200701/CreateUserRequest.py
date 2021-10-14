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
from aliyunsdkccc.endpoint import endpoint_data

class CreateUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'CreateUser','CCC')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LoginName(self):
		return self.get_query_params().get('LoginName')

	def set_LoginName(self,LoginName):
		self.add_query_param('LoginName',LoginName)

	def get_RoleId(self):
		return self.get_query_params().get('RoleId')

	def set_RoleId(self,RoleId):
		self.add_query_param('RoleId',RoleId)

	def get_Mobile(self):
		return self.get_query_params().get('Mobile')

	def set_Mobile(self,Mobile):
		self.add_query_param('Mobile',Mobile)

	def get_WorkMode(self):
		return self.get_query_params().get('WorkMode')

	def set_WorkMode(self,WorkMode):
		self.add_query_param('WorkMode',WorkMode)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_DisplayName(self):
		return self.get_query_params().get('DisplayName')

	def set_DisplayName(self,DisplayName):
		self.add_query_param('DisplayName',DisplayName)

	def get_ResetPassword(self):
		return self.get_query_params().get('ResetPassword')

	def set_ResetPassword(self,ResetPassword):
		self.add_query_param('ResetPassword',ResetPassword)

	def get_SkillLevelList(self):
		return self.get_query_params().get('SkillLevelList')

	def set_SkillLevelList(self,SkillLevelList):
		self.add_query_param('SkillLevelList',SkillLevelList)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)