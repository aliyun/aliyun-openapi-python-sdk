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

class CreatePrefixListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreatePrefixList','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_MaxEntries(self):
		return self.get_query_params().get('MaxEntries')

	def set_MaxEntries(self,MaxEntries):
		self.add_query_param('MaxEntries',MaxEntries)

	def get_AddressFamily(self):
		return self.get_query_params().get('AddressFamily')

	def set_AddressFamily(self,AddressFamily):
		self.add_query_param('AddressFamily',AddressFamily)

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

	def get_PrefixListName(self):
		return self.get_query_params().get('PrefixListName')

	def set_PrefixListName(self,PrefixListName):
		self.add_query_param('PrefixListName',PrefixListName)

	def get_Entrys(self):
		return self.get_query_params().get('Entry')

	def set_Entrys(self, Entrys):
		for depth1 in range(len(Entrys)):
			if Entrys[depth1].get('Cidr') is not None:
				self.add_query_param('Entry.' + str(depth1 + 1) + '.Cidr', Entrys[depth1].get('Cidr'))
			if Entrys[depth1].get('Description') is not None:
				self.add_query_param('Entry.' + str(depth1 + 1) + '.Description', Entrys[depth1].get('Description'))