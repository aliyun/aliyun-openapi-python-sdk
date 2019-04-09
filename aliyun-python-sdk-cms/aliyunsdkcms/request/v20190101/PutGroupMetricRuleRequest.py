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
class PutGroupMetricRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutGroupMetricRule','cms')

	def get_Webhook(self):
		return self.get_query_params().get('Webhook')

	def set_Webhook(self,Webhook):
		self.add_query_param('Webhook',Webhook)

	def get_EscalationsWarnComparisonOperator(self):
		return self.get_query_params().get('Escalations.Warn.ComparisonOperator')

	def set_EscalationsWarnComparisonOperator(self,EscalationsWarnComparisonOperator):
		self.add_query_param('Escalations.Warn.ComparisonOperator',EscalationsWarnComparisonOperator)

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_EscalationsInfoStatistics(self):
		return self.get_query_params().get('Escalations.Info.Statistics')

	def set_EscalationsInfoStatistics(self,EscalationsInfoStatistics):
		self.add_query_param('Escalations.Info.Statistics',EscalationsInfoStatistics)

	def get_EffectiveInterval(self):
		return self.get_query_params().get('EffectiveInterval')

	def set_EffectiveInterval(self,EffectiveInterval):
		self.add_query_param('EffectiveInterval',EffectiveInterval)

	def get_EscalationsInfoComparisonOperator(self):
		return self.get_query_params().get('Escalations.Info.ComparisonOperator')

	def set_EscalationsInfoComparisonOperator(self,EscalationsInfoComparisonOperator):
		self.add_query_param('Escalations.Info.ComparisonOperator',EscalationsInfoComparisonOperator)

	def get_NoEffectiveInterval(self):
		return self.get_query_params().get('NoEffectiveInterval')

	def set_NoEffectiveInterval(self,NoEffectiveInterval):
		self.add_query_param('NoEffectiveInterval',NoEffectiveInterval)

	def get_EmailSubject(self):
		return self.get_query_params().get('EmailSubject')

	def set_EmailSubject(self,EmailSubject):
		self.add_query_param('EmailSubject',EmailSubject)

	def get_SilenceTime(self):
		return self.get_query_params().get('SilenceTime')

	def set_SilenceTime(self,SilenceTime):
		self.add_query_param('SilenceTime',SilenceTime)

	def get_MetricName(self):
		return self.get_query_params().get('MetricName')

	def set_MetricName(self,MetricName):
		self.add_query_param('MetricName',MetricName)

	def get_EscalationsWarnTimes(self):
		return self.get_query_params().get('Escalations.Warn.Times')

	def set_EscalationsWarnTimes(self,EscalationsWarnTimes):
		self.add_query_param('Escalations.Warn.Times',EscalationsWarnTimes)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_EscalationsWarnThreshold(self):
		return self.get_query_params().get('Escalations.Warn.Threshold')

	def set_EscalationsWarnThreshold(self,EscalationsWarnThreshold):
		self.add_query_param('Escalations.Warn.Threshold',EscalationsWarnThreshold)

	def get_EscalationsCriticalStatistics(self):
		return self.get_query_params().get('Escalations.Critical.Statistics')

	def set_EscalationsCriticalStatistics(self,EscalationsCriticalStatistics):
		self.add_query_param('Escalations.Critical.Statistics',EscalationsCriticalStatistics)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_EscalationsInfoTimes(self):
		return self.get_query_params().get('Escalations.Info.Times')

	def set_EscalationsInfoTimes(self,EscalationsInfoTimes):
		self.add_query_param('Escalations.Info.Times',EscalationsInfoTimes)

	def get_EscalationsCriticalTimes(self):
		return self.get_query_params().get('Escalations.Critical.Times')

	def set_EscalationsCriticalTimes(self,EscalationsCriticalTimes):
		self.add_query_param('Escalations.Critical.Times',EscalationsCriticalTimes)

	def get_EscalationsWarnStatistics(self):
		return self.get_query_params().get('Escalations.Warn.Statistics')

	def set_EscalationsWarnStatistics(self,EscalationsWarnStatistics):
		self.add_query_param('Escalations.Warn.Statistics',EscalationsWarnStatistics)

	def get_EscalationsInfoThreshold(self):
		return self.get_query_params().get('Escalations.Info.Threshold')

	def set_EscalationsInfoThreshold(self,EscalationsInfoThreshold):
		self.add_query_param('Escalations.Info.Threshold',EscalationsInfoThreshold)

	def get_Namespace(self):
		return self.get_query_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_query_param('Namespace',Namespace)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)

	def get_RuleId(self):
		return self.get_query_params().get('RuleId')

	def set_RuleId(self,RuleId):
		self.add_query_param('RuleId',RuleId)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_EscalationsCriticalComparisonOperator(self):
		return self.get_query_params().get('Escalations.Critical.ComparisonOperator')

	def set_EscalationsCriticalComparisonOperator(self,EscalationsCriticalComparisonOperator):
		self.add_query_param('Escalations.Critical.ComparisonOperator',EscalationsCriticalComparisonOperator)

	def get_EscalationsCriticalThreshold(self):
		return self.get_query_params().get('Escalations.Critical.Threshold')

	def set_EscalationsCriticalThreshold(self,EscalationsCriticalThreshold):
		self.add_query_param('Escalations.Critical.Threshold',EscalationsCriticalThreshold)

	def get_Dimensions(self):
		return self.get_query_params().get('Dimensions')

	def set_Dimensions(self,Dimensions):
		self.add_query_param('Dimensions',Dimensions)