# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class SaveSingleTaskForCreatingOrderRenewRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain-intl', '2017-12-18', 'SaveSingleTaskForCreatingOrderRenew','domain')

	def get_SubscriptionDuration(self):
		return self.get_query_params().get('SubscriptionDuration')

	def set_SubscriptionDuration(self,SubscriptionDuration):
		self.add_query_param('SubscriptionDuration',SubscriptionDuration)

	def get_PromotionNo(self):
		return self.get_query_params().get('PromotionNo')

	def set_PromotionNo(self,PromotionNo):
		self.add_query_param('PromotionNo',PromotionNo)

	def get_CurrentExpirationDate(self):
		return self.get_query_params().get('CurrentExpirationDate')

	def set_CurrentExpirationDate(self,CurrentExpirationDate):
		self.add_query_param('CurrentExpirationDate',CurrentExpirationDate)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

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