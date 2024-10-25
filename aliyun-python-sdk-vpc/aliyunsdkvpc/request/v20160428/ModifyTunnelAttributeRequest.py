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

class ModifyTunnelAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyTunnelAttribute','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TunnelOptionsSpecification(self): # Struct
		return self.get_query_params().get('TunnelOptionsSpecification')

	def set_TunnelOptionsSpecification(self, TunnelOptionsSpecification):  # Struct
		if TunnelOptionsSpecification.get('TunnelIpsecConfig') is not None:
			if TunnelOptionsSpecification.get('TunnelIpsecConfig').get('IpsecPfs') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIpsecConfig.IpsecPfs', TunnelOptionsSpecification.get('TunnelIpsecConfig').get('IpsecPfs'))
			if TunnelOptionsSpecification.get('TunnelIpsecConfig').get('IpsecLifetime') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIpsecConfig.IpsecLifetime', TunnelOptionsSpecification.get('TunnelIpsecConfig').get('IpsecLifetime'))
			if TunnelOptionsSpecification.get('TunnelIpsecConfig').get('IpsecAuthAlg') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIpsecConfig.IpsecAuthAlg', TunnelOptionsSpecification.get('TunnelIpsecConfig').get('IpsecAuthAlg'))
			if TunnelOptionsSpecification.get('TunnelIpsecConfig').get('IpsecEncAlg') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIpsecConfig.IpsecEncAlg', TunnelOptionsSpecification.get('TunnelIpsecConfig').get('IpsecEncAlg'))
		if TunnelOptionsSpecification.get('TunnelBgpConfig') is not None:
			if TunnelOptionsSpecification.get('TunnelBgpConfig').get('LocalAsn') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelBgpConfig.LocalAsn', TunnelOptionsSpecification.get('TunnelBgpConfig').get('LocalAsn'))
			if TunnelOptionsSpecification.get('TunnelBgpConfig').get('TunnelCidr') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelBgpConfig.TunnelCidr', TunnelOptionsSpecification.get('TunnelBgpConfig').get('TunnelCidr'))
			if TunnelOptionsSpecification.get('TunnelBgpConfig').get('LocalBgpIp') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelBgpConfig.LocalBgpIp', TunnelOptionsSpecification.get('TunnelBgpConfig').get('LocalBgpIp'))
		if TunnelOptionsSpecification.get('RemoteCaCertificate') is not None:
			self.add_query_param('TunnelOptionsSpecification.RemoteCaCertificate', TunnelOptionsSpecification.get('RemoteCaCertificate'))
		if TunnelOptionsSpecification.get('TunnelIkeConfig') is not None:
			if TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeVersion') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIkeConfig.IkeVersion', TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeVersion'))
			if TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeMode') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIkeConfig.IkeMode', TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeMode'))
			if TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeAuthAlg') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIkeConfig.IkeAuthAlg', TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeAuthAlg'))
			if TunnelOptionsSpecification.get('TunnelIkeConfig').get('Psk') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIkeConfig.Psk', TunnelOptionsSpecification.get('TunnelIkeConfig').get('Psk'))
			if TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkePfs') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIkeConfig.IkePfs', TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkePfs'))
			if TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeLifetime') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIkeConfig.IkeLifetime', TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeLifetime'))
			if TunnelOptionsSpecification.get('TunnelIkeConfig').get('LocalId') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIkeConfig.LocalId', TunnelOptionsSpecification.get('TunnelIkeConfig').get('LocalId'))
			if TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeEncAlg') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIkeConfig.IkeEncAlg', TunnelOptionsSpecification.get('TunnelIkeConfig').get('IkeEncAlg'))
			if TunnelOptionsSpecification.get('TunnelIkeConfig').get('RemoteId') is not None:
				self.add_query_param('TunnelOptionsSpecification.TunnelIkeConfig.RemoteId', TunnelOptionsSpecification.get('TunnelIkeConfig').get('RemoteId'))
		if TunnelOptionsSpecification.get('EnableNatTraversal') is not None:
			self.add_query_param('TunnelOptionsSpecification.EnableNatTraversal', TunnelOptionsSpecification.get('EnableNatTraversal'))
		if TunnelOptionsSpecification.get('EnableDpd') is not None:
			self.add_query_param('TunnelOptionsSpecification.EnableDpd', TunnelOptionsSpecification.get('EnableDpd'))
		if TunnelOptionsSpecification.get('CustomerGatewayId') is not None:
			self.add_query_param('TunnelOptionsSpecification.CustomerGatewayId', TunnelOptionsSpecification.get('CustomerGatewayId'))
	def get_VpnConnectionId(self): # String
		return self.get_query_params().get('VpnConnectionId')

	def set_VpnConnectionId(self, VpnConnectionId):  # String
		self.add_query_param('VpnConnectionId', VpnConnectionId)
	def get_TunnelId(self): # String
		return self.get_query_params().get('TunnelId')

	def set_TunnelId(self, TunnelId):  # String
		self.add_query_param('TunnelId', TunnelId)
