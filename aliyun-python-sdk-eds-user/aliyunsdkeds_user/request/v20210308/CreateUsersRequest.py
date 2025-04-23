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
from aliyunsdkeds_user.endpoint import endpoint_data

class CreateUsersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eds-user', '2021-03-08', 'CreateUsers','eds-user')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AutoLockTime(self): # String
		return self.get_query_params().get('AutoLockTime')

	def set_AutoLockTime(self, AutoLockTime):  # String
		self.add_query_param('AutoLockTime', AutoLockTime)
	def get_IsLocalAdmin(self): # Boolean
		return self.get_query_params().get('IsLocalAdmin')

	def set_IsLocalAdmin(self, IsLocalAdmin):  # Boolean
		self.add_query_param('IsLocalAdmin', IsLocalAdmin)
	def get_Userss(self): # RepeatList
		return self.get_body_params().get('Users')

	def set_Userss(self, Users):  # RepeatList
		for depth1 in range(len(Users)):
			if Users[depth1].get('Password') is not None:
				self.add_body_params('Users.' + str(depth1 + 1) + '.Password', Users[depth1].get('Password'))
			if Users[depth1].get('RealNickName') is not None:
				self.add_body_params('Users.' + str(depth1 + 1) + '.RealNickName', Users[depth1].get('RealNickName'))
			if Users[depth1].get('Phone') is not None:
				self.add_body_params('Users.' + str(depth1 + 1) + '.Phone', Users[depth1].get('Phone'))
			if Users[depth1].get('OwnerType') is not None:
				self.add_body_params('Users.' + str(depth1 + 1) + '.OwnerType', Users[depth1].get('OwnerType'))
			if Users[depth1].get('EndUserId') is not None:
				self.add_body_params('Users.' + str(depth1 + 1) + '.EndUserId', Users[depth1].get('EndUserId'))
			if Users[depth1].get('Remark') is not None:
				self.add_body_params('Users.' + str(depth1 + 1) + '.Remark', Users[depth1].get('Remark'))
			if Users[depth1].get('Email') is not None:
				self.add_body_params('Users.' + str(depth1 + 1) + '.Email', Users[depth1].get('Email'))
			if Users[depth1].get('OrgId') is not None:
				self.add_body_params('Users.' + str(depth1 + 1) + '.OrgId', Users[depth1].get('OrgId'))
	def get_Password(self): # String
		return self.get_body_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_body_params('Password', Password)
	def get_PasswordExpireDays(self): # String
		return self.get_query_params().get('PasswordExpireDays')

	def set_PasswordExpireDays(self, PasswordExpireDays):  # String
		self.add_query_param('PasswordExpireDays', PasswordExpireDays)
