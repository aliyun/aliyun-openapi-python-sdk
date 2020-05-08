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

	def get_Ruless(self):
		return self.get_query_params().get('Ruless')

	def set_Ruless(self,Ruless):
		for i in range(len(Ruless)):	
			if Ruless[i].get('Webhook') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Webhook' , Ruless[i].get('Webhook'))
			if Ruless[i].get('Escalations.Warn.ComparisonOperator') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Warn.ComparisonOperator' , Ruless[i].get('Escalations.Warn.ComparisonOperator'))
			if Ruless[i].get('RuleName') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.RuleName' , Ruless[i].get('RuleName'))
			if Ruless[i].get('Escalations.Info.Statistics') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Info.Statistics' , Ruless[i].get('Escalations.Info.Statistics'))
			if Ruless[i].get('EffectiveInterval') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.EffectiveInterval' , Ruless[i].get('EffectiveInterval'))
			if Ruless[i].get('Escalations.Info.ComparisonOperator') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Info.ComparisonOperator' , Ruless[i].get('Escalations.Info.ComparisonOperator'))
			if Ruless[i].get('NoEffectiveInterval') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.NoEffectiveInterval' , Ruless[i].get('NoEffectiveInterval'))
			if Ruless[i].get('EmailSubject') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.EmailSubject' , Ruless[i].get('EmailSubject'))
			if Ruless[i].get('SilenceTime') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.SilenceTime' , Ruless[i].get('SilenceTime'))
			if Ruless[i].get('MetricName') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.MetricName' , Ruless[i].get('MetricName'))
			if Ruless[i].get('Escalations.Warn.Times') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Warn.Times' , Ruless[i].get('Escalations.Warn.Times'))
			if Ruless[i].get('Period') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Period' , Ruless[i].get('Period'))
			if Ruless[i].get('Escalations.Warn.Threshold') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Warn.Threshold' , Ruless[i].get('Escalations.Warn.Threshold'))
			if Ruless[i].get('ContactGroups') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.ContactGroups' , Ruless[i].get('ContactGroups'))
			if Ruless[i].get('Escalations.Critical.Statistics') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Critical.Statistics' , Ruless[i].get('Escalations.Critical.Statistics'))
			if Ruless[i].get('Resources') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Resources' , Ruless[i].get('Resources'))
			if Ruless[i].get('Escalations.Info.Times') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Info.Times' , Ruless[i].get('Escalations.Info.Times'))
			if Ruless[i].get('Escalations.Critical.Times') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Critical.Times' , Ruless[i].get('Escalations.Critical.Times'))
			if Ruless[i].get('Escalations.Warn.Statistics') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Warn.Statistics' , Ruless[i].get('Escalations.Warn.Statistics'))
			if Ruless[i].get('Escalations.Info.Threshold') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Info.Threshold' , Ruless[i].get('Escalations.Info.Threshold'))
			if Ruless[i].get('Namespace') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Namespace' , Ruless[i].get('Namespace'))
			if Ruless[i].get('Interval') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Interval' , Ruless[i].get('Interval'))
			if Ruless[i].get('RuleId') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.RuleId' , Ruless[i].get('RuleId'))
			if Ruless[i].get('Escalations.Critical.ComparisonOperator') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Critical.ComparisonOperator' , Ruless[i].get('Escalations.Critical.ComparisonOperator'))
			if Ruless[i].get('Escalations.Critical.Threshold') is not None:
				self.add_query_param('Rules.' + str(i + 1) + '.Escalations.Critical.Threshold' , Ruless[i].get('Escalations.Critical.Threshold'))
