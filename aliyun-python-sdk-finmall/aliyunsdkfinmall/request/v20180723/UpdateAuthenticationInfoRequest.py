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
class UpdateAuthenticationInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'finmall', '2018-07-23', 'UpdateAuthenticationInfo','finmall')

	def get_IdCardNumber(self):
		return self.get_body_params().get('IdCardNumber')

	def set_IdCardNumber(self,IdCardNumber):
		self.add_body_params('IdCardNumber', IdCardNumber)

	def get_Address(self):
		return self.get_body_params().get('Address')

	def set_Address(self,Address):
		self.add_body_params('Address', Address)

	def get_EmployeeEmail(self):
		return self.get_body_params().get('EmployeeEmail')

	def set_EmployeeEmail(self,EmployeeEmail):
		self.add_body_params('EmployeeEmail', EmployeeEmail)

	def get_EmployeePhoneNumber(self):
		return self.get_body_params().get('EmployeePhoneNumber')

	def set_EmployeePhoneNumber(self,EmployeePhoneNumber):
		self.add_body_params('EmployeePhoneNumber', EmployeePhoneNumber)

	def get_PhoneNumber(self):
		return self.get_body_params().get('PhoneNumber')

	def set_PhoneNumber(self,PhoneNumber):
		self.add_body_params('PhoneNumber', PhoneNumber)

	def get_BusinessLicense(self):
		return self.get_body_params().get('BusinessLicense')

	def set_BusinessLicense(self,BusinessLicense):
		self.add_body_params('BusinessLicense', BusinessLicense)

	def get_LegalPersonName(self):
		return self.get_body_params().get('LegalPersonName')

	def set_LegalPersonName(self,LegalPersonName):
		self.add_body_params('LegalPersonName', LegalPersonName)

	def get_UserId(self):
		return self.get_body_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_body_params('UserId', UserId)

	def get_SmsIvToken(self):
		return self.get_body_params().get('SmsIvToken')

	def set_SmsIvToken(self,SmsIvToken):
		self.add_body_params('SmsIvToken', SmsIvToken)

	def get_BankCard(self):
		return self.get_body_params().get('BankCard')

	def set_BankCard(self,BankCard):
		self.add_body_params('BankCard', BankCard)

	def get_Email(self):
		return self.get_body_params().get('Email')

	def set_Email(self,Email):
		self.add_body_params('Email', Email)

	def get_EmployeeName(self):
		return self.get_body_params().get('EmployeeName')

	def set_EmployeeName(self,EmployeeName):
		self.add_body_params('EmployeeName', EmployeeName)

	def get_EmployeeIdCardNumber(self):
		return self.get_body_params().get('EmployeeIdCardNumber')

	def set_EmployeeIdCardNumber(self,EmployeeIdCardNumber):
		self.add_body_params('EmployeeIdCardNumber', EmployeeIdCardNumber)