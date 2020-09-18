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

class CreateMetricRuleTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateMetricRuleTemplate','cms')
		self.set_method('POST')

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_AlertTemplatess(self):
		return self.get_query_params().get('AlertTemplates')

	def set_AlertTemplatess(self, AlertTemplatess):
		for depth1 in range(len(AlertTemplatess)):
			if AlertTemplatess[depth1].get('Period') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Period', AlertTemplatess[depth1].get('Period'))
			if AlertTemplatess[depth1].get('Escalations.Warn.Threshold') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Warn.Threshold', AlertTemplatess[depth1].get('Escalations.Warn.Threshold'))
			if AlertTemplatess[depth1].get('Webhook') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Webhook', AlertTemplatess[depth1].get('Webhook'))
			if AlertTemplatess[depth1].get('Escalations.Warn.ComparisonOperator') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Warn.ComparisonOperator', AlertTemplatess[depth1].get('Escalations.Warn.ComparisonOperator'))
			if AlertTemplatess[depth1].get('Escalations.Critical.Statistics') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Critical.Statistics', AlertTemplatess[depth1].get('Escalations.Critical.Statistics'))
			if AlertTemplatess[depth1].get('Escalations.Info.Times') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Info.Times', AlertTemplatess[depth1].get('Escalations.Info.Times'))
			if AlertTemplatess[depth1].get('RuleName') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.RuleName', AlertTemplatess[depth1].get('RuleName'))
			if AlertTemplatess[depth1].get('Escalations.Info.Statistics') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Info.Statistics', AlertTemplatess[depth1].get('Escalations.Info.Statistics'))
			if AlertTemplatess[depth1].get('Escalations.Critical.Times') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Critical.Times', AlertTemplatess[depth1].get('Escalations.Critical.Times'))
			if AlertTemplatess[depth1].get('Escalations.Info.ComparisonOperator') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Info.ComparisonOperator', AlertTemplatess[depth1].get('Escalations.Info.ComparisonOperator'))
			if AlertTemplatess[depth1].get('Escalations.Warn.Statistics') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Warn.Statistics', AlertTemplatess[depth1].get('Escalations.Warn.Statistics'))
			if AlertTemplatess[depth1].get('Escalations.Info.Threshold') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Info.Threshold', AlertTemplatess[depth1].get('Escalations.Info.Threshold'))
			if AlertTemplatess[depth1].get('Namespace') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Namespace', AlertTemplatess[depth1].get('Namespace'))
			if AlertTemplatess[depth1].get('Selector') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Selector', AlertTemplatess[depth1].get('Selector'))
			if AlertTemplatess[depth1].get('MetricName') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.MetricName', AlertTemplatess[depth1].get('MetricName'))
			if AlertTemplatess[depth1].get('Category') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Category', AlertTemplatess[depth1].get('Category'))
			if AlertTemplatess[depth1].get('Escalations.Critical.ComparisonOperator') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Critical.ComparisonOperator', AlertTemplatess[depth1].get('Escalations.Critical.ComparisonOperator'))
			if AlertTemplatess[depth1].get('Escalations.Warn.Times') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Warn.Times', AlertTemplatess[depth1].get('Escalations.Warn.Times'))
			if AlertTemplatess[depth1].get('Escalations.Critical.Threshold') is not None:
				self.add_query_param('AlertTemplates.' + str(depth1 + 1) + '.Escalations.Critical.Threshold', AlertTemplatess[depth1].get('Escalations.Critical.Threshold'))