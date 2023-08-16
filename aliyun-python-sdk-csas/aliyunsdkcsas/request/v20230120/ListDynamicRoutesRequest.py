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

class ListDynamicRoutesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListDynamicRoutes')
		self.set_method('GET')

	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ApplicationId(self): # String
		return self.get_query_params().get('ApplicationId')

	def set_ApplicationId(self, ApplicationId):  # String
		self.add_query_param('ApplicationId', ApplicationId)
	def get_DynamicRouteIds(self): # Array
		return self.get_query_params().get('DynamicRouteIds')

	def set_DynamicRouteIds(self, DynamicRouteIds):  # Array
		for index1, value1 in enumerate(DynamicRouteIds):
			self.add_query_param('DynamicRouteIds.' + str(index1 + 1), value1)
	def get_TagId(self): # String
		return self.get_query_params().get('TagId')

	def set_TagId(self, TagId):  # String
		self.add_query_param('TagId', TagId)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_RegionIds(self): # Array
		return self.get_query_params().get('RegionIds')

	def set_RegionIds(self, RegionIds):  # Array
		for index1, value1 in enumerate(RegionIds):
			self.add_query_param('RegionIds.' + str(index1 + 1), value1)
	def get_NextHop(self): # String
		return self.get_query_params().get('NextHop')

	def set_NextHop(self, NextHop):  # String
		self.add_query_param('NextHop', NextHop)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
