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

class CreateDatasetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'CreateDataset','2.2.0')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_DsId(self): # String
		return self.get_query_params().get('DsId')

	def set_DsId(self, DsId):  # String
		self.add_query_param('DsId', DsId)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
	def get_TargetDirectoryId(self): # String
		return self.get_query_params().get('TargetDirectoryId')

	def set_TargetDirectoryId(self, TargetDirectoryId):  # String
		self.add_query_param('TargetDirectoryId', TargetDirectoryId)
	def get_UserDefineCubeName(self): # String
		return self.get_query_params().get('UserDefineCubeName')

	def set_UserDefineCubeName(self, UserDefineCubeName):  # String
		self.add_query_param('UserDefineCubeName', UserDefineCubeName)
	def get_WorkspaceId(self): # String
		return self.get_query_params().get('WorkspaceId')

	def set_WorkspaceId(self, WorkspaceId):  # String
		self.add_query_param('WorkspaceId', WorkspaceId)
