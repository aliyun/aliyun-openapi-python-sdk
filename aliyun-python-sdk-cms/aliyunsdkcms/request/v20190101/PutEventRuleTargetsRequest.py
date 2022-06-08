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

class PutEventRuleTargetsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutEventRuleTargets','cms')
		self.set_method('POST')

	def get_WebhookParameterss(self): # RepeatList
		return self.get_query_params().get('WebhookParameters')

	def set_WebhookParameterss(self, WebhookParameters):  # RepeatList
		for depth1 in range(len(WebhookParameters)):
			if WebhookParameters[depth1].get('Protocol') is not None:
				self.add_query_param('WebhookParameters.' + str(depth1 + 1) + '.Protocol', WebhookParameters[depth1].get('Protocol'))
			if WebhookParameters[depth1].get('Method') is not None:
				self.add_query_param('WebhookParameters.' + str(depth1 + 1) + '.Method', WebhookParameters[depth1].get('Method'))
			if WebhookParameters[depth1].get('Id') is not None:
				self.add_query_param('WebhookParameters.' + str(depth1 + 1) + '.Id', WebhookParameters[depth1].get('Id'))
			if WebhookParameters[depth1].get('Url') is not None:
				self.add_query_param('WebhookParameters.' + str(depth1 + 1) + '.Url', WebhookParameters[depth1].get('Url'))
	def get_ContactParameterss(self): # RepeatList
		return self.get_query_params().get('ContactParameters')

	def set_ContactParameterss(self, ContactParameters):  # RepeatList
		for depth1 in range(len(ContactParameters)):
			if ContactParameters[depth1].get('Level') is not None:
				self.add_query_param('ContactParameters.' + str(depth1 + 1) + '.Level', ContactParameters[depth1].get('Level'))
			if ContactParameters[depth1].get('Id') is not None:
				self.add_query_param('ContactParameters.' + str(depth1 + 1) + '.Id', ContactParameters[depth1].get('Id'))
			if ContactParameters[depth1].get('ContactGroupName') is not None:
				self.add_query_param('ContactParameters.' + str(depth1 + 1) + '.ContactGroupName', ContactParameters[depth1].get('ContactGroupName'))
	def get_SlsParameterss(self): # RepeatList
		return self.get_query_params().get('SlsParameters')

	def set_SlsParameterss(self, SlsParameters):  # RepeatList
		for depth1 in range(len(SlsParameters)):
			if SlsParameters[depth1].get('Project') is not None:
				self.add_query_param('SlsParameters.' + str(depth1 + 1) + '.Project', SlsParameters[depth1].get('Project'))
			if SlsParameters[depth1].get('Id') is not None:
				self.add_query_param('SlsParameters.' + str(depth1 + 1) + '.Id', SlsParameters[depth1].get('Id'))
			if SlsParameters[depth1].get('Region') is not None:
				self.add_query_param('SlsParameters.' + str(depth1 + 1) + '.Region', SlsParameters[depth1].get('Region'))
			if SlsParameters[depth1].get('LogStore') is not None:
				self.add_query_param('SlsParameters.' + str(depth1 + 1) + '.LogStore', SlsParameters[depth1].get('LogStore'))
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_OpenApiParameterss(self): # RepeatList
		return self.get_query_params().get('OpenApiParameters')

	def set_OpenApiParameterss(self, OpenApiParameters):  # RepeatList
		for depth1 in range(len(OpenApiParameters)):
			if OpenApiParameters[depth1].get('Product') is not None:
				self.add_query_param('OpenApiParameters.' + str(depth1 + 1) + '.Product', OpenApiParameters[depth1].get('Product'))
			if OpenApiParameters[depth1].get('Role') is not None:
				self.add_query_param('OpenApiParameters.' + str(depth1 + 1) + '.Role', OpenApiParameters[depth1].get('Role'))
			if OpenApiParameters[depth1].get('Action') is not None:
				self.add_query_param('OpenApiParameters.' + str(depth1 + 1) + '.Action', OpenApiParameters[depth1].get('Action'))
			if OpenApiParameters[depth1].get('Id') is not None:
				self.add_query_param('OpenApiParameters.' + str(depth1 + 1) + '.Id', OpenApiParameters[depth1].get('Id'))
			if OpenApiParameters[depth1].get('Arn') is not None:
				self.add_query_param('OpenApiParameters.' + str(depth1 + 1) + '.Arn', OpenApiParameters[depth1].get('Arn'))
			if OpenApiParameters[depth1].get('Region') is not None:
				self.add_query_param('OpenApiParameters.' + str(depth1 + 1) + '.Region', OpenApiParameters[depth1].get('Region'))
			if OpenApiParameters[depth1].get('Version') is not None:
				self.add_query_param('OpenApiParameters.' + str(depth1 + 1) + '.Version', OpenApiParameters[depth1].get('Version'))
			if OpenApiParameters[depth1].get('JsonParams') is not None:
				self.add_query_param('OpenApiParameters.' + str(depth1 + 1) + '.JsonParams', OpenApiParameters[depth1].get('JsonParams'))
	def get_MnsParameterss(self): # RepeatList
		return self.get_query_params().get('MnsParameters')

	def set_MnsParameterss(self, MnsParameters):  # RepeatList
		for depth1 in range(len(MnsParameters)):
			if MnsParameters[depth1].get('Topic') is not None:
				self.add_query_param('MnsParameters.' + str(depth1 + 1) + '.Topic', MnsParameters[depth1].get('Topic'))
			if MnsParameters[depth1].get('Id') is not None:
				self.add_query_param('MnsParameters.' + str(depth1 + 1) + '.Id', MnsParameters[depth1].get('Id'))
			if MnsParameters[depth1].get('Region') is not None:
				self.add_query_param('MnsParameters.' + str(depth1 + 1) + '.Region', MnsParameters[depth1].get('Region'))
			if MnsParameters[depth1].get('Queue') is not None:
				self.add_query_param('MnsParameters.' + str(depth1 + 1) + '.Queue', MnsParameters[depth1].get('Queue'))
	def get_FcParameterss(self): # RepeatList
		return self.get_query_params().get('FcParameters')

	def set_FcParameterss(self, FcParameters):  # RepeatList
		for depth1 in range(len(FcParameters)):
			if FcParameters[depth1].get('FunctionName') is not None:
				self.add_query_param('FcParameters.' + str(depth1 + 1) + '.FunctionName', FcParameters[depth1].get('FunctionName'))
			if FcParameters[depth1].get('ServiceName') is not None:
				self.add_query_param('FcParameters.' + str(depth1 + 1) + '.ServiceName', FcParameters[depth1].get('ServiceName'))
			if FcParameters[depth1].get('Id') is not None:
				self.add_query_param('FcParameters.' + str(depth1 + 1) + '.Id', FcParameters[depth1].get('Id'))
			if FcParameters[depth1].get('Region') is not None:
				self.add_query_param('FcParameters.' + str(depth1 + 1) + '.Region', FcParameters[depth1].get('Region'))
