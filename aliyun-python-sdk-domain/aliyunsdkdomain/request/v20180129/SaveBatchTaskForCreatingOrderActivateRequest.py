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


	def get_OrderActivateParams(self):
		return self.get_query_params().get('OrderActivateParam')

	def set_OrderActivateParams(self, OrderActivateParams):
		for depth1 in range(len(OrderActivateParams)):
			if OrderActivateParams[depth1].get('Country') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Country', OrderActivateParams[depth1].get('Country'))
			if OrderActivateParams[depth1].get('SubscriptionDuration') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.SubscriptionDuration', OrderActivateParams[depth1].get('SubscriptionDuration'))
			if OrderActivateParams[depth1].get('PermitPremiumActivation') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.PermitPremiumActivation', OrderActivateParams[depth1].get('PermitPremiumActivation'))
			if OrderActivateParams[depth1].get('City') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.City', OrderActivateParams[depth1].get('City'))
			if OrderActivateParams[depth1].get('Dns2') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Dns2', OrderActivateParams[depth1].get('Dns2'))
			if OrderActivateParams[depth1].get('Dns1') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Dns1', OrderActivateParams[depth1].get('Dns1'))
			if OrderActivateParams[depth1].get('RegistrantProfileId') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.RegistrantProfileId', OrderActivateParams[depth1].get('RegistrantProfileId'))
			if OrderActivateParams[depth1].get('AliyunDns') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.AliyunDns', OrderActivateParams[depth1].get('AliyunDns'))
			if OrderActivateParams[depth1].get('ZhCity') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhCity', OrderActivateParams[depth1].get('ZhCity'))
			if OrderActivateParams[depth1].get('TelExt') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.TelExt', OrderActivateParams[depth1].get('TelExt'))
			if OrderActivateParams[depth1].get('ZhRegistrantName') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhRegistrantName', OrderActivateParams[depth1].get('ZhRegistrantName'))
			if OrderActivateParams[depth1].get('Province') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Province', OrderActivateParams[depth1].get('Province'))
			if OrderActivateParams[depth1].get('PostalCode') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.PostalCode', OrderActivateParams[depth1].get('PostalCode'))
			if OrderActivateParams[depth1].get('Email') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Email', OrderActivateParams[depth1].get('Email'))
			if OrderActivateParams[depth1].get('ZhRegistrantOrganization') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhRegistrantOrganization', OrderActivateParams[depth1].get('ZhRegistrantOrganization'))
			if OrderActivateParams[depth1].get('Address') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Address', OrderActivateParams[depth1].get('Address'))
			if OrderActivateParams[depth1].get('TelArea') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.TelArea', OrderActivateParams[depth1].get('TelArea'))
			if OrderActivateParams[depth1].get('DomainName') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.DomainName', OrderActivateParams[depth1].get('DomainName'))
			if OrderActivateParams[depth1].get('ZhAddress') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhAddress', OrderActivateParams[depth1].get('ZhAddress'))
			if OrderActivateParams[depth1].get('RegistrantType') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.RegistrantType', OrderActivateParams[depth1].get('RegistrantType'))
			if OrderActivateParams[depth1].get('Telephone') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.Telephone', OrderActivateParams[depth1].get('Telephone'))
			if OrderActivateParams[depth1].get('TrademarkDomainActivation') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.TrademarkDomainActivation', OrderActivateParams[depth1].get('TrademarkDomainActivation'))
			if OrderActivateParams[depth1].get('ZhProvince') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.ZhProvince', OrderActivateParams[depth1].get('ZhProvince'))
			if OrderActivateParams[depth1].get('RegistrantOrganization') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.RegistrantOrganization', OrderActivateParams[depth1].get('RegistrantOrganization'))
			if OrderActivateParams[depth1].get('EnableDomainProxy') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.EnableDomainProxy', OrderActivateParams[depth1].get('EnableDomainProxy'))
			if OrderActivateParams[depth1].get('RegistrantName') is not None:
				self.add_query_param('OrderActivateParam.' + str(depth1 + 1) + '.RegistrantName', OrderActivateParams[depth1].get('RegistrantName'))

	def get_CouponNo(self):
		return self.get_query_params().get('CouponNo')

	def set_CouponNo(self,CouponNo):
		self.add_query_param('CouponNo',CouponNo)

	def get_UseCoupon(self):
		return self.get_query_params().get('UseCoupon')

	def set_UseCoupon(self,UseCoupon):
		self.add_query_param('UseCoupon',UseCoupon)

	def get_PromotionNo(self):
		return self.get_query_params().get('PromotionNo')

	def set_PromotionNo(self,PromotionNo):
		self.add_query_param('PromotionNo',PromotionNo)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_UsePromotion(self):
		return self.get_query_params().get('UsePromotion')

	def set_UsePromotion(self,UsePromotion):
		self.add_query_param('UsePromotion',UsePromotion)