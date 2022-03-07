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
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'CreateTaskExportTask','outboundbot')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HasAnswered(self):
		return self.get_query_params().get('HasAnswered')

	def set_HasAnswered(self,HasAnswered):
		self.add_query_param('HasAnswered',HasAnswered)

	def get_ActualTimeLte(self):
		return self.get_query_params().get('ActualTimeLte')

	def set_ActualTimeLte(self,ActualTimeLte):
		self.add_query_param('ActualTimeLte',ActualTimeLte)

	def get_OtherId(self):
		return self.get_query_params().get('OtherId')

	def set_OtherId(self,OtherId):
		self.add_query_param('OtherId',OtherId)

	def get_TaskCreateTimeLte(self):
		return self.get_query_params().get('TaskCreateTimeLte')

	def set_TaskCreateTimeLte(self,TaskCreateTimeLte):
		self.add_query_param('TaskCreateTimeLte',TaskCreateTimeLte)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_TaskCreateTimeGte(self):
		return self.get_query_params().get('TaskCreateTimeGte')

	def set_TaskCreateTimeGte(self,TaskCreateTimeGte):
		self.add_query_param('TaskCreateTimeGte',TaskCreateTimeGte)

	def get_CalledNumber(self):
		return self.get_query_params().get('CalledNumber')

	def set_CalledNumber(self,CalledNumber):
		self.add_query_param('CalledNumber',CalledNumber)

	def get_UserIdMatch(self):
		return self.get_query_params().get('UserIdMatch')

	def set_UserIdMatch(self,UserIdMatch):
		self.add_query_param('UserIdMatch',UserIdMatch)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ScriptNameQuery(self):
		return self.get_query_params().get('ScriptNameQuery')

	def set_ScriptNameQuery(self,ScriptNameQuery):
		self.add_query_param('ScriptNameQuery',ScriptNameQuery)

	def get_PageIndex(self):
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self,PageIndex):
		self.add_query_param('PageIndex',PageIndex)

	def get_SortOrder(self):
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self,SortOrder):
		self.add_query_param('SortOrder',SortOrder)

	def get_TaskStatusStringList(self):
		return self.get_query_params().get('TaskStatusStringList')

	def set_TaskStatusStringList(self,TaskStatusStringList):
		self.add_query_param('TaskStatusStringList',TaskStatusStringList)

	def get_JobGroupNameQuery(self):
		return self.get_query_params().get('JobGroupNameQuery')

	def set_JobGroupNameQuery(self,JobGroupNameQuery):
		self.add_query_param('JobGroupNameQuery',JobGroupNameQuery)

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)

	def get_HasHangUpByRejection(self):
		return self.get_query_params().get('HasHangUpByRejection')

	def set_HasHangUpByRejection(self,HasHangUpByRejection):
		self.add_query_param('HasHangUpByRejection',HasHangUpByRejection)

	def get_HasReachedEndOfFlow(self):
		return self.get_query_params().get('HasReachedEndOfFlow')

	def set_HasReachedEndOfFlow(self,HasReachedEndOfFlow):
		self.add_query_param('HasReachedEndOfFlow',HasReachedEndOfFlow)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_RecordingDurationGte(self):
		return self.get_query_params().get('RecordingDurationGte')

	def set_RecordingDurationGte(self,RecordingDurationGte):
		self.add_query_param('RecordingDurationGte',RecordingDurationGte)

	def get_CallDurationLte(self):
		return self.get_query_params().get('CallDurationLte')

	def set_CallDurationLte(self,CallDurationLte):
		self.add_query_param('CallDurationLte',CallDurationLte)

	def get_JobGroupId(self):
		return self.get_query_params().get('JobGroupId')

	def set_JobGroupId(self,JobGroupId):
		self.add_query_param('JobGroupId',JobGroupId)

	def get_SortBy(self):
		return self.get_query_params().get('SortBy')

	def set_SortBy(self,SortBy):
		self.add_query_param('SortBy',SortBy)

	def get_JobStatusStringList(self):
		return self.get_query_params().get('JobStatusStringList')

	def set_JobStatusStringList(self,JobStatusStringList):
		self.add_query_param('JobStatusStringList',JobStatusStringList)

	def get_ActualTimeGte(self):
		return self.get_query_params().get('ActualTimeGte')

	def set_ActualTimeGte(self,ActualTimeGte):
		self.add_query_param('ActualTimeGte',ActualTimeGte)

	def get_CallDurationGte(self):
		return self.get_query_params().get('CallDurationGte')

	def set_CallDurationGte(self,CallDurationGte):
		self.add_query_param('CallDurationGte',CallDurationGte)

	def get_RecordingDurationLte(self):
		return self.get_query_params().get('RecordingDurationLte')

	def set_RecordingDurationLte(self,RecordingDurationLte):
		self.add_query_param('RecordingDurationLte',RecordingDurationLte)