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

class QueryAuditLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'QueryAuditLog','2.2.0')
		self.set_method('POST')

	def get_AccessSourceFlag(self): # String
		return self.get_query_params().get('AccessSourceFlag')

	def set_AccessSourceFlag(self, AccessSourceFlag):  # String
		self.add_query_param('AccessSourceFlag', AccessSourceFlag)
	def get_StartDate(self): # String
		return self.get_query_params().get('StartDate')

	def set_StartDate(self, StartDate):  # String
		self.add_query_param('StartDate', StartDate)
	def get_LogType(self): # String
		return self.get_query_params().get('LogType')

	def set_LogType(self, LogType):  # String
		self.add_query_param('LogType', LogType)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_OperatorTypes(self): # String
		return self.get_query_params().get('OperatorTypes')

	def set_OperatorTypes(self, OperatorTypes):  # String
		self.add_query_param('OperatorTypes', OperatorTypes)
	def get_EndDate(self): # String
		return self.get_query_params().get('EndDate')

	def set_EndDate(self, EndDate):  # String
		self.add_query_param('EndDate', EndDate)
	def get_OperatorId(self): # String
		return self.get_query_params().get('OperatorId')

	def set_OperatorId(self, OperatorId):  # String
		self.add_query_param('OperatorId', OperatorId)
	def get_WorkspaceId(self): # String
		return self.get_query_params().get('WorkspaceId')

	def set_WorkspaceId(self, WorkspaceId):  # String
		self.add_query_param('WorkspaceId', WorkspaceId)
	def get_UserAccessDevice(self): # String
		return self.get_query_params().get('UserAccessDevice')

	def set_UserAccessDevice(self, UserAccessDevice):  # String
		self.add_query_param('UserAccessDevice', UserAccessDevice)
