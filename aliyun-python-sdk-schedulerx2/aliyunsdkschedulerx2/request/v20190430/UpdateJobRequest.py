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
from aliyunsdkschedulerx2.endpoint import endpoint_data

class UpdateJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'schedulerx2', '2019-04-30', 'UpdateJob')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NamespaceSource(self): # String
		return self.get_body_params().get('NamespaceSource')

	def set_NamespaceSource(self, NamespaceSource):  # String
		self.add_body_params('NamespaceSource', NamespaceSource)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_AttemptInterval(self): # Integer
		return self.get_body_params().get('AttemptInterval')

	def set_AttemptInterval(self, AttemptInterval):  # Integer
		self.add_body_params('AttemptInterval', AttemptInterval)
	def get_Content(self): # String
		return self.get_body_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_body_params('Content', Content)
	def get_Timeout(self): # Long
		return self.get_body_params().get('Timeout')

	def set_Timeout(self, Timeout):  # Long
		self.add_body_params('Timeout', Timeout)
	def get_TimeoutKillEnable(self): # Boolean
		return self.get_body_params().get('TimeoutKillEnable')

	def set_TimeoutKillEnable(self, TimeoutKillEnable):  # Boolean
		self.add_body_params('TimeoutKillEnable', TimeoutKillEnable)
	def get_JobId(self): # Long
		return self.get_body_params().get('JobId')

	def set_JobId(self, JobId):  # Long
		self.add_body_params('JobId', JobId)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_ConsumerSize(self): # Integer
		return self.get_body_params().get('ConsumerSize')

	def set_ConsumerSize(self, ConsumerSize):  # Integer
		self.add_body_params('ConsumerSize', ConsumerSize)
	def get_JarUrl(self): # String
		return self.get_body_params().get('JarUrl')

	def set_JarUrl(self, JarUrl):  # String
		self.add_body_params('JarUrl', JarUrl)
	def get_Calendar(self): # String
		return self.get_body_params().get('Calendar')

	def set_Calendar(self, Calendar):  # String
		self.add_body_params('Calendar', Calendar)
	def get_FailEnable(self): # Boolean
		return self.get_body_params().get('FailEnable')

	def set_FailEnable(self, FailEnable):  # Boolean
		self.add_body_params('FailEnable', FailEnable)
	def get_SendChannel(self): # String
		return self.get_body_params().get('SendChannel')

	def set_SendChannel(self, SendChannel):  # String
		self.add_body_params('SendChannel', SendChannel)
	def get_DataOffset(self): # Integer
		return self.get_body_params().get('DataOffset')

	def set_DataOffset(self, DataOffset):  # Integer
		self.add_body_params('DataOffset', DataOffset)
	def get_GroupId(self): # String
		return self.get_body_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_body_params('GroupId', GroupId)
	def get_TaskMaxAttempt(self): # Integer
		return self.get_body_params().get('TaskMaxAttempt')

	def set_TaskMaxAttempt(self, TaskMaxAttempt):  # Integer
		self.add_body_params('TaskMaxAttempt', TaskMaxAttempt)
	def get_MaxAttempt(self): # Integer
		return self.get_body_params().get('MaxAttempt')

	def set_MaxAttempt(self, MaxAttempt):  # Integer
		self.add_body_params('MaxAttempt', MaxAttempt)
	def get_MissWorkerEnable(self): # Boolean
		return self.get_body_params().get('MissWorkerEnable')

	def set_MissWorkerEnable(self, MissWorkerEnable):  # Boolean
		self.add_body_params('MissWorkerEnable', MissWorkerEnable)
	def get_DispatcherSize(self): # Integer
		return self.get_body_params().get('DispatcherSize')

	def set_DispatcherSize(self, DispatcherSize):  # Integer
		self.add_body_params('DispatcherSize', DispatcherSize)
	def get_TaskAttemptInterval(self): # Integer
		return self.get_body_params().get('TaskAttemptInterval')

	def set_TaskAttemptInterval(self, TaskAttemptInterval):  # Integer
		self.add_body_params('TaskAttemptInterval', TaskAttemptInterval)
	def get_ExecuteMode(self): # String
		return self.get_body_params().get('ExecuteMode')

	def set_ExecuteMode(self, ExecuteMode):  # String
		self.add_body_params('ExecuteMode', ExecuteMode)
	def get_QueueSize(self): # Integer
		return self.get_body_params().get('QueueSize')

	def set_QueueSize(self, QueueSize):  # Integer
		self.add_body_params('QueueSize', QueueSize)
	def get_TimeExpression(self): # String
		return self.get_body_params().get('TimeExpression')

	def set_TimeExpression(self, TimeExpression):  # String
		self.add_body_params('TimeExpression', TimeExpression)
	def get_ClassName(self): # String
		return self.get_body_params().get('ClassName')

	def set_ClassName(self, ClassName):  # String
		self.add_body_params('ClassName', ClassName)
	def get_TimeoutEnable(self): # Boolean
		return self.get_body_params().get('TimeoutEnable')

	def set_TimeoutEnable(self, TimeoutEnable):  # Boolean
		self.add_body_params('TimeoutEnable', TimeoutEnable)
	def get_ContactInfos(self): # RepeatList
		return self.get_body_params().get('ContactInfo')

	def set_ContactInfos(self, ContactInfo):  # RepeatList
		for depth1 in range(len(ContactInfo)):
			if ContactInfo[depth1].get('Ding') is not None:
				self.add_body_params('ContactInfo.' + str(depth1 + 1) + '.Ding', ContactInfo[depth1].get('Ding'))
			if ContactInfo[depth1].get('UserPhone') is not None:
				self.add_body_params('ContactInfo.' + str(depth1 + 1) + '.UserPhone', ContactInfo[depth1].get('UserPhone'))
			if ContactInfo[depth1].get('UserMail') is not None:
				self.add_body_params('ContactInfo.' + str(depth1 + 1) + '.UserMail', ContactInfo[depth1].get('UserMail'))
			if ContactInfo[depth1].get('UserName') is not None:
				self.add_body_params('ContactInfo.' + str(depth1 + 1) + '.UserName', ContactInfo[depth1].get('UserName'))
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_Namespace(self): # String
		return self.get_body_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_body_params('Namespace', Namespace)
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
