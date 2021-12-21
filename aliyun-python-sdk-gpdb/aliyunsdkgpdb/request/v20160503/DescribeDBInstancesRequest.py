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
from aliyunsdkgpdb.endpoint import endpoint_data

class DescribeDBInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'DescribeDBInstances')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBInstanceModes(self): # Array
		return self.get_query_params().get('DBInstanceModes')

	def set_DBInstanceModes(self, DBInstanceModes):  # Array
		for index1, value1 in enumerate(DBInstanceModes):
			self.add_query_param('DBInstanceModes.' + str(index1 + 1), value1)
	def get_DBInstanceStatuses(self): # Array
		return self.get_query_params().get('DBInstanceStatuses')

	def set_DBInstanceStatuses(self, DBInstanceStatuses):  # Array
		for index1, value1 in enumerate(DBInstanceStatuses):
			self.add_query_param('DBInstanceStatuses.' + str(index1 + 1), value1)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_DBInstanceDescription(self): # String
		return self.get_query_params().get('DBInstanceDescription')

	def set_DBInstanceDescription(self, DBInstanceDescription):  # String
		self.add_query_param('DBInstanceDescription', DBInstanceDescription)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_DBInstanceIds(self): # String
		return self.get_query_params().get('DBInstanceIds')

	def set_DBInstanceIds(self, DBInstanceIds):  # String
		self.add_query_param('DBInstanceIds', DBInstanceIds)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_DBInstanceCategories(self): # Array
		return self.get_query_params().get('DBInstanceCategories')

	def set_DBInstanceCategories(self, DBInstanceCategories):  # Array
		for index1, value1 in enumerate(DBInstanceCategories):
			self.add_query_param('DBInstanceCategories.' + str(index1 + 1), value1)
	def get_InstanceDeployTypes(self): # Array
		return self.get_query_params().get('InstanceDeployTypes')

	def set_InstanceDeployTypes(self, InstanceDeployTypes):  # Array
		for index1, value1 in enumerate(InstanceDeployTypes):
			self.add_query_param('InstanceDeployTypes.' + str(index1 + 1), value1)
	def get_InstanceNetworkType(self): # String
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self, InstanceNetworkType):  # String
		self.add_query_param('InstanceNetworkType', InstanceNetworkType)
