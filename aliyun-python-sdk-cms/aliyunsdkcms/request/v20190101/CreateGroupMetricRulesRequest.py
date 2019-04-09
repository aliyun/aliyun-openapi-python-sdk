# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
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

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_GroupMetricRuless(self):
		return self.get_query_params().get('GroupMetricRuless')

	def set_GroupMetricRuless(self,GroupMetricRuless):
		for i in range(len(GroupMetricRuless)):	
			if GroupMetricRuless[i].get('Webhook') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Webhook' , GroupMetricRuless[i].get('Webhook'))
			if GroupMetricRuless[i].get('Escalations.Warn.ComparisonOperator') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Warn.ComparisonOperator' , GroupMetricRuless[i].get('Escalations.Warn.ComparisonOperator'))
			if GroupMetricRuless[i].get('RuleName') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.RuleName' , GroupMetricRuless[i].get('RuleName'))
			if GroupMetricRuless[i].get('Escalations.Info.Statistics') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Info.Statistics' , GroupMetricRuless[i].get('Escalations.Info.Statistics'))
			if GroupMetricRuless[i].get('EffectiveInterval') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.EffectiveInterval' , GroupMetricRuless[i].get('EffectiveInterval'))
			if GroupMetricRuless[i].get('Escalations.Info.ComparisonOperator') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Info.ComparisonOperator' , GroupMetricRuless[i].get('Escalations.Info.ComparisonOperator'))
			if GroupMetricRuless[i].get('NoEffectiveInterval') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.NoEffectiveInterval' , GroupMetricRuless[i].get('NoEffectiveInterval'))
			if GroupMetricRuless[i].get('EmailSubject') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.EmailSubject' , GroupMetricRuless[i].get('EmailSubject'))
			if GroupMetricRuless[i].get('SilenceTime') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.SilenceTime' , GroupMetricRuless[i].get('SilenceTime'))
			if GroupMetricRuless[i].get('MetricName') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.MetricName' , GroupMetricRuless[i].get('MetricName'))
			if GroupMetricRuless[i].get('Escalations.Warn.Times') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Warn.Times' , GroupMetricRuless[i].get('Escalations.Warn.Times'))
			if GroupMetricRuless[i].get('Period') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Period' , GroupMetricRuless[i].get('Period'))
			if GroupMetricRuless[i].get('Escalations.Warn.Threshold') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Warn.Threshold' , GroupMetricRuless[i].get('Escalations.Warn.Threshold'))
			if GroupMetricRuless[i].get('Escalations.Critical.Statistics') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Critical.Statistics' , GroupMetricRuless[i].get('Escalations.Critical.Statistics'))
			if GroupMetricRuless[i].get('Escalations.Info.Times') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Info.Times' , GroupMetricRuless[i].get('Escalations.Info.Times'))
			if GroupMetricRuless[i].get('Escalations.Critical.Times') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Critical.Times' , GroupMetricRuless[i].get('Escalations.Critical.Times'))
			if GroupMetricRuless[i].get('Escalations.Warn.Statistics') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Warn.Statistics' , GroupMetricRuless[i].get('Escalations.Warn.Statistics'))
			if GroupMetricRuless[i].get('Escalations.Info.Threshold') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Info.Threshold' , GroupMetricRuless[i].get('Escalations.Info.Threshold'))
			if GroupMetricRuless[i].get('Namespace') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Namespace' , GroupMetricRuless[i].get('Namespace'))
			if GroupMetricRuless[i].get('Interval') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Interval' , GroupMetricRuless[i].get('Interval'))
			if GroupMetricRuless[i].get('Category') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Category' , GroupMetricRuless[i].get('Category'))
			if GroupMetricRuless[i].get('RuleId') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.RuleId' , GroupMetricRuless[i].get('RuleId'))
			if GroupMetricRuless[i].get('Escalations.Critical.ComparisonOperator') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Critical.ComparisonOperator' , GroupMetricRuless[i].get('Escalations.Critical.ComparisonOperator'))
			if GroupMetricRuless[i].get('Escalations.Critical.Threshold') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Escalations.Critical.Threshold' , GroupMetricRuless[i].get('Escalations.Critical.Threshold'))
			if GroupMetricRuless[i].get('Dimensions') is not None:
				self.add_query_param('GroupMetricRules.' + str(i + 1) + '.Dimensions' , GroupMetricRuless[i].get('Dimensions'))
