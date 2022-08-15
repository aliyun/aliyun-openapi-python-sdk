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

class CreateVpnAttachmentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateVpnAttachment','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IkeConfig(self): # String
		return self.get_query_params().get('IkeConfig')

	def set_IkeConfig(self, IkeConfig):  # String
		self.add_query_param('IkeConfig', IkeConfig)
	def get_AutoConfigRoute(self): # Boolean
		return self.get_query_params().get('AutoConfigRoute')

	def set_AutoConfigRoute(self, AutoConfigRoute):  # Boolean
		self.add_query_param('AutoConfigRoute', AutoConfigRoute)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
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
	def get_NetworkType(self): # String
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self, NetworkType):  # String
		self.add_query_param('NetworkType', NetworkType)
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
	def get_RemoteCaCert(self): # String
		return self.get_query_params().get('RemoteCaCert')

	def set_RemoteCaCert(self, RemoteCaCert):  # String
		self.add_query_param('RemoteCaCert', RemoteCaCert)
	def get_RemoteSubnet(self): # String
		return self.get_query_params().get('RemoteSubnet')

	def set_RemoteSubnet(self, RemoteSubnet):  # String
		self.add_query_param('RemoteSubnet', RemoteSubnet)
	def get_EffectImmediately(self): # Boolean
		return self.get_query_params().get('EffectImmediately')

	def set_EffectImmediately(self, EffectImmediately):  # Boolean
		self.add_query_param('EffectImmediately', EffectImmediately)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_EnableDpd(self): # Boolean
		return self.get_query_params().get('EnableDpd')

	def set_EnableDpd(self, EnableDpd):  # Boolean
		self.add_query_param('EnableDpd', EnableDpd)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_EnableNatTraversal(self): # Boolean
		return self.get_query_params().get('EnableNatTraversal')

	def set_EnableNatTraversal(self, EnableNatTraversal):  # Boolean
		self.add_query_param('EnableNatTraversal', EnableNatTraversal)
