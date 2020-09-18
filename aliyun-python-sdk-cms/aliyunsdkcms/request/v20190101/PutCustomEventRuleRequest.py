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

class PutCustomEventRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutCustomEventRule','cms')
		self.set_method('POST')

	def get_Webhook(self):
		return self.get_query_params().get('Webhook')

	def set_Webhook(self,Webhook):
		self.add_query_param('Webhook',Webhook)

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_Threshold(self):
		return self.get_query_params().get('Threshold')

	def set_Threshold(self,Threshold):
		self.add_query_param('Threshold',Threshold)

	def get_EffectiveInterval(self):
		return self.get_query_params().get('EffectiveInterval')

	def set_EffectiveInterval(self,EffectiveInterval):
		self.add_query_param('EffectiveInterval',EffectiveInterval)

	def get_EventName(self):
		return self.get_query_params().get('EventName')

	def set_EventName(self,EventName):
		self.add_query_param('EventName',EventName)

	def get_EmailSubject(self):
		return self.get_query_params().get('EmailSubject')

	def set_EmailSubject(self,EmailSubject):
		self.add_query_param('EmailSubject',EmailSubject)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_ContactGroups(self):
		return self.get_query_params().get('ContactGroups')

	def set_ContactGroups(self,ContactGroups):
		self.add_query_param('ContactGroups',ContactGroups)

	def get_Level(self):
		return self.get_query_params().get('Level')

	def set_Level(self,Level):
		self.add_query_param('Level',Level)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_RuleId(self):
		return self.get_query_params().get('RuleId')

	def set_RuleId(self,RuleId):
		self.add_query_param('RuleId',RuleId)