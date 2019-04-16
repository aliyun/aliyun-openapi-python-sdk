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
class ModifyHostAvailabilityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'ModifyHostAvailability','cms')

	def get_InstanceLists(self):
		return self.get_query_params().get('InstanceLists')

	def set_InstanceLists(self,InstanceLists):
		for i in range(len(InstanceLists)):	
			if InstanceLists[i] is not None:
				self.add_query_param('InstanceList.' + str(i + 1) , InstanceLists[i]);

	def get_TaskOptionHttpMethod(self):
		return self.get_query_params().get('TaskOption.HttpMethod')

	def set_TaskOptionHttpMethod(self,TaskOptionHttpMethod):
		self.add_query_param('TaskOption.HttpMethod',TaskOptionHttpMethod)

	def get_AlertConfigEscalationLists(self):
		return self.get_query_params().get('AlertConfigEscalationLists')

	def set_AlertConfigEscalationLists(self,AlertConfigEscalationLists):
		for i in range(len(AlertConfigEscalationLists)):	
			if AlertConfigEscalationLists[i].get('Times') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(i + 1) + '.Times' , AlertConfigEscalationLists[i].get('Times'))
			if AlertConfigEscalationLists[i].get('MetricName') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(i + 1) + '.MetricName' , AlertConfigEscalationLists[i].get('MetricName'))
			if AlertConfigEscalationLists[i].get('Value') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(i + 1) + '.Value' , AlertConfigEscalationLists[i].get('Value'))
			if AlertConfigEscalationLists[i].get('Operator') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(i + 1) + '.Operator' , AlertConfigEscalationLists[i].get('Operator'))
			if AlertConfigEscalationLists[i].get('Aggregate') is not None:
				self.add_query_param('AlertConfigEscalationList.' + str(i + 1) + '.Aggregate' , AlertConfigEscalationLists[i].get('Aggregate'))


	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

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

	def get_AlertConfigEndTime(self):
		return self.get_query_params().get('AlertConfig.EndTime')

	def set_AlertConfigEndTime(self,AlertConfigEndTime):
		self.add_query_param('AlertConfig.EndTime',AlertConfigEndTime)

	def get_TaskOptionHttpURI(self):
		return self.get_query_params().get('TaskOption.HttpURI')

	def set_TaskOptionHttpURI(self,TaskOptionHttpURI):
		self.add_query_param('TaskOption.HttpURI',TaskOptionHttpURI)

	def get_TaskOptionHttpNegative(self):
		return self.get_query_params().get('TaskOption.HttpNegative')

	def set_TaskOptionHttpNegative(self,TaskOptionHttpNegative):
		self.add_query_param('TaskOption.HttpNegative',TaskOptionHttpNegative)

	def get_TaskScope(self):
		return self.get_query_params().get('TaskScope')

	def set_TaskScope(self,TaskScope):
		self.add_query_param('TaskScope',TaskScope)

	def get_AlertConfigNotifyType(self):
		return self.get_query_params().get('AlertConfig.NotifyType')

	def set_AlertConfigNotifyType(self,AlertConfigNotifyType):
		self.add_query_param('AlertConfig.NotifyType',AlertConfigNotifyType)

	def get_AlertConfigStartTime(self):
		return self.get_query_params().get('AlertConfig.StartTime')

	def set_AlertConfigStartTime(self,AlertConfigStartTime):
		self.add_query_param('AlertConfig.StartTime',AlertConfigStartTime)

	def get_TaskOptionTelnetOrPingHost(self):
		return self.get_query_params().get('TaskOption.TelnetOrPingHost')

	def set_TaskOptionTelnetOrPingHost(self,TaskOptionTelnetOrPingHost):
		self.add_query_param('TaskOption.TelnetOrPingHost',TaskOptionTelnetOrPingHost)

	def get_TaskOptionHttpResponseMatchContent(self):
		return self.get_query_params().get('TaskOption.HttpResponseMatchContent')

	def set_TaskOptionHttpResponseMatchContent(self,TaskOptionHttpResponseMatchContent):
		self.add_query_param('TaskOption.HttpResponseMatchContent',TaskOptionHttpResponseMatchContent)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_AlertConfigWebHook(self):
		return self.get_query_params().get('AlertConfig.WebHook')

	def set_AlertConfigWebHook(self,AlertConfigWebHook):
		self.add_query_param('AlertConfig.WebHook',AlertConfigWebHook)