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

class SetApplicationProvisioningConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'SetApplicationProvisioningConfig','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ProvisionProtocolType(self): # String
		return self.get_query_params().get('ProvisionProtocolType')

	def set_ProvisionProtocolType(self, ProvisionProtocolType):  # String
		self.add_query_param('ProvisionProtocolType', ProvisionProtocolType)
	def get_ApplicationId(self): # String
		return self.get_query_params().get('ApplicationId')

	def set_ApplicationId(self, ApplicationId):  # String
		self.add_query_param('ApplicationId', ApplicationId)
	def get_CallbackProvisioningConfig(self): # Struct
		return self.get_query_params().get('CallbackProvisioningConfig')

	def set_CallbackProvisioningConfig(self, CallbackProvisioningConfig):  # Struct
		if CallbackProvisioningConfig.get('ListenEventScopes') is not None:
			for index1, value1 in enumerate(CallbackProvisioningConfig.get('ListenEventScopes')):
				self.add_query_param('CallbackProvisioningConfig.ListenEventScopes.' + str(index1 + 1), value1)
		if CallbackProvisioningConfig.get('EncryptRequired') is not None:
			self.add_query_param('CallbackProvisioningConfig.EncryptRequired', CallbackProvisioningConfig.get('EncryptRequired'))
		if CallbackProvisioningConfig.get('CallbackUrl') is not None:
			self.add_query_param('CallbackProvisioningConfig.CallbackUrl', CallbackProvisioningConfig.get('CallbackUrl'))
		if CallbackProvisioningConfig.get('EncryptKey') is not None:
			self.add_query_param('CallbackProvisioningConfig.EncryptKey', CallbackProvisioningConfig.get('EncryptKey'))
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ProvisionPassword(self): # Boolean
		return self.get_query_params().get('ProvisionPassword')

	def set_ProvisionPassword(self, ProvisionPassword):  # Boolean
		self.add_query_param('ProvisionPassword', ProvisionPassword)
	def get_ScimProvisioningConfig(self): # Struct
		return self.get_query_params().get('ScimProvisioningConfig')

	def set_ScimProvisioningConfig(self, ScimProvisioningConfig):  # Struct
		if ScimProvisioningConfig.get('FullPushScopes') is not None:
			for index1, value1 in enumerate(ScimProvisioningConfig.get('FullPushScopes')):
				self.add_query_param('ScimProvisioningConfig.FullPushScopes.' + str(index1 + 1), value1)
		if ScimProvisioningConfig.get('AuthnConfiguration') is not None:
			if ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnMode') is not None:
				self.add_query_param('ScimProvisioningConfig.AuthnConfiguration.AuthnMode', ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnMode'))
			if ScimProvisioningConfig.get('AuthnConfiguration').get('GrantType') is not None:
				self.add_query_param('ScimProvisioningConfig.AuthnConfiguration.GrantType', ScimProvisioningConfig.get('AuthnConfiguration').get('GrantType'))
			if ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam') is not None:
				if ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('ClientId') is not None:
					self.add_query_param('ScimProvisioningConfig.AuthnConfiguration.AuthnParam.ClientId', ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('ClientId'))
				if ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('ClientSecret') is not None:
					self.add_query_param('ScimProvisioningConfig.AuthnConfiguration.AuthnParam.ClientSecret', ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('ClientSecret'))
				if ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('AccessToken') is not None:
					self.add_query_param('ScimProvisioningConfig.AuthnConfiguration.AuthnParam.AccessToken', ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('AccessToken'))
				if ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('TokenEndpoint') is not None:
					self.add_query_param('ScimProvisioningConfig.AuthnConfiguration.AuthnParam.TokenEndpoint', ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('TokenEndpoint'))
				if ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('AuthnMethod') is not None:
					self.add_query_param('ScimProvisioningConfig.AuthnConfiguration.AuthnParam.AuthnMethod', ScimProvisioningConfig.get('AuthnConfiguration').get('AuthnParam').get('AuthnMethod'))
		if ScimProvisioningConfig.get('ScimBaseUrl') is not None:
			self.add_query_param('ScimProvisioningConfig.ScimBaseUrl', ScimProvisioningConfig.get('ScimBaseUrl'))
		if ScimProvisioningConfig.get('ProvisioningActions') is not None:
			for index1, value1 in enumerate(ScimProvisioningConfig.get('ProvisioningActions')):
				self.add_query_param('ScimProvisioningConfig.ProvisioningActions.' + str(index1 + 1), value1)
