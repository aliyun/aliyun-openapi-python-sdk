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

class GetSubscriptionPriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'GetSubscriptionPrice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_query_param('ProductCode', ProductCode)
	def get_Quantity(self): # Integer
		return self.get_query_params().get('Quantity')

	def set_Quantity(self, Quantity):  # Integer
		self.add_query_param('Quantity', Quantity)
	def get_SubscriptionType(self): # String
		return self.get_query_params().get('SubscriptionType')

	def set_SubscriptionType(self, SubscriptionType):  # String
		self.add_query_param('SubscriptionType', SubscriptionType)
	def get_ModuleLists(self): # RepeatList
		return self.get_query_params().get('ModuleList')

	def set_ModuleLists(self, ModuleList):  # RepeatList
		for depth1 in range(len(ModuleList)):
			if ModuleList[depth1].get('ModuleCode') is not None:
				self.add_query_param('ModuleList.' + str(depth1 + 1) + '.ModuleCode', ModuleList[depth1].get('ModuleCode'))
			if ModuleList[depth1].get('ModuleStatus') is not None:
				self.add_query_param('ModuleList.' + str(depth1 + 1) + '.ModuleStatus', ModuleList[depth1].get('ModuleStatus'))
			if ModuleList[depth1].get('Tag') is not None:
				self.add_query_param('ModuleList.' + str(depth1 + 1) + '.Tag', ModuleList[depth1].get('Tag'))
			if ModuleList[depth1].get('Config') is not None:
				self.add_query_param('ModuleList.' + str(depth1 + 1) + '.Config', ModuleList[depth1].get('Config'))
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ProductType(self): # String
		return self.get_query_params().get('ProductType')

	def set_ProductType(self, ProductType):  # String
		self.add_query_param('ProductType', ProductType)
	def get_ServicePeriodQuantity(self): # Integer
		return self.get_query_params().get('ServicePeriodQuantity')

	def set_ServicePeriodQuantity(self, ServicePeriodQuantity):  # Integer
		self.add_query_param('ServicePeriodQuantity', ServicePeriodQuantity)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ServicePeriodUnit(self): # String
		return self.get_query_params().get('ServicePeriodUnit')

	def set_ServicePeriodUnit(self, ServicePeriodUnit):  # String
		self.add_query_param('ServicePeriodUnit', ServicePeriodUnit)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
	def get_OrderType(self): # String
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # String
		self.add_query_param('OrderType', OrderType)
