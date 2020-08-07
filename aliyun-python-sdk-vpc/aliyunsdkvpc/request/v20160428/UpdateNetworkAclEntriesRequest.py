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

class UpdateNetworkAclEntriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'UpdateNetworkAclEntries','vpc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_EgressAclEntriess(self):
		return self.get_query_params().get('EgressAclEntriess')

	def set_EgressAclEntriess(self, EgressAclEntriess):
		for depth1 in range(len(EgressAclEntriess)):
			if EgressAclEntriess[depth1].get('NetworkAclEntryName') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.NetworkAclEntryName', EgressAclEntriess[depth1].get('NetworkAclEntryName'))
			if EgressAclEntriess[depth1].get('NetworkAclEntryId') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.NetworkAclEntryId', EgressAclEntriess[depth1].get('NetworkAclEntryId'))
			if EgressAclEntriess[depth1].get('Policy') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.Policy', EgressAclEntriess[depth1].get('Policy'))
			if EgressAclEntriess[depth1].get('Protocol') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.Protocol', EgressAclEntriess[depth1].get('Protocol'))
			if EgressAclEntriess[depth1].get('DestinationCidrIp') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.DestinationCidrIp', EgressAclEntriess[depth1].get('DestinationCidrIp'))
			if EgressAclEntriess[depth1].get('Port') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.Port', EgressAclEntriess[depth1].get('Port'))
			if EgressAclEntriess[depth1].get('EntryType') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.EntryType', EgressAclEntriess[depth1].get('EntryType'))
			if EgressAclEntriess[depth1].get('Description') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.Description', EgressAclEntriess[depth1].get('Description'))

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_NetworkAclId(self):
		return self.get_query_params().get('NetworkAclId')

	def set_NetworkAclId(self,NetworkAclId):
		self.add_query_param('NetworkAclId',NetworkAclId)

	def get_UpdateIngressAclEntries(self):
		return self.get_query_params().get('UpdateIngressAclEntries')

	def set_UpdateIngressAclEntries(self,UpdateIngressAclEntries):
		self.add_query_param('UpdateIngressAclEntries',UpdateIngressAclEntries)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_UpdateEgressAclEntries(self):
		return self.get_query_params().get('UpdateEgressAclEntries')

	def set_UpdateEgressAclEntries(self,UpdateEgressAclEntries):
		self.add_query_param('UpdateEgressAclEntries',UpdateEgressAclEntries)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_IngressAclEntriess(self):
		return self.get_query_params().get('IngressAclEntriess')

	def set_IngressAclEntriess(self, IngressAclEntriess):
		for depth1 in range(len(IngressAclEntriess)):
			if IngressAclEntriess[depth1].get('NetworkAclEntryName') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.NetworkAclEntryName', IngressAclEntriess[depth1].get('NetworkAclEntryName'))
			if IngressAclEntriess[depth1].get('NetworkAclEntryId') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.NetworkAclEntryId', IngressAclEntriess[depth1].get('NetworkAclEntryId'))
			if IngressAclEntriess[depth1].get('Policy') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.Policy', IngressAclEntriess[depth1].get('Policy'))
			if IngressAclEntriess[depth1].get('Protocol') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.Protocol', IngressAclEntriess[depth1].get('Protocol'))
			if IngressAclEntriess[depth1].get('SourceCidrIp') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.SourceCidrIp', IngressAclEntriess[depth1].get('SourceCidrIp'))
			if IngressAclEntriess[depth1].get('Port') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.Port', IngressAclEntriess[depth1].get('Port'))
			if IngressAclEntriess[depth1].get('EntryType') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.EntryType', IngressAclEntriess[depth1].get('EntryType'))
			if IngressAclEntriess[depth1].get('Description') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.Description', IngressAclEntriess[depth1].get('Description'))