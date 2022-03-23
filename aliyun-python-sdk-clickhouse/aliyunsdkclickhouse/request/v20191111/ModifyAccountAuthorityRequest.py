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
from aliyunsdkclickhouse.endpoint import endpoint_data

class ModifyAccountAuthorityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'clickhouse', '2019-11-11', 'ModifyAccountAuthority')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_TotalDictionaries(self): # String
		return self.get_query_params().get('TotalDictionaries')

	def set_TotalDictionaries(self, TotalDictionaries):  # String
		self.add_query_param('TotalDictionaries', TotalDictionaries)
	def get_AccountName(self): # String
		return self.get_query_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_query_param('AccountName', AccountName)
	def get_DmlAuthority(self): # String
		return self.get_query_params().get('DmlAuthority')

	def set_DmlAuthority(self, DmlAuthority):  # String
		self.add_query_param('DmlAuthority', DmlAuthority)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_AllowDatabases(self): # String
		return self.get_query_params().get('AllowDatabases')

	def set_AllowDatabases(self, AllowDatabases):  # String
		self.add_query_param('AllowDatabases', AllowDatabases)
	def get_AllowDictionaries(self): # String
		return self.get_query_params().get('AllowDictionaries')

	def set_AllowDictionaries(self, AllowDictionaries):  # String
		self.add_query_param('AllowDictionaries', AllowDictionaries)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_DdlAuthority(self): # Boolean
		return self.get_query_params().get('DdlAuthority')

	def set_DdlAuthority(self, DdlAuthority):  # Boolean
		self.add_query_param('DdlAuthority', DdlAuthority)
	def get_TotalDatabases(self): # String
		return self.get_query_params().get('TotalDatabases')

	def set_TotalDatabases(self, TotalDatabases):  # String
		self.add_query_param('TotalDatabases', TotalDatabases)
