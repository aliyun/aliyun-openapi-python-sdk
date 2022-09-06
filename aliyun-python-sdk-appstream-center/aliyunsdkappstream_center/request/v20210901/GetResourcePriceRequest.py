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

class GetResourcePriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'appstream-center', '2021-09-01', 'GetResourcePrice')
		self.set_method('POST')

	def get_BizRegionId(self): # String
		return self.get_query_params().get('BizRegionId')

	def set_BizRegionId(self, BizRegionId):  # String
		self.add_query_param('BizRegionId', BizRegionId)
	def get_Period(self): # Long
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Long
		self.add_query_param('Period', Period)
	def get_Amount(self): # Long
		return self.get_query_params().get('Amount')

	def set_Amount(self, Amount):  # Long
		self.add_query_param('Amount', Amount)
	def get_NodeInstanceType(self): # String
		return self.get_query_params().get('NodeInstanceType')

	def set_NodeInstanceType(self, NodeInstanceType):  # String
		self.add_query_param('NodeInstanceType', NodeInstanceType)
	def get_ProductType(self): # String
		return self.get_query_params().get('ProductType')

	def set_ProductType(self, ProductType):  # String
		self.add_query_param('ProductType', ProductType)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
