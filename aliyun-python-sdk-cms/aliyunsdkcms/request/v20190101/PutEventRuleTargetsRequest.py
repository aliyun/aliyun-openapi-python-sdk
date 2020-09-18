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

	def get_WebhookParameterss(self):
		return self.get_query_params().get('WebhookParameters')

	def set_WebhookParameterss(self, WebhookParameterss):
		for depth1 in range(len(WebhookParameterss)):
			if WebhookParameterss[depth1].get('Protocol') is not None:
				self.add_query_param('WebhookParameters.' + str(depth1 + 1) + '.Protocol', WebhookParameterss[depth1].get('Protocol'))
			if WebhookParameterss[depth1].get('Method') is not None:
				self.add_query_param('WebhookParameters.' + str(depth1 + 1) + '.Method', WebhookParameterss[depth1].get('Method'))
			if WebhookParameterss[depth1].get('Id') is not None:
				self.add_query_param('WebhookParameters.' + str(depth1 + 1) + '.Id', WebhookParameterss[depth1].get('Id'))
			if WebhookParameterss[depth1].get('Url') is not None:
				self.add_query_param('WebhookParameters.' + str(depth1 + 1) + '.Url', WebhookParameterss[depth1].get('Url'))

	def get_ContactParameterss(self):
		return self.get_query_params().get('ContactParameters')

	def set_ContactParameterss(self, ContactParameterss):
		for depth1 in range(len(ContactParameterss)):
			if ContactParameterss[depth1].get('Level') is not None:
				self.add_query_param('ContactParameters.' + str(depth1 + 1) + '.Level', ContactParameterss[depth1].get('Level'))
			if ContactParameterss[depth1].get('Id') is not None:
				self.add_query_param('ContactParameters.' + str(depth1 + 1) + '.Id', ContactParameterss[depth1].get('Id'))
			if ContactParameterss[depth1].get('ContactGroupName') is not None:
				self.add_query_param('ContactParameters.' + str(depth1 + 1) + '.ContactGroupName', ContactParameterss[depth1].get('ContactGroupName'))

	def get_SlsParameterss(self):
		return self.get_query_params().get('SlsParameters')

	def set_SlsParameterss(self, SlsParameterss):
		for depth1 in range(len(SlsParameterss)):
			if SlsParameterss[depth1].get('Project') is not None:
				self.add_query_param('SlsParameters.' + str(depth1 + 1) + '.Project', SlsParameterss[depth1].get('Project'))
			if SlsParameterss[depth1].get('Id') is not None:
				self.add_query_param('SlsParameters.' + str(depth1 + 1) + '.Id', SlsParameterss[depth1].get('Id'))
			if SlsParameterss[depth1].get('Region') is not None:
				self.add_query_param('SlsParameters.' + str(depth1 + 1) + '.Region', SlsParameterss[depth1].get('Region'))
			if SlsParameterss[depth1].get('LogStore') is not None:
				self.add_query_param('SlsParameters.' + str(depth1 + 1) + '.LogStore', SlsParameterss[depth1].get('LogStore'))

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_MnsParameterss(self):
		return self.get_query_params().get('MnsParameters')

	def set_MnsParameterss(self, MnsParameterss):
		for depth1 in range(len(MnsParameterss)):
			if MnsParameterss[depth1].get('Id') is not None:
				self.add_query_param('MnsParameters.' + str(depth1 + 1) + '.Id', MnsParameterss[depth1].get('Id'))
			if MnsParameterss[depth1].get('Region') is not None:
				self.add_query_param('MnsParameters.' + str(depth1 + 1) + '.Region', MnsParameterss[depth1].get('Region'))
			if MnsParameterss[depth1].get('Queue') is not None:
				self.add_query_param('MnsParameters.' + str(depth1 + 1) + '.Queue', MnsParameterss[depth1].get('Queue'))

	def get_FcParameterss(self):
		return self.get_query_params().get('FcParameters')

	def set_FcParameterss(self, FcParameterss):
		for depth1 in range(len(FcParameterss)):
			if FcParameterss[depth1].get('FunctionName') is not None:
				self.add_query_param('FcParameters.' + str(depth1 + 1) + '.FunctionName', FcParameterss[depth1].get('FunctionName'))
			if FcParameterss[depth1].get('ServiceName') is not None:
				self.add_query_param('FcParameters.' + str(depth1 + 1) + '.ServiceName', FcParameterss[depth1].get('ServiceName'))
			if FcParameterss[depth1].get('Id') is not None:
				self.add_query_param('FcParameters.' + str(depth1 + 1) + '.Id', FcParameterss[depth1].get('Id'))
			if FcParameterss[depth1].get('Region') is not None:
				self.add_query_param('FcParameters.' + str(depth1 + 1) + '.Region', FcParameterss[depth1].get('Region'))