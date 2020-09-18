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

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_GroupMetricRuless(self):
		return self.get_query_params().get('GroupMetricRules')

	def set_GroupMetricRuless(self, GroupMetricRuless):
		for depth1 in range(len(GroupMetricRuless)):
			if GroupMetricRuless[depth1].get('Webhook') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Webhook', GroupMetricRuless[depth1].get('Webhook'))
			if GroupMetricRuless[depth1].get('Escalations.Warn.ComparisonOperator') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Warn.ComparisonOperator', GroupMetricRuless[depth1].get('Escalations.Warn.ComparisonOperator'))
			if GroupMetricRuless[depth1].get('RuleName') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.RuleName', GroupMetricRuless[depth1].get('RuleName'))
			if GroupMetricRuless[depth1].get('Escalations.Info.Statistics') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Info.Statistics', GroupMetricRuless[depth1].get('Escalations.Info.Statistics'))
			if GroupMetricRuless[depth1].get('EffectiveInterval') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.EffectiveInterval', GroupMetricRuless[depth1].get('EffectiveInterval'))
			if GroupMetricRuless[depth1].get('Escalations.Info.ComparisonOperator') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Info.ComparisonOperator', GroupMetricRuless[depth1].get('Escalations.Info.ComparisonOperator'))
			if GroupMetricRuless[depth1].get('NoEffectiveInterval') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.NoEffectiveInterval', GroupMetricRuless[depth1].get('NoEffectiveInterval'))
			if GroupMetricRuless[depth1].get('EmailSubject') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.EmailSubject', GroupMetricRuless[depth1].get('EmailSubject'))
			if GroupMetricRuless[depth1].get('SilenceTime') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.SilenceTime', GroupMetricRuless[depth1].get('SilenceTime'))
			if GroupMetricRuless[depth1].get('MetricName') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.MetricName', GroupMetricRuless[depth1].get('MetricName'))
			if GroupMetricRuless[depth1].get('Escalations.Warn.Times') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Warn.Times', GroupMetricRuless[depth1].get('Escalations.Warn.Times'))
			if GroupMetricRuless[depth1].get('Period') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Period', GroupMetricRuless[depth1].get('Period'))
			if GroupMetricRuless[depth1].get('Escalations.Warn.Threshold') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Warn.Threshold', GroupMetricRuless[depth1].get('Escalations.Warn.Threshold'))
			if GroupMetricRuless[depth1].get('Escalations.Critical.Statistics') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Critical.Statistics', GroupMetricRuless[depth1].get('Escalations.Critical.Statistics'))
			if GroupMetricRuless[depth1].get('Escalations.Info.Times') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Info.Times', GroupMetricRuless[depth1].get('Escalations.Info.Times'))
			if GroupMetricRuless[depth1].get('Escalations.Critical.Times') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Critical.Times', GroupMetricRuless[depth1].get('Escalations.Critical.Times'))
			if GroupMetricRuless[depth1].get('Escalations.Warn.Statistics') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Warn.Statistics', GroupMetricRuless[depth1].get('Escalations.Warn.Statistics'))
			if GroupMetricRuless[depth1].get('Escalations.Info.Threshold') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Info.Threshold', GroupMetricRuless[depth1].get('Escalations.Info.Threshold'))
			if GroupMetricRuless[depth1].get('Namespace') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Namespace', GroupMetricRuless[depth1].get('Namespace'))
			if GroupMetricRuless[depth1].get('Interval') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Interval', GroupMetricRuless[depth1].get('Interval'))
			if GroupMetricRuless[depth1].get('Category') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Category', GroupMetricRuless[depth1].get('Category'))
			if GroupMetricRuless[depth1].get('RuleId') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.RuleId', GroupMetricRuless[depth1].get('RuleId'))
			if GroupMetricRuless[depth1].get('Escalations.Critical.ComparisonOperator') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Critical.ComparisonOperator', GroupMetricRuless[depth1].get('Escalations.Critical.ComparisonOperator'))
			if GroupMetricRuless[depth1].get('Escalations.Critical.Threshold') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Escalations.Critical.Threshold', GroupMetricRuless[depth1].get('Escalations.Critical.Threshold'))
			if GroupMetricRuless[depth1].get('Dimensions') is not None:
				self.add_query_param('GroupMetricRules.' + str(depth1 + 1) + '.Dimensions', GroupMetricRuless[depth1].get('Dimensions'))