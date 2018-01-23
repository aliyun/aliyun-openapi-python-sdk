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
class SaveBatchTaskForCreatingOrderActivateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain-intl', '2017-12-18', 'SaveBatchTaskForCreatingOrderActivate','domain')

	def get_OrderActivateParams(self):
		return self.get_query_params().get('OrderActivateParams')

	def set_OrderActivateParams(self,OrderActivateParams):
		for i in range(len(OrderActivateParams)):	
			if OrderActivateParams[i].get('DomainName') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.DomainName' , OrderActivateParams[i].get('DomainName'))
			if OrderActivateParams[i].get('SubscriptionDuration') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.SubscriptionDuration' , OrderActivateParams[i].get('SubscriptionDuration'))
			if OrderActivateParams[i].get('RegistrantProfileId') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.RegistrantProfileId' , OrderActivateParams[i].get('RegistrantProfileId'))
			if OrderActivateParams[i].get('EnableDomainProxy') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.EnableDomainProxy' , OrderActivateParams[i].get('EnableDomainProxy'))
			if OrderActivateParams[i].get('PermitPremiumActivation') is not None:
				self.add_query_param('OrderActivateParam.' + str(i + 1) + '.PermitPremiumActivation' , OrderActivateParams[i].get('PermitPremiumActivation'))


	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)