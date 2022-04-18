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
from aliyunsdksddp.endpoint import endpoint_data

class DescribeInstanceSourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'DescribeInstanceSources','sddp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_query_param('ProductCode', ProductCode)
	def get_ProductId(self): # Long
		return self.get_query_params().get('ProductId')

	def set_ProductId(self, ProductId):  # Long
		self.add_query_param('ProductId', ProductId)
	def get_SearchKey(self): # String
		return self.get_query_params().get('SearchKey')

	def set_SearchKey(self, SearchKey):  # String
		self.add_query_param('SearchKey', SearchKey)
	def get_SearchType(self): # String
		return self.get_query_params().get('SearchType')

	def set_SearchType(self, SearchType):  # String
		self.add_query_param('SearchType', SearchType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_ServiceRegionId(self): # String
		return self.get_query_params().get('ServiceRegionId')

	def set_ServiceRegionId(self, ServiceRegionId):  # String
		self.add_query_param('ServiceRegionId', ServiceRegionId)
	def get_EngineType(self): # String
		return self.get_query_params().get('EngineType')

	def set_EngineType(self, EngineType):  # String
		self.add_query_param('EngineType', EngineType)
	def get_AuditStatus(self): # Integer
		return self.get_query_params().get('AuditStatus')

	def set_AuditStatus(self, AuditStatus):  # Integer
		self.add_query_param('AuditStatus', AuditStatus)
	def get_AuthStatus(self): # Integer
		return self.get_query_params().get('AuthStatus')

	def set_AuthStatus(self, AuthStatus):  # Integer
		self.add_query_param('AuthStatus', AuthStatus)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
