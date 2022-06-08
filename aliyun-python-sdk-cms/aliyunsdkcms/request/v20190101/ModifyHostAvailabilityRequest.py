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

class ModifyHostAvailabilityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'ModifyHostAvailability','cms')
		self.set_method('POST')

	def get_TaskOptionHttpMethod(self): # String
		return self.get_query_params().get('TaskOption.HttpMethod')

	def set_TaskOptionHttpMethod(self, TaskOptionHttpMethod):  # String
		self.add_query_param('TaskOption.HttpMethod', TaskOptionHttpMethod)
	def get_TaskOptionHttpHeader(self): # String
		return self.get_query_params().get('TaskOption.HttpHeader')

	def set_TaskOptionHttpHeader(self, TaskOptionHttpHeader):  # String
		self.add_query_param('TaskOption.HttpHeader', TaskOptionHttpHeader)
	def get_AlertConfigEscalationLists(self): # RepeatList
		return self.get_query_params().get('AlertConfigEscalationList')

	def set_AlertConfigEscalationLists(self, AlertConfigEscalationList):  # RepeatList
		for depth1 in range(len(AlertConfigEscalationList)):
			if AlertConfigEscalationList[depth1].get('Times') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.Times', AlertConfigEscalationList[depth1].get('Times'))
			if AlertConfigEscalationList[depth1].get('MetricName') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.MetricName', AlertConfigEscalationList[depth1].get('MetricName'))
			if AlertConfigEscalationList[depth1].get('Value') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.Value', AlertConfigEscalationList[depth1].get('Value'))
			if AlertConfigEscalationList[depth1].get('Operator') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.Operator', AlertConfigEscalationList[depth1].get('Operator'))
			if AlertConfigEscalationList[depth1].get('Aggregate') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.Aggregate', AlertConfigEscalationList[depth1].get('Aggregate'))
	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_AlertConfigSilenceTime(self): # Integer
		return self.get_query_params().get('AlertConfig.SilenceTime')

	def set_AlertConfigSilenceTime(self, AlertConfigSilenceTime):  # Integer
		self.add_query_param('AlertConfig.SilenceTime', AlertConfigSilenceTime)
	def get_TaskOptionHttpResponseCharset(self): # String
		return self.get_query_params().get('TaskOption.HttpResponseCharset')

	def set_TaskOptionHttpResponseCharset(self, TaskOptionHttpResponseCharset):  # String
		self.add_query_param('TaskOption.HttpResponseCharset', TaskOptionHttpResponseCharset)
	def get_TaskOptionHttpNegative(self): # Boolean
		return self.get_query_params().get('TaskOption.HttpNegative')

	def set_TaskOptionHttpNegative(self, TaskOptionHttpNegative):  # Boolean
		self.add_query_param('TaskOption.HttpNegative', TaskOptionHttpNegative)
	def get_TaskOptionInterval(self): # Integer
		return self.get_query_params().get('TaskOption.Interval')

	def set_TaskOptionInterval(self, TaskOptionInterval):  # Integer
		self.add_query_param('TaskOption.Interval', TaskOptionInterval)
	def get_AlertConfigNotifyType(self): # Integer
		return self.get_query_params().get('AlertConfig.NotifyType')

	def set_AlertConfigNotifyType(self, AlertConfigNotifyType):  # Integer
		self.add_query_param('AlertConfig.NotifyType', AlertConfigNotifyType)
	def get_TaskOptionTelnetOrPingHost(self): # String
		return self.get_query_params().get('TaskOption.TelnetOrPingHost')

	def set_TaskOptionTelnetOrPingHost(self, TaskOptionTelnetOrPingHost):  # String
		self.add_query_param('TaskOption.TelnetOrPingHost', TaskOptionTelnetOrPingHost)
	def get_TaskOptionHttpResponseMatchContent(self): # String
		return self.get_query_params().get('TaskOption.HttpResponseMatchContent')

	def set_TaskOptionHttpResponseMatchContent(self, TaskOptionHttpResponseMatchContent):  # String
		self.add_query_param('TaskOption.HttpResponseMatchContent', TaskOptionHttpResponseMatchContent)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_InstanceLists(self): # RepeatList
		return self.get_query_params().get('InstanceList')

	def set_InstanceLists(self, InstanceList):  # RepeatList
		for depth1 in range(len(InstanceList)):
			self.add_query_param('InstanceList.' + str(depth1 + 1), InstanceList[depth1])
	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_AlertConfigEndTime(self): # Integer
		return self.get_query_params().get('AlertConfig.EndTime')

	def set_AlertConfigEndTime(self, AlertConfigEndTime):  # Integer
		self.add_query_param('AlertConfig.EndTime', AlertConfigEndTime)
	def get_TaskOptionHttpURI(self): # String
		return self.get_query_params().get('TaskOption.HttpURI')

	def set_TaskOptionHttpURI(self, TaskOptionHttpURI):  # String
		self.add_query_param('TaskOption.HttpURI', TaskOptionHttpURI)
	def get_TaskScope(self): # String
		return self.get_query_params().get('TaskScope')

	def set_TaskScope(self, TaskScope):  # String
		self.add_query_param('TaskScope', TaskScope)
	def get_TaskOptionHttpPostContent(self): # String
		return self.get_query_params().get('TaskOption.HttpPostContent')

	def set_TaskOptionHttpPostContent(self, TaskOptionHttpPostContent):  # String
		self.add_query_param('TaskOption.HttpPostContent', TaskOptionHttpPostContent)
	def get_AlertConfigStartTime(self): # Integer
		return self.get_query_params().get('AlertConfig.StartTime')

	def set_AlertConfigStartTime(self, AlertConfigStartTime):  # Integer
		self.add_query_param('AlertConfig.StartTime', AlertConfigStartTime)
	def get_AlertConfigWebHook(self): # String
		return self.get_query_params().get('AlertConfig.WebHook')

	def set_AlertConfigWebHook(self, AlertConfigWebHook):  # String
		self.add_query_param('AlertConfig.WebHook', AlertConfigWebHook)
