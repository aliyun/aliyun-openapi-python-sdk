# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2018-03-08', 'CreateTask','cms')

	def get_ReportProject(self):
		return self.get_query_params().get('ReportProject')

	def set_ReportProject(self,ReportProject):
		self.add_query_param('ReportProject',ReportProject)

	def get_TaskType(self):
		return self.get_query_params().get('TaskType')

	def set_TaskType(self,TaskType):
		self.add_query_param('TaskType',TaskType)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_AlertName(self):
		return self.get_query_params().get('AlertName')

	def set_AlertName(self,AlertName):
		self.add_query_param('AlertName',AlertName)

	def get_Ip(self):
		return self.get_query_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_query_param('Ip',Ip)

	def get_AgentGroup(self):
		return self.get_query_params().get('AgentGroup')

	def set_AgentGroup(self,AgentGroup):
		self.add_query_param('AgentGroup',AgentGroup)

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_TaskState(self):
		return self.get_query_params().get('TaskState')

	def set_TaskState(self,TaskState):
		self.add_query_param('TaskState',TaskState)

	def get_ClientIds(self):
		return self.get_query_params().get('ClientIds')

	def set_ClientIds(self,ClientIds):
		self.add_query_param('ClientIds',ClientIds)

	def get_AlertInfo(self):
		return self.get_query_params().get('AlertInfo')

	def set_AlertInfo(self,AlertInfo):
		self.add_query_param('AlertInfo',AlertInfo)

	def get_AgentType(self):
		return self.get_query_params().get('AgentType')

	def set_AgentType(self,AgentType):
		self.add_query_param('AgentType',AgentType)

	def get_IspCity(self):
		return self.get_query_params().get('IspCity')

	def set_IspCity(self,IspCity):
		self.add_query_param('IspCity',IspCity)

	def get_Options(self):
		return self.get_query_params().get('Options')

	def set_Options(self,Options):
		self.add_query_param('Options',Options)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)

	def get_AlertRule(self):
		return self.get_query_params().get('AlertRule')

	def set_AlertRule(self,AlertRule):
		self.add_query_param('AlertRule',AlertRule)

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)