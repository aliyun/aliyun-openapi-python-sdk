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


	def get_Commoditiess(self):
		return self.get_query_params().get('Commoditiess')

	def set_Commoditiess(self, Commoditiess):
		for depth1 in range(len(Commoditiess)):
			if Commoditiess[depth1].get('Amount') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.Amount', Commoditiess[depth1].get('Amount'))
			if Commoditiess[depth1].get('Period') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.Period', Commoditiess[depth1].get('Period'))
			if Commoditiess[depth1].get('NodeType') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.NodeType', Commoditiess[depth1].get('NodeType'))
			if Commoditiess[depth1].get('SystemDiskCategory') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.SystemDiskCategory', Commoditiess[depth1].get('SystemDiskCategory'))
			if Commoditiess[depth1].get('InternetChargeType') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.InternetChargeType', Commoditiess[depth1].get('InternetChargeType'))
			if Commoditiess[depth1].get('SystemDiskSize') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.SystemDiskSize', Commoditiess[depth1].get('SystemDiskSize'))
			if Commoditiess[depth1].get('InternetMaxBandWidthOut') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.InternetMaxBandWidthOut', Commoditiess[depth1].get('InternetMaxBandWidthOut'))
			if Commoditiess[depth1].get('InstanceType') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.InstanceType', Commoditiess[depth1].get('InstanceType'))
			if Commoditiess[depth1].get('NetworkType') is not None:
				self.add_query_param('Commodities.' + str(depth1 + 1) + '.NetworkType', Commoditiess[depth1].get('NetworkType'))

	def get_PriceUnit(self):
		return self.get_query_params().get('PriceUnit')

	def set_PriceUnit(self,PriceUnit):
		self.add_query_param('PriceUnit',PriceUnit)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_OrderType(self):
		return self.get_query_params().get('OrderType')

	def set_OrderType(self,OrderType):
		self.add_query_param('OrderType',OrderType)