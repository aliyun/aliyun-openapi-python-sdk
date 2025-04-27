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

class DescribeResourceGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eds-user', '2021-03-08', 'DescribeResourceGroups','eds-user')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceGroupName(self): # String
		return self.get_query_params().get('ResourceGroupName')

	def set_ResourceGroupName(self, ResourceGroupName):  # String
		self.add_query_param('ResourceGroupName', ResourceGroupName)
	def get_NeedContainResourceGroupWithOfficeSite(self): # Long
		return self.get_query_params().get('NeedContainResourceGroupWithOfficeSite')

	def set_NeedContainResourceGroupWithOfficeSite(self, NeedContainResourceGroupWithOfficeSite):  # Long
		self.add_query_param('NeedContainResourceGroupWithOfficeSite', NeedContainResourceGroupWithOfficeSite)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_Platform(self): # String
		return self.get_query_params().get('Platform')

	def set_Platform(self, Platform):  # String
		self.add_query_param('Platform', Platform)
	def get_ResourceGroupIds(self): # Array
		return self.get_query_params().get('ResourceGroupIds')

	def set_ResourceGroupIds(self, ResourceGroupIds):  # Array
		for index1, value1 in enumerate(ResourceGroupIds):
			self.add_query_param('ResourceGroupIds.' + str(index1 + 1), value1)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
