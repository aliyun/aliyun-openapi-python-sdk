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
from aliyunsdkehpc.endpoint import endpoint_data

class DescribePriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'DescribePrice')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Commoditiess(self): # RepeatList
		return self.get_query_params().get('Commodities')

	def set_Commoditiess(self, Commodities):  # RepeatList
		for depth1 in range(len(Commodities)):
			if Commodities[depth1].get('Amount') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.Amount', Commodities[depth1].get('Amount'))
			if Commodities[depth1].get('Period') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.Period', Commodities[depth1].get('Period'))
			if Commodities[depth1].get('NodeType') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.NodeType', Commodities[depth1].get('NodeType'))
			if Commodities[depth1].get('DataDisks') is not None:
				for depth2 in range(len(Commodities[depth1].get('DataDisks'))):
					if Commodities[depth1].get('DataDisks')[depth2].get('size') is not None:
						self.add_query_param('Commodities.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.size', Commodities[depth1].get('DataDisks')[depth2].get('size'))
					if Commodities[depth1].get('DataDisks')[depth2].get('encrypted') is not None:
						self.add_query_param('Commodities.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.encrypted', Commodities[depth1].get('DataDisks')[depth2].get('encrypted'))
					if Commodities[depth1].get('DataDisks')[depth2].get('performanceLevel') is not None:
						self.add_query_param('Commodities.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.performanceLevel', Commodities[depth1].get('DataDisks')[depth2].get('performanceLevel'))
					if Commodities[depth1].get('DataDisks')[depth2].get('category') is not None:
						self.add_query_param('Commodities.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.category', Commodities[depth1].get('DataDisks')[depth2].get('category'))
					if Commodities[depth1].get('DataDisks')[depth2].get('deleteWithInstance') is not None:
						self.add_query_param('Commodities.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.deleteWithInstance', Commodities[depth1].get('DataDisks')[depth2].get('deleteWithInstance'))
			if Commodities[depth1].get('SystemDiskCategory') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.SystemDiskCategory', Commodities[depth1].get('SystemDiskCategory'))
			if Commodities[depth1].get('InternetChargeType') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.InternetChargeType', Commodities[depth1].get('InternetChargeType'))
			if Commodities[depth1].get('SystemDiskPerformanceLevel') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.SystemDiskPerformanceLevel', Commodities[depth1].get('SystemDiskPerformanceLevel'))
			if Commodities[depth1].get('SystemDiskSize') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.SystemDiskSize', Commodities[depth1].get('SystemDiskSize'))
			if Commodities[depth1].get('InternetMaxBandWidthOut') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.InternetMaxBandWidthOut', Commodities[depth1].get('InternetMaxBandWidthOut'))
			if Commodities[depth1].get('InstanceType') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.InstanceType', Commodities[depth1].get('InstanceType'))
			if Commodities[depth1].get('NetworkType') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.NetworkType', Commodities[depth1].get('NetworkType'))
	def get_PriceUnit(self): # String
		return self.get_query_params().get('PriceUnit')

	def set_PriceUnit(self, PriceUnit):  # String
		self.add_query_param('PriceUnit', PriceUnit)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_OrderType(self): # String
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # String
		self.add_query_param('OrderType', OrderType)
