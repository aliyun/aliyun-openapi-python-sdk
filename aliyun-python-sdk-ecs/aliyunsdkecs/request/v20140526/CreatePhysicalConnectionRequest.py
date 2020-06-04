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

class CreatePhysicalConnectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreatePhysicalConnection','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AccessPointId(self):
		return self.get_query_params().get('AccessPointId')

	def set_AccessPointId(self,AccessPointId):
		self.add_query_param('AccessPointId',AccessPointId)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PortType(self):
		return self.get_query_params().get('PortType')

	def set_PortType(self,PortType):
		self.add_query_param('PortType',PortType)

	def get_CircuitCode(self):
		return self.get_query_params().get('CircuitCode')

	def set_CircuitCode(self,CircuitCode):
		self.add_query_param('CircuitCode',CircuitCode)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_UserCidr(self):
		return self.get_query_params().get('UserCidr')

	def set_UserCidr(self,UserCidr):
		self.add_query_param('UserCidr',UserCidr)

	def get_RedundantPhysicalConnectionId(self):
		return self.get_query_params().get('RedundantPhysicalConnectionId')

	def set_RedundantPhysicalConnectionId(self,RedundantPhysicalConnectionId):
		self.add_query_param('RedundantPhysicalConnectionId',RedundantPhysicalConnectionId)

	def get_PeerLocation(self):
		return self.get_query_params().get('PeerLocation')

	def set_PeerLocation(self,PeerLocation):
		self.add_query_param('PeerLocation',PeerLocation)

	def get_bandwidth(self):
		return self.get_query_params().get('bandwidth')

	def set_bandwidth(self,bandwidth):
		self.add_query_param('bandwidth',bandwidth)

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

	def get_LineOperator(self):
		return self.get_query_params().get('LineOperator')

	def set_LineOperator(self,LineOperator):
		self.add_query_param('LineOperator',LineOperator)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)