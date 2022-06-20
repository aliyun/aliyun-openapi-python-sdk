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
from aliyunsdksas.endpoint import endpoint_data

class ModifyStrategyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ModifyStrategy')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CycleDays(self): # String
		return self.get_query_params().get('CycleDays')

	def set_CycleDays(self, CycleDays):  # String
		self.add_query_param('CycleDays', CycleDays)
	def get_RiskSubTypeName(self): # String
		return self.get_query_params().get('RiskSubTypeName')

	def set_RiskSubTypeName(self, RiskSubTypeName):  # String
		self.add_query_param('RiskSubTypeName', RiskSubTypeName)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_Id(self): # String
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_query_param('Id', Id)
	def get_RiskCustomParams(self): # String
		return self.get_query_params().get('RiskCustomParams')

	def set_RiskCustomParams(self, RiskCustomParams):  # String
		self.add_query_param('RiskCustomParams', RiskCustomParams)
	def get_CustomType(self): # String
		return self.get_query_params().get('CustomType')

	def set_CustomType(self, CustomType):  # String
		self.add_query_param('CustomType', CustomType)
	def get_CycleStartTime(self): # String
		return self.get_query_params().get('CycleStartTime')

	def set_CycleStartTime(self, CycleStartTime):  # String
		self.add_query_param('CycleStartTime', CycleStartTime)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
