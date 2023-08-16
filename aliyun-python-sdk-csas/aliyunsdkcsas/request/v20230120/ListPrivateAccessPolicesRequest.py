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

class ListPrivateAccessPolicesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListPrivateAccessPolices')
		self.set_method('GET')

	def get_PolicyIds(self): # Array
		return self.get_query_params().get('PolicyIds')

	def set_PolicyIds(self, PolicyIds):  # Array
		for index1, value1 in enumerate(PolicyIds):
			self.add_query_param('PolicyIds.' + str(index1 + 1), value1)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ApplicationId(self): # String
		return self.get_query_params().get('ApplicationId')

	def set_ApplicationId(self, ApplicationId):  # String
		self.add_query_param('ApplicationId', ApplicationId)
	def get_TagId(self): # String
		return self.get_query_params().get('TagId')

	def set_TagId(self, TagId):  # String
		self.add_query_param('TagId', TagId)
	def get_UserGroupId(self): # String
		return self.get_query_params().get('UserGroupId')

	def set_UserGroupId(self, UserGroupId):  # String
		self.add_query_param('UserGroupId', UserGroupId)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_PolicyAction(self): # String
		return self.get_query_params().get('PolicyAction')

	def set_PolicyAction(self, PolicyAction):  # String
		self.add_query_param('PolicyAction', PolicyAction)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
