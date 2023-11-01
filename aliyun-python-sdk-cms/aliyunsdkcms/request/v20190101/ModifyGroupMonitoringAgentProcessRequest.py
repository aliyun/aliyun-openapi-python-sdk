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

class ModifyGroupMonitoringAgentProcessRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'ModifyGroupMonitoringAgentProcess','cms')
		self.set_method('POST')

	def get_AlertConfig(self): # Array
		return self.get_query_params().get('AlertConfig')

	def set_AlertConfig(self, AlertConfig):  # Array
		for index1, value1 in enumerate(AlertConfig):
			if value1.get('Times') is not None:
				self.add_query_param('AlertConfig.' + str(index1 + 1) + '.Times', value1.get('Times'))
			if value1.get('Webhook') is not None:
				self.add_query_param('AlertConfig.' + str(index1 + 1) + '.Webhook', value1.get('Webhook'))
			if value1.get('NoEffectiveInterval') is not None:
				self.add_query_param('AlertConfig.' + str(index1 + 1) + '.NoEffectiveInterval', value1.get('NoEffectiveInterval'))
			if value1.get('TargetList') is not None:
				for index2, value2 in enumerate(value1.get('TargetList')):
					if value2.get('Level') is not None:
						self.add_query_param('AlertConfig.' + str(index1 + 1) + '.TargetList.' + str(index2 + 1) + '.Level', value2.get('Level'))
					if value2.get('Id') is not None:
						self.add_query_param('AlertConfig.' + str(index1 + 1) + '.TargetList.' + str(index2 + 1) + '.Id', value2.get('Id'))
					if value2.get('Arn') is not None:
						self.add_query_param('AlertConfig.' + str(index1 + 1) + '.TargetList.' + str(index2 + 1) + '.Arn', value2.get('Arn'))
					if value2.get('JsonParams') is not None:
						self.add_query_param('AlertConfig.' + str(index1 + 1) + '.TargetList.' + str(index2 + 1) + '.JsonParams', value2.get('JsonParams'))
			if value1.get('SilenceTime') is not None:
				self.add_query_param('AlertConfig.' + str(index1 + 1) + '.SilenceTime', value1.get('SilenceTime'))
			if value1.get('Threshold') is not None:
				self.add_query_param('AlertConfig.' + str(index1 + 1) + '.Threshold', value1.get('Threshold'))
			if value1.get('ComparisonOperator') is not None:
				self.add_query_param('AlertConfig.' + str(index1 + 1) + '.ComparisonOperator', value1.get('ComparisonOperator'))
			if value1.get('EffectiveInterval') is not None:
				self.add_query_param('AlertConfig.' + str(index1 + 1) + '.EffectiveInterval', value1.get('EffectiveInterval'))
			if value1.get('EscalationsLevel') is not None:
				self.add_query_param('AlertConfig.' + str(index1 + 1) + '.EscalationsLevel', value1.get('EscalationsLevel'))
			if value1.get('Statistics') is not None:
				self.add_query_param('AlertConfig.' + str(index1 + 1) + '.Statistics', value1.get('Statistics'))
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_MatchExpressFilterRelation(self): # String
		return self.get_query_params().get('MatchExpressFilterRelation')

	def set_MatchExpressFilterRelation(self, MatchExpressFilterRelation):  # String
		self.add_query_param('MatchExpressFilterRelation', MatchExpressFilterRelation)
	def get_Id(self): # String
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_query_param('Id', Id)
