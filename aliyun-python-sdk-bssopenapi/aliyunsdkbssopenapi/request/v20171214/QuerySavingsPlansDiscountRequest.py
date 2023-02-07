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

class QuerySavingsPlansDiscountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'QuerySavingsPlansDiscount','bssopenapi')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CommodityCode(self): # String
		return self.get_query_params().get('CommodityCode')

	def set_CommodityCode(self, CommodityCode):  # String
		self.add_query_param('CommodityCode', CommodityCode)
	def get_Locale(self): # String
		return self.get_query_params().get('Locale')

	def set_Locale(self, Locale):  # String
		self.add_query_param('Locale', Locale)
	def get_PageNum(self): # Integer
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # Integer
		self.add_query_param('PageNum', PageNum)
	def get_Cycle(self): # String
		return self.get_query_params().get('Cycle')

	def set_Cycle(self, Cycle):  # String
		self.add_query_param('Cycle', Cycle)
	def get_Spec(self): # String
		return self.get_query_params().get('Spec')

	def set_Spec(self, Spec):  # String
		self.add_query_param('Spec', Spec)
	def get_ModuleCode(self): # String
		return self.get_query_params().get('ModuleCode')

	def set_ModuleCode(self, ModuleCode):  # String
		self.add_query_param('ModuleCode', ModuleCode)
	def get_PayMode(self): # String
		return self.get_query_params().get('PayMode')

	def set_PayMode(self, PayMode):  # String
		self.add_query_param('PayMode', PayMode)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_SpnType(self): # String
		return self.get_query_params().get('SpnType')

	def set_SpnType(self, SpnType):  # String
		self.add_query_param('SpnType', SpnType)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
