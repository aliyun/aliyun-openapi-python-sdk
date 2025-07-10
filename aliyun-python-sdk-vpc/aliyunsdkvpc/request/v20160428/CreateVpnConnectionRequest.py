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
from aliyunsdkvpc.endpoint import endpoint_data

class CreateVpnConnectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateVpnConnection','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IkeConfig(self): # String
		return self.get_query_params().get('IkeConfig')

	def set_IkeConfig(self, IkeConfig):  # String
		self.add_query_param('IkeConfig', IkeConfig)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_AutoConfigRoute(self): # Boolean
		return self.get_query_params().get('AutoConfigRoute')

	def set_AutoConfigRoute(self, AutoConfigRoute):  # Boolean
		self.add_query_param('AutoConfigRoute', AutoConfigRoute)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_IpsecConfig(self): # String
		return self.get_query_params().get('IpsecConfig')

	def set_IpsecConfig(self, IpsecConfig):  # String
		self.add_query_param('IpsecConfig', IpsecConfig)
	def get_BgpConfig(self): # String
		return self.get_query_params().get('BgpConfig')

	def set_BgpConfig(self, BgpConfig):  # String
		self.add_query_param('BgpConfig', BgpConfig)
	def get_HealthCheckConfig(self): # String
		return self.get_query_params().get('HealthCheckConfig')

	def set_HealthCheckConfig(self, HealthCheckConfig):  # String
		self.add_query_param('HealthCheckConfig', HealthCheckConfig)
	def get_CustomerGatewayId(self): # String
		return self.get_query_params().get('CustomerGatewayId')

	def set_CustomerGatewayId(self, CustomerGatewayId):  # String
		self.add_query_param('CustomerGatewayId', CustomerGatewayId)
	def get_LocalSubnet(self): # String
		return self.get_query_params().get('LocalSubnet')

	def set_LocalSubnet(self, LocalSubnet):  # String
		self.add_query_param('LocalSubnet', LocalSubnet)
	def get_EnableTunnelsBgp(self): # Boolean
		return self.get_query_params().get('EnableTunnelsBgp')

	def set_EnableTunnelsBgp(self, EnableTunnelsBgp):  # Boolean
		self.add_query_param('EnableTunnelsBgp', EnableTunnelsBgp)
	def get_RemoteSubnet(self): # String
		return self.get_query_params().get('RemoteSubnet')

	def set_RemoteSubnet(self, RemoteSubnet):  # String
		self.add_query_param('RemoteSubnet', RemoteSubnet)
	def get_EffectImmediately(self): # Boolean
		return self.get_query_params().get('EffectImmediately')

	def set_EffectImmediately(self, EffectImmediately):  # Boolean
		self.add_query_param('EffectImmediately', EffectImmediately)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_VpnGatewayId(self): # String
		return self.get_query_params().get('VpnGatewayId')

	def set_VpnGatewayId(self, VpnGatewayId):  # String
		self.add_query_param('VpnGatewayId', VpnGatewayId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_EnableDpd(self): # Boolean
		return self.get_query_params().get('EnableDpd')

	def set_EnableDpd(self, EnableDpd):  # Boolean
		self.add_query_param('EnableDpd', EnableDpd)
	def get_Tagss(self): # RepeatList
		return self.get_query_params().get('Tags')

	def set_Tagss(self, Tags):  # RepeatList
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
	def get_TunnelOptionsSpecification(self): # Array
		return self.get_body_params().get('TunnelOptionsSpecification')

	def set_TunnelOptionsSpecification(self, TunnelOptionsSpecification):  # Array
		for index1, value1 in enumerate(TunnelOptionsSpecification):
			if value1.get('TunnelIpsecConfig') is not None:
				if value1.get('TunnelIpsecConfig').get('IpsecPfs') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIpsecConfig.IpsecPfs', value1.get('TunnelIpsecConfig').get('IpsecPfs'))
				if value1.get('TunnelIpsecConfig').get('IpsecLifetime') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIpsecConfig.IpsecLifetime', value1.get('TunnelIpsecConfig').get('IpsecLifetime'))
				if value1.get('TunnelIpsecConfig').get('IpsecAuthAlg') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIpsecConfig.IpsecAuthAlg', value1.get('TunnelIpsecConfig').get('IpsecAuthAlg'))
				if value1.get('TunnelIpsecConfig').get('IpsecEncAlg') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIpsecConfig.IpsecEncAlg', value1.get('TunnelIpsecConfig').get('IpsecEncAlg'))
			if value1.get('Role') is not None:
				self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.Role', value1.get('Role'))
			if value1.get('TunnelBgpConfig') is not None:
				if value1.get('TunnelBgpConfig').get('LocalAsn') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelBgpConfig.LocalAsn', value1.get('TunnelBgpConfig').get('LocalAsn'))
				if value1.get('TunnelBgpConfig').get('TunnelCidr') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelBgpConfig.TunnelCidr', value1.get('TunnelBgpConfig').get('TunnelCidr'))
				if value1.get('TunnelBgpConfig').get('LocalBgpIp') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelBgpConfig.LocalBgpIp', value1.get('TunnelBgpConfig').get('LocalBgpIp'))
			if value1.get('RemoteCaCertificate') is not None:
				self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.RemoteCaCertificate', value1.get('RemoteCaCertificate'))
			if value1.get('TunnelIkeConfig') is not None:
				if value1.get('TunnelIkeConfig').get('IkeVersion') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIkeConfig.IkeVersion', value1.get('TunnelIkeConfig').get('IkeVersion'))
				if value1.get('TunnelIkeConfig').get('IkeMode') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIkeConfig.IkeMode', value1.get('TunnelIkeConfig').get('IkeMode'))
				if value1.get('TunnelIkeConfig').get('IkeAuthAlg') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIkeConfig.IkeAuthAlg', value1.get('TunnelIkeConfig').get('IkeAuthAlg'))
				if value1.get('TunnelIkeConfig').get('Psk') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIkeConfig.Psk', value1.get('TunnelIkeConfig').get('Psk'))
				if value1.get('TunnelIkeConfig').get('IkePfs') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIkeConfig.IkePfs', value1.get('TunnelIkeConfig').get('IkePfs'))
				if value1.get('TunnelIkeConfig').get('IkeLifetime') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIkeConfig.IkeLifetime', value1.get('TunnelIkeConfig').get('IkeLifetime'))
				if value1.get('TunnelIkeConfig').get('LocalId') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIkeConfig.LocalId', value1.get('TunnelIkeConfig').get('LocalId'))
				if value1.get('TunnelIkeConfig').get('IkeEncAlg') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIkeConfig.IkeEncAlg', value1.get('TunnelIkeConfig').get('IkeEncAlg'))
				if value1.get('TunnelIkeConfig').get('RemoteId') is not None:
					self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.TunnelIkeConfig.RemoteId', value1.get('TunnelIkeConfig').get('RemoteId'))
			if value1.get('EnableNatTraversal') is not None:
				self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.EnableNatTraversal', value1.get('EnableNatTraversal'))
			if value1.get('EnableDpd') is not None:
				self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.EnableDpd', value1.get('EnableDpd'))
			if value1.get('CustomerGatewayId') is not None:
				self.add_body_params('TunnelOptionsSpecification.' + str(index1 + 1) + '.CustomerGatewayId', value1.get('CustomerGatewayId'))
	def get_RemoteCaCertificate(self): # String
		return self.get_query_params().get('RemoteCaCertificate')

	def set_RemoteCaCertificate(self, RemoteCaCertificate):  # String
		self.add_query_param('RemoteCaCertificate', RemoteCaCertificate)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_EnableNatTraversal(self): # Boolean
		return self.get_query_params().get('EnableNatTraversal')

	def set_EnableNatTraversal(self, EnableNatTraversal):  # Boolean
		self.add_query_param('EnableNatTraversal', EnableNatTraversal)
