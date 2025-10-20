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

class CreateFederatedCredentialProviderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'CreateFederatedCredentialProvider','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_OidcProviderConfig(self): # Struct
		return self.get_query_params().get('OidcProviderConfig')

	def set_OidcProviderConfig(self, OidcProviderConfig):  # Struct
		if OidcProviderConfig.get('JwksSource') is not None:
			self.add_query_param('OidcProviderConfig.JwksSource', OidcProviderConfig.get('JwksSource'))
		if OidcProviderConfig.get('StaticJwks') is not None:
			self.add_query_param('OidcProviderConfig.StaticJwks', OidcProviderConfig.get('StaticJwks'))
		if OidcProviderConfig.get('TrustCondition') is not None:
			self.add_query_param('OidcProviderConfig.TrustCondition', OidcProviderConfig.get('TrustCondition'))
		if OidcProviderConfig.get('JwksUri') is not None:
			self.add_query_param('OidcProviderConfig.JwksUri', OidcProviderConfig.get('JwksUri'))
		if OidcProviderConfig.get('Audiences') is not None:
			for index1, value1 in enumerate(OidcProviderConfig.get('Audiences')):
				self.add_query_param('OidcProviderConfig.Audiences.' + str(index1 + 1), value1)
		if OidcProviderConfig.get('Issuer') is not None:
			self.add_query_param('OidcProviderConfig.Issuer', OidcProviderConfig.get('Issuer'))
	def get_FederatedCredentialProviderName(self): # String
		return self.get_query_params().get('FederatedCredentialProviderName')

	def set_FederatedCredentialProviderName(self, FederatedCredentialProviderName):  # String
		self.add_query_param('FederatedCredentialProviderName', FederatedCredentialProviderName)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_NetworkAccessEndpointId(self): # String
		return self.get_query_params().get('NetworkAccessEndpointId')

	def set_NetworkAccessEndpointId(self, NetworkAccessEndpointId):  # String
		self.add_query_param('NetworkAccessEndpointId', NetworkAccessEndpointId)
	def get_PrivateCaProviderConfig(self): # Struct
		return self.get_query_params().get('PrivateCaProviderConfig')

	def set_PrivateCaProviderConfig(self, PrivateCaProviderConfig):  # Struct
		if PrivateCaProviderConfig.get('Certificates') is not None:
			for index1, value1 in enumerate(PrivateCaProviderConfig.get('Certificates')):
				if value1.get('Content') is not None:
					self.add_query_param('PrivateCaProviderConfig.Certificates.' + str(index1 + 1) + '.Content', value1.get('Content'))
		if PrivateCaProviderConfig.get('TrustCondition') is not None:
			self.add_query_param('PrivateCaProviderConfig.TrustCondition', PrivateCaProviderConfig.get('TrustCondition'))
		if PrivateCaProviderConfig.get('TrustAnchorSource') is not None:
			self.add_query_param('PrivateCaProviderConfig.TrustAnchorSource', PrivateCaProviderConfig.get('TrustAnchorSource'))
	def get_FederatedCredentialProviderType(self): # String
		return self.get_query_params().get('FederatedCredentialProviderType')

	def set_FederatedCredentialProviderType(self, FederatedCredentialProviderType):  # String
		self.add_query_param('FederatedCredentialProviderType', FederatedCredentialProviderType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Pkcs7ProviderConfig(self): # Struct
		return self.get_query_params().get('Pkcs7ProviderConfig')

	def set_Pkcs7ProviderConfig(self, Pkcs7ProviderConfig):  # Struct
		if Pkcs7ProviderConfig.get('SigningTimeValueExpression') is not None:
			self.add_query_param('Pkcs7ProviderConfig.SigningTimeValueExpression', Pkcs7ProviderConfig.get('SigningTimeValueExpression'))
		if Pkcs7ProviderConfig.get('Certificates') is not None:
			for index1, value1 in enumerate(Pkcs7ProviderConfig.get('Certificates')):
				if value1.get('Content') is not None:
					self.add_query_param('Pkcs7ProviderConfig.Certificates.' + str(index1 + 1) + '.Content', value1.get('Content'))
		if Pkcs7ProviderConfig.get('TrustCondition') is not None:
			self.add_query_param('Pkcs7ProviderConfig.TrustCondition', Pkcs7ProviderConfig.get('TrustCondition'))
		if Pkcs7ProviderConfig.get('CmsVerificationMode') is not None:
			self.add_query_param('Pkcs7ProviderConfig.CmsVerificationMode', Pkcs7ProviderConfig.get('CmsVerificationMode'))
		if Pkcs7ProviderConfig.get('TrustAnchorSource') is not None:
			self.add_query_param('Pkcs7ProviderConfig.TrustAnchorSource', Pkcs7ProviderConfig.get('TrustAnchorSource'))
		if Pkcs7ProviderConfig.get('SignatureEffectiveTime') is not None:
			self.add_query_param('Pkcs7ProviderConfig.SignatureEffectiveTime', Pkcs7ProviderConfig.get('SignatureEffectiveTime'))
