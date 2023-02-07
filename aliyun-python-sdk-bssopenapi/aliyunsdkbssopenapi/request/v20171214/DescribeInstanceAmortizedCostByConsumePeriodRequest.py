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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class DescribeInstanceAmortizedCostByConsumePeriodRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'DescribeInstanceAmortizedCostByConsumePeriod','bssopenapi')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductDetail(self): # String
		return self.get_body_params().get('ProductDetail')

	def set_ProductDetail(self, ProductDetail):  # String
		self.add_body_params('ProductDetail', ProductDetail)
	def get_ProductCode(self): # String
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_body_params('ProductCode', ProductCode)
	def get_BillOwnerIdLists(self): # RepeatList
		return self.get_body_params().get('BillOwnerIdList')

	def set_BillOwnerIdLists(self, BillOwnerIdList):  # RepeatList
		for depth1 in range(len(BillOwnerIdList)):
			self.add_body_params('BillOwnerIdList.' + str(depth1 + 1), BillOwnerIdList[depth1])
	def get_SubscriptionType(self): # String
		return self.get_body_params().get('SubscriptionType')

	def set_SubscriptionType(self, SubscriptionType):  # String
		self.add_body_params('SubscriptionType', SubscriptionType)
	def get_BillingCycle(self): # String
		return self.get_body_params().get('BillingCycle')

	def set_BillingCycle(self, BillingCycle):  # String
		self.add_body_params('BillingCycle', BillingCycle)
	def get_CostUnitCode(self): # String
		return self.get_body_params().get('CostUnitCode')

	def set_CostUnitCode(self, CostUnitCode):  # String
		self.add_body_params('CostUnitCode', CostUnitCode)
	def get_AmortizationPeriodFilters(self): # RepeatList
		return self.get_body_params().get('AmortizationPeriodFilter')

	def set_AmortizationPeriodFilters(self, AmortizationPeriodFilter):  # RepeatList
		for depth1 in range(len(AmortizationPeriodFilter)):
			self.add_body_params('AmortizationPeriodFilter.' + str(depth1 + 1), AmortizationPeriodFilter[depth1])
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_BillUserIdLists(self): # RepeatList
		return self.get_body_params().get('BillUserIdList')

	def set_BillUserIdLists(self, BillUserIdList):  # RepeatList
		for depth1 in range(len(BillUserIdList)):
			self.add_body_params('BillUserIdList.' + str(depth1 + 1), BillUserIdList[depth1])
	def get_InstanceIdLists(self): # RepeatList
		return self.get_body_params().get('InstanceIdList')

	def set_InstanceIdLists(self, InstanceIdList):  # RepeatList
		for depth1 in range(len(InstanceIdList)):
			self.add_body_params('InstanceIdList.' + str(depth1 + 1), InstanceIdList[depth1])
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
