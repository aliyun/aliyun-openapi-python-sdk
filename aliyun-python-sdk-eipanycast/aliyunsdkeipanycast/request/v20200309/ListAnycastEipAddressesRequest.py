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


	def get_BusinessStatus(self):
		return self.get_query_params().get('BusinessStatus')

	def set_BusinessStatus(self,BusinessStatus):
		self.add_query_param('BusinessStatus',BusinessStatus)

	def get_ServiceLocation(self):
		return self.get_query_params().get('ServiceLocation')

	def set_ServiceLocation(self,ServiceLocation):
		self.add_query_param('ServiceLocation',ServiceLocation)

	def get_AnycastEipAddress(self):
		return self.get_query_params().get('AnycastEipAddress')

	def set_AnycastEipAddress(self,AnycastEipAddress):
		self.add_query_param('AnycastEipAddress',AnycastEipAddress)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_AnycastId(self):
		return self.get_query_params().get('AnycastId')

	def set_AnycastId(self,AnycastId):
		self.add_query_param('AnycastId',AnycastId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_BindInstanceIdss(self):
		return self.get_query_params().get('BindInstanceIds')

	def set_BindInstanceIdss(self, BindInstanceIdss):
		for depth1 in range(len(BindInstanceIdss)):
			if BindInstanceIdss[depth1] is not None:
				self.add_query_param('BindInstanceIds.' + str(depth1 + 1) , BindInstanceIdss[depth1])

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)