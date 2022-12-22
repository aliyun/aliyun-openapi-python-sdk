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

class CreatePhysicalConnectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreatePhysicalConnection','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AccessPointId(self): # String
		return self.get_query_params().get('AccessPointId')

	def set_AccessPointId(self, AccessPointId):  # String
		self.add_query_param('AccessPointId', AccessPointId)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_PortType(self): # String
		return self.get_query_params().get('PortType')

	def set_PortType(self, PortType):  # String
		self.add_query_param('PortType', PortType)
	def get_CircuitCode(self): # String
		return self.get_query_params().get('CircuitCode')

	def set_CircuitCode(self, CircuitCode):  # String
		self.add_query_param('CircuitCode', CircuitCode)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_RedundantPhysicalConnectionId(self): # String
		return self.get_query_params().get('RedundantPhysicalConnectionId')

	def set_RedundantPhysicalConnectionId(self, RedundantPhysicalConnectionId):  # String
		self.add_query_param('RedundantPhysicalConnectionId', RedundantPhysicalConnectionId)
	def get_PeerLocation(self): # String
		return self.get_query_params().get('PeerLocation')

	def set_PeerLocation(self, PeerLocation):  # String
		self.add_query_param('PeerLocation', PeerLocation)
	def get_bandwidth(self): # Integer
		return self.get_query_params().get('bandwidth')

	def set_bandwidth(self, bandwidth):  # Integer
		self.add_query_param('bandwidth', bandwidth)
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
	def get_LineOperator(self): # String
		return self.get_query_params().get('LineOperator')

	def set_LineOperator(self, LineOperator):  # String
		self.add_query_param('LineOperator', LineOperator)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
