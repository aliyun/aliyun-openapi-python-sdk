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
from aliyunsdkecs.endpoint import endpoint_data

class CreateVirtualBorderRouterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateVirtualBorderRouter','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_CircuitCode(self): # String
		return self.get_query_params().get('CircuitCode')

	def set_CircuitCode(self, CircuitCode):  # String
		self.add_query_param('CircuitCode', CircuitCode)
	def get_VlanId(self): # Integer
		return self.get_query_params().get('VlanId')

	def set_VlanId(self, VlanId):  # Integer
		self.add_query_param('VlanId', VlanId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_PeerGatewayIp(self): # String
		return self.get_query_params().get('PeerGatewayIp')

	def set_PeerGatewayIp(self, PeerGatewayIp):  # String
		self.add_query_param('PeerGatewayIp', PeerGatewayIp)
	def get_PeeringSubnetMask(self): # String
		return self.get_query_params().get('PeeringSubnetMask')

	def set_PeeringSubnetMask(self, PeeringSubnetMask):  # String
		self.add_query_param('PeeringSubnetMask', PeeringSubnetMask)
	def get_LocalGatewayIp(self): # String
		return self.get_query_params().get('LocalGatewayIp')

	def set_LocalGatewayIp(self, LocalGatewayIp):  # String
		self.add_query_param('LocalGatewayIp', LocalGatewayIp)
	def get_UserCidr(self): # String
		return self.get_query_params().get('UserCidr')

	def set_UserCidr(self, UserCidr):  # String
		self.add_query_param('UserCidr', UserCidr)
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
	def get_PhysicalConnectionId(self): # String
		return self.get_query_params().get('PhysicalConnectionId')

	def set_PhysicalConnectionId(self, PhysicalConnectionId):  # String
		self.add_query_param('PhysicalConnectionId', PhysicalConnectionId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_VbrOwnerId(self): # Long
		return self.get_query_params().get('VbrOwnerId')

	def set_VbrOwnerId(self, VbrOwnerId):  # Long
		self.add_query_param('VbrOwnerId', VbrOwnerId)
