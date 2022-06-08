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
import json

class PutResourceMetricRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutResourceMetricRule','cms')
		self.set_method('POST')

	def get_Webhook(self): # String
		return self.get_query_params().get('Webhook')

	def set_Webhook(self, Webhook):  # String
		self.add_query_param('Webhook', Webhook)
	def get_EscalationsWarnComparisonOperator(self): # String
		return self.get_query_params().get('Escalations.Warn.ComparisonOperator')

	def set_EscalationsWarnComparisonOperator(self, EscalationsWarnComparisonOperator):  # String
		self.add_query_param('Escalations.Warn.ComparisonOperator', EscalationsWarnComparisonOperator)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_EffectiveInterval(self): # String
		return self.get_query_params().get('EffectiveInterval')

	def set_EffectiveInterval(self, EffectiveInterval):  # String
		self.add_query_param('EffectiveInterval', EffectiveInterval)
	def get_NoDataPolicy(self): # String
		return self.get_query_params().get('NoDataPolicy')

	def set_NoDataPolicy(self, NoDataPolicy):  # String
		self.add_query_param('NoDataPolicy', NoDataPolicy)
	def get_NoEffectiveInterval(self): # String
		return self.get_query_params().get('NoEffectiveInterval')

	def set_NoEffectiveInterval(self, NoEffectiveInterval):  # String
		self.add_query_param('NoEffectiveInterval', NoEffectiveInterval)
	def get_EmailSubject(self): # String
		return self.get_query_params().get('EmailSubject')

	def set_EmailSubject(self, EmailSubject):  # String
		self.add_query_param('EmailSubject', EmailSubject)
	def get_MetricName(self): # String
		return self.get_query_params().get('MetricName')

	def set_MetricName(self, MetricName):  # String
		self.add_query_param('MetricName', MetricName)
	def get_EscalationsWarnTimes(self): # Integer
		return self.get_query_params().get('Escalations.Warn.Times')

	def set_EscalationsWarnTimes(self, EscalationsWarnTimes):  # Integer
		self.add_query_param('Escalations.Warn.Times', EscalationsWarnTimes)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_EscalationsWarnThreshold(self): # String
		return self.get_query_params().get('Escalations.Warn.Threshold')

	def set_EscalationsWarnThreshold(self, EscalationsWarnThreshold):  # String
		self.add_query_param('Escalations.Warn.Threshold', EscalationsWarnThreshold)
	def get_ContactGroups(self): # String
		return self.get_query_params().get('ContactGroups')

	def set_ContactGroups(self, ContactGroups):  # String
		self.add_query_param('ContactGroups', ContactGroups)
	def get_EscalationsCriticalStatistics(self): # String
		return self.get_query_params().get('Escalations.Critical.Statistics')

	def set_EscalationsCriticalStatistics(self, EscalationsCriticalStatistics):  # String
		self.add_query_param('Escalations.Critical.Statistics', EscalationsCriticalStatistics)
	def get_Labelss(self): # RepeatList
		return self.get_query_params().get('Labels')

	def set_Labelss(self, Labels):  # RepeatList
		for depth1 in range(len(Labels)):
			if Labels[depth1].get('Value') is not None:
				self.add_query_param('Labels.' + str(depth1 + 1) + '.Value', Labels[depth1].get('Value'))
			if Labels[depth1].get('Key') is not None:
				self.add_query_param('Labels.' + str(depth1 + 1) + '.Key', Labels[depth1].get('Key'))
	def get_Interval(self): # String
		return self.get_query_params().get('Interval')

	def set_Interval(self, Interval):  # String
		self.add_query_param('Interval', Interval)
	def get_RuleId(self): # String
		return self.get_query_params().get('RuleId')

	def set_RuleId(self, RuleId):  # String
		self.add_query_param('RuleId', RuleId)
	def get_EscalationsCriticalThreshold(self): # String
		return self.get_query_params().get('Escalations.Critical.Threshold')

	def set_EscalationsCriticalThreshold(self, EscalationsCriticalThreshold):  # String
		self.add_query_param('Escalations.Critical.Threshold', EscalationsCriticalThreshold)
	def get_EscalationsInfoStatistics(self): # String
		return self.get_query_params().get('Escalations.Info.Statistics')

	def set_EscalationsInfoStatistics(self, EscalationsInfoStatistics):  # String
		self.add_query_param('Escalations.Info.Statistics', EscalationsInfoStatistics)
	def get_EscalationsInfoComparisonOperator(self): # String
		return self.get_query_params().get('Escalations.Info.ComparisonOperator')

	def set_EscalationsInfoComparisonOperator(self, EscalationsInfoComparisonOperator):  # String
		self.add_query_param('Escalations.Info.ComparisonOperator', EscalationsInfoComparisonOperator)
	def get_SilenceTime(self): # Integer
		return self.get_query_params().get('SilenceTime')

	def set_SilenceTime(self, SilenceTime):  # Integer
		self.add_query_param('SilenceTime', SilenceTime)
	def get_Prometheus(self): # Struct
		return self.get_query_params().get('Prometheus')

	def set_Prometheus(self, Prometheus):  # Struct
		self.add_query_param("Prometheus", json.dumps(Prometheus))
	def get_CompositeExpression(self): # Struct
		return self.get_query_params().get('CompositeExpression')

	def set_CompositeExpression(self, CompositeExpression):  # Struct
		self.add_query_param("CompositeExpression", json.dumps(CompositeExpression))
	def get_Resources(self): # String
		return self.get_query_params().get('Resources')

	def set_Resources(self, Resources):  # String
		self.add_query_param('Resources', Resources)
	def get_EscalationsInfoTimes(self): # Integer
		return self.get_query_params().get('Escalations.Info.Times')

	def set_EscalationsInfoTimes(self, EscalationsInfoTimes):  # Integer
		self.add_query_param('Escalations.Info.Times', EscalationsInfoTimes)
	def get_EscalationsCriticalTimes(self): # Integer
		return self.get_query_params().get('Escalations.Critical.Times')

	def set_EscalationsCriticalTimes(self, EscalationsCriticalTimes):  # Integer
		self.add_query_param('Escalations.Critical.Times', EscalationsCriticalTimes)
	def get_EscalationsWarnStatistics(self): # String
		return self.get_query_params().get('Escalations.Warn.Statistics')

	def set_EscalationsWarnStatistics(self, EscalationsWarnStatistics):  # String
		self.add_query_param('Escalations.Warn.Statistics', EscalationsWarnStatistics)
	def get_EscalationsInfoThreshold(self): # String
		return self.get_query_params().get('Escalations.Info.Threshold')

	def set_EscalationsInfoThreshold(self, EscalationsInfoThreshold):  # String
		self.add_query_param('Escalations.Info.Threshold', EscalationsInfoThreshold)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_EscalationsCriticalComparisonOperator(self): # String
		return self.get_query_params().get('Escalations.Critical.ComparisonOperator')

	def set_EscalationsCriticalComparisonOperator(self, EscalationsCriticalComparisonOperator):  # String
		self.add_query_param('Escalations.Critical.ComparisonOperator', EscalationsCriticalComparisonOperator)
