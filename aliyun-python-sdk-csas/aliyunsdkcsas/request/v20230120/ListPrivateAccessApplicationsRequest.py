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

class ListPrivateAccessApplicationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListPrivateAccessApplications')
		self.set_method('GET')

	def get_PolicyId(self): # String
		return self.get_query_params().get('PolicyId')

	def set_PolicyId(self, PolicyId):  # String
		self.add_query_param('PolicyId', PolicyId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Address(self): # String
		return self.get_query_params().get('Address')

	def set_Address(self, Address):  # String
		self.add_query_param('Address', Address)
	def get_TagId(self): # String
		return self.get_query_params().get('TagId')

	def set_TagId(self, TagId):  # String
		self.add_query_param('TagId', TagId)
	def get_ConnectorId(self): # String
		return self.get_query_params().get('ConnectorId')

	def set_ConnectorId(self, ConnectorId):  # String
		self.add_query_param('ConnectorId', ConnectorId)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_ApplicationIds(self): # Array
		return self.get_query_params().get('ApplicationIds')

	def set_ApplicationIds(self, ApplicationIds):  # Array
		for index1, value1 in enumerate(ApplicationIds):
			self.add_query_param('ApplicationIds.' + str(index1 + 1), value1)
	def get_AccessModes(self): # String
		return self.get_query_params().get('AccessModes')

	def set_AccessModes(self, AccessModes):  # String
		self.add_query_param('AccessModes', AccessModes)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
