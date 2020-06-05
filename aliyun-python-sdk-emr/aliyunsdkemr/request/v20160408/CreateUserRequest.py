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
from aliyunsdkemr.endpoint import endpoint_data

class CreateUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateUser','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_UserType(self):
		return self.get_query_params().get('UserType')

	def set_UserType(self,UserType):
		self.add_query_param('UserType',UserType)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_UserAccountParamLists(self):
		return self.get_query_params().get('UserAccountParamLists')

	def set_UserAccountParamLists(self, UserAccountParamLists):
		for depth1 in range(len(UserAccountParamLists)):
			if UserAccountParamLists[depth1].get('AccountType') is not None:
				self.add_query_param('UserAccountParamList.' + str(depth1 + 1) + '.AccountType', UserAccountParamLists[depth1].get('AccountType'))
			if UserAccountParamLists[depth1].get('AuthType') is not None:
				self.add_query_param('UserAccountParamList.' + str(depth1 + 1) + '.AuthType', UserAccountParamLists[depth1].get('AuthType'))
			if UserAccountParamLists[depth1].get('AccountPassword') is not None:
				self.add_query_param('UserAccountParamList.' + str(depth1 + 1) + '.AccountPassword', UserAccountParamLists[depth1].get('AccountPassword'))

	def get_GroupIdLists(self):
		return self.get_query_params().get('GroupIdLists')

	def set_GroupIdLists(self, GroupIdLists):
		for depth1 in range(len(GroupIdLists)):
			if GroupIdLists[depth1] is not None:
				self.add_query_param('GroupIdList.' + str(depth1 + 1) , GroupIdLists[depth1])

	def get_RoleIdLists(self):
		return self.get_query_params().get('RoleIdLists')

	def set_RoleIdLists(self, RoleIdLists):
		for depth1 in range(len(RoleIdLists)):
			if RoleIdLists[depth1] is not None:
				self.add_query_param('RoleIdList.' + str(depth1 + 1) , RoleIdLists[depth1])

	def get_AliyunUserId(self):
		return self.get_query_params().get('AliyunUserId')

	def set_AliyunUserId(self,AliyunUserId):
		self.add_query_param('AliyunUserId',AliyunUserId)

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)