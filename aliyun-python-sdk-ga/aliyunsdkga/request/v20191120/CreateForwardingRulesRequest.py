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
from aliyunsdkga.endpoint import endpoint_data

class CreateForwardingRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateForwardingRules','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_AcceleratorId(self): # String
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self, AcceleratorId):  # String
		self.add_query_param('AcceleratorId', AcceleratorId)
	def get_ForwardingRules(self): # Array
		return self.get_query_params().get('ForwardingRules')

	def set_ForwardingRules(self, ForwardingRules):  # Array
		for index1, value1 in enumerate(ForwardingRules):
			if value1.get('Priority') is not None:
				self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.Priority', value1.get('Priority'))
			if value1.get('RuleConditions') is not None:
				for index2, value2 in enumerate(value1.get('RuleConditions')):
					if value2.get('RuleConditionType') is not None:
						self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.RuleConditionType', value2.get('RuleConditionType'))
					if value2.get('RuleConditionValue') is not None:
						self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.RuleConditionValue', value2.get('RuleConditionValue'))
					if value2.get('PathConfig') is not None:
						if value2.get('PathConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('PathConfig').get('Values')):
								self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.PathConfig.Values.' + str(index3 + 1), value3)
					if value2.get('HostConfig') is not None:
						if value2.get('HostConfig').get('Values') is not None:
							for index3, value3 in enumerate(value2.get('HostConfig').get('Values')):
								self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.RuleConditions.' + str(index2 + 1) + '.HostConfig.Values.' + str(index3 + 1), value3)
			if value1.get('RuleActions') is not None:
				for index2, value2 in enumerate(value1.get('RuleActions')):
					if value2.get('Order') is not None:
						self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.Order', value2.get('Order'))
					if value2.get('RuleActionType') is not None:
						self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RuleActionType', value2.get('RuleActionType'))
					if value2.get('RuleActionValue') is not None:
						self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.RuleActionValue', value2.get('RuleActionValue'))
					if value2.get('ForwardGroupConfig') is not None:
						if value2.get('ForwardGroupConfig').get('ServerGroupTuples') is not None:
							for index3, value3 in enumerate(value2.get('ForwardGroupConfig').get('ServerGroupTuples')):
								if value3.get('EndpointGroupId') is not None:
									self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.RuleActions.' + str(index2 + 1) + '.ForwardGroupConfig.ServerGroupTuples.' + str(index3 + 1) + '.EndpointGroupId', value3.get('EndpointGroupId'))
			if value1.get('ForwardingRuleName') is not None:
				self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.ForwardingRuleName', value1.get('ForwardingRuleName'))
			if value1.get('RuleDirection') is not None:
				self.add_query_param('ForwardingRules.' + str(index1 + 1) + '.RuleDirection', value1.get('RuleDirection'))
