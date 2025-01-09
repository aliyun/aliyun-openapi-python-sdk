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

class SetApplicationSsoConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'SetApplicationSsoConfig','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ApplicationId(self): # String
		return self.get_query_params().get('ApplicationId')

	def set_ApplicationId(self, ApplicationId):  # String
		self.add_query_param('ApplicationId', ApplicationId)
	def get_InitLoginUrl(self): # String
		return self.get_query_params().get('InitLoginUrl')

	def set_InitLoginUrl(self, InitLoginUrl):  # String
		self.add_query_param('InitLoginUrl', InitLoginUrl)
	def get_InitLoginType(self): # String
		return self.get_query_params().get('InitLoginType')

	def set_InitLoginType(self, InitLoginType):  # String
		self.add_query_param('InitLoginType', InitLoginType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_OidcSsoConfig(self): # Struct
		return self.get_query_params().get('OidcSsoConfig')

	def set_OidcSsoConfig(self, OidcSsoConfig):  # Struct
		if OidcSsoConfig.get('CodeEffectiveTime') is not None:
			self.add_query_param('OidcSsoConfig.CodeEffectiveTime', OidcSsoConfig.get('CodeEffectiveTime'))
		if OidcSsoConfig.get('ResponseTypes') is not None:
			for index1, value1 in enumerate(OidcSsoConfig.get('ResponseTypes')):
				self.add_query_param('OidcSsoConfig.ResponseTypes.' + str(index1 + 1), value1)
		if OidcSsoConfig.get('GrantScopes') is not None:
			for index1, value1 in enumerate(OidcSsoConfig.get('GrantScopes')):
				self.add_query_param('OidcSsoConfig.GrantScopes.' + str(index1 + 1), value1)
		if OidcSsoConfig.get('RefreshTokenEffective') is not None:
			self.add_query_param('OidcSsoConfig.RefreshTokenEffective', OidcSsoConfig.get('RefreshTokenEffective'))
		if OidcSsoConfig.get('GrantTypes') is not None:
			for index1, value1 in enumerate(OidcSsoConfig.get('GrantTypes')):
				self.add_query_param('OidcSsoConfig.GrantTypes.' + str(index1 + 1), value1)
		if OidcSsoConfig.get('IdTokenEffectiveTime') is not None:
			self.add_query_param('OidcSsoConfig.IdTokenEffectiveTime', OidcSsoConfig.get('IdTokenEffectiveTime'))
		if OidcSsoConfig.get('PkceChallengeMethods') is not None:
			for index1, value1 in enumerate(OidcSsoConfig.get('PkceChallengeMethods')):
				self.add_query_param('OidcSsoConfig.PkceChallengeMethods.' + str(index1 + 1), value1)
		if OidcSsoConfig.get('PasswordAuthenticationSourceId') is not None:
			self.add_query_param('OidcSsoConfig.PasswordAuthenticationSourceId', OidcSsoConfig.get('PasswordAuthenticationSourceId'))
		if OidcSsoConfig.get('AccessTokenEffectiveTime') is not None:
			self.add_query_param('OidcSsoConfig.AccessTokenEffectiveTime', OidcSsoConfig.get('AccessTokenEffectiveTime'))
		if OidcSsoConfig.get('PostLogoutRedirectUris') is not None:
			for index1, value1 in enumerate(OidcSsoConfig.get('PostLogoutRedirectUris')):
				self.add_query_param('OidcSsoConfig.PostLogoutRedirectUris.' + str(index1 + 1), value1)
		if OidcSsoConfig.get('PasswordTotpMfaRequired') is not None:
			self.add_query_param('OidcSsoConfig.PasswordTotpMfaRequired', OidcSsoConfig.get('PasswordTotpMfaRequired'))
		if OidcSsoConfig.get('CustomClaims') is not None:
			for index1, value1 in enumerate(OidcSsoConfig.get('CustomClaims')):
				if value1.get('ClaimValueExpression') is not None:
					self.add_query_param('OidcSsoConfig.CustomClaims.' + str(index1 + 1) + '.ClaimValueExpression', value1.get('ClaimValueExpression'))
				if value1.get('ClaimName') is not None:
					self.add_query_param('OidcSsoConfig.CustomClaims.' + str(index1 + 1) + '.ClaimName', value1.get('ClaimName'))
		if OidcSsoConfig.get('SubjectIdExpression') is not None:
			self.add_query_param('OidcSsoConfig.SubjectIdExpression', OidcSsoConfig.get('SubjectIdExpression'))
		if OidcSsoConfig.get('PkceRequired') is not None:
			self.add_query_param('OidcSsoConfig.PkceRequired', OidcSsoConfig.get('PkceRequired'))
		if OidcSsoConfig.get('RedirectUris') is not None:
			for index1, value1 in enumerate(OidcSsoConfig.get('RedirectUris')):
				self.add_query_param('OidcSsoConfig.RedirectUris.' + str(index1 + 1), value1)
	def get_SamlSsoConfig(self): # Struct
		return self.get_query_params().get('SamlSsoConfig')

	def set_SamlSsoConfig(self, SamlSsoConfig):  # Struct
		if SamlSsoConfig.get('SignatureAlgorithm') is not None:
			self.add_query_param('SamlSsoConfig.SignatureAlgorithm', SamlSsoConfig.get('SignatureAlgorithm'))
		if SamlSsoConfig.get('NameIdFormat') is not None:
			self.add_query_param('SamlSsoConfig.NameIdFormat', SamlSsoConfig.get('NameIdFormat'))
		if SamlSsoConfig.get('IdPEntityId') is not None:
			self.add_query_param('SamlSsoConfig.IdPEntityId', SamlSsoConfig.get('IdPEntityId'))
		if SamlSsoConfig.get('AssertionSigned') is not None:
			self.add_query_param('SamlSsoConfig.AssertionSigned', SamlSsoConfig.get('AssertionSigned'))
		if SamlSsoConfig.get('SpSsoAcsUrl') is not None:
			self.add_query_param('SamlSsoConfig.SpSsoAcsUrl', SamlSsoConfig.get('SpSsoAcsUrl'))
		if SamlSsoConfig.get('NameIdValueExpression') is not None:
			self.add_query_param('SamlSsoConfig.NameIdValueExpression', SamlSsoConfig.get('NameIdValueExpression'))
		if SamlSsoConfig.get('AttributeStatements') is not None:
			for index1, value1 in enumerate(SamlSsoConfig.get('AttributeStatements')):
				if value1.get('AttributeValueExpression') is not None:
					self.add_query_param('SamlSsoConfig.AttributeStatements.' + str(index1 + 1) + '.AttributeValueExpression', value1.get('AttributeValueExpression'))
				if value1.get('AttributeName') is not None:
					self.add_query_param('SamlSsoConfig.AttributeStatements.' + str(index1 + 1) + '.AttributeName', value1.get('AttributeName'))
		if SamlSsoConfig.get('DefaultRelayState') is not None:
			self.add_query_param('SamlSsoConfig.DefaultRelayState', SamlSsoConfig.get('DefaultRelayState'))
		if SamlSsoConfig.get('SpEntityId') is not None:
			self.add_query_param('SamlSsoConfig.SpEntityId', SamlSsoConfig.get('SpEntityId'))
		if SamlSsoConfig.get('OptionalRelayStates') is not None:
			for index1, value1 in enumerate(SamlSsoConfig.get('OptionalRelayStates')):
				if value1.get('RelayState') is not None:
					self.add_query_param('SamlSsoConfig.OptionalRelayStates.' + str(index1 + 1) + '.RelayState', value1.get('RelayState'))
				if value1.get('DisplayName') is not None:
					self.add_query_param('SamlSsoConfig.OptionalRelayStates.' + str(index1 + 1) + '.DisplayName', value1.get('DisplayName'))
		if SamlSsoConfig.get('ResponseSigned') is not None:
			self.add_query_param('SamlSsoConfig.ResponseSigned', SamlSsoConfig.get('ResponseSigned'))
