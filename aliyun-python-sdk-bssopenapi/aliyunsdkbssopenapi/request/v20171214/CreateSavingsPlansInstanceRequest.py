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

class CreateSavingsPlansInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'CreateSavingsPlansInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Specification(self): # String
		return self.get_query_params().get('Specification')

	def set_Specification(self, Specification):  # String
		self.add_query_param('Specification', Specification)
	def get_PoolValue(self): # String
		return self.get_query_params().get('PoolValue')

	def set_PoolValue(self, PoolValue):  # String
		self.add_query_param('PoolValue', PoolValue)
	def get_CommodityCode(self): # String
		return self.get_query_params().get('CommodityCode')

	def set_CommodityCode(self, CommodityCode):  # String
		self.add_query_param('CommodityCode', CommodityCode)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_EffectiveDate(self): # String
		return self.get_query_params().get('EffectiveDate')

	def set_EffectiveDate(self, EffectiveDate):  # String
		self.add_query_param('EffectiveDate', EffectiveDate)
	def get_Duration(self): # String
		return self.get_query_params().get('Duration')

	def set_Duration(self, Duration):  # String
		self.add_query_param('Duration', Duration)
	def get_SpecType(self): # String
		return self.get_query_params().get('SpecType')

	def set_SpecType(self, SpecType):  # String
		self.add_query_param('SpecType', SpecType)
	def get_PayMode(self): # String
		return self.get_query_params().get('PayMode')

	def set_PayMode(self, PayMode):  # String
		self.add_query_param('PayMode', PayMode)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
	def get_PricingCycle(self): # String
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self, PricingCycle):  # String
		self.add_query_param('PricingCycle', PricingCycle)
