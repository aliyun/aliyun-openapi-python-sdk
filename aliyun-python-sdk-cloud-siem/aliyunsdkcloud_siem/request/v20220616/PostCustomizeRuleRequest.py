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

class PostCustomizeRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'PostCustomizeRule','cloud-siem')
		self.set_method('POST')

	def get_RuleDesc(self): # String
		return self.get_body_params().get('RuleDesc')

	def set_RuleDesc(self, RuleDesc):  # String
		self.add_body_params('RuleDesc', RuleDesc)
	def get_RuleName(self): # String
		return self.get_body_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_body_params('RuleName', RuleName)
	def get_AlertTypeMds(self): # String
		return self.get_body_params().get('AlertTypeMds')

	def set_AlertTypeMds(self, AlertTypeMds):  # String
		self.add_body_params('AlertTypeMds', AlertTypeMds)
	def get_RuleThreshold(self): # String
		return self.get_body_params().get('RuleThreshold')

	def set_RuleThreshold(self, RuleThreshold):  # String
		self.add_body_params('RuleThreshold', RuleThreshold)
	def get_LogSourceMds(self): # String
		return self.get_body_params().get('LogSourceMds')

	def set_LogSourceMds(self, LogSourceMds):  # String
		self.add_body_params('LogSourceMds', LogSourceMds)
	def get_LogType(self): # String
		return self.get_body_params().get('LogType')

	def set_LogType(self, LogType):  # String
		self.add_body_params('LogType', LogType)
	def get_LogTypeMds(self): # String
		return self.get_body_params().get('LogTypeMds')

	def set_LogTypeMds(self, LogTypeMds):  # String
		self.add_body_params('LogTypeMds', LogTypeMds)
	def get_Id(self): # Long
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_body_params('Id', Id)
	def get_EventTransferSwitch(self): # Integer
		return self.get_body_params().get('EventTransferSwitch')

	def set_EventTransferSwitch(self, EventTransferSwitch):  # Integer
		self.add_body_params('EventTransferSwitch', EventTransferSwitch)
	def get_QueryCycle(self): # String
		return self.get_body_params().get('QueryCycle')

	def set_QueryCycle(self, QueryCycle):  # String
		self.add_body_params('QueryCycle', QueryCycle)
	def get_LogSource(self): # String
		return self.get_body_params().get('LogSource')

	def set_LogSource(self, LogSource):  # String
		self.add_body_params('LogSource', LogSource)
	def get_AlertType(self): # String
		return self.get_body_params().get('AlertType')

	def set_AlertType(self, AlertType):  # String
		self.add_body_params('AlertType', AlertType)
	def get_EventTransferType(self): # String
		return self.get_body_params().get('EventTransferType')

	def set_EventTransferType(self, EventTransferType):  # String
		self.add_body_params('EventTransferType', EventTransferType)
	def get_RuleCondition(self): # String
		return self.get_body_params().get('RuleCondition')

	def set_RuleCondition(self, RuleCondition):  # String
		self.add_body_params('RuleCondition', RuleCondition)
	def get_EventTransferExt(self): # String
		return self.get_body_params().get('EventTransferExt')

	def set_EventTransferExt(self, EventTransferExt):  # String
		self.add_body_params('EventTransferExt', EventTransferExt)
	def get_ThreatLevel(self): # String
		return self.get_body_params().get('ThreatLevel')

	def set_ThreatLevel(self, ThreatLevel):  # String
		self.add_body_params('ThreatLevel', ThreatLevel)
	def get_RuleGroup(self): # String
		return self.get_body_params().get('RuleGroup')

	def set_RuleGroup(self, RuleGroup):  # String
		self.add_body_params('RuleGroup', RuleGroup)
