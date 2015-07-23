# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class AddTagsToResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'AddTagsToResource')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_proxyId(self):
		return self.get_query_params().get('proxyId')

	def set_proxyId(self,proxyId):
		self.add_query_param('proxyId',proxyId)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_Tag1key(self):
		return self.get_query_params().get('Tag1key')

	def set_Tag1key(self,Tag1key):
		self.add_query_param('Tag1key',Tag1key)

	def get_Tag2key(self):
		return self.get_query_params().get('Tag2key')

	def set_Tag2key(self,Tag2key):
		self.add_query_param('Tag2key',Tag2key)

	def get_Tag3key(self):
		return self.get_query_params().get('Tag3key')

	def set_Tag3key(self,Tag3key):
		self.add_query_param('Tag3key',Tag3key)

	def get_Tag4key(self):
		return self.get_query_params().get('Tag4key')

	def set_Tag4key(self,Tag4key):
		self.add_query_param('Tag4key',Tag4key)

	def get_Tag5key(self):
		return self.get_query_params().get('Tag5key')

	def set_Tag5key(self,Tag5key):
		self.add_query_param('Tag5key',Tag5key)

	def get_Tag1value(self):
		return self.get_query_params().get('Tag1value')

	def set_Tag1value(self,Tag1value):
		self.add_query_param('Tag1value',Tag1value)

	def get_Tag2value(self):
		return self.get_query_params().get('Tag2value')

	def set_Tag2value(self,Tag2value):
		self.add_query_param('Tag2value',Tag2value)

	def get_Tag3value(self):
		return self.get_query_params().get('Tag3value')

	def set_Tag3value(self,Tag3value):
		self.add_query_param('Tag3value',Tag3value)

	def get_Tag4value(self):
		return self.get_query_params().get('Tag4value')

	def set_Tag4value(self,Tag4value):
		self.add_query_param('Tag4value',Tag4value)

	def get_Tag5value(self):
		return self.get_query_params().get('Tag5value')

	def set_Tag5value(self,Tag5value):
		self.add_query_param('Tag5value',Tag5value)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)