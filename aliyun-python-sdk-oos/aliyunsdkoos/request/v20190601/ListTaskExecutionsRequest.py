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

class ListTaskExecutionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'ListTaskExecutions','oos')

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_IncludeChildTaskExecution(self):
		return self.get_query_params().get('IncludeChildTaskExecution')

	def set_IncludeChildTaskExecution(self,IncludeChildTaskExecution):
		self.add_query_param('IncludeChildTaskExecution',IncludeChildTaskExecution)

	def get_ExecutionId(self):
		return self.get_query_params().get('ExecutionId')

	def set_ExecutionId(self,ExecutionId):
		self.add_query_param('ExecutionId',ExecutionId)

	def get_ParentTaskExecutionId(self):
		return self.get_query_params().get('ParentTaskExecutionId')

	def set_ParentTaskExecutionId(self,ParentTaskExecutionId):
		self.add_query_param('ParentTaskExecutionId',ParentTaskExecutionId)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_EndDateBefore(self):
		return self.get_query_params().get('EndDateBefore')

	def set_EndDateBefore(self,EndDateBefore):
		self.add_query_param('EndDateBefore',EndDateBefore)

	def get_SortOrder(self):
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self,SortOrder):
		self.add_query_param('SortOrder',SortOrder)

	def get_StartDateAfter(self):
		return self.get_query_params().get('StartDateAfter')

	def set_StartDateAfter(self,StartDateAfter):
		self.add_query_param('StartDateAfter',StartDateAfter)

	def get_StartDateBefore(self):
		return self.get_query_params().get('StartDateBefore')

	def set_StartDateBefore(self,StartDateBefore):
		self.add_query_param('StartDateBefore',StartDateBefore)

	def get_EndDateAfter(self):
		return self.get_query_params().get('EndDateAfter')

	def set_EndDateAfter(self,EndDateAfter):
		self.add_query_param('EndDateAfter',EndDateAfter)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_TaskExecutionId(self):
		return self.get_query_params().get('TaskExecutionId')

	def set_TaskExecutionId(self,TaskExecutionId):
		self.add_query_param('TaskExecutionId',TaskExecutionId)

	def get_SortField(self):
		return self.get_query_params().get('SortField')

	def set_SortField(self,SortField):
		self.add_query_param('SortField',SortField)

	def get_TaskAction(self):
		return self.get_query_params().get('TaskAction')

	def set_TaskAction(self,TaskAction):
		self.add_query_param('TaskAction',TaskAction)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)