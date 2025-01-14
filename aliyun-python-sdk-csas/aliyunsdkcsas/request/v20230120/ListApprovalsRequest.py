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

class ListApprovalsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListApprovals')
		self.set_method('GET')

	def get_SchemaId(self): # String
		return self.get_query_params().get('SchemaId')

	def set_SchemaId(self, SchemaId):  # String
		self.add_query_param('SchemaId', SchemaId)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_CreateEndTime(self): # Long
		return self.get_query_params().get('CreateEndTime')

	def set_CreateEndTime(self, CreateEndTime):  # Long
		self.add_query_param('CreateEndTime', CreateEndTime)
	def get_OperatorUserId(self): # String
		return self.get_query_params().get('OperatorUserId')

	def set_OperatorUserId(self, OperatorUserId):  # String
		self.add_query_param('OperatorUserId', OperatorUserId)
	def get_SchemaName(self): # String
		return self.get_query_params().get('SchemaName')

	def set_SchemaName(self, SchemaName):  # String
		self.add_query_param('SchemaName', SchemaName)
	def get_PolicyType(self): # String
		return self.get_query_params().get('PolicyType')

	def set_PolicyType(self, PolicyType):  # String
		self.add_query_param('PolicyType', PolicyType)
	def get_ProcessName(self): # String
		return self.get_query_params().get('ProcessName')

	def set_ProcessName(self, ProcessName):  # String
		self.add_query_param('ProcessName', ProcessName)
	def get_CurrentPage(self): # Long
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Long
		self.add_query_param('CurrentPage', CurrentPage)
	def get_ApprovalIds(self): # Array
		return self.get_query_params().get('ApprovalIds')

	def set_ApprovalIds(self, ApprovalIds):  # Array
		for index1, value1 in enumerate(ApprovalIds):
			self.add_query_param('ApprovalIds.' + str(index1 + 1), value1)
	def get_CreateStartTime(self): # Long
		return self.get_query_params().get('CreateStartTime')

	def set_CreateStartTime(self, CreateStartTime):  # Long
		self.add_query_param('CreateStartTime', CreateStartTime)
	def get_ProcessId(self): # String
		return self.get_query_params().get('ProcessId')

	def set_ProcessId(self, ProcessId):  # String
		self.add_query_param('ProcessId', ProcessId)
	def get_CreatorDepartment(self): # String
		return self.get_query_params().get('CreatorDepartment')

	def set_CreatorDepartment(self, CreatorDepartment):  # String
		self.add_query_param('CreatorDepartment', CreatorDepartment)
	def get_OperatorUsername(self): # String
		return self.get_query_params().get('OperatorUsername')

	def set_OperatorUsername(self, OperatorUsername):  # String
		self.add_query_param('OperatorUsername', OperatorUsername)
	def get_CreatorUserId(self): # String
		return self.get_query_params().get('CreatorUserId')

	def set_CreatorUserId(self, CreatorUserId):  # String
		self.add_query_param('CreatorUserId', CreatorUserId)
	def get_CreatorUsername(self): # String
		return self.get_query_params().get('CreatorUsername')

	def set_CreatorUsername(self, CreatorUsername):  # String
		self.add_query_param('CreatorUsername', CreatorUsername)
	def get_Statuses(self): # Array
		return self.get_query_params().get('Statuses')

	def set_Statuses(self, Statuses):  # Array
		for index1, value1 in enumerate(Statuses):
			self.add_query_param('Statuses.' + str(index1 + 1), value1)
	def get_CreatorDevTag(self): # String
		return self.get_query_params().get('CreatorDevTag')

	def set_CreatorDevTag(self, CreatorDevTag):  # String
		self.add_query_param('CreatorDevTag', CreatorDevTag)
