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
from aliyunsdkdomain.endpoint import endpoint_data

class SaveBatchTaskForCreatingOrderActivateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveBatchTaskForCreatingOrderActivate')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OrderActivateParams(self): # RepeatList
		return self.get_query_params().get('OrderActivateParam')

	def set_OrderActivateParams(self, OrderActivateParam):  # RepeatList
		for depth1 in range(len(OrderActivateParam)):
			if OrderActivateParam[depth1].get('Country') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Country', OrderActivateParam[depth1].get('Country'))
			if OrderActivateParam[depth1].get('SubscriptionDuration') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.SubscriptionDuration', OrderActivateParam[depth1].get('SubscriptionDuration'))
			if OrderActivateParam[depth1].get('PermitPremiumActivation') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.PermitPremiumActivation', OrderActivateParam[depth1].get('PermitPremiumActivation'))
			if OrderActivateParam[depth1].get('City') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.City', OrderActivateParam[depth1].get('City'))
			if OrderActivateParam[depth1].get('Dns2') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Dns2', OrderActivateParam[depth1].get('Dns2'))
			if OrderActivateParam[depth1].get('Dns1') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Dns1', OrderActivateParam[depth1].get('Dns1'))
			if OrderActivateParam[depth1].get('RegistrantProfileId') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.RegistrantProfileId', OrderActivateParam[depth1].get('RegistrantProfileId'))
			if OrderActivateParam[depth1].get('AliyunDns') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.AliyunDns', OrderActivateParam[depth1].get('AliyunDns'))
			if OrderActivateParam[depth1].get('ZhCity') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhCity', OrderActivateParam[depth1].get('ZhCity'))
			if OrderActivateParam[depth1].get('TelExt') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.TelExt', OrderActivateParam[depth1].get('TelExt'))
			if OrderActivateParam[depth1].get('ZhRegistrantName') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhRegistrantName', OrderActivateParam[depth1].get('ZhRegistrantName'))
			if OrderActivateParam[depth1].get('Province') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Province', OrderActivateParam[depth1].get('Province'))
			if OrderActivateParam[depth1].get('PostalCode') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.PostalCode', OrderActivateParam[depth1].get('PostalCode'))
			if OrderActivateParam[depth1].get('Email') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Email', OrderActivateParam[depth1].get('Email'))
			if OrderActivateParam[depth1].get('ZhRegistrantOrganization') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhRegistrantOrganization', OrderActivateParam[depth1].get('ZhRegistrantOrganization'))
			if OrderActivateParam[depth1].get('Address') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Address', OrderActivateParam[depth1].get('Address'))
			if OrderActivateParam[depth1].get('TelArea') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.TelArea', OrderActivateParam[depth1].get('TelArea'))
			if OrderActivateParam[depth1].get('DomainName') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.DomainName', OrderActivateParam[depth1].get('DomainName'))
			if OrderActivateParam[depth1].get('RegistrantType') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.RegistrantType', OrderActivateParam[depth1].get('RegistrantType'))
			if OrderActivateParam[depth1].get('ZhAddress') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhAddress', OrderActivateParam[depth1].get('ZhAddress'))
			if OrderActivateParam[depth1].get('Telephone') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Telephone', OrderActivateParam[depth1].get('Telephone'))
			if OrderActivateParam[depth1].get('TrademarkDomainActivation') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.TrademarkDomainActivation', OrderActivateParam[depth1].get('TrademarkDomainActivation'))
			if OrderActivateParam[depth1].get('ZhProvince') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhProvince', OrderActivateParam[depth1].get('ZhProvince'))
			if OrderActivateParam[depth1].get('RegistrantOrganization') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.RegistrantOrganization', OrderActivateParam[depth1].get('RegistrantOrganization'))
			if OrderActivateParam[depth1].get('EnableDomainProxy') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.EnableDomainProxy', OrderActivateParam[depth1].get('EnableDomainProxy'))
			if OrderActivateParam[depth1].get('RegistrantName') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.RegistrantName', OrderActivateParam[depth1].get('RegistrantName'))
	def get_CouponNo(self): # String
		return self.get_query_params().get('CouponNo')

	def set_CouponNo(self, CouponNo):  # String
		self.add_query_param('CouponNo', CouponNo)
	def get_UseCoupon(self): # Boolean
		return self.get_query_params().get('UseCoupon')

	def set_UseCoupon(self, UseCoupon):  # Boolean
		self.add_query_param('UseCoupon', UseCoupon)
	def get_PromotionNo(self): # String
		return self.get_query_params().get('PromotionNo')

	def set_PromotionNo(self, PromotionNo):  # String
		self.add_query_param('PromotionNo', PromotionNo)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_UsePromotion(self): # Boolean
		return self.get_query_params().get('UsePromotion')

	def set_UsePromotion(self, UsePromotion):  # Boolean
		self.add_query_param('UsePromotion', UsePromotion)
