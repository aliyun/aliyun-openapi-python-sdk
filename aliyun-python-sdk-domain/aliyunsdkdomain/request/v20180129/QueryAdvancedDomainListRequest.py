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
class QueryAdvancedDomainListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'QueryAdvancedDomainList')

	def get_ProductDomainType(self):
		return self.get_query_params().get('ProductDomainType')

	def set_ProductDomainType(self,ProductDomainType):
		self.add_query_param('ProductDomainType',ProductDomainType)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_Excluded(self):
		return self.get_query_params().get('Excluded')

	def set_Excluded(self,Excluded):
		self.add_query_param('Excluded',Excluded)

	def get_StartLength(self):
		return self.get_query_params().get('StartLength')

	def set_StartLength(self,StartLength):
		self.add_query_param('StartLength',StartLength)

	def get_ExcludedSuffix(self):
		return self.get_query_params().get('ExcludedSuffix')

	def set_ExcludedSuffix(self,ExcludedSuffix):
		self.add_query_param('ExcludedSuffix',ExcludedSuffix)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_ExcludedPrefix(self):
		return self.get_query_params().get('ExcludedPrefix')

	def set_ExcludedPrefix(self,ExcludedPrefix):
		self.add_query_param('ExcludedPrefix',ExcludedPrefix)

	def get_KeyWord(self):
		return self.get_query_params().get('KeyWord')

	def set_KeyWord(self,KeyWord):
		self.add_query_param('KeyWord',KeyWord)

	def get_ProductDomainTypeSort(self):
		return self.get_query_params().get('ProductDomainTypeSort')

	def set_ProductDomainTypeSort(self,ProductDomainTypeSort):
		self.add_query_param('ProductDomainTypeSort',ProductDomainTypeSort)

	def get_EndExpirationDate(self):
		return self.get_query_params().get('EndExpirationDate')

	def set_EndExpirationDate(self,EndExpirationDate):
		self.add_query_param('EndExpirationDate',EndExpirationDate)

	def get_Suffixs(self):
		return self.get_query_params().get('Suffixs')

	def set_Suffixs(self,Suffixs):
		self.add_query_param('Suffixs',Suffixs)

	def get_DomainNameSort(self):
		return self.get_query_params().get('DomainNameSort')

	def set_DomainNameSort(self,DomainNameSort):
		self.add_query_param('DomainNameSort',DomainNameSort)

	def get_ExpirationDateSort(self):
		return self.get_query_params().get('ExpirationDateSort')

	def set_ExpirationDateSort(self,ExpirationDateSort):
		self.add_query_param('ExpirationDateSort',ExpirationDateSort)

	def get_StartExpirationDate(self):
		return self.get_query_params().get('StartExpirationDate')

	def set_StartExpirationDate(self,StartExpirationDate):
		self.add_query_param('StartExpirationDate',StartExpirationDate)

	def get_DomainStatus(self):
		return self.get_query_params().get('DomainStatus')

	def set_DomainStatus(self,DomainStatus):
		self.add_query_param('DomainStatus',DomainStatus)

	def get_DomainGroupId(self):
		return self.get_query_params().get('DomainGroupId')

	def set_DomainGroupId(self,DomainGroupId):
		self.add_query_param('DomainGroupId',DomainGroupId)

	def get_KeyWordSuffix(self):
		return self.get_query_params().get('KeyWordSuffix')

	def set_KeyWordSuffix(self,KeyWordSuffix):
		self.add_query_param('KeyWordSuffix',KeyWordSuffix)

	def get_KeyWordPrefix(self):
		return self.get_query_params().get('KeyWordPrefix')

	def set_KeyWordPrefix(self,KeyWordPrefix):
		self.add_query_param('KeyWordPrefix',KeyWordPrefix)

	def get_TradeType(self):
		return self.get_query_params().get('TradeType')

	def set_TradeType(self,TradeType):
		self.add_query_param('TradeType',TradeType)

	def get_EndRegistrationDate(self):
		return self.get_query_params().get('EndRegistrationDate')

	def set_EndRegistrationDate(self,EndRegistrationDate):
		self.add_query_param('EndRegistrationDate',EndRegistrationDate)

	def get_Form(self):
		return self.get_query_params().get('Form')

	def set_Form(self,Form):
		self.add_query_param('Form',Form)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_RegistrationDateSort(self):
		return self.get_query_params().get('RegistrationDateSort')

	def set_RegistrationDateSort(self,RegistrationDateSort):
		self.add_query_param('RegistrationDateSort',RegistrationDateSort)

	def get_StartRegistrationDate(self):
		return self.get_query_params().get('StartRegistrationDate')

	def set_StartRegistrationDate(self,StartRegistrationDate):
		self.add_query_param('StartRegistrationDate',StartRegistrationDate)

	def get_EndLength(self):
		return self.get_query_params().get('EndLength')

	def set_EndLength(self,EndLength):
		self.add_query_param('EndLength',EndLength)