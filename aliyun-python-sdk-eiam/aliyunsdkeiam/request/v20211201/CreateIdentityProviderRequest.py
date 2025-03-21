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

class CreateIdentityProviderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'CreateIdentityProvider','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_DingtalkAppConfig(self): # Struct
		return self.get_query_params().get('DingtalkAppConfig')

	def set_DingtalkAppConfig(self, DingtalkAppConfig):  # Struct
		if DingtalkAppConfig.get('CorpId') is not None:
			self.add_query_param('DingtalkAppConfig.CorpId', DingtalkAppConfig.get('CorpId'))
		if DingtalkAppConfig.get('DingtalkVersion') is not None:
			self.add_query_param('DingtalkAppConfig.DingtalkVersion', DingtalkAppConfig.get('DingtalkVersion'))
		if DingtalkAppConfig.get('AppSecret') is not None:
			self.add_query_param('DingtalkAppConfig.AppSecret', DingtalkAppConfig.get('AppSecret'))
		if DingtalkAppConfig.get('AppKey') is not None:
			self.add_query_param('DingtalkAppConfig.AppKey', DingtalkAppConfig.get('AppKey'))
	def get_NetworkAccessEndpointId(self): # String
		return self.get_query_params().get('NetworkAccessEndpointId')

	def set_NetworkAccessEndpointId(self, NetworkAccessEndpointId):  # String
		self.add_query_param('NetworkAccessEndpointId', NetworkAccessEndpointId)
	def get_AutoUpdateUserConfig(self): # Struct
		return self.get_query_params().get('AutoUpdateUserConfig')

	def set_AutoUpdateUserConfig(self, AutoUpdateUserConfig):  # Struct
		if AutoUpdateUserConfig.get('AutoUpdateUserStatus') is not None:
			self.add_query_param('AutoUpdateUserConfig.AutoUpdateUserStatus', AutoUpdateUserConfig.get('AutoUpdateUserStatus'))
	def get_LogoUrl(self): # String
		return self.get_query_params().get('LogoUrl')

	def set_LogoUrl(self, LogoUrl):  # String
		self.add_query_param('LogoUrl', LogoUrl)
	def get_UdPullConfig(self): # Struct
		return self.get_query_params().get('UdPullConfig')

	def set_UdPullConfig(self, UdPullConfig):  # Struct
		if UdPullConfig.get('GroupSyncStatus') is not None:
			self.add_query_param('UdPullConfig.GroupSyncStatus', UdPullConfig.get('GroupSyncStatus'))
		if UdPullConfig.get('UdSyncScopeConfig') is not None:
			if UdPullConfig.get('UdSyncScopeConfig').get('TargetScope') is not None:
				self.add_query_param('UdPullConfig.UdSyncScopeConfig.TargetScope', UdPullConfig.get('UdSyncScopeConfig').get('TargetScope'))
			if UdPullConfig.get('UdSyncScopeConfig').get('SourceScopes') is not None:
				for index1, value1 in enumerate(UdPullConfig.get('UdSyncScopeConfig').get('SourceScopes')):
					self.add_query_param('UdPullConfig.UdSyncScopeConfig.SourceScopes.' + str(index1 + 1), value1)
		if UdPullConfig.get('PeriodicSyncStatus') is not None:
			self.add_query_param('UdPullConfig.PeriodicSyncStatus', UdPullConfig.get('PeriodicSyncStatus'))
		if UdPullConfig.get('PeriodicSyncConfig') is not None:
			if UdPullConfig.get('PeriodicSyncConfig').get('PeriodicSyncTimes') is not None:
				for index1, value1 in enumerate(UdPullConfig.get('PeriodicSyncConfig').get('PeriodicSyncTimes')):
					self.add_query_param('UdPullConfig.PeriodicSyncConfig.PeriodicSyncTimes.' + str(index1 + 1), value1)
			if UdPullConfig.get('PeriodicSyncConfig').get('PeriodicSyncCron') is not None:
				self.add_query_param('UdPullConfig.PeriodicSyncConfig.PeriodicSyncCron', UdPullConfig.get('PeriodicSyncConfig').get('PeriodicSyncCron'))
			if UdPullConfig.get('PeriodicSyncConfig').get('PeriodicSyncType') is not None:
				self.add_query_param('UdPullConfig.PeriodicSyncConfig.PeriodicSyncType', UdPullConfig.get('PeriodicSyncConfig').get('PeriodicSyncType'))
		if UdPullConfig.get('IncrementalCallbackStatus') is not None:
			self.add_query_param('UdPullConfig.IncrementalCallbackStatus', UdPullConfig.get('IncrementalCallbackStatus'))
	def get_LarkConfig(self): # Struct
		return self.get_query_params().get('LarkConfig')

	def set_LarkConfig(self, LarkConfig):  # Struct
		if LarkConfig.get('EnterpriseNumber') is not None:
			self.add_query_param('LarkConfig.EnterpriseNumber', LarkConfig.get('EnterpriseNumber'))
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
		if WeComConfig.get('CorpId') is not None:
			self.add_query_param('WeComConfig.CorpId', WeComConfig.get('CorpId'))
		if WeComConfig.get('CorpSecret') is not None:
			self.add_query_param('WeComConfig.CorpSecret', WeComConfig.get('CorpSecret'))
		if WeComConfig.get('AuthorizeCallbackDomain') is not None:
			self.add_query_param('WeComConfig.AuthorizeCallbackDomain', WeComConfig.get('AuthorizeCallbackDomain'))
		if WeComConfig.get('TrustableDomain') is not None:
			self.add_query_param('WeComConfig.TrustableDomain', WeComConfig.get('TrustableDomain'))
	def get_AutoCreateUserConfig(self): # Struct
		return self.get_query_params().get('AutoCreateUserConfig')

	def set_AutoCreateUserConfig(self, AutoCreateUserConfig):  # Struct
		if AutoCreateUserConfig.get('AutoCreateUserStatus') is not None:
			self.add_query_param('AutoCreateUserConfig.AutoCreateUserStatus', AutoCreateUserConfig.get('AutoCreateUserStatus'))
		if AutoCreateUserConfig.get('TargetOrganizationalUnitIds') is not None:
			for index1, value1 in enumerate(AutoCreateUserConfig.get('TargetOrganizationalUnitIds')):
				self.add_query_param('AutoCreateUserConfig.TargetOrganizationalUnitIds.' + str(index1 + 1), value1)
	def get_AuthnConfig(self): # Struct
		return self.get_query_params().get('AuthnConfig')

	def set_AuthnConfig(self, AuthnConfig):  # Struct
		if AuthnConfig.get('AuthnStatus') is not None:
			self.add_query_param('AuthnConfig.AuthnStatus', AuthnConfig.get('AuthnStatus'))
		if AuthnConfig.get('AutoUpdatePasswordStatus') is not None:
			self.add_query_param('AuthnConfig.AutoUpdatePasswordStatus', AuthnConfig.get('AutoUpdatePasswordStatus'))
	def get_BindingConfig(self): # Struct
		return self.get_query_params().get('BindingConfig')

	def set_BindingConfig(self, BindingConfig):  # Struct
		if BindingConfig.get('AutoMatchUserProfileExpressions') is not None:
			for index1, value1 in enumerate(BindingConfig.get('AutoMatchUserProfileExpressions')):
				if value1.get('SourceValueExpression') is not None:
					self.add_query_param('BindingConfig.AutoMatchUserProfileExpressions.' + str(index1 + 1) + '.SourceValueExpression', value1.get('SourceValueExpression'))
				if value1.get('TargetFieldDescription') is not None:
					self.add_query_param('BindingConfig.AutoMatchUserProfileExpressions.' + str(index1 + 1) + '.TargetFieldDescription', value1.get('TargetFieldDescription'))
				if value1.get('TargetField') is not None:
					self.add_query_param('BindingConfig.AutoMatchUserProfileExpressions.' + str(index1 + 1) + '.TargetField', value1.get('TargetField'))
				if value1.get('ExpressionMappingType') is not None:
					self.add_query_param('BindingConfig.AutoMatchUserProfileExpressions.' + str(index1 + 1) + '.ExpressionMappingType', value1.get('ExpressionMappingType'))
		if BindingConfig.get('MappingBindingStatus') is not None:
			self.add_query_param('BindingConfig.MappingBindingStatus', BindingConfig.get('MappingBindingStatus'))
		if BindingConfig.get('AutoMatchUserStatus') is not None:
			self.add_query_param('BindingConfig.AutoMatchUserStatus', BindingConfig.get('AutoMatchUserStatus'))
	def get_IdentityProviderName(self): # String
		return self.get_query_params().get('IdentityProviderName')

	def set_IdentityProviderName(self, IdentityProviderName):  # String
		self.add_query_param('IdentityProviderName', IdentityProviderName)
	def get_LdapConfig(self): # Struct
		return self.get_query_params().get('LdapConfig')

	def set_LdapConfig(self, LdapConfig):  # Struct
		if LdapConfig.get('GroupMemberAttributeName') is not None:
			self.add_query_param('LdapConfig.GroupMemberAttributeName', LdapConfig.get('GroupMemberAttributeName'))
		if LdapConfig.get('StartTlsStatus') is not None:
			self.add_query_param('LdapConfig.StartTlsStatus', LdapConfig.get('StartTlsStatus'))
		if LdapConfig.get('LdapServerHost') is not None:
			self.add_query_param('LdapConfig.LdapServerHost', LdapConfig.get('LdapServerHost'))
		if LdapConfig.get('GroupObjectClass') is not None:
			self.add_query_param('LdapConfig.GroupObjectClass', LdapConfig.get('GroupObjectClass'))
		if LdapConfig.get('UserObjectClass') is not None:
			self.add_query_param('LdapConfig.UserObjectClass', LdapConfig.get('UserObjectClass'))
		if LdapConfig.get('UserObjectClassCustomFilter') is not None:
			self.add_query_param('LdapConfig.UserObjectClassCustomFilter', LdapConfig.get('UserObjectClassCustomFilter'))
		if LdapConfig.get('CertificateFingerprints') is not None:
			for index1, value1 in enumerate(LdapConfig.get('CertificateFingerprints')):
				self.add_query_param('LdapConfig.CertificateFingerprints.' + str(index1 + 1), value1)
		if LdapConfig.get('LdapProtocol') is not None:
			self.add_query_param('LdapConfig.LdapProtocol', LdapConfig.get('LdapProtocol'))
		if LdapConfig.get('GroupObjectClassCustomFilter') is not None:
			self.add_query_param('LdapConfig.GroupObjectClassCustomFilter', LdapConfig.get('GroupObjectClassCustomFilter'))
		if LdapConfig.get('OrganizationUnitObjectClass') is not None:
			self.add_query_param('LdapConfig.OrganizationUnitObjectClass', LdapConfig.get('OrganizationUnitObjectClass'))
		if LdapConfig.get('AdministratorUsername') is not None:
			self.add_query_param('LdapConfig.AdministratorUsername', LdapConfig.get('AdministratorUsername'))
		if LdapConfig.get('UserLoginIdentifier') is not None:
			self.add_query_param('LdapConfig.UserLoginIdentifier', LdapConfig.get('UserLoginIdentifier'))
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
	def get_UdPushConfig(self): # Struct
		return self.get_query_params().get('UdPushConfig')

	def set_UdPushConfig(self, UdPushConfig):  # Struct
		if UdPushConfig.get('PeriodicSyncStatus') is not None:
			self.add_query_param('UdPushConfig.PeriodicSyncStatus', UdPushConfig.get('PeriodicSyncStatus'))
		if UdPushConfig.get('IncrementalCallbackStatus') is not None:
			self.add_query_param('UdPushConfig.IncrementalCallbackStatus', UdPushConfig.get('IncrementalCallbackStatus'))
		if UdPushConfig.get('UdSyncScopeConfigs') is not None:
			for index1, value1 in enumerate(UdPushConfig.get('UdSyncScopeConfigs')):
				if value1.get('TargetScope') is not None:
					self.add_query_param('UdPushConfig.UdSyncScopeConfigs.' + str(index1 + 1) + '.TargetScope', value1.get('TargetScope'))
				if value1.get('SourceScopes') is not None:
					for index2, value2 in enumerate(value1.get('SourceScopes')):
						self.add_query_param('UdPushConfig.UdSyncScopeConfigs.' + str(index1 + 1) + '.SourceScopes.' + str(index2 + 1), value2)
	def get_IdentityProviderType(self): # String
		return self.get_query_params().get('IdentityProviderType')

	def set_IdentityProviderType(self, IdentityProviderType):  # String
		self.add_query_param('IdentityProviderType', IdentityProviderType)
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
			if OidcConfig.get('AuthnParam').get('ClientId') is not None:
				self.add_query_param('OidcConfig.AuthnParam.ClientId', OidcConfig.get('AuthnParam').get('ClientId'))
			if OidcConfig.get('AuthnParam').get('ClientSecret') is not None:
				self.add_query_param('OidcConfig.AuthnParam.ClientSecret', OidcConfig.get('AuthnParam').get('ClientSecret'))
			if OidcConfig.get('AuthnParam').get('AuthnMethod') is not None:
				self.add_query_param('OidcConfig.AuthnParam.AuthnMethod', OidcConfig.get('AuthnParam').get('AuthnMethod'))
		if OidcConfig.get('GrantType') is not None:
			self.add_query_param('OidcConfig.GrantType', OidcConfig.get('GrantType'))
