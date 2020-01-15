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

class CreateDynamicTagGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateDynamicTagGroup','cms')

	def get_EnableSubscribeEvent(self):
		return self.get_query_params().get('EnableSubscribeEvent')

	def set_EnableSubscribeEvent(self,EnableSubscribeEvent):
		self.add_query_param('EnableSubscribeEvent',EnableSubscribeEvent)

	def get_MatchExpressFilterRelation(self):
		return self.get_query_params().get('MatchExpressFilterRelation')

	def set_MatchExpressFilterRelation(self,MatchExpressFilterRelation):
		self.add_query_param('MatchExpressFilterRelation',MatchExpressFilterRelation)

	def get_EnableInstallAgent(self):
		return self.get_query_params().get('EnableInstallAgent')

	def set_EnableInstallAgent(self,EnableInstallAgent):
		self.add_query_param('EnableInstallAgent',EnableInstallAgent)

	def get_MatchExpresss(self):
		return self.get_query_params().get('MatchExpresss')

	def set_MatchExpresss(self,MatchExpresss):
		for i in range(len(MatchExpresss)):	
			if MatchExpresss[i].get('TagValue') is not None:
				self.add_query_param('MatchExpress.' + str(i + 1) + '.TagValue' , MatchExpresss[i].get('TagValue'))
			if MatchExpresss[i].get('TagValueMatchFunction') is not None:
				self.add_query_param('MatchExpress.' + str(i + 1) + '.TagValueMatchFunction' , MatchExpresss[i].get('TagValueMatchFunction'))


	def get_ContactGroupLists(self):
		return self.get_query_params().get('ContactGroupLists')

	def set_ContactGroupLists(self,ContactGroupLists):
		for i in range(len(ContactGroupLists)):	
			if ContactGroupLists[i] is not None:
				self.add_query_param('ContactGroupList.' + str(i + 1) , ContactGroupLists[i]);

	def get_TemplateIdLists(self):
		return self.get_query_params().get('TemplateIdLists')

	def set_TemplateIdLists(self,TemplateIdLists):
		for i in range(len(TemplateIdLists)):	
			if TemplateIdLists[i] is not None:
				self.add_query_param('TemplateIdList.' + str(i + 1) , TemplateIdLists[i]);

	def get_TagKey(self):
		return self.get_query_params().get('TagKey')

	def set_TagKey(self,TagKey):
		self.add_query_param('TagKey',TagKey)