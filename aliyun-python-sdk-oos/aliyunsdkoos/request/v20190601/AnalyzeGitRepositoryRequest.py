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
from aliyunsdkoos.endpoint import endpoint_data

class AnalyzeGitRepositoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'AnalyzeGitRepository','oos')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RepoId(self): # String
		return self.get_query_params().get('RepoId')

	def set_RepoId(self, RepoId):  # String
		self.add_query_param('RepoId', RepoId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_RepoFullName(self): # String
		return self.get_query_params().get('RepoFullName')

	def set_RepoFullName(self, RepoFullName):  # String
		self.add_query_param('RepoFullName', RepoFullName)
	def get_Branch(self): # String
		return self.get_query_params().get('Branch')

	def set_Branch(self, Branch):  # String
		self.add_query_param('Branch', Branch)
	def get_Platform(self): # String
		return self.get_query_params().get('Platform')

	def set_Platform(self, Platform):  # String
		self.add_query_param('Platform', Platform)
	def get_Owner(self): # String
		return self.get_query_params().get('Owner')

	def set_Owner(self, Owner):  # String
		self.add_query_param('Owner', Owner)
	def get_OrgId(self): # String
		return self.get_query_params().get('OrgId')

	def set_OrgId(self, OrgId):  # String
		self.add_query_param('OrgId', OrgId)
