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
from aliyunsdkddosbgp.endpoint import endpoint_data

class CreateSchedruleOnDemandRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ddosbgp', '2018-07-20', 'CreateSchedruleOnDemand')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TimeZone(self): # String
		return self.get_query_params().get('TimeZone')

	def set_TimeZone(self, TimeZone):  # String
		self.add_query_param('TimeZone', TimeZone)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_RuleConditionMbps(self): # String
		return self.get_query_params().get('RuleConditionMbps')

	def set_RuleConditionMbps(self, RuleConditionMbps):  # String
		self.add_query_param('RuleConditionMbps', RuleConditionMbps)
	def get_RuleAction(self): # String
		return self.get_query_params().get('RuleAction')

	def set_RuleAction(self, RuleAction):  # String
		self.add_query_param('RuleAction', RuleAction)
	def get_RuleUndoMode(self): # String
		return self.get_query_params().get('RuleUndoMode')

	def set_RuleUndoMode(self, RuleUndoMode):  # String
		self.add_query_param('RuleUndoMode', RuleUndoMode)
	def get_RuleUndoEndTime(self): # String
		return self.get_query_params().get('RuleUndoEndTime')

	def set_RuleUndoEndTime(self, RuleUndoEndTime):  # String
		self.add_query_param('RuleUndoEndTime', RuleUndoEndTime)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_RuleUndoBeginTime(self): # String
		return self.get_query_params().get('RuleUndoBeginTime')

	def set_RuleUndoBeginTime(self, RuleUndoBeginTime):  # String
		self.add_query_param('RuleUndoBeginTime', RuleUndoBeginTime)
	def get_RuleConditionCnt(self): # String
		return self.get_query_params().get('RuleConditionCnt')

	def set_RuleConditionCnt(self, RuleConditionCnt):  # String
		self.add_query_param('RuleConditionCnt', RuleConditionCnt)
	def get_RuleSwitch(self): # String
		return self.get_query_params().get('RuleSwitch')

	def set_RuleSwitch(self, RuleSwitch):  # String
		self.add_query_param('RuleSwitch', RuleSwitch)
	def get_RuleConditionKpps(self): # String
		return self.get_query_params().get('RuleConditionKpps')

	def set_RuleConditionKpps(self, RuleConditionKpps):  # String
		self.add_query_param('RuleConditionKpps', RuleConditionKpps)
