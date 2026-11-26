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

class CreateDatabaseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'CreateDatabase','GPDB')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_Owner(self): # String
		return self.get_query_params().get('Owner')

	def set_Owner(self, Owner):  # String
		self.add_query_param('Owner', Owner)
	def get_Collate(self): # String
		return self.get_query_params().get('Collate')

	def set_Collate(self, Collate):  # String
		self.add_query_param('Collate', Collate)
	def get_Ctype(self): # String
		return self.get_query_params().get('Ctype')

	def set_Ctype(self, Ctype):  # String
		self.add_query_param('Ctype', Ctype)
	def get_DatabaseName(self): # String
		return self.get_query_params().get('DatabaseName')

	def set_DatabaseName(self, DatabaseName):  # String
		self.add_query_param('DatabaseName', DatabaseName)
	def get_CharacterSetName(self): # String
		return self.get_query_params().get('CharacterSetName')

	def set_CharacterSetName(self, CharacterSetName):  # String
		self.add_query_param('CharacterSetName', CharacterSetName)
