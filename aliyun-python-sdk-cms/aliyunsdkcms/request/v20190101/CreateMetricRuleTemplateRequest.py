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
class CreateMetricRuleTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateMetricRuleTemplate','cms')

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_AlertTemplatess(self):
		return self.get_query_params().get('AlertTemplatess')

	def set_AlertTemplatess(self,AlertTemplatess):
		for i in range(len(AlertTemplatess)):	
			if AlertTemplatess[i].get('Period') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Period' , AlertTemplatess[i].get('Period'))
			if AlertTemplatess[i].get('Escalations.Warn.Threshold') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Warn.Threshold' , AlertTemplatess[i].get('Escalations.Warn.Threshold'))
			if AlertTemplatess[i].get('Escalations.Warn.ComparisonOperator') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Warn.ComparisonOperator' , AlertTemplatess[i].get('Escalations.Warn.ComparisonOperator'))
			if AlertTemplatess[i].get('Escalations.Critical.Statistics') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Critical.Statistics' , AlertTemplatess[i].get('Escalations.Critical.Statistics'))
			if AlertTemplatess[i].get('Escalations.Info.Times') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Info.Times' , AlertTemplatess[i].get('Escalations.Info.Times'))
			if AlertTemplatess[i].get('RuleName') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.RuleName' , AlertTemplatess[i].get('RuleName'))
			if AlertTemplatess[i].get('Escalations.Info.Statistics') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Info.Statistics' , AlertTemplatess[i].get('Escalations.Info.Statistics'))
			if AlertTemplatess[i].get('Escalations.Critical.Times') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Critical.Times' , AlertTemplatess[i].get('Escalations.Critical.Times'))
			if AlertTemplatess[i].get('Escalations.Info.ComparisonOperator') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Info.ComparisonOperator' , AlertTemplatess[i].get('Escalations.Info.ComparisonOperator'))
			if AlertTemplatess[i].get('Escalations.Warn.Statistics') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Warn.Statistics' , AlertTemplatess[i].get('Escalations.Warn.Statistics'))
			if AlertTemplatess[i].get('Escalations.Info.Threshold') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Info.Threshold' , AlertTemplatess[i].get('Escalations.Info.Threshold'))
			if AlertTemplatess[i].get('Namespace') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Namespace' , AlertTemplatess[i].get('Namespace'))
			if AlertTemplatess[i].get('Selector') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Selector' , AlertTemplatess[i].get('Selector'))
			if AlertTemplatess[i].get('MetricName') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.MetricName' , AlertTemplatess[i].get('MetricName'))
			if AlertTemplatess[i].get('Category') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Category' , AlertTemplatess[i].get('Category'))
			if AlertTemplatess[i].get('Escalations.Critical.ComparisonOperator') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Critical.ComparisonOperator' , AlertTemplatess[i].get('Escalations.Critical.ComparisonOperator'))
			if AlertTemplatess[i].get('Escalations.Warn.Times') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Warn.Times' , AlertTemplatess[i].get('Escalations.Warn.Times'))
			if AlertTemplatess[i].get('Escalations.Critical.Threshold') is not None:
				self.add_query_param('AlertTemplates.' + str(i + 1) + '.Escalations.Critical.Threshold' , AlertTemplatess[i].get('Escalations.Critical.Threshold'))
