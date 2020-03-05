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
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'DescribePrice','ehs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Commoditiess(self):
		return self.get_query_params().get('Commoditiess')

	def set_Commoditiess(self,Commoditiess):
		for i in range(len(Commoditiess)):	
			if Commoditiess[i].get('Amount') is not None:
				self.add_query_param('Commodities.' + str(i + 1) + '.Amount' , Commoditiess[i].get('Amount'))
			if Commoditiess[i].get('Period') is not None:
				self.add_query_param('Commodities.' + str(i + 1) + '.Period' , Commoditiess[i].get('Period'))
			if Commoditiess[i].get('NodeType') is not None:
				self.add_query_param('Commodities.' + str(i + 1) + '.NodeType' , Commoditiess[i].get('NodeType'))
			if Commoditiess[i].get('SystemDiskCategory') is not None:
				self.add_query_param('Commodities.' + str(i + 1) + '.SystemDiskCategory' , Commoditiess[i].get('SystemDiskCategory'))
			if Commoditiess[i].get('SystemDiskSize') is not None:
				self.add_query_param('Commodities.' + str(i + 1) + '.SystemDiskSize' , Commoditiess[i].get('SystemDiskSize'))
			if Commoditiess[i].get('InstanceType') is not None:
				self.add_query_param('Commodities.' + str(i + 1) + '.InstanceType' , Commoditiess[i].get('InstanceType'))
			if Commoditiess[i].get('NetworkType') is not None:
				self.add_query_param('Commodities.' + str(i + 1) + '.NetworkType' , Commoditiess[i].get('NetworkType'))


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