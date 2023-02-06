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
from aliyunsdkecs.endpoint import endpoint_data

class ModifyImageSharePermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyImageSharePermission','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_IsPublic(self): # Boolean
		return self.get_query_params().get('IsPublic')

	def set_IsPublic(self, IsPublic):  # Boolean
		self.add_query_param('IsPublic', IsPublic)
	def get_LaunchPermission(self): # String
		return self.get_query_params().get('LaunchPermission')

	def set_LaunchPermission(self, LaunchPermission):  # String
		self.add_query_param('LaunchPermission', LaunchPermission)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_AddAccounts(self): # RepeatList
		return self.get_query_params().get('AddAccount')

	def set_AddAccounts(self, AddAccount):  # RepeatList
		for depth1 in range(len(AddAccount)):
			self.add_query_param('AddAccount.' + str(depth1 + 1), AddAccount[depth1])
	def get_RemoveAccounts(self): # RepeatList
		return self.get_query_params().get('RemoveAccount')

	def set_RemoveAccounts(self, RemoveAccount):  # RepeatList
		for depth1 in range(len(RemoveAccount)):
			self.add_query_param('RemoveAccount.' + str(depth1 + 1), RemoveAccount[depth1])
