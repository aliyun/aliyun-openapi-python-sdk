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

class CreateSslVpnServerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateSslVpnServer','vpc')
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
	def get_LocalSubnet(self): # String
		return self.get_query_params().get('LocalSubnet')

	def set_LocalSubnet(self, LocalSubnet):  # String
		self.add_query_param('LocalSubnet', LocalSubnet)
	def get_IDaaSRegionId(self): # String
		return self.get_query_params().get('IDaaSRegionId')

	def set_IDaaSRegionId(self, IDaaSRegionId):  # String
		self.add_query_param('IDaaSRegionId', IDaaSRegionId)
	def get_EnableMultiFactorAuth(self): # Boolean
		return self.get_query_params().get('EnableMultiFactorAuth')

	def set_EnableMultiFactorAuth(self, EnableMultiFactorAuth):  # Boolean
		self.add_query_param('EnableMultiFactorAuth', EnableMultiFactorAuth)
	def get_IDaaSInstanceId(self): # String
		return self.get_query_params().get('IDaaSInstanceId')

	def set_IDaaSInstanceId(self, IDaaSInstanceId):  # String
		self.add_query_param('IDaaSInstanceId', IDaaSInstanceId)
	def get_Cipher(self): # String
		return self.get_query_params().get('Cipher')

	def set_Cipher(self, Cipher):  # String
		self.add_query_param('Cipher', Cipher)
	def get_ClientIpPool(self): # String
		return self.get_query_params().get('ClientIpPool')

	def set_ClientIpPool(self, ClientIpPool):  # String
		self.add_query_param('ClientIpPool', ClientIpPool)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_Compress(self): # Boolean
		return self.get_query_params().get('Compress')

	def set_Compress(self, Compress):  # Boolean
		self.add_query_param('Compress', Compress)
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
	def get_Port(self): # Integer
		return self.get_query_params().get('Port')

	def set_Port(self, Port):  # Integer
		self.add_query_param('Port', Port)
	def get_Proto(self): # String
		return self.get_query_params().get('Proto')

	def set_Proto(self, Proto):  # String
		self.add_query_param('Proto', Proto)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
