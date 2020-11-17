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
from aliyunsdkconfig.endpoint import endpoint_data

class ListDiscoveredResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Config', '2019-01-08', 'ListDiscoveredResources','Config')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceDeleted(self):
		return self.get_query_params().get('ResourceDeleted')

	def set_ResourceDeleted(self,ResourceDeleted):
		self.add_query_param('ResourceDeleted',ResourceDeleted)

	def get_MultiAccount(self):
		return self.get_query_params().get('MultiAccount')

	def set_MultiAccount(self,MultiAccount):
		self.add_query_param('MultiAccount',MultiAccount)

	def get_Regions(self):
		return self.get_query_params().get('Regions')

	def set_Regions(self,Regions):
		self.add_query_param('Regions',Regions)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ComplianceType(self):
		return self.get_query_params().get('ComplianceType')

	def set_ComplianceType(self,ComplianceType):
		self.add_query_param('ComplianceType',ComplianceType)

	def get_ResourceId(self):
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self,ResourceId):
		self.add_query_param('ResourceId',ResourceId)

	def get_ResourceTypes(self):
		return self.get_query_params().get('ResourceTypes')

	def set_ResourceTypes(self,ResourceTypes):
		self.add_query_param('ResourceTypes',ResourceTypes)

	def get_MemberId(self):
		return self.get_query_params().get('MemberId')

	def set_MemberId(self,MemberId):
		self.add_query_param('MemberId',MemberId)