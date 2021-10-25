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

class ModifyFullNatEntryAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyFullNatEntryAttribute','vpc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FullNatEntryDescription(self):
		return self.get_query_params().get('FullNatEntryDescription')

	def set_FullNatEntryDescription(self,FullNatEntryDescription):
		self.add_query_param('FullNatEntryDescription',FullNatEntryDescription)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_AccessIp(self):
		return self.get_query_params().get('AccessIp')

	def set_AccessIp(self,AccessIp):
		self.add_query_param('AccessIp',AccessIp)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_FullNatEntryId(self):
		return self.get_query_params().get('FullNatEntryId')

	def set_FullNatEntryId(self,FullNatEntryId):
		self.add_query_param('FullNatEntryId',FullNatEntryId)

	def get_NatIpPort(self):
		return self.get_query_params().get('NatIpPort')

	def set_NatIpPort(self,NatIpPort):
		self.add_query_param('NatIpPort',NatIpPort)

	def get_FullNatTableId(self):
		return self.get_query_params().get('FullNatTableId')

	def set_FullNatTableId(self,FullNatTableId):
		self.add_query_param('FullNatTableId',FullNatTableId)

	def get_AccessPort(self):
		return self.get_query_params().get('AccessPort')

	def set_AccessPort(self,AccessPort):
		self.add_query_param('AccessPort',AccessPort)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

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

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_FullNatEntryName(self):
		return self.get_query_params().get('FullNatEntryName')

	def set_FullNatEntryName(self,FullNatEntryName):
		self.add_query_param('FullNatEntryName',FullNatEntryName)

	def get_NatIp(self):
		return self.get_query_params().get('NatIp')

	def set_NatIp(self,NatIp):
		self.add_query_param('NatIp',NatIp)

	def get_NetworkInterfaceId(self):
		return self.get_query_params().get('NetworkInterfaceId')

	def set_NetworkInterfaceId(self,NetworkInterfaceId):
		self.add_query_param('NetworkInterfaceId',NetworkInterfaceId)