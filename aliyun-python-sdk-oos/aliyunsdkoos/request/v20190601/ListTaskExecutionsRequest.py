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

class ListTaskExecutionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'ListTaskExecutions','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_IncludeChildTaskExecution(self): # Boolean
		return self.get_query_params().get('IncludeChildTaskExecution')

	def set_IncludeChildTaskExecution(self, IncludeChildTaskExecution):  # Boolean
		self.add_query_param('IncludeChildTaskExecution', IncludeChildTaskExecution)
	def get_ExecutionId(self): # String
		return self.get_query_params().get('ExecutionId')

	def set_ExecutionId(self, ExecutionId):  # String
		self.add_query_param('ExecutionId', ExecutionId)
	def get_ParentTaskExecutionId(self): # String
		return self.get_query_params().get('ParentTaskExecutionId')

	def set_ParentTaskExecutionId(self, ParentTaskExecutionId):  # String
		self.add_query_param('ParentTaskExecutionId', ParentTaskExecutionId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_EndDateBefore(self): # String
		return self.get_query_params().get('EndDateBefore')

	def set_EndDateBefore(self, EndDateBefore):  # String
		self.add_query_param('EndDateBefore', EndDateBefore)
	def get_SortOrder(self): # String
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self, SortOrder):  # String
		self.add_query_param('SortOrder', SortOrder)
	def get_StartDateAfter(self): # String
		return self.get_query_params().get('StartDateAfter')

	def set_StartDateAfter(self, StartDateAfter):  # String
		self.add_query_param('StartDateAfter', StartDateAfter)
	def get_StartDateBefore(self): # String
		return self.get_query_params().get('StartDateBefore')

	def set_StartDateBefore(self, StartDateBefore):  # String
		self.add_query_param('StartDateBefore', StartDateBefore)
	def get_EndDateAfter(self): # String
		return self.get_query_params().get('EndDateAfter')

	def set_EndDateAfter(self, EndDateAfter):  # String
		self.add_query_param('EndDateAfter', EndDateAfter)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_TaskExecutionId(self): # String
		return self.get_query_params().get('TaskExecutionId')

	def set_TaskExecutionId(self, TaskExecutionId):  # String
		self.add_query_param('TaskExecutionId', TaskExecutionId)
	def get_SortField(self): # String
		return self.get_query_params().get('SortField')

	def set_SortField(self, SortField):  # String
		self.add_query_param('SortField', SortField)
	def get_TaskAction(self): # String
		return self.get_query_params().get('TaskAction')

	def set_TaskAction(self, TaskAction):  # String
		self.add_query_param('TaskAction', TaskAction)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
