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

	def get_AlertConfigs(self):
		return self.get_query_params().get('AlertConfigs')

	def set_AlertConfigs(self,AlertConfigs):
		for i in range(len(AlertConfigs)):	
			if AlertConfigs[i].get('Times') is not None:
				self.add_query_param('AlertConfig.' + str(i + 1) + '.Times' , AlertConfigs[i].get('Times'))
			if AlertConfigs[i].get('NoEffectiveInterval') is not None:
				self.add_query_param('AlertConfig.' + str(i + 1) + '.NoEffectiveInterval' , AlertConfigs[i].get('NoEffectiveInterval'))
			if AlertConfigs[i].get('Webhook') is not None:
				self.add_query_param('AlertConfig.' + str(i + 1) + '.Webhook' , AlertConfigs[i].get('Webhook'))
			if AlertConfigs[i].get('SilenceTime') is not None:
				self.add_query_param('AlertConfig.' + str(i + 1) + '.SilenceTime' , AlertConfigs[i].get('SilenceTime'))
			if AlertConfigs[i].get('Threshold') is not None:
				self.add_query_param('AlertConfig.' + str(i + 1) + '.Threshold' , AlertConfigs[i].get('Threshold'))
			if AlertConfigs[i].get('EffectiveInterval') is not None:
				self.add_query_param('AlertConfig.' + str(i + 1) + '.EffectiveInterval' , AlertConfigs[i].get('EffectiveInterval'))
			if AlertConfigs[i].get('ComparisonOperator') is not None:
				self.add_query_param('AlertConfig.' + str(i + 1) + '.ComparisonOperator' , AlertConfigs[i].get('ComparisonOperator'))
			if AlertConfigs[i].get('EscalationsLevel') is not None:
				self.add_query_param('AlertConfig.' + str(i + 1) + '.EscalationsLevel' , AlertConfigs[i].get('EscalationsLevel'))
			if AlertConfigs[i].get('Statistics') is not None:
				self.add_query_param('AlertConfig.' + str(i + 1) + '.Statistics' , AlertConfigs[i].get('Statistics'))


	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_ProcessName(self):
		return self.get_query_params().get('ProcessName')

	def set_ProcessName(self,ProcessName):
		self.add_query_param('ProcessName',ProcessName)

	def get_MatchExpressFilterRelation(self):
		return self.get_query_params().get('MatchExpressFilterRelation')

	def set_MatchExpressFilterRelation(self,MatchExpressFilterRelation):
		self.add_query_param('MatchExpressFilterRelation',MatchExpressFilterRelation)

	def get_MatchExpresss(self):
		return self.get_query_params().get('MatchExpresss')

	def set_MatchExpresss(self,MatchExpresss):
		for i in range(len(MatchExpresss)):	
			if MatchExpresss[i].get('Function') is not None:
				self.add_query_param('MatchExpress.' + str(i + 1) + '.Function' , MatchExpresss[i].get('Function'))
			if MatchExpresss[i].get('Name') is not None:
				self.add_query_param('MatchExpress.' + str(i + 1) + '.Name' , MatchExpresss[i].get('Name'))
			if MatchExpresss[i].get('Value') is not None:
				self.add_query_param('MatchExpress.' + str(i + 1) + '.Value' , MatchExpresss[i].get('Value'))
