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

class ListRegistrationPoliciesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListRegistrationPolicies')
		self.set_method('GET')

	def get_PolicyIds(self): # Array
		return self.get_query_params().get('PolicyIds')

	def set_PolicyIds(self, PolicyIds):  # Array
		for index1, value1 in enumerate(PolicyIds):
			self.add_query_param('PolicyIds.' + str(index1 + 1), value1)
	def get_MatchMode(self): # String
		return self.get_query_params().get('MatchMode')

	def set_MatchMode(self, MatchMode):  # String
		self.add_query_param('MatchMode', MatchMode)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_UserGroupId(self): # String
		return self.get_query_params().get('UserGroupId')

	def set_UserGroupId(self, UserGroupId):  # String
		self.add_query_param('UserGroupId', UserGroupId)
	def get_CurrentPage(self): # Long
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Long
		self.add_query_param('CurrentPage', CurrentPage)
	def get_PersonalLimitType(self): # String
		return self.get_query_params().get('PersonalLimitType')

	def set_PersonalLimitType(self, PersonalLimitType):  # String
		self.add_query_param('PersonalLimitType', PersonalLimitType)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_CompanyLimitType(self): # String
		return self.get_query_params().get('CompanyLimitType')

	def set_CompanyLimitType(self, CompanyLimitType):  # String
		self.add_query_param('CompanyLimitType', CompanyLimitType)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
