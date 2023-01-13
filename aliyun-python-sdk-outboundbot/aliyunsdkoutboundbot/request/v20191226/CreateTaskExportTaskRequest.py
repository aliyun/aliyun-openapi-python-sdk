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
from aliyunsdkoutboundbot.endpoint import endpoint_data

class CreateTaskExportTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'CreateTaskExportTask')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_HasAnswered(self): # Boolean
		return self.get_query_params().get('HasAnswered')

	def set_HasAnswered(self, HasAnswered):  # Boolean
		self.add_query_param('HasAnswered', HasAnswered)
	def get_ActualTimeLte(self): # Long
		return self.get_query_params().get('ActualTimeLte')

	def set_ActualTimeLte(self, ActualTimeLte):  # Long
		self.add_query_param('ActualTimeLte', ActualTimeLte)
	def get_OtherId(self): # String
		return self.get_query_params().get('OtherId')

	def set_OtherId(self, OtherId):  # String
		self.add_query_param('OtherId', OtherId)
	def get_TaskCreateTimeLte(self): # Long
		return self.get_query_params().get('TaskCreateTimeLte')

	def set_TaskCreateTimeLte(self, TaskCreateTimeLte):  # Long
		self.add_query_param('TaskCreateTimeLte', TaskCreateTimeLte)
	def get_JobId(self): # String
		return self.get_query_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_query_param('JobId', JobId)
	def get_TaskCreateTimeGte(self): # Long
		return self.get_query_params().get('TaskCreateTimeGte')

	def set_TaskCreateTimeGte(self, TaskCreateTimeGte):  # Long
		self.add_query_param('TaskCreateTimeGte', TaskCreateTimeGte)
	def get_CalledNumber(self): # String
		return self.get_query_params().get('CalledNumber')

	def set_CalledNumber(self, CalledNumber):  # String
		self.add_query_param('CalledNumber', CalledNumber)
	def get_UserIdMatch(self): # String
		return self.get_query_params().get('UserIdMatch')

	def set_UserIdMatch(self, UserIdMatch):  # String
		self.add_query_param('UserIdMatch', UserIdMatch)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ScriptNameQuery(self): # String
		return self.get_query_params().get('ScriptNameQuery')

	def set_ScriptNameQuery(self, ScriptNameQuery):  # String
		self.add_query_param('ScriptNameQuery', ScriptNameQuery)
	def get_PageIndex(self): # Integer
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self, PageIndex):  # Integer
		self.add_query_param('PageIndex', PageIndex)
	def get_SortOrder(self): # String
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self, SortOrder):  # String
		self.add_query_param('SortOrder', SortOrder)
	def get_TaskStatusStringList(self): # String
		return self.get_query_params().get('TaskStatusStringList')

	def set_TaskStatusStringList(self, TaskStatusStringList):  # String
		self.add_query_param('TaskStatusStringList', TaskStatusStringList)
	def get_JobGroupNameQuery(self): # String
		return self.get_query_params().get('JobGroupNameQuery')

	def set_JobGroupNameQuery(self, JobGroupNameQuery):  # String
		self.add_query_param('JobGroupNameQuery', JobGroupNameQuery)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_HasHangUpByRejection(self): # Boolean
		return self.get_query_params().get('HasHangUpByRejection')

	def set_HasHangUpByRejection(self, HasHangUpByRejection):  # Boolean
		self.add_query_param('HasHangUpByRejection', HasHangUpByRejection)
	def get_HasReachedEndOfFlow(self): # Boolean
		return self.get_query_params().get('HasReachedEndOfFlow')

	def set_HasReachedEndOfFlow(self, HasReachedEndOfFlow):  # Boolean
		self.add_query_param('HasReachedEndOfFlow', HasReachedEndOfFlow)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_RecordingDurationGte(self): # Long
		return self.get_query_params().get('RecordingDurationGte')

	def set_RecordingDurationGte(self, RecordingDurationGte):  # Long
		self.add_query_param('RecordingDurationGte', RecordingDurationGte)
	def get_CallDurationLte(self): # Long
		return self.get_query_params().get('CallDurationLte')

	def set_CallDurationLte(self, CallDurationLte):  # Long
		self.add_query_param('CallDurationLte', CallDurationLte)
	def get_JobGroupId(self): # String
		return self.get_query_params().get('JobGroupId')

	def set_JobGroupId(self, JobGroupId):  # String
		self.add_query_param('JobGroupId', JobGroupId)
	def get_SortBy(self): # String
		return self.get_query_params().get('SortBy')

	def set_SortBy(self, SortBy):  # String
		self.add_query_param('SortBy', SortBy)
	def get_JobStatusStringList(self): # String
		return self.get_query_params().get('JobStatusStringList')

	def set_JobStatusStringList(self, JobStatusStringList):  # String
		self.add_query_param('JobStatusStringList', JobStatusStringList)
	def get_ActualTimeGte(self): # Long
		return self.get_query_params().get('ActualTimeGte')

	def set_ActualTimeGte(self, ActualTimeGte):  # Long
		self.add_query_param('ActualTimeGte', ActualTimeGte)
	def get_CallDurationGte(self): # Long
		return self.get_query_params().get('CallDurationGte')

	def set_CallDurationGte(self, CallDurationGte):  # Long
		self.add_query_param('CallDurationGte', CallDurationGte)
	def get_RecordingDurationLte(self): # Long
		return self.get_query_params().get('RecordingDurationLte')

	def set_RecordingDurationLte(self, RecordingDurationLte):  # Long
		self.add_query_param('RecordingDurationLte', RecordingDurationLte)
