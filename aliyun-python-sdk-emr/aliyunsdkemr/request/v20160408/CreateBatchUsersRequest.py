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

class CreateBatchUsersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateBatchUsers','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_UserBaseParamLists(self):
		return self.get_query_params().get('UserBaseParamLists')

	def set_UserBaseParamLists(self,UserBaseParamLists):
		for i in range(len(UserBaseParamLists)):	
			if UserBaseParamLists[i].get('AliyunUserId') is not None:
				self.add_query_param('UserBaseParamList.' + str(i + 1) + '.AliyunUserId' , UserBaseParamLists[i].get('AliyunUserId'))
			if UserBaseParamLists[i].get('UserName') is not None:
				self.add_query_param('UserBaseParamList.' + str(i + 1) + '.UserName' , UserBaseParamLists[i].get('UserName'))
			if UserBaseParamLists[i].get('UserType') is not None:
				self.add_query_param('UserBaseParamList.' + str(i + 1) + '.UserType' , UserBaseParamLists[i].get('UserType'))
			if UserBaseParamLists[i].get('IsSuperAdmin') is not None:
				self.add_query_param('UserBaseParamList.' + str(i + 1) + '.IsSuperAdmin' , UserBaseParamLists[i].get('IsSuperAdmin'))


	def get_RoleIds(self):
		return self.get_query_params().get('RoleIds')

	def set_RoleIds(self,RoleIds):
		for i in range(len(RoleIds)):	
			if RoleIds[i] is not None:
				self.add_query_param('RoleId.' + str(i + 1) , RoleIds[i]);

	def get_GroupIds(self):
		return self.get_query_params().get('GroupIds')

	def set_GroupIds(self,GroupIds):
		for i in range(len(GroupIds)):	
			if GroupIds[i] is not None:
				self.add_query_param('GroupId.' + str(i + 1) , GroupIds[i]);

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)