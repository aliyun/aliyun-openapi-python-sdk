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

class UpdateIdentityProviderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'UpdateIdentityProvider','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_DingtalkAppConfig(self): # Struct
		return self.get_query_params().get('DingtalkAppConfig')

	def set_DingtalkAppConfig(self, DingtalkAppConfig):  # Struct
		if DingtalkAppConfig.get('AppSecret') is not None:
			self.add_query_param('DingtalkAppConfig.AppSecret', DingtalkAppConfig.get('AppSecret'))
		if DingtalkAppConfig.get('AppKey') is not None:
			self.add_query_param('DingtalkAppConfig.AppKey', DingtalkAppConfig.get('AppKey'))
	def get_NetworkAccessEndpointId(self): # String
		return self.get_query_params().get('NetworkAccessEndpointId')

	def set_NetworkAccessEndpointId(self, NetworkAccessEndpointId):  # String
		self.add_query_param('NetworkAccessEndpointId', NetworkAccessEndpointId)
	def get_LogoUrl(self): # String
		return self.get_query_params().get('LogoUrl')

	def set_LogoUrl(self, LogoUrl):  # String
		self.add_query_param('LogoUrl', LogoUrl)
	def get_IdentityProviderId(self): # String
		return self.get_query_params().get('IdentityProviderId')

	def set_IdentityProviderId(self, IdentityProviderId):  # String
		self.add_query_param('IdentityProviderId', IdentityProviderId)
	def get_LarkConfig(self): # Struct
		return self.get_query_params().get('LarkConfig')

	def set_LarkConfig(self, LarkConfig):  # Struct
		if LarkConfig.get('AppId') is not None:
			self.add_query_param('LarkConfig.AppId', LarkConfig.get('AppId'))
		if LarkConfig.get('AppSecret') is not None:
			self.add_query_param('LarkConfig.AppSecret', LarkConfig.get('AppSecret'))
		if LarkConfig.get('VerificationToken') is not None:
			self.add_query_param('LarkConfig.VerificationToken', LarkConfig.get('VerificationToken'))
		if LarkConfig.get('EncryptKey') is not None:
			self.add_query_param('LarkConfig.EncryptKey', LarkConfig.get('EncryptKey'))
	def get_WeComConfig(self): # Struct
		return self.get_query_params().get('WeComConfig')

	def set_WeComConfig(self, WeComConfig):  # Struct
		if WeComConfig.get('AgentId') is not None:
			self.add_query_param('WeComConfig.AgentId', WeComConfig.get('AgentId'))
		if WeComConfig.get('CorpSecret') is not None:
			self.add_query_param('WeComConfig.CorpSecret', WeComConfig.get('CorpSecret'))
		if WeComConfig.get('AuthorizeCallbackDomain') is not None:
			self.add_query_param('WeComConfig.AuthorizeCallbackDomain', WeComConfig.get('AuthorizeCallbackDomain'))
		if WeComConfig.get('TrustableDomain') is not None:
			self.add_query_param('WeComConfig.TrustableDomain', WeComConfig.get('TrustableDomain'))
	def get_IdentityProviderName(self): # String
		return self.get_query_params().get('IdentityProviderName')

	def set_IdentityProviderName(self, IdentityProviderName):  # String
		self.add_query_param('IdentityProviderName', IdentityProviderName)
	def get_LdapConfig(self): # Struct
		return self.get_query_params().get('LdapConfig')

	def set_LdapConfig(self, LdapConfig):  # Struct
		if LdapConfig.get('StartTlsStatus') is not None:
			self.add_query_param('LdapConfig.StartTlsStatus', LdapConfig.get('StartTlsStatus'))
		if LdapConfig.get('LdapServerHost') is not None:
			self.add_query_param('LdapConfig.LdapServerHost', LdapConfig.get('LdapServerHost'))
		if LdapConfig.get('AdministratorUsername') is not None:
			self.add_query_param('LdapConfig.AdministratorUsername', LdapConfig.get('AdministratorUsername'))
		if LdapConfig.get('CertificateFingerprints') is not None:
			for index1, value1 in enumerate(LdapConfig.get('CertificateFingerprints')):
				self.add_query_param('LdapConfig.CertificateFingerprints.' + str(index1 + 1), value1)
		if LdapConfig.get('LdapProtocol') is not None:
			self.add_query_param('LdapConfig.LdapProtocol', LdapConfig.get('LdapProtocol'))
		if LdapConfig.get('AdministratorPassword') is not None:
			self.add_query_param('LdapConfig.AdministratorPassword', LdapConfig.get('AdministratorPassword'))
		if LdapConfig.get('CertificateFingerprintStatus') is not None:
			self.add_query_param('LdapConfig.CertificateFingerprintStatus', LdapConfig.get('CertificateFingerprintStatus'))
		if LdapConfig.get('LdapServerPort') is not None:
			self.add_query_param('LdapConfig.LdapServerPort', LdapConfig.get('LdapServerPort'))
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_OidcConfig(self): # Struct
		return self.get_query_params().get('OidcConfig')

	def set_OidcConfig(self, OidcConfig):  # Struct
		if OidcConfig.get('GrantScopes') is not None:
			for index1, value1 in enumerate(OidcConfig.get('GrantScopes')):
				self.add_query_param('OidcConfig.GrantScopes.' + str(index1 + 1), value1)
		if OidcConfig.get('EndpointConfig') is not None:
			if OidcConfig.get('EndpointConfig').get('UserinfoEndpoint') is not None:
				self.add_query_param('OidcConfig.EndpointConfig.UserinfoEndpoint', OidcConfig.get('EndpointConfig').get('UserinfoEndpoint'))
			if OidcConfig.get('EndpointConfig').get('AuthorizationEndpoint') is not None:
				self.add_query_param('OidcConfig.EndpointConfig.AuthorizationEndpoint', OidcConfig.get('EndpointConfig').get('AuthorizationEndpoint'))
			if OidcConfig.get('EndpointConfig').get('JwksUri') is not None:
				self.add_query_param('OidcConfig.EndpointConfig.JwksUri', OidcConfig.get('EndpointConfig').get('JwksUri'))
			if OidcConfig.get('EndpointConfig').get('TokenEndpoint') is not None:
				self.add_query_param('OidcConfig.EndpointConfig.TokenEndpoint', OidcConfig.get('EndpointConfig').get('TokenEndpoint'))
			if OidcConfig.get('EndpointConfig').get('Issuer') is not None:
				self.add_query_param('OidcConfig.EndpointConfig.Issuer', OidcConfig.get('EndpointConfig').get('Issuer'))
		if OidcConfig.get('PkceChallengeMethod') is not None:
			self.add_query_param('OidcConfig.PkceChallengeMethod', OidcConfig.get('PkceChallengeMethod'))
		if OidcConfig.get('PkceRequired') is not None:
			self.add_query_param('OidcConfig.PkceRequired', OidcConfig.get('PkceRequired'))
		if OidcConfig.get('AuthnParam') is not None:
			if OidcConfig.get('AuthnParam').get('ClientSecret') is not None:
				self.add_query_param('OidcConfig.AuthnParam.ClientSecret', OidcConfig.get('AuthnParam').get('ClientSecret'))
			if OidcConfig.get('AuthnParam').get('AuthnMethod') is not None:
				self.add_query_param('OidcConfig.AuthnParam.AuthnMethod', OidcConfig.get('AuthnParam').get('AuthnMethod'))
		if OidcConfig.get('GrantType') is not None:
			self.add_query_param('OidcConfig.GrantType', OidcConfig.get('GrantType'))
