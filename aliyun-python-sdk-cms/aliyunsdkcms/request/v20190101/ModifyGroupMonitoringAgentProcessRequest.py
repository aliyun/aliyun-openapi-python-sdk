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

	def get_AlertConfigs(self):
		return self.get_query_params().get('AlertConfig')

	def set_AlertConfigs(self, AlertConfigs):
		for depth1 in range(len(AlertConfigs)):
			if AlertConfigs[depth1].get('Times') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.Times', AlertConfigs[depth1].get('Times'))
			if AlertConfigs[depth1].get('NoEffectiveInterval') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.NoEffectiveInterval', AlertConfigs[depth1].get('NoEffectiveInterval'))
			if AlertConfigs[depth1].get('Webhook') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.Webhook', AlertConfigs[depth1].get('Webhook'))
			if AlertConfigs[depth1].get('SilenceTime') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.SilenceTime', AlertConfigs[depth1].get('SilenceTime'))
			if AlertConfigs[depth1].get('Threshold') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.Threshold', AlertConfigs[depth1].get('Threshold'))
			if AlertConfigs[depth1].get('EffectiveInterval') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.EffectiveInterval', AlertConfigs[depth1].get('EffectiveInterval'))
			if AlertConfigs[depth1].get('ComparisonOperator') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.ComparisonOperator', AlertConfigs[depth1].get('ComparisonOperator'))
			if AlertConfigs[depth1].get('EscalationsLevel') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.EscalationsLevel', AlertConfigs[depth1].get('EscalationsLevel'))
			if AlertConfigs[depth1].get('Statistics') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.Statistics', AlertConfigs[depth1].get('Statistics'))

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_MatchExpressFilterRelation(self):
		return self.get_query_params().get('MatchExpressFilterRelation')

	def set_MatchExpressFilterRelation(self,MatchExpressFilterRelation):
		self.add_query_param('MatchExpressFilterRelation',MatchExpressFilterRelation)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)