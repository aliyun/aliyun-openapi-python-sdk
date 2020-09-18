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

class PutResourceMetricRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutResourceMetricRules','cms')
		self.set_method('POST')

	def get_Ruless(self):
		return self.get_query_params().get('Rules')

	def set_Ruless(self, Ruless):
		for depth1 in range(len(Ruless)):
			if Ruless[depth1].get('Webhook') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Webhook', Ruless[depth1].get('Webhook'))
			if Ruless[depth1].get('Escalations.Warn.ComparisonOperator') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Warn.ComparisonOperator', Ruless[depth1].get('Escalations.Warn.ComparisonOperator'))
			if Ruless[depth1].get('RuleName') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.RuleName', Ruless[depth1].get('RuleName'))
			if Ruless[depth1].get('Escalations.Info.Statistics') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Info.Statistics', Ruless[depth1].get('Escalations.Info.Statistics'))
			if Ruless[depth1].get('EffectiveInterval') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.EffectiveInterval', Ruless[depth1].get('EffectiveInterval'))
			if Ruless[depth1].get('Escalations.Info.ComparisonOperator') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Info.ComparisonOperator', Ruless[depth1].get('Escalations.Info.ComparisonOperator'))
			if Ruless[depth1].get('NoEffectiveInterval') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.NoEffectiveInterval', Ruless[depth1].get('NoEffectiveInterval'))
			if Ruless[depth1].get('EmailSubject') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.EmailSubject', Ruless[depth1].get('EmailSubject'))
			if Ruless[depth1].get('SilenceTime') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.SilenceTime', Ruless[depth1].get('SilenceTime'))
			if Ruless[depth1].get('MetricName') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.MetricName', Ruless[depth1].get('MetricName'))
			if Ruless[depth1].get('Escalations.Warn.Times') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Warn.Times', Ruless[depth1].get('Escalations.Warn.Times'))
			if Ruless[depth1].get('Period') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Period', Ruless[depth1].get('Period'))
			if Ruless[depth1].get('Escalations.Warn.Threshold') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Warn.Threshold', Ruless[depth1].get('Escalations.Warn.Threshold'))
			if Ruless[depth1].get('ContactGroups') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.ContactGroups', Ruless[depth1].get('ContactGroups'))
			if Ruless[depth1].get('Escalations.Critical.Statistics') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Critical.Statistics', Ruless[depth1].get('Escalations.Critical.Statistics'))
			if Ruless[depth1].get('Resources') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Resources', Ruless[depth1].get('Resources'))
			if Ruless[depth1].get('Escalations.Info.Times') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Info.Times', Ruless[depth1].get('Escalations.Info.Times'))
			if Ruless[depth1].get('Escalations.Critical.Times') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Critical.Times', Ruless[depth1].get('Escalations.Critical.Times'))
			if Ruless[depth1].get('Escalations.Warn.Statistics') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Warn.Statistics', Ruless[depth1].get('Escalations.Warn.Statistics'))
			if Ruless[depth1].get('Escalations.Info.Threshold') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Info.Threshold', Ruless[depth1].get('Escalations.Info.Threshold'))
			if Ruless[depth1].get('Namespace') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Namespace', Ruless[depth1].get('Namespace'))
			if Ruless[depth1].get('Interval') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Interval', Ruless[depth1].get('Interval'))
			if Ruless[depth1].get('RuleId') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.RuleId', Ruless[depth1].get('RuleId'))
			if Ruless[depth1].get('Escalations.Critical.ComparisonOperator') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Critical.ComparisonOperator', Ruless[depth1].get('Escalations.Critical.ComparisonOperator'))
			if Ruless[depth1].get('Escalations.Critical.Threshold') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Critical.Threshold', Ruless[depth1].get('Escalations.Critical.Threshold'))