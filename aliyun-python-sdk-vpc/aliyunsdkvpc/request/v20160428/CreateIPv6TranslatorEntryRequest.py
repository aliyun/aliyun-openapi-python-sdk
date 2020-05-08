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

class CreateIPv6TranslatorEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateIPv6TranslatorEntry','Vpc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BackendIpv4Port(self):
		return self.get_query_params().get('BackendIpv4Port')

	def set_BackendIpv4Port(self,BackendIpv4Port):
		self.add_query_param('BackendIpv4Port',BackendIpv4Port)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_EntryName(self):
		return self.get_query_params().get('EntryName')

	def set_EntryName(self,EntryName):
		self.add_query_param('EntryName',EntryName)

	def get_AclStatus(self):
		return self.get_query_params().get('AclStatus')

	def set_AclStatus(self,AclStatus):
		self.add_query_param('AclStatus',AclStatus)

	def get_EntryBandwidth(self):
		return self.get_query_params().get('EntryBandwidth')

	def set_EntryBandwidth(self,EntryBandwidth):
		self.add_query_param('EntryBandwidth',EntryBandwidth)

	def get_AclType(self):
		return self.get_query_params().get('AclType')

	def set_AclType(self,AclType):
		self.add_query_param('AclType',AclType)

	def get_AllocateIpv6Port(self):
		return self.get_query_params().get('AllocateIpv6Port')

	def set_AllocateIpv6Port(self,AllocateIpv6Port):
		self.add_query_param('AllocateIpv6Port',AllocateIpv6Port)

	def get_EntryDescription(self):
		return self.get_query_params().get('EntryDescription')

	def set_EntryDescription(self,EntryDescription):
		self.add_query_param('EntryDescription',EntryDescription)

	def get_BackendIpv4Addr(self):
		return self.get_query_params().get('BackendIpv4Addr')

	def set_BackendIpv4Addr(self,BackendIpv4Addr):
		self.add_query_param('BackendIpv4Addr',BackendIpv4Addr)

	def get_AclId(self):
		return self.get_query_params().get('AclId')

	def set_AclId(self,AclId):
		self.add_query_param('AclId',AclId)

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

	def get_TransProtocol(self):
		return self.get_query_params().get('TransProtocol')

	def set_TransProtocol(self,TransProtocol):
		self.add_query_param('TransProtocol',TransProtocol)

	def get_Ipv6TranslatorId(self):
		return self.get_query_params().get('Ipv6TranslatorId')

	def set_Ipv6TranslatorId(self,Ipv6TranslatorId):
		self.add_query_param('Ipv6TranslatorId',Ipv6TranslatorId)