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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class RevokeColumnPermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'RevokeColumnPermission')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RevokeUserName(self):
		return self.get_query_params().get('RevokeUserName')

	def set_RevokeUserName(self,RevokeUserName):
		self.add_query_param('RevokeUserName',RevokeUserName)

	def get_MaxComputeProjectName(self):
		return self.get_query_params().get('MaxComputeProjectName')

	def set_MaxComputeProjectName(self,MaxComputeProjectName):
		self.add_query_param('MaxComputeProjectName',MaxComputeProjectName)

	def get_Columns(self):
		return self.get_query_params().get('Columns')

	def set_Columns(self,Columns):
		self.add_query_param('Columns',Columns)

	def get_RevokeUserId(self):
		return self.get_query_params().get('RevokeUserId')

	def set_RevokeUserId(self,RevokeUserId):
		self.add_query_param('RevokeUserId',RevokeUserId)

	def get_TableName(self):
		return self.get_query_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_query_param('TableName',TableName)

	def get_WorkspaceId(self):
		return self.get_query_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_query_param('WorkspaceId',WorkspaceId)