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

	def get_Ruless(self): # RepeatList
		return self.get_query_params().get('Rules')

	def set_Ruless(self, Rules):  # RepeatList
		for depth1 in range(len(Rules)):
			if Rules[depth1].get('Webhook') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Webhook', Rules[depth1].get('Webhook'))
			if Rules[depth1].get('Escalations.Warn.ComparisonOperator') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Warn.ComparisonOperator', Rules[depth1].get('Escalations.Warn.ComparisonOperator'))
			if Rules[depth1].get('DynamicAlertSensitivity') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.DynamicAlertSensitivity', Rules[depth1].get('DynamicAlertSensitivity'))
			if Rules[depth1].get('RuleName') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.RuleName', Rules[depth1].get('RuleName'))
			if Rules[depth1].get('Escalations.Info.Statistics') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Info.Statistics', Rules[depth1].get('Escalations.Info.Statistics'))
			if Rules[depth1].get('EffectiveInterval') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.EffectiveInterval', Rules[depth1].get('EffectiveInterval'))
			if Rules[depth1].get('DynamicAlertHistoryDataRange') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.DynamicAlertHistoryDataRange', Rules[depth1].get('DynamicAlertHistoryDataRange'))
			if Rules[depth1].get('Escalations.Warn.PreCondition') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Warn.PreCondition', Rules[depth1].get('Escalations.Warn.PreCondition'))
			if Rules[depth1].get('Escalations.Info.ComparisonOperator') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Info.ComparisonOperator', Rules[depth1].get('Escalations.Info.ComparisonOperator'))
			if Rules[depth1].get('NoDataPolicy') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.NoDataPolicy', Rules[depth1].get('NoDataPolicy'))
			if Rules[depth1].get('NoEffectiveInterval') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.NoEffectiveInterval', Rules[depth1].get('NoEffectiveInterval'))
			if Rules[depth1].get('EmailSubject') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.EmailSubject', Rules[depth1].get('EmailSubject'))
			if Rules[depth1].get('Options') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Options', Rules[depth1].get('Options'))
			if Rules[depth1].get('SilenceTime') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.SilenceTime', Rules[depth1].get('SilenceTime'))
			if Rules[depth1].get('Prometheus') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Prometheus', Rules[depth1].get('Prometheus'))
			if Rules[depth1].get('Escalations.Info.PreCondition') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Info.PreCondition', Rules[depth1].get('Escalations.Info.PreCondition'))
			if Rules[depth1].get('MetricName') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.MetricName', Rules[depth1].get('MetricName'))
			if Rules[depth1].get('Escalations.Warn.Times') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Warn.Times', Rules[depth1].get('Escalations.Warn.Times'))
			if Rules[depth1].get('CompositeExpression') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.CompositeExpression', Rules[depth1].get('CompositeExpression'))
			if Rules[depth1].get('Escalations.Warn.Threshold') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Warn.Threshold', Rules[depth1].get('Escalations.Warn.Threshold'))
			if Rules[depth1].get('Period') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Period', Rules[depth1].get('Period'))
			if Rules[depth1].get('ContactGroups') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.ContactGroups', Rules[depth1].get('ContactGroups'))
			if Rules[depth1].get('Escalations.Critical.Statistics') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Critical.Statistics', Rules[depth1].get('Escalations.Critical.Statistics'))
			if Rules[depth1].get('RuleType') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.RuleType', Rules[depth1].get('RuleType'))
			if Rules[depth1].get('GroupId') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.GroupId', Rules[depth1].get('GroupId'))
			if Rules[depth1].get('Escalations.Info.Times') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Info.Times', Rules[depth1].get('Escalations.Info.Times'))
			if Rules[depth1].get('Resources') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Resources', Rules[depth1].get('Resources'))
			if Rules[depth1].get('Labels') is not None:
				for depth2 in range(len(Rules[depth1].get('Labels'))):
					if Rules[depth1].get('Labels')[depth2].get('Value') is not None:
						self.add_query_param('Rules.' + str(depth1 + 1) + str(depth2 + 1) + '.Value', Rules[depth1].get('Labels')[depth2].get('Value'))
					if Rules[depth1].get('Labels')[depth2].get('Key') is not None:
						self.add_query_param('Rules.' + str(depth1 + 1) + str(depth2 + 1) + '.Key', Rules[depth1].get('Labels')[depth2].get('Key'))
			if Rules[depth1].get('Escalations.Critical.Times') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Critical.Times', Rules[depth1].get('Escalations.Critical.Times'))
			if Rules[depth1].get('Escalations.Info.Threshold') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Info.Threshold', Rules[depth1].get('Escalations.Info.Threshold'))
			if Rules[depth1].get('Escalations.Warn.Statistics') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Warn.Statistics', Rules[depth1].get('Escalations.Warn.Statistics'))
			if Rules[depth1].get('Namespace') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Namespace', Rules[depth1].get('Namespace'))
			if Rules[depth1].get('Interval') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Interval', Rules[depth1].get('Interval'))
			if Rules[depth1].get('RuleId') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.RuleId', Rules[depth1].get('RuleId'))
			if Rules[depth1].get('Escalations.Critical.ComparisonOperator') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Critical.ComparisonOperator', Rules[depth1].get('Escalations.Critical.ComparisonOperator'))
			if Rules[depth1].get('Escalations.Critical.PreCondition') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Critical.PreCondition', Rules[depth1].get('Escalations.Critical.PreCondition'))
			if Rules[depth1].get('Escalations.Critical.Threshold') is not None:
				self.add_query_param('Rules.' + str(depth1 + 1) + '.Escalations.Critical.Threshold', Rules[depth1].get('Escalations.Critical.Threshold'))
