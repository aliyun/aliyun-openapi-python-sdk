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
class CreateUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'CreateUser','ccc')

	def get_SkillLevels(self):
		return self.get_query_params().get('SkillLevels')

	def set_SkillLevels(self,SkillLevels):
		for i in range(len(SkillLevels)):	
			if SkillLevels[i] is not None:
				self.add_query_param('SkillLevel.' + str(i + 1) , SkillLevels[i]);

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_LoginName(self):
		return self.get_query_params().get('LoginName')

	def set_LoginName(self,LoginName):
		self.add_query_param('LoginName',LoginName)

	def get_Phone(self):
		return self.get_query_params().get('Phone')

	def set_Phone(self,Phone):
		self.add_query_param('Phone',Phone)

	def get_RoleIds(self):
		return self.get_query_params().get('RoleIds')

	def set_RoleIds(self,RoleIds):
		for i in range(len(RoleIds)):	
			if RoleIds[i] is not None:
				self.add_query_param('RoleId.' + str(i + 1) , RoleIds[i]);

	def get_DisplayName(self):
		return self.get_query_params().get('DisplayName')

	def set_DisplayName(self,DisplayName):
		self.add_query_param('DisplayName',DisplayName)

	def get_SkillGroupIds(self):
		return self.get_query_params().get('SkillGroupIds')

	def set_SkillGroupIds(self,SkillGroupIds):
		for i in range(len(SkillGroupIds)):	
			if SkillGroupIds[i] is not None:
				self.add_query_param('SkillGroupId.' + str(i + 1) , SkillGroupIds[i]);

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)