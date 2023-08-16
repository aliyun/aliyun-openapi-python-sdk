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

class ListUserGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListUserGroups')
		self.set_method('GET')

	def get_AttributeValue(self): # String
		return self.get_query_params().get('AttributeValue')

	def set_AttributeValue(self, AttributeValue):  # String
		self.add_query_param('AttributeValue', AttributeValue)
	def get_PAPolicyId(self): # String
		return self.get_query_params().get('PAPolicyId')

	def set_PAPolicyId(self, PAPolicyId):  # String
		self.add_query_param('PAPolicyId', PAPolicyId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_UserGroupIds(self): # Array
		return self.get_query_params().get('UserGroupIds')

	def set_UserGroupIds(self, UserGroupIds):  # Array
		for index1, value1 in enumerate(UserGroupIds):
			self.add_query_param('UserGroupIds.' + str(index1 + 1), value1)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
