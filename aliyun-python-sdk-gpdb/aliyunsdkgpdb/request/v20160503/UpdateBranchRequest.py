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

class UpdateBranchRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'UpdateBranch','GPDB')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BranchId(self): # String
		return self.get_query_params().get('BranchId')

	def set_BranchId(self, BranchId):  # String
		self.add_query_param('BranchId', BranchId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_ExpiresAt(self): # String
		return self.get_query_params().get('ExpiresAt')

	def set_ExpiresAt(self, ExpiresAt):  # String
		self.add_query_param('ExpiresAt', ExpiresAt)
	def get_Protected(self): # Boolean
		return self.get_query_params().get('Protected')

	def set_Protected(self, Protected):  # Boolean
		self.add_query_param('Protected', Protected)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_ProjectId(self): # String
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # String
		self.add_query_param('ProjectId', ProjectId)
	def get_ClearExpiresAt(self): # Boolean
		return self.get_query_params().get('ClearExpiresAt')

	def set_ClearExpiresAt(self, ClearExpiresAt):  # Boolean
		self.add_query_param('ClearExpiresAt', ClearExpiresAt)
	def get_BranchName(self): # String
		return self.get_query_params().get('BranchName')

	def set_BranchName(self, BranchName):  # String
		self.add_query_param('BranchName', BranchName)
