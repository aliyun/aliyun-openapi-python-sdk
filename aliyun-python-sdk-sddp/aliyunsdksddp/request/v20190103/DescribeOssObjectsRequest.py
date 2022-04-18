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

class DescribeOssObjectsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'DescribeOssObjects','sddp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RiskLevelId(self): # Integer
		return self.get_query_params().get('RiskLevelId')

	def set_RiskLevelId(self, RiskLevelId):  # Integer
		self.add_query_param('RiskLevelId', RiskLevelId)
	def get_LastScanTimeEnd(self): # Long
		return self.get_query_params().get('LastScanTimeEnd')

	def set_LastScanTimeEnd(self, LastScanTimeEnd):  # Long
		self.add_query_param('LastScanTimeEnd', LastScanTimeEnd)
	def get_LastScanTimeStart(self): # Long
		return self.get_query_params().get('LastScanTimeStart')

	def set_LastScanTimeStart(self, LastScanTimeStart):  # Long
		self.add_query_param('LastScanTimeStart', LastScanTimeStart)
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
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_RuleId(self): # Long
		return self.get_query_params().get('RuleId')

	def set_RuleId(self, RuleId):  # Long
		self.add_query_param('RuleId', RuleId)
