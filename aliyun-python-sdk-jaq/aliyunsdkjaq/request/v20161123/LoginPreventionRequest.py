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
class LoginPreventionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'jaq', '2016-11-23', 'LoginPrevention')

	def get_CallerName(self):
		return self.get_query_params().get('CallerName')

	def set_CallerName(self,CallerName):
		self.add_query_param('CallerName',CallerName)

	def get_Ip(self):
		return self.get_query_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_query_param('Ip',Ip)

	def get_ProtocolVersion(self):
		return self.get_query_params().get('ProtocolVersion')

	def set_ProtocolVersion(self,ProtocolVersion):
		self.add_query_param('ProtocolVersion',ProtocolVersion)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_PhoneNumber(self):
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self,PhoneNumber):
		self.add_query_param('PhoneNumber',PhoneNumber)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_IdType(self):
		return self.get_query_params().get('IdType')

	def set_IdType(self,IdType):
		self.add_query_param('IdType',IdType)

	def get_CurrentUrl(self):
		return self.get_query_params().get('CurrentUrl')

	def set_CurrentUrl(self,CurrentUrl):
		self.add_query_param('CurrentUrl',CurrentUrl)

	def get_Agent(self):
		return self.get_query_params().get('Agent')

	def set_Agent(self,Agent):
		self.add_query_param('Agent',Agent)

	def get_Cookie(self):
		return self.get_query_params().get('Cookie')

	def set_Cookie(self,Cookie):
		self.add_query_param('Cookie',Cookie)

	def get_SessionId(self):
		return self.get_query_params().get('SessionId')

	def set_SessionId(self,SessionId):
		self.add_query_param('SessionId',SessionId)

	def get_MacAddress(self):
		return self.get_query_params().get('MacAddress')

	def set_MacAddress(self,MacAddress):
		self.add_query_param('MacAddress',MacAddress)

	def get_Referer(self):
		return self.get_query_params().get('Referer')

	def set_Referer(self,Referer):
		self.add_query_param('Referer',Referer)

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)

	def get_CompanyName(self):
		return self.get_query_params().get('CompanyName')

	def set_CompanyName(self,CompanyName):
		self.add_query_param('CompanyName',CompanyName)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_IDNumber(self):
		return self.get_query_params().get('IDNumber')

	def set_IDNumber(self,IDNumber):
		self.add_query_param('IDNumber',IDNumber)

	def get_BankCardNumber(self):
		return self.get_query_params().get('BankCardNumber')

	def set_BankCardNumber(self,BankCardNumber):
		self.add_query_param('BankCardNumber',BankCardNumber)

	def get_RegisterIp(self):
		return self.get_query_params().get('RegisterIp')

	def set_RegisterIp(self,RegisterIp):
		self.add_query_param('RegisterIp',RegisterIp)

	def get_RegisterDate(self):
		return self.get_query_params().get('RegisterDate')

	def set_RegisterDate(self,RegisterDate):
		self.add_query_param('RegisterDate',RegisterDate)

	def get_AccountExist(self):
		return self.get_query_params().get('AccountExist')

	def set_AccountExist(self,AccountExist):
		self.add_query_param('AccountExist',AccountExist)

	def get_ExtendData(self):
		return self.get_query_params().get('ExtendData')

	def set_ExtendData(self,ExtendData):
		self.add_query_param('ExtendData',ExtendData)

	def get_JsToken(self):
		return self.get_query_params().get('JsToken')

	def set_JsToken(self,JsToken):
		self.add_query_param('JsToken',JsToken)

	def get_SDKToken(self):
		return self.get_query_params().get('SDKToken')

	def set_SDKToken(self,SDKToken):
		self.add_query_param('SDKToken',SDKToken)

	def get_PasswordHash(self):
		return self.get_query_params().get('PasswordHash')

	def set_PasswordHash(self,PasswordHash):
		self.add_query_param('PasswordHash',PasswordHash)

	def get_LoginType(self):
		return self.get_query_params().get('LoginType')

	def set_LoginType(self,LoginType):
		self.add_query_param('LoginType',LoginType)

	def get_PasswordCorrect(self):
		return self.get_query_params().get('PasswordCorrect')

	def set_PasswordCorrect(self,PasswordCorrect):
		self.add_query_param('PasswordCorrect',PasswordCorrect)