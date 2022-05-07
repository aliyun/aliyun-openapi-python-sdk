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

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_EgressAclEntriess(self): # RepeatList
		return self.get_query_params().get('EgressAclEntries')

	def set_EgressAclEntriess(self, EgressAclEntries):  # RepeatList
		for depth1 in range(len(EgressAclEntries)):
			if EgressAclEntries[depth1].get('NetworkAclEntryId') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.NetworkAclEntryId', EgressAclEntries[depth1].get('NetworkAclEntryId'))
			if EgressAclEntries[depth1].get('EntryType') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.EntryType', EgressAclEntries[depth1].get('EntryType'))
			if EgressAclEntries[depth1].get('NetworkAclEntryName') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.NetworkAclEntryName', EgressAclEntries[depth1].get('NetworkAclEntryName'))
			if EgressAclEntries[depth1].get('Policy') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.Policy', EgressAclEntries[depth1].get('Policy'))
			if EgressAclEntries[depth1].get('Description') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.Description', EgressAclEntries[depth1].get('Description'))
			if EgressAclEntries[depth1].get('Protocol') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.Protocol', EgressAclEntries[depth1].get('Protocol'))
			if EgressAclEntries[depth1].get('DestinationCidrIp') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.DestinationCidrIp', EgressAclEntries[depth1].get('DestinationCidrIp'))
			if EgressAclEntries[depth1].get('Port') is not None:
				self.add_query_param('EgressAclEntries.' + str(depth1 + 1) + '.Port', EgressAclEntries[depth1].get('Port'))
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_NetworkAclId(self): # String
		return self.get_query_params().get('NetworkAclId')

	def set_NetworkAclId(self, NetworkAclId):  # String
		self.add_query_param('NetworkAclId', NetworkAclId)
	def get_UpdateIngressAclEntries(self): # Boolean
		return self.get_query_params().get('UpdateIngressAclEntries')

	def set_UpdateIngressAclEntries(self, UpdateIngressAclEntries):  # Boolean
		self.add_query_param('UpdateIngressAclEntries', UpdateIngressAclEntries)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_UpdateEgressAclEntries(self): # Boolean
		return self.get_query_params().get('UpdateEgressAclEntries')

	def set_UpdateEgressAclEntries(self, UpdateEgressAclEntries):  # Boolean
		self.add_query_param('UpdateEgressAclEntries', UpdateEgressAclEntries)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_IngressAclEntriess(self): # RepeatList
		return self.get_query_params().get('IngressAclEntries')

	def set_IngressAclEntriess(self, IngressAclEntries):  # RepeatList
		for depth1 in range(len(IngressAclEntries)):
			if IngressAclEntries[depth1].get('NetworkAclEntryId') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.NetworkAclEntryId', IngressAclEntries[depth1].get('NetworkAclEntryId'))
			if IngressAclEntries[depth1].get('EntryType') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.EntryType', IngressAclEntries[depth1].get('EntryType'))
			if IngressAclEntries[depth1].get('NetworkAclEntryName') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.NetworkAclEntryName', IngressAclEntries[depth1].get('NetworkAclEntryName'))
			if IngressAclEntries[depth1].get('Policy') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.Policy', IngressAclEntries[depth1].get('Policy'))
			if IngressAclEntries[depth1].get('SourceCidrIp') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.SourceCidrIp', IngressAclEntries[depth1].get('SourceCidrIp'))
			if IngressAclEntries[depth1].get('Description') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.Description', IngressAclEntries[depth1].get('Description'))
			if IngressAclEntries[depth1].get('Protocol') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.Protocol', IngressAclEntries[depth1].get('Protocol'))
			if IngressAclEntries[depth1].get('Port') is not None:
				self.add_query_param('IngressAclEntries.' + str(depth1 + 1) + '.Port', IngressAclEntries[depth1].get('Port'))
