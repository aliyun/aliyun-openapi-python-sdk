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
class VerifyCustomerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'finmall', '2018-07-23', 'VerifyCustomer','finmall')

	def get_IdCardNumber(self):
		return self.get_query_params().get('IdCardNumber')

	def set_IdCardNumber(self,IdCardNumber):
		self.add_query_param('IdCardNumber',IdCardNumber)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_IdCardFrontPage(self):
		return self.get_query_params().get('IdCardFrontPage')

	def set_IdCardFrontPage(self,IdCardFrontPage):
		self.add_query_param('IdCardFrontPage',IdCardFrontPage)

	def get_PhoneNumber(self):
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self,PhoneNumber):
		self.add_query_param('PhoneNumber',PhoneNumber)

	def get_BusinessLicense(self):
		return self.get_query_params().get('BusinessLicense')

	def set_BusinessLicense(self,BusinessLicense):
		self.add_query_param('BusinessLicense',BusinessLicense)

	def get_IdCardBackPage(self):
		return self.get_query_params().get('IdCardBackPage')

	def set_IdCardBackPage(self,IdCardBackPage):
		self.add_query_param('IdCardBackPage',IdCardBackPage)

	def get_LegalPersonName(self):
		return self.get_query_params().get('LegalPersonName')

	def set_LegalPersonName(self,LegalPersonName):
		self.add_query_param('LegalPersonName',LegalPersonName)

	def get_EnterpriseName(self):
		return self.get_query_params().get('EnterpriseName')

	def set_EnterpriseName(self,EnterpriseName):
		self.add_query_param('EnterpriseName',EnterpriseName)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_LoanSubject(self):
		return self.get_query_params().get('LoanSubject')

	def set_LoanSubject(self,LoanSubject):
		self.add_query_param('LoanSubject',LoanSubject)

	def get_ZhimaReturnUrl(self):
		return self.get_query_params().get('ZhimaReturnUrl')

	def set_ZhimaReturnUrl(self,ZhimaReturnUrl):
		self.add_query_param('ZhimaReturnUrl',ZhimaReturnUrl)

	def get_BankCard(self):
		return self.get_query_params().get('BankCard')

	def set_BankCard(self,BankCard):
		self.add_query_param('BankCard',BankCard)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)