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
from aliyunsdkrds.endpoint import endpoint_data

class RemoveTagsFromResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'RemoveTagsFromResource')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Tag4value(self): # String
		return self.get_query_params().get('Tag.4.value')

	def set_Tag4value(self, Tag4value):  # String
		self.add_query_param('Tag.4.value', Tag4value)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Tag2key(self): # String
		return self.get_query_params().get('Tag.2.key')

	def set_Tag2key(self, Tag2key):  # String
		self.add_query_param('Tag.2.key', Tag2key)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Tag3key(self): # String
		return self.get_query_params().get('Tag.3.key')

	def set_Tag3key(self, Tag3key):  # String
		self.add_query_param('Tag.3.key', Tag3key)
	def get_Tag1value(self): # String
		return self.get_query_params().get('Tag.1.value')

	def set_Tag1value(self, Tag1value):  # String
		self.add_query_param('Tag.1.value', Tag1value)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_Tag3value(self): # String
		return self.get_query_params().get('Tag.3.value')

	def set_Tag3value(self, Tag3value):  # String
		self.add_query_param('Tag.3.value', Tag3value)
	def get_proxyId(self): # String
		return self.get_query_params().get('proxyId')

	def set_proxyId(self, proxyId):  # String
		self.add_query_param('proxyId', proxyId)
	def get_Tag5key(self): # String
		return self.get_query_params().get('Tag.5.key')

	def set_Tag5key(self, Tag5key):  # String
		self.add_query_param('Tag.5.key', Tag5key)
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
	def get_Tag5value(self): # String
		return self.get_query_params().get('Tag.5.value')

	def set_Tag5value(self, Tag5value):  # String
		self.add_query_param('Tag.5.value', Tag5value)
	def get_Tags(self): # String
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # String
		self.add_query_param('Tags', Tags)
	def get_Tag1key(self): # String
		return self.get_query_params().get('Tag.1.key')

	def set_Tag1key(self, Tag1key):  # String
		self.add_query_param('Tag.1.key', Tag1key)
	def get_Tag2value(self): # String
		return self.get_query_params().get('Tag.2.value')

	def set_Tag2value(self, Tag2value):  # String
		self.add_query_param('Tag.2.value', Tag2value)
	def get_Tag4key(self): # String
		return self.get_query_params().get('Tag.4.key')

	def set_Tag4key(self, Tag4key):  # String
		self.add_query_param('Tag.4.key', Tag4key)
