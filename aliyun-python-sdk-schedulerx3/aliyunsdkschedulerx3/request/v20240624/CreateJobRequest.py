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
import json

class CreateJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SchedulerX3', '2024-06-24', 'CreateJob')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ExecutorBlockStrategy(self): # Integer
		return self.get_body_params().get('ExecutorBlockStrategy')

	def set_ExecutorBlockStrategy(self, ExecutorBlockStrategy):  # Integer
		self.add_body_params('ExecutorBlockStrategy', ExecutorBlockStrategy)
	def get_Timezone(self): # String
		return self.get_body_params().get('Timezone')

	def set_Timezone(self, Timezone):  # String
		self.add_body_params('Timezone', Timezone)
	def get_RouteStrategy(self): # Integer
		return self.get_body_params().get('RouteStrategy')

	def set_RouteStrategy(self, RouteStrategy):  # Integer
		self.add_body_params('RouteStrategy', RouteStrategy)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_AttemptInterval(self): # Integer
		return self.get_body_params().get('AttemptInterval')

	def set_AttemptInterval(self, AttemptInterval):  # Integer
		self.add_body_params('AttemptInterval', AttemptInterval)
	def get_StartTime(self): # Long
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_body_params('StartTime', StartTime)
	def get_AppName(self): # String
		return self.get_body_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_body_params('AppName', AppName)
	def get_NoticeContacts(self): # Array
		return self.get_body_params().get('NoticeContacts')

	def set_NoticeContacts(self, NoticeContacts):  # Array
		self.add_body_params("NoticeContacts", json.dumps(NoticeContacts))
	def get_NoticeConfig(self): # Struct
		return self.get_body_params().get('NoticeConfig')

	def set_NoticeConfig(self, NoticeConfig):  # Struct
		self.add_body_params("NoticeConfig", json.dumps(NoticeConfig))
	def get_Calendar(self): # String
		return self.get_body_params().get('Calendar')

	def set_Calendar(self, Calendar):  # String
		self.add_body_params('Calendar', Calendar)
	def get_MaxAttempt(self): # Integer
		return self.get_body_params().get('MaxAttempt')

	def set_MaxAttempt(self, MaxAttempt):  # Integer
		self.add_body_params('MaxAttempt', MaxAttempt)
	def get_ClusterId(self): # String
		return self.get_body_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_body_params('ClusterId', ClusterId)
	def get_Priority(self): # Integer
		return self.get_body_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_body_params('Priority', Priority)
	def get_JobType(self): # String
		return self.get_body_params().get('JobType')

	def set_JobType(self, JobType):  # String
		self.add_body_params('JobType', JobType)
	def get_TimeExpression(self): # String
		return self.get_body_params().get('TimeExpression')

	def set_TimeExpression(self, TimeExpression):  # String
		self.add_body_params('TimeExpression', TimeExpression)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_MaxConcurrency(self): # Integer
		return self.get_body_params().get('MaxConcurrency')

	def set_MaxConcurrency(self, MaxConcurrency):  # Integer
		self.add_body_params('MaxConcurrency', MaxConcurrency)
	def get_TimeType(self): # Integer
		return self.get_body_params().get('TimeType')

	def set_TimeType(self, TimeType):  # Integer
		self.add_body_params('TimeType', TimeType)
	def get_Parameters(self): # String
		return self.get_body_params().get('Parameters')

	def set_Parameters(self, Parameters):  # String
		self.add_body_params('Parameters', Parameters)
	def get_JobHandler(self): # String
		return self.get_body_params().get('JobHandler')

	def set_JobHandler(self, JobHandler):  # String
		self.add_body_params('JobHandler', JobHandler)
	def get_Status(self): # Integer
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_body_params('Status', Status)
