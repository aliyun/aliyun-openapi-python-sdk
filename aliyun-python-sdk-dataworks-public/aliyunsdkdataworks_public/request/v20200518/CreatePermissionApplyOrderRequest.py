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

class CreatePermissionApplyOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreatePermissionApplyOrder')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ApplyReason(self): # String
		return self.get_query_params().get('ApplyReason')

	def set_ApplyReason(self, ApplyReason):  # String
		self.add_query_param('ApplyReason', ApplyReason)
	def get_MaxComputeProjectName(self): # String
		return self.get_query_params().get('MaxComputeProjectName')

	def set_MaxComputeProjectName(self, MaxComputeProjectName):  # String
		self.add_query_param('MaxComputeProjectName', MaxComputeProjectName)
	def get_ApplyObjects(self): # RepeatList
		return self.get_query_params().get('ApplyObject')

	def set_ApplyObjects(self, ApplyObject):  # RepeatList
		for depth1 in range(len(ApplyObject)):
			if ApplyObject[depth1].get('ColumnMetaList') is not None:
				for depth2 in range(len(ApplyObject[depth1].get('ColumnMetaList'))):
					if ApplyObject[depth1].get('ColumnMetaList')[depth2].get('Name') is not None:
						self.add_query_param('ApplyObject.' + str(depth1 + 1) + '.ColumnMetaList.'  + str(depth2 + 1) + '.Name', ApplyObject[depth1].get('ColumnMetaList')[depth2].get('Name'))
			if ApplyObject[depth1].get('Name') is not None:
				self.add_query_param('ApplyObject.' + str(depth1 + 1) + '.Name', ApplyObject[depth1].get('Name'))
			if ApplyObject[depth1].get('Actions') is not None:
				self.add_query_param('ApplyObject.' + str(depth1 + 1) + '.Actions', ApplyObject[depth1].get('Actions'))
	def get_ApplyUserIds(self): # String
		return self.get_query_params().get('ApplyUserIds')

	def set_ApplyUserIds(self, ApplyUserIds):  # String
		self.add_query_param('ApplyUserIds', ApplyUserIds)
	def get_Deadline(self): # Long
		return self.get_query_params().get('Deadline')

	def set_Deadline(self, Deadline):  # Long
		self.add_query_param('Deadline', Deadline)
	def get_WorkspaceId(self): # Integer
		return self.get_query_params().get('WorkspaceId')

	def set_WorkspaceId(self, WorkspaceId):  # Integer
		self.add_query_param('WorkspaceId', WorkspaceId)
	def get_OrderType(self): # Integer
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # Integer
		self.add_query_param('OrderType', OrderType)
	def get_EngineType(self): # String
		return self.get_query_params().get('EngineType')

	def set_EngineType(self, EngineType):  # String
		self.add_query_param('EngineType', EngineType)
