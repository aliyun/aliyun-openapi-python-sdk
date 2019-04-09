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
class PutEventRuleTargetsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutEventRuleTargets','cms')

	def get_WebhookParameterss(self):
		return self.get_query_params().get('WebhookParameterss')

	def set_WebhookParameterss(self,WebhookParameterss):
		for i in range(len(WebhookParameterss)):	
			if WebhookParameterss[i].get('Protocol') is not None:
				self.add_query_param('WebhookParameters.' + str(i + 1) + '.Protocol' , WebhookParameterss[i].get('Protocol'))
			if WebhookParameterss[i].get('Method') is not None:
				self.add_query_param('WebhookParameters.' + str(i + 1) + '.Method' , WebhookParameterss[i].get('Method'))
			if WebhookParameterss[i].get('Id') is not None:
				self.add_query_param('WebhookParameters.' + str(i + 1) + '.Id' , WebhookParameterss[i].get('Id'))
			if WebhookParameterss[i].get('Url') is not None:
				self.add_query_param('WebhookParameters.' + str(i + 1) + '.Url' , WebhookParameterss[i].get('Url'))


	def get_ContactParameterss(self):
		return self.get_query_params().get('ContactParameterss')

	def set_ContactParameterss(self,ContactParameterss):
		for i in range(len(ContactParameterss)):	
			if ContactParameterss[i].get('Level') is not None:
				self.add_query_param('ContactParameters.' + str(i + 1) + '.Level' , ContactParameterss[i].get('Level'))
			if ContactParameterss[i].get('Id') is not None:
				self.add_query_param('ContactParameters.' + str(i + 1) + '.Id' , ContactParameterss[i].get('Id'))
			if ContactParameterss[i].get('ContactGroupName') is not None:
				self.add_query_param('ContactParameters.' + str(i + 1) + '.ContactGroupName' , ContactParameterss[i].get('ContactGroupName'))


	def get_SlsParameterss(self):
		return self.get_query_params().get('SlsParameterss')

	def set_SlsParameterss(self,SlsParameterss):
		for i in range(len(SlsParameterss)):	
			if SlsParameterss[i].get('Project') is not None:
				self.add_query_param('SlsParameters.' + str(i + 1) + '.Project' , SlsParameterss[i].get('Project'))
			if SlsParameterss[i].get('Id') is not None:
				self.add_query_param('SlsParameters.' + str(i + 1) + '.Id' , SlsParameterss[i].get('Id'))
			if SlsParameterss[i].get('Region') is not None:
				self.add_query_param('SlsParameters.' + str(i + 1) + '.Region' , SlsParameterss[i].get('Region'))
			if SlsParameterss[i].get('LogStore') is not None:
				self.add_query_param('SlsParameters.' + str(i + 1) + '.LogStore' , SlsParameterss[i].get('LogStore'))


	def get_FcParameterss(self):
		return self.get_query_params().get('FcParameterss')

	def set_FcParameterss(self,FcParameterss):
		for i in range(len(FcParameterss)):	
			if FcParameterss[i].get('FunctionName') is not None:
				self.add_query_param('FcParameters.' + str(i + 1) + '.FunctionName' , FcParameterss[i].get('FunctionName'))
			if FcParameterss[i].get('ServiceName') is not None:
				self.add_query_param('FcParameters.' + str(i + 1) + '.ServiceName' , FcParameterss[i].get('ServiceName'))
			if FcParameterss[i].get('Id') is not None:
				self.add_query_param('FcParameters.' + str(i + 1) + '.Id' , FcParameterss[i].get('Id'))
			if FcParameterss[i].get('Region') is not None:
				self.add_query_param('FcParameters.' + str(i + 1) + '.Region' , FcParameterss[i].get('Region'))


	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_MnsParameterss(self):
		return self.get_query_params().get('MnsParameterss')

	def set_MnsParameterss(self,MnsParameterss):
		for i in range(len(MnsParameterss)):	
			if MnsParameterss[i].get('Id') is not None:
				self.add_query_param('MnsParameters.' + str(i + 1) + '.Id' , MnsParameterss[i].get('Id'))
			if MnsParameterss[i].get('Region') is not None:
				self.add_query_param('MnsParameters.' + str(i + 1) + '.Region' , MnsParameterss[i].get('Region'))
			if MnsParameterss[i].get('Queue') is not None:
				self.add_query_param('MnsParameters.' + str(i + 1) + '.Queue' , MnsParameterss[i].get('Queue'))
