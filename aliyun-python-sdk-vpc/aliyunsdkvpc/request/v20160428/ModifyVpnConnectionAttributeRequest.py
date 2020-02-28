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

class ModifyVpnConnectionAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyVpnConnectionAttribute','Vpc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IkeConfig(self):
		return self.get_query_params().get('IkeConfig')

	def set_IkeConfig(self,IkeConfig):
		self.add_query_param('IkeConfig',IkeConfig)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_AutoConfigRoute(self):
		return self.get_query_params().get('AutoConfigRoute')

	def set_AutoConfigRoute(self,AutoConfigRoute):
		self.add_query_param('AutoConfigRoute',AutoConfigRoute)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_IpsecConfig(self):
		return self.get_query_params().get('IpsecConfig')

	def set_IpsecConfig(self,IpsecConfig):
		self.add_query_param('IpsecConfig',IpsecConfig)

	def get_HealthCheckConfig(self):
		return self.get_query_params().get('HealthCheckConfig')

	def set_HealthCheckConfig(self,HealthCheckConfig):
		self.add_query_param('HealthCheckConfig',HealthCheckConfig)

	def get_LocalSubnet(self):
		return self.get_query_params().get('LocalSubnet')

	def set_LocalSubnet(self,LocalSubnet):
		self.add_query_param('LocalSubnet',LocalSubnet)

	def get_RemoteSubnet(self):
		return self.get_query_params().get('RemoteSubnet')

	def set_RemoteSubnet(self,RemoteSubnet):
		self.add_query_param('RemoteSubnet',RemoteSubnet)

	def get_EffectImmediately(self):
		return self.get_query_params().get('EffectImmediately')

	def set_EffectImmediately(self,EffectImmediately):
		self.add_query_param('EffectImmediately',EffectImmediately)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_VpnConnectionId(self):
		return self.get_query_params().get('VpnConnectionId')

	def set_VpnConnectionId(self,VpnConnectionId):
		self.add_query_param('VpnConnectionId',VpnConnectionId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)