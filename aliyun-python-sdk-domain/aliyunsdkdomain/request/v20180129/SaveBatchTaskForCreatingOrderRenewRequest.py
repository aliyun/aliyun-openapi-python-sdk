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

class SaveBatchTaskForCreatingOrderRenewRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveBatchTaskForCreatingOrderRenew')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


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

	def get_OrderRenewParams(self):
		return self.get_query_params().get('OrderRenewParam')

	def set_OrderRenewParams(self, OrderRenewParams):
		for depth1 in range(len(OrderRenewParams)):
			if OrderRenewParams[depth1].get('SubscriptionDuration') is not None:
				self.add_query_param('OrderRenewParam.' + str(depth1 + 1) + '.SubscriptionDuration', OrderRenewParams[depth1].get('SubscriptionDuration'))
			if OrderRenewParams[depth1].get('CurrentExpirationDate') is not None:
				self.add_query_param('OrderRenewParam.' + str(depth1 + 1) + '.CurrentExpirationDate', OrderRenewParams[depth1].get('CurrentExpirationDate'))
			if OrderRenewParams[depth1].get('DomainName') is not None:
				self.add_query_param('OrderRenewParam.' + str(depth1 + 1) + '.DomainName', OrderRenewParams[depth1].get('DomainName'))

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_UsePromotion(self):
		return self.get_query_params().get('UsePromotion')

	def set_UsePromotion(self,UsePromotion):
		self.add_query_param('UsePromotion',UsePromotion)