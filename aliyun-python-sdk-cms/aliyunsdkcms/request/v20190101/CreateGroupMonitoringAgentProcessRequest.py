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

class CreateGroupMonitoringAgentProcessRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateGroupMonitoringAgentProcess','cms')
		self.set_method('POST')

	def get_AlertConfigs(self): # RepeatList
		return self.get_query_params().get('AlertConfig')

	def set_AlertConfigs(self, AlertConfig):  # RepeatList
		for depth1 in range(len(AlertConfig)):
			if AlertConfig[depth1].get('Times') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.Times', AlertConfig[depth1].get('Times'))
			if AlertConfig[depth1].get('Webhook') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.Webhook', AlertConfig[depth1].get('Webhook'))
			if AlertConfig[depth1].get('NoEffectiveInterval') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.NoEffectiveInterval', AlertConfig[depth1].get('NoEffectiveInterval'))
			if AlertConfig[depth1].get('SilenceTime') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.SilenceTime', AlertConfig[depth1].get('SilenceTime'))
			if AlertConfig[depth1].get('Threshold') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.Threshold', AlertConfig[depth1].get('Threshold'))
			if AlertConfig[depth1].get('ComparisonOperator') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.ComparisonOperator', AlertConfig[depth1].get('ComparisonOperator'))
			if AlertConfig[depth1].get('EffectiveInterval') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.EffectiveInterval', AlertConfig[depth1].get('EffectiveInterval'))
			if AlertConfig[depth1].get('EscalationsLevel') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.EscalationsLevel', AlertConfig[depth1].get('EscalationsLevel'))
			if AlertConfig[depth1].get('Statistics') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.Statistics', AlertConfig[depth1].get('Statistics'))
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_ProcessName(self): # String
		return self.get_query_params().get('ProcessName')

	def set_ProcessName(self, ProcessName):  # String
		self.add_query_param('ProcessName', ProcessName)
	def get_MatchExpressFilterRelation(self): # String
		return self.get_query_params().get('MatchExpressFilterRelation')

	def set_MatchExpressFilterRelation(self, MatchExpressFilterRelation):  # String
		self.add_query_param('MatchExpressFilterRelation', MatchExpressFilterRelation)
	def get_MatchExpresss(self): # RepeatList
		return self.get_query_params().get('MatchExpress')

	def set_MatchExpresss(self, MatchExpress):  # RepeatList
		for depth1 in range(len(MatchExpress)):
			if MatchExpress[depth1].get('Function') is not None:
				self.add_query_param('MatchExpress.' + str(depth1 + 1) + '.Function', MatchExpress[depth1].get('Function'))
			if MatchExpress[depth1].get('Name') is not None:
				self.add_query_param('MatchExpress.' + str(depth1 + 1) + '.Name', MatchExpress[depth1].get('Name'))
			if MatchExpress[depth1].get('Value') is not None:
				self.add_query_param('MatchExpress.' + str(depth1 + 1) + '.Value', MatchExpress[depth1].get('Value'))
