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

class CreateHostAvailabilityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateHostAvailability','cms')
		self.set_method('POST')

	def get_TaskOptionHttpMethod(self):
		return self.get_query_params().get('TaskOption.HttpMethod')

	def set_TaskOptionHttpMethod(self,TaskOptionHttpMethod):
		self.add_query_param('TaskOption.HttpMethod',TaskOptionHttpMethod)

	def get_TaskOptionHttpHeader(self):
		return self.get_query_params().get('TaskOption.HttpHeader')

	def set_TaskOptionHttpHeader(self,TaskOptionHttpHeader):
		self.add_query_param('TaskOption.HttpHeader',TaskOptionHttpHeader)

	def get_AlertConfigEscalationLists(self):
		return self.get_query_params().get('AlertConfigEscalationList')

	def set_AlertConfigEscalationLists(self, AlertConfigEscalationLists):
		for depth1 in range(len(AlertConfigEscalationLists)):
			if AlertConfigEscalationLists[depth1].get('Times') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.Times', AlertConfigEscalationLists[depth1].get('Times'))
			if AlertConfigEscalationLists[depth1].get('MetricName') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.MetricName', AlertConfigEscalationLists[depth1].get('MetricName'))
			if AlertConfigEscalationLists[depth1].get('Value') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.Value', AlertConfigEscalationLists[depth1].get('Value'))
			if AlertConfigEscalationLists[depth1].get('Operator') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.Operator', AlertConfigEscalationLists[depth1].get('Operator'))
			if AlertConfigEscalationLists[depth1].get('Aggregate') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(depth1 + 1) + '.Aggregate', AlertConfigEscalationLists[depth1].get('Aggregate'))

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_AlertConfigSilenceTime(self):
		return self.get_query_params().get('AlertConfig.SilenceTime')

	def set_AlertConfigSilenceTime(self,AlertConfigSilenceTime):
		self.add_query_param('AlertConfig.SilenceTime',AlertConfigSilenceTime)

	def get_TaskOptionHttpResponseCharset(self):
		return self.get_query_params().get('TaskOption.HttpResponseCharset')

	def set_TaskOptionHttpResponseCharset(self,TaskOptionHttpResponseCharset):
		self.add_query_param('TaskOption.HttpResponseCharset',TaskOptionHttpResponseCharset)

	def get_TaskOptionHttpNegative(self):
		return self.get_query_params().get('TaskOption.HttpNegative')

	def set_TaskOptionHttpNegative(self,TaskOptionHttpNegative):
		self.add_query_param('TaskOption.HttpNegative',TaskOptionHttpNegative)

	def get_AlertConfigNotifyType(self):
		return self.get_query_params().get('AlertConfig.NotifyType')

	def set_AlertConfigNotifyType(self,AlertConfigNotifyType):
		self.add_query_param('AlertConfig.NotifyType',AlertConfigNotifyType)

	def get_TaskOptionTelnetOrPingHost(self):
		return self.get_query_params().get('TaskOption.TelnetOrPingHost')

	def set_TaskOptionTelnetOrPingHost(self,TaskOptionTelnetOrPingHost):
		self.add_query_param('TaskOption.TelnetOrPingHost',TaskOptionTelnetOrPingHost)

	def get_TaskOptionHttpResponseMatchContent(self):
		return self.get_query_params().get('TaskOption.HttpResponseMatchContent')

	def set_TaskOptionHttpResponseMatchContent(self,TaskOptionHttpResponseMatchContent):
		self.add_query_param('TaskOption.HttpResponseMatchContent',TaskOptionHttpResponseMatchContent)

	def get_InstanceLists(self):
		return self.get_query_params().get('InstanceList')

	def set_InstanceLists(self, InstanceLists):
		for depth1 in range(len(InstanceLists)):
			if InstanceLists[depth1] is not None:
				self.add_query_param('InstanceList.' + str(depth1 + 1) , InstanceLists[depth1])

	def get_TaskType(self):
		return self.get_query_params().get('TaskType')

	def set_TaskType(self,TaskType):
		self.add_query_param('TaskType',TaskType)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_AlertConfigEndTime(self):
		return self.get_query_params().get('AlertConfig.EndTime')

	def set_AlertConfigEndTime(self,AlertConfigEndTime):
		self.add_query_param('AlertConfig.EndTime',AlertConfigEndTime)

	def get_TaskOptionHttpURI(self):
		return self.get_query_params().get('TaskOption.HttpURI')

	def set_TaskOptionHttpURI(self,TaskOptionHttpURI):
		self.add_query_param('TaskOption.HttpURI',TaskOptionHttpURI)

	def get_TaskScope(self):
		return self.get_query_params().get('TaskScope')

	def set_TaskScope(self,TaskScope):
		self.add_query_param('TaskScope',TaskScope)

	def get_TaskOptionHttpPostContent(self):
		return self.get_query_params().get('TaskOption.HttpPostContent')

	def set_TaskOptionHttpPostContent(self,TaskOptionHttpPostContent):
		self.add_query_param('TaskOption.HttpPostContent',TaskOptionHttpPostContent)

	def get_AlertConfigStartTime(self):
		return self.get_query_params().get('AlertConfig.StartTime')

	def set_AlertConfigStartTime(self,AlertConfigStartTime):
		self.add_query_param('AlertConfig.StartTime',AlertConfigStartTime)

	def get_AlertConfigWebHook(self):
		return self.get_query_params().get('AlertConfig.WebHook')

	def set_AlertConfigWebHook(self,AlertConfigWebHook):
		self.add_query_param('AlertConfig.WebHook',AlertConfigWebHook)