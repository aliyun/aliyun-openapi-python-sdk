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


class SaveBatchTaskForCreatingOrderActivateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveBatchTaskForCreatingOrderActivate')

	def get_OrderActivateParams(self):
		return self.get_query_params().get('OrderActivateParams')

	def set_OrderActivateParams(self,OrderActivateParams):
		for i in range(len(OrderActivateParams)):	
			if OrderActivateParams[i].get('Country') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.Country' , OrderActivateParams[i].get('Country'))
			if OrderActivateParams[i].get('SubscriptionDuration') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.SubscriptionDuration' , OrderActivateParams[i].get('SubscriptionDuration'))
			if OrderActivateParams[i].get('PermitPremiumActivation') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.PermitPremiumActivation' , OrderActivateParams[i].get('PermitPremiumActivation'))
			if OrderActivateParams[i].get('City') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.City' , OrderActivateParams[i].get('City'))
			if OrderActivateParams[i].get('Dns2') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.Dns2' , OrderActivateParams[i].get('Dns2'))
			if OrderActivateParams[i].get('Dns1') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.Dns1' , OrderActivateParams[i].get('Dns1'))
			if OrderActivateParams[i].get('RegistrantProfileId') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.RegistrantProfileId' , OrderActivateParams[i].get('RegistrantProfileId'))
			if OrderActivateParams[i].get('AliyunDns') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.AliyunDns' , OrderActivateParams[i].get('AliyunDns'))
			if OrderActivateParams[i].get('ZhCity') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.ZhCity' , OrderActivateParams[i].get('ZhCity'))
			if OrderActivateParams[i].get('TelExt') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.TelExt' , OrderActivateParams[i].get('TelExt'))
			if OrderActivateParams[i].get('ZhRegistrantName') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.ZhRegistrantName' , OrderActivateParams[i].get('ZhRegistrantName'))
			if OrderActivateParams[i].get('Province') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.Province' , OrderActivateParams[i].get('Province'))
			if OrderActivateParams[i].get('PostalCode') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.PostalCode' , OrderActivateParams[i].get('PostalCode'))
			if OrderActivateParams[i].get('Email') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.Email' , OrderActivateParams[i].get('Email'))
			if OrderActivateParams[i].get('ZhRegistrantOrganization') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.ZhRegistrantOrganization' , OrderActivateParams[i].get('ZhRegistrantOrganization'))
			if OrderActivateParams[i].get('Address') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.Address' , OrderActivateParams[i].get('Address'))
			if OrderActivateParams[i].get('TelArea') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.TelArea' , OrderActivateParams[i].get('TelArea'))
			if OrderActivateParams[i].get('DomainName') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.DomainName' , OrderActivateParams[i].get('DomainName'))
			if OrderActivateParams[i].get('ZhAddress') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.ZhAddress' , OrderActivateParams[i].get('ZhAddress'))
			if OrderActivateParams[i].get('RegistrantType') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.RegistrantType' , OrderActivateParams[i].get('RegistrantType'))
			if OrderActivateParams[i].get('Telephone') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.Telephone' , OrderActivateParams[i].get('Telephone'))
			if OrderActivateParams[i].get('TrademarkDomainActivation') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.TrademarkDomainActivation' , OrderActivateParams[i].get('TrademarkDomainActivation'))
			if OrderActivateParams[i].get('ZhProvince') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.ZhProvince' , OrderActivateParams[i].get('ZhProvince'))
			if OrderActivateParams[i].get('RegistrantOrganization') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.RegistrantOrganization' , OrderActivateParams[i].get('RegistrantOrganization'))
			if OrderActivateParams[i].get('EnableDomainProxy') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.EnableDomainProxy' , OrderActivateParams[i].get('EnableDomainProxy'))
			if OrderActivateParams[i].get('RegistrantName') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.RegistrantName' , OrderActivateParams[i].get('RegistrantName'))


	def get_PromotionNo(self):
		return self.get_query_params().get('PromotionNo')

	def set_PromotionNo(self,PromotionNo):
		self.add_query_param('PromotionNo',PromotionNo)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_CouponNo(self):
		return self.get_query_params().get('CouponNo')

	def set_CouponNo(self,CouponNo):
		self.add_query_param('CouponNo',CouponNo)

	def get_UseCoupon(self):
		return self.get_query_params().get('UseCoupon')

	def set_UseCoupon(self,UseCoupon):
		self.add_query_param('UseCoupon',UseCoupon)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_UsePromotion(self):
		return self.get_query_params().get('UsePromotion')

	def set_UsePromotion(self,UsePromotion):
		self.add_query_param('UsePromotion',UsePromotion)