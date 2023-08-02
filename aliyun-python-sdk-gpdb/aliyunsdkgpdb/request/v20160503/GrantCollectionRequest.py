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
from aliyunsdkgpdb.endpoint import endpoint_data

class GrantCollectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'GrantCollection')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_GrantType(self): # String
		return self.get_query_params().get('GrantType')

	def set_GrantType(self, GrantType):  # String
		self.add_query_param('GrantType', GrantType)
	def get_ManagerAccount(self): # String
		return self.get_query_params().get('ManagerAccount')

	def set_ManagerAccount(self, ManagerAccount):  # String
		self.add_query_param('ManagerAccount', ManagerAccount)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_ManagerAccountPassword(self): # String
		return self.get_query_params().get('ManagerAccountPassword')

	def set_ManagerAccountPassword(self, ManagerAccountPassword):  # String
		self.add_query_param('ManagerAccountPassword', ManagerAccountPassword)
	def get_Collection(self): # String
		return self.get_query_params().get('Collection')

	def set_Collection(self, Collection):  # String
		self.add_query_param('Collection', Collection)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_GrantToNamespace(self): # String
		return self.get_query_params().get('GrantToNamespace')

	def set_GrantToNamespace(self, GrantToNamespace):  # String
		self.add_query_param('GrantToNamespace', GrantToNamespace)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
