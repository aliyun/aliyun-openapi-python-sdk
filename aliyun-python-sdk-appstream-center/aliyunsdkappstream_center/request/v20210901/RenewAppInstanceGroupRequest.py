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

class RenewAppInstanceGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'appstream-center', '2021-09-01', 'RenewAppInstanceGroup')
		self.set_method('POST')

	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_PromotionId(self): # String
		return self.get_query_params().get('PromotionId')

	def set_PromotionId(self, PromotionId):  # String
		self.add_query_param('PromotionId', PromotionId)
	def get_ProductType(self): # String
		return self.get_query_params().get('ProductType')

	def set_ProductType(self, ProductType):  # String
		self.add_query_param('ProductType', ProductType)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_AppInstanceGroupId(self): # String
		return self.get_query_params().get('AppInstanceGroupId')

	def set_AppInstanceGroupId(self, AppInstanceGroupId):  # String
		self.add_query_param('AppInstanceGroupId', AppInstanceGroupId)
