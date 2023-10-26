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
from aliyunsdkecs.endpoint import endpoint_data

class DescribeSavingsPlanPriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeSavingsPlanPrice','ecs')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_ResourceIds(self): # RepeatList
		return self.get_query_params().get('ResourceId')

	def set_ResourceIds(self, ResourceId):  # RepeatList
		for depth1 in range(len(ResourceId)):
			self.add_query_param('ResourceId.' + str(depth1 + 1), ResourceId[depth1])
	def get_InstanceTypeFamily(self): # String
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamily(self, InstanceTypeFamily):  # String
		self.add_query_param('InstanceTypeFamily', InstanceTypeFamily)
	def get_PlanType(self): # String
		return self.get_query_params().get('PlanType')

	def set_PlanType(self, PlanType):  # String
		self.add_query_param('PlanType', PlanType)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_OfferingType(self): # String
		return self.get_query_params().get('OfferingType')

	def set_OfferingType(self, OfferingType):  # String
		self.add_query_param('OfferingType', OfferingType)
	def get_CommittedAmount(self): # String
		return self.get_query_params().get('CommittedAmount')

	def set_CommittedAmount(self, CommittedAmount):  # String
		self.add_query_param('CommittedAmount', CommittedAmount)
