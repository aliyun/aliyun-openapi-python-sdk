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
from aliyunsdkdbfs.endpoint import endpoint_data

class InsertSynchronizConstantsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DBFS', '2020-04-18', 'InsertSynchronizConstants')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ZoneData(self):
		return self.get_query_params().get('ZoneData')

	def set_ZoneData(self,ZoneData):
		self.add_query_param('ZoneData',ZoneData)

	def get_OsversionData(self):
		return self.get_query_params().get('OsversionData')

	def set_OsversionData(self,OsversionData):
		self.add_query_param('OsversionData',OsversionData)

	def get_EndpointData(self):
		return self.get_query_params().get('EndpointData')

	def set_EndpointData(self,EndpointData):
		self.add_query_param('EndpointData',EndpointData)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_MasterData(self):
		return self.get_query_params().get('MasterData')

	def set_MasterData(self,MasterData):
		self.add_query_param('MasterData',MasterData)

	def get_ProductCodeData(self):
		return self.get_query_params().get('ProductCodeData')

	def set_ProductCodeData(self,ProductCodeData):
		self.add_query_param('ProductCodeData',ProductCodeData)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_AccessData(self):
		return self.get_query_params().get('AccessData')

	def set_AccessData(self,AccessData):
		self.add_query_param('AccessData',AccessData)

	def get_RegionData(self):
		return self.get_query_params().get('RegionData')

	def set_RegionData(self,RegionData):
		self.add_query_param('RegionData',RegionData)