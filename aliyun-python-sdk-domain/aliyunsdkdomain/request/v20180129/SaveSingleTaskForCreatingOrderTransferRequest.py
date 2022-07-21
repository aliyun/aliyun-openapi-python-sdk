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

class SaveSingleTaskForCreatingOrderTransferRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveSingleTaskForCreatingOrderTransfer')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RegistrantProfileId(self): # Long
		return self.get_query_params().get('RegistrantProfileId')

	def set_RegistrantProfileId(self, RegistrantProfileId):  # Long
		self.add_query_param('RegistrantProfileId', RegistrantProfileId)
	def get_CouponNo(self): # String
		return self.get_query_params().get('CouponNo')

	def set_CouponNo(self, CouponNo):  # String
		self.add_query_param('CouponNo', CouponNo)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_UseCoupon(self): # Boolean
		return self.get_query_params().get('UseCoupon')

	def set_UseCoupon(self, UseCoupon):  # Boolean
		self.add_query_param('UseCoupon', UseCoupon)
	def get_PermitPremiumTransfer(self): # Boolean
		return self.get_query_params().get('PermitPremiumTransfer')

	def set_PermitPremiumTransfer(self, PermitPremiumTransfer):  # Boolean
		self.add_query_param('PermitPremiumTransfer', PermitPremiumTransfer)
	def get_PromotionNo(self): # String
		return self.get_query_params().get('PromotionNo')

	def set_PromotionNo(self, PromotionNo):  # String
		self.add_query_param('PromotionNo', PromotionNo)
	def get_AuthorizationCode(self): # String
		return self.get_query_params().get('AuthorizationCode')

	def set_AuthorizationCode(self, AuthorizationCode):  # String
		self.add_query_param('AuthorizationCode', AuthorizationCode)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
	def get_UsePromotion(self): # Boolean
		return self.get_query_params().get('UsePromotion')

	def set_UsePromotion(self, UsePromotion):  # Boolean
		self.add_query_param('UsePromotion', UsePromotion)
