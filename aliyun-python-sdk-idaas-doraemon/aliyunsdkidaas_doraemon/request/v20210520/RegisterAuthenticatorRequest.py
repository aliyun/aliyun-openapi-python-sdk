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
from aliyunsdkidaas_doraemon.endpoint import endpoint_data

class RegisterAuthenticatorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idaas-doraemon', '2021-05-20', 'RegisterAuthenticator')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_LogParams(self): # String
		return self.get_query_params().get('LogParams')

	def set_LogParams(self, LogParams):  # String
		self.add_query_param('LogParams', LogParams)
	def get_ClientExtendParamsJson(self): # String
		return self.get_query_params().get('ClientExtendParamsJson')

	def set_ClientExtendParamsJson(self, ClientExtendParamsJson):  # String
		self.add_query_param('ClientExtendParamsJson', ClientExtendParamsJson)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_ServerExtendParamsJson(self): # String
		return self.get_query_params().get('ServerExtendParamsJson')

	def set_ServerExtendParamsJson(self, ServerExtendParamsJson):  # String
		self.add_query_param('ServerExtendParamsJson', ServerExtendParamsJson)
	def get_RegistrationContext(self): # String
		return self.get_query_params().get('RegistrationContext')

	def set_RegistrationContext(self, RegistrationContext):  # String
		self.add_query_param('RegistrationContext', RegistrationContext)
	def get_AuthenticatorName(self): # String
		return self.get_query_params().get('AuthenticatorName')

	def set_AuthenticatorName(self, AuthenticatorName):  # String
		self.add_query_param('AuthenticatorName', AuthenticatorName)
	def get_RequireChallengeBase64(self): # String
		return self.get_query_params().get('RequireChallengeBase64')

	def set_RequireChallengeBase64(self, RequireChallengeBase64):  # String
		self.add_query_param('RequireChallengeBase64', RequireChallengeBase64)
	def get_AuthenticatorType(self): # String
		return self.get_query_params().get('AuthenticatorType')

	def set_AuthenticatorType(self, AuthenticatorType):  # String
		self.add_query_param('AuthenticatorType', AuthenticatorType)
	def get_ClientExtendParamsJsonSign(self): # String
		return self.get_query_params().get('ClientExtendParamsJsonSign')

	def set_ClientExtendParamsJsonSign(self, ClientExtendParamsJsonSign):  # String
		self.add_query_param('ClientExtendParamsJsonSign', ClientExtendParamsJsonSign)
	def get_UserSourceIp(self): # String
		return self.get_query_params().get('UserSourceIp')

	def set_UserSourceIp(self, UserSourceIp):  # String
		self.add_query_param('UserSourceIp', UserSourceIp)
	def get_ApplicationExternalId(self): # String
		return self.get_query_params().get('ApplicationExternalId')

	def set_ApplicationExternalId(self, ApplicationExternalId):  # String
		self.add_query_param('ApplicationExternalId', ApplicationExternalId)
