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

class ListUsersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListUsers')
		self.set_method('GET')

	def get_FuzzyUsername(self): # String
		return self.get_query_params().get('FuzzyUsername')

	def set_FuzzyUsername(self, FuzzyUsername):  # String
		self.add_query_param('FuzzyUsername', FuzzyUsername)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_Department(self): # String
		return self.get_query_params().get('Department')

	def set_Department(self, Department):  # String
		self.add_query_param('Department', Department)
	def get_CurrentPage(self): # Long
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Long
		self.add_query_param('CurrentPage', CurrentPage)
	def get_PreciseUsername(self): # String
		return self.get_query_params().get('PreciseUsername')

	def set_PreciseUsername(self, PreciseUsername):  # String
		self.add_query_param('PreciseUsername', PreciseUsername)
	def get_SaseUserIds(self): # Array
		return self.get_query_params().get('SaseUserIds')

	def set_SaseUserIds(self, SaseUserIds):  # Array
		for index1, value1 in enumerate(SaseUserIds):
			self.add_query_param('SaseUserIds.' + str(index1 + 1), value1)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
