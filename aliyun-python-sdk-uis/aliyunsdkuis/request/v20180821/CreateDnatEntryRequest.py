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
from aliyunsdkuis.endpoint import endpoint_data

class CreateDnatEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Uis', '2018-08-21', 'CreateDnatEntry','uis')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_OriginalIp(self):
		return self.get_query_params().get('OriginalIp')

	def set_OriginalIp(self,OriginalIp):
		self.add_query_param('OriginalIp',OriginalIp)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_IpProtocol(self):
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self,IpProtocol):
		self.add_query_param('IpProtocol',IpProtocol)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OriginalPort(self):
		return self.get_query_params().get('OriginalPort')

	def set_OriginalPort(self,OriginalPort):
		self.add_query_param('OriginalPort',OriginalPort)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DestinationIp(self):
		return self.get_query_params().get('DestinationIp')

	def set_DestinationIp(self,DestinationIp):
		self.add_query_param('DestinationIp',DestinationIp)

	def get_DestinationPort(self):
		return self.get_query_params().get('DestinationPort')

	def set_DestinationPort(self,DestinationPort):
		self.add_query_param('DestinationPort',DestinationPort)

	def get_UisNodeId(self):
		return self.get_query_params().get('UisNodeId')

	def set_UisNodeId(self,UisNodeId):
		self.add_query_param('UisNodeId',UisNodeId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)