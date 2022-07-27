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

class ModifyVpcPrefixListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyVpcPrefixList','vpc')
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
	def get_MaxEntries(self): # Integer
		return self.get_query_params().get('MaxEntries')

	def set_MaxEntries(self, MaxEntries):  # Integer
		self.add_query_param('MaxEntries', MaxEntries)
	def get_RemovePrefixListEntrys(self): # RepeatList
		return self.get_query_params().get('RemovePrefixListEntry')

	def set_RemovePrefixListEntrys(self, RemovePrefixListEntry):  # RepeatList
		for depth1 in range(len(RemovePrefixListEntry)):
			if RemovePrefixListEntry[depth1].get('Cidr') is not None:
				self.add_query_param('RemovePrefixListEntry.' + str(depth1 + 1) + '.Cidr', RemovePrefixListEntry[depth1].get('Cidr'))
			if RemovePrefixListEntry[depth1].get('Description') is not None:
				self.add_query_param('RemovePrefixListEntry.' + str(depth1 + 1) + '.Description', RemovePrefixListEntry[depth1].get('Description'))
	def get_PrefixListId(self): # String
		return self.get_query_params().get('PrefixListId')

	def set_PrefixListId(self, PrefixListId):  # String
		self.add_query_param('PrefixListId', PrefixListId)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
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
	def get_AddPrefixListEntrys(self): # RepeatList
		return self.get_query_params().get('AddPrefixListEntry')

	def set_AddPrefixListEntrys(self, AddPrefixListEntry):  # RepeatList
		for depth1 in range(len(AddPrefixListEntry)):
			if AddPrefixListEntry[depth1].get('Cidr') is not None:
				self.add_query_param('AddPrefixListEntry.' + str(depth1 + 1) + '.Cidr', AddPrefixListEntry[depth1].get('Cidr'))
			if AddPrefixListEntry[depth1].get('Description') is not None:
				self.add_query_param('AddPrefixListEntry.' + str(depth1 + 1) + '.Description', AddPrefixListEntry[depth1].get('Description'))
	def get_PrefixListName(self): # String
		return self.get_query_params().get('PrefixListName')

	def set_PrefixListName(self, PrefixListName):  # String
		self.add_query_param('PrefixListName', PrefixListName)
	def get_PrefixListDescription(self): # String
		return self.get_query_params().get('PrefixListDescription')

	def set_PrefixListDescription(self, PrefixListDescription):  # String
		self.add_query_param('PrefixListDescription', PrefixListDescription)
