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
from aliyunsdkdypnsapi.endpoint import endpoint_data

class SendSmsVerifyCodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dypnsapi', '2017-05-25', 'SendSmsVerifyCode','dypnsapi')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_CountryCode(self): # String
		return self.get_query_params().get('CountryCode')

	def set_CountryCode(self, CountryCode):  # String
		self.add_query_param('CountryCode', CountryCode)
	def get_PhoneNumber(self): # String
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self, PhoneNumber):  # String
		self.add_query_param('PhoneNumber', PhoneNumber)
	def get_SmsUpExtendCode(self): # String
		return self.get_query_params().get('SmsUpExtendCode')

	def set_SmsUpExtendCode(self, SmsUpExtendCode):  # String
		self.add_query_param('SmsUpExtendCode', SmsUpExtendCode)
	def get_SignName(self): # String
		return self.get_query_params().get('SignName')

	def set_SignName(self, SignName):  # String
		self.add_query_param('SignName', SignName)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_ValidTime(self): # Long
		return self.get_query_params().get('ValidTime')

	def set_ValidTime(self, ValidTime):  # Long
		self.add_query_param('ValidTime', ValidTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ReturnVerifyCode(self): # Boolean
		return self.get_query_params().get('ReturnVerifyCode')

	def set_ReturnVerifyCode(self, ReturnVerifyCode):  # Boolean
		self.add_query_param('ReturnVerifyCode', ReturnVerifyCode)
	def get_CodeType(self): # Long
		return self.get_query_params().get('CodeType')

	def set_CodeType(self, CodeType):  # Long
		self.add_query_param('CodeType', CodeType)
	def get_SchemeName(self): # String
		return self.get_query_params().get('SchemeName')

	def set_SchemeName(self, SchemeName):  # String
		self.add_query_param('SchemeName', SchemeName)
	def get_DuplicatePolicy(self): # Long
		return self.get_query_params().get('DuplicatePolicy')

	def set_DuplicatePolicy(self, DuplicatePolicy):  # Long
		self.add_query_param('DuplicatePolicy', DuplicatePolicy)
	def get_OutId(self): # String
		return self.get_query_params().get('OutId')

	def set_OutId(self, OutId):  # String
		self.add_query_param('OutId', OutId)
	def get_Interval(self): # Long
		return self.get_query_params().get('Interval')

	def set_Interval(self, Interval):  # Long
		self.add_query_param('Interval', Interval)
	def get_TemplateCode(self): # String
		return self.get_query_params().get('TemplateCode')

	def set_TemplateCode(self, TemplateCode):  # String
		self.add_query_param('TemplateCode', TemplateCode)
	def get_TemplateParam(self): # String
		return self.get_query_params().get('TemplateParam')

	def set_TemplateParam(self, TemplateParam):  # String
		self.add_query_param('TemplateParam', TemplateParam)
	def get_CodeLength(self): # Long
		return self.get_query_params().get('CodeLength')

	def set_CodeLength(self, CodeLength):  # Long
		self.add_query_param('CodeLength', CodeLength)
