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

class CreateGroupMetricRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateGroupMetricRules','cms')
		self.set_method('POST')

	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_GroupMetricRuless(self): # RepeatList
		return self.get_query_params().get('GroupMetricRules')

	def set_GroupMetricRuless(self, GroupMetricRules):  # RepeatList
		for depth1 in range(len(GroupMetricRules)):
			if GroupMetricRules[depth1].get('Webhook') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Webhook', GroupMetricRules[depth1].get('Webhook'))
			if GroupMetricRules[depth1].get('Escalations.Warn.ComparisonOperator') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Warn.ComparisonOperator', GroupMetricRules[depth1].get('Escalations.Warn.ComparisonOperator'))
			if GroupMetricRules[depth1].get('DynamicAlertSensitivity') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.DynamicAlertSensitivity', GroupMetricRules[depth1].get('DynamicAlertSensitivity'))
			if GroupMetricRules[depth1].get('RuleName') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.RuleName', GroupMetricRules[depth1].get('RuleName'))
			if GroupMetricRules[depth1].get('Escalations.Info.Statistics') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Info.Statistics', GroupMetricRules[depth1].get('Escalations.Info.Statistics'))
			if GroupMetricRules[depth1].get('EffectiveInterval') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.EffectiveInterval', GroupMetricRules[depth1].get('EffectiveInterval'))
			if GroupMetricRules[depth1].get('DynamicAlertHistoryDataRange') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.DynamicAlertHistoryDataRange', GroupMetricRules[depth1].get('DynamicAlertHistoryDataRange'))
			if GroupMetricRules[depth1].get('Escalations.Warn.PreCondition') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Warn.PreCondition', GroupMetricRules[depth1].get('Escalations.Warn.PreCondition'))
			if GroupMetricRules[depth1].get('Escalations.Info.ComparisonOperator') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Info.ComparisonOperator', GroupMetricRules[depth1].get('Escalations.Info.ComparisonOperator'))
			if GroupMetricRules[depth1].get('NoDataPolicy') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.NoDataPolicy', GroupMetricRules[depth1].get('NoDataPolicy'))
			if GroupMetricRules[depth1].get('NoEffectiveInterval') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.NoEffectiveInterval', GroupMetricRules[depth1].get('NoEffectiveInterval'))
			if GroupMetricRules[depth1].get('EmailSubject') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.EmailSubject', GroupMetricRules[depth1].get('EmailSubject'))
			if GroupMetricRules[depth1].get('SilenceTime') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.SilenceTime', GroupMetricRules[depth1].get('SilenceTime'))
			if GroupMetricRules[depth1].get('Escalations.Info.PreCondition') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Info.PreCondition', GroupMetricRules[depth1].get('Escalations.Info.PreCondition'))
			if GroupMetricRules[depth1].get('MetricName') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.MetricName', GroupMetricRules[depth1].get('MetricName'))
			if GroupMetricRules[depth1].get('Escalations.Warn.Times') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Warn.Times', GroupMetricRules[depth1].get('Escalations.Warn.Times'))
			if GroupMetricRules[depth1].get('CompositeExpression') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.CompositeExpression', GroupMetricRules[depth1].get('CompositeExpression'))
			if GroupMetricRules[depth1].get('Escalations.Warn.Threshold') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Warn.Threshold', GroupMetricRules[depth1].get('Escalations.Warn.Threshold'))
			if GroupMetricRules[depth1].get('Period') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Period', GroupMetricRules[depth1].get('Period'))
			if GroupMetricRules[depth1].get('ContactGroups') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.ContactGroups', GroupMetricRules[depth1].get('ContactGroups'))
			if GroupMetricRules[depth1].get('Escalations.Critical.Statistics') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Critical.Statistics', GroupMetricRules[depth1].get('Escalations.Critical.Statistics'))
			if GroupMetricRules[depth1].get('RuleType') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.RuleType', GroupMetricRules[depth1].get('RuleType'))
			if GroupMetricRules[depth1].get('Escalations.Info.Times') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Info.Times', GroupMetricRules[depth1].get('Escalations.Info.Times'))
			if GroupMetricRules[depth1].get('ExtraDimensionJson') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.ExtraDimensionJson', GroupMetricRules[depth1].get('ExtraDimensionJson'))
			if GroupMetricRules[depth1].get('Labels') is not None:
				for depth2 in range(len(GroupMetricRules[depth1].get('Labels'))):
					if GroupMetricRules[depth1].get('Labels')[depth2].get('Value') is not None:
						self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Value', GroupMetricRules[depth1].get('Labels')[depth2].get('Value'))
					if GroupMetricRules[depth1].get('Labels')[depth2].get('Key') is not None:
						self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Key', GroupMetricRules[depth1].get('Labels')[depth2].get('Key'))
			if GroupMetricRules[depth1].get('Escalations.Critical.Times') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Critical.Times', GroupMetricRules[depth1].get('Escalations.Critical.Times'))
			if GroupMetricRules[depth1].get('Escalations.Info.Threshold') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Info.Threshold', GroupMetricRules[depth1].get('Escalations.Info.Threshold'))
			if GroupMetricRules[depth1].get('Escalations.Warn.Statistics') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Warn.Statistics', GroupMetricRules[depth1].get('Escalations.Warn.Statistics'))
			if GroupMetricRules[depth1].get('Namespace') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Namespace', GroupMetricRules[depth1].get('Namespace'))
			if GroupMetricRules[depth1].get('Interval') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Interval', GroupMetricRules[depth1].get('Interval'))
			if GroupMetricRules[depth1].get('RuleId') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.RuleId', GroupMetricRules[depth1].get('RuleId'))
			if GroupMetricRules[depth1].get('Category') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Category', GroupMetricRules[depth1].get('Category'))
			if GroupMetricRules[depth1].get('Escalations.Critical.ComparisonOperator') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Critical.ComparisonOperator', GroupMetricRules[depth1].get('Escalations.Critical.ComparisonOperator'))
			if GroupMetricRules[depth1].get('Escalations.Critical.PreCondition') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Critical.PreCondition', GroupMetricRules[depth1].get('Escalations.Critical.PreCondition'))
			if GroupMetricRules[depth1].get('Escalations.Critical.Threshold') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Critical.Threshold', GroupMetricRules[depth1].get('Escalations.Critical.Threshold'))
			if GroupMetricRules[depth1].get('Dimensions') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Dimensions', GroupMetricRules[depth1].get('Dimensions'))
