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
from aliyunsdkeipanycast.endpoint import endpoint_data

class ListAnycastEipAddressesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eipanycast', '2020-03-09', 'ListAnycastEipAddresses','eipanycast')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_BusinessStatus(self): # String
		return self.get_query_params().get('BusinessStatus')

	def set_BusinessStatus(self, BusinessStatus):  # String
		self.add_query_param('BusinessStatus', BusinessStatus)
	def get_ServiceLocation(self): # String
		return self.get_query_params().get('ServiceLocation')

	def set_ServiceLocation(self, ServiceLocation):  # String
		self.add_query_param('ServiceLocation', ServiceLocation)
	def get_AnycastEipAddress(self): # String
		return self.get_query_params().get('AnycastEipAddress')

	def set_AnycastEipAddress(self, AnycastEipAddress):  # String
		self.add_query_param('AnycastEipAddress', AnycastEipAddress)
	def get_AnycastIdss(self): # RepeatList
		return self.get_query_params().get('AnycastIds')

	def set_AnycastIdss(self, AnycastIds):  # RepeatList
		for depth1 in range(len(AnycastIds)):
			self.add_query_param('AnycastIds.' + str(depth1 + 1), AnycastIds[depth1])
	def get_Tagss(self): # RepeatList
		return self.get_query_params().get('Tags')

	def set_Tagss(self, Tags):  # RepeatList
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_AnycastId(self): # String
		return self.get_query_params().get('AnycastId')

	def set_AnycastId(self, AnycastId):  # String
		self.add_query_param('AnycastId', AnycastId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_BindInstanceIdss(self): # RepeatList
		return self.get_query_params().get('BindInstanceIds')

	def set_BindInstanceIdss(self, BindInstanceIds):  # RepeatList
		for depth1 in range(len(BindInstanceIds)):
			self.add_query_param('BindInstanceIds.' + str(depth1 + 1), BindInstanceIds[depth1])
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
