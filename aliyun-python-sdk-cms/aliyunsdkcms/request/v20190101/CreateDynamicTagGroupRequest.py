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
		self.set_method('POST')

	def get_EnableSubscribeEvent(self): # Boolean
		return self.get_query_params().get('EnableSubscribeEvent')

	def set_EnableSubscribeEvent(self, EnableSubscribeEvent):  # Boolean
		self.add_query_param('EnableSubscribeEvent', EnableSubscribeEvent)
	def get_MatchExpressFilterRelation(self): # String
		return self.get_query_params().get('MatchExpressFilterRelation')

	def set_MatchExpressFilterRelation(self, MatchExpressFilterRelation):  # String
		self.add_query_param('MatchExpressFilterRelation', MatchExpressFilterRelation)
	def get_EnableInstallAgent(self): # Boolean
		return self.get_query_params().get('EnableInstallAgent')

	def set_EnableInstallAgent(self, EnableInstallAgent):  # Boolean
		self.add_query_param('EnableInstallAgent', EnableInstallAgent)
	def get_MatchExpresss(self): # RepeatList
		return self.get_query_params().get('MatchExpress')

	def set_MatchExpresss(self, MatchExpress):  # RepeatList
		for depth1 in range(len(MatchExpress)):
			if MatchExpress[depth1].get('TagValue') is not None:
				self.add_query_param('MatchExpress.' + str(depth1 + 1) + '.TagValue', MatchExpress[depth1].get('TagValue'))
			if MatchExpress[depth1].get('TagValueMatchFunction') is not None:
				self.add_query_param('MatchExpress.' + str(depth1 + 1) + '.TagValueMatchFunction', MatchExpress[depth1].get('TagValueMatchFunction'))
	def get_ContactGroupLists(self): # RepeatList
		return self.get_query_params().get('ContactGroupList')

	def set_ContactGroupLists(self, ContactGroupList):  # RepeatList
		for depth1 in range(len(ContactGroupList)):
			self.add_query_param('ContactGroupList.' + str(depth1 + 1), ContactGroupList[depth1])
	def get_TemplateIdLists(self): # RepeatList
		return self.get_query_params().get('TemplateIdList')

	def set_TemplateIdLists(self, TemplateIdList):  # RepeatList
		for depth1 in range(len(TemplateIdList)):
			self.add_query_param('TemplateIdList.' + str(depth1 + 1), TemplateIdList[depth1])
	def get_TagKey(self): # String
		return self.get_query_params().get('TagKey')

	def set_TagKey(self, TagKey):  # String
		self.add_query_param('TagKey', TagKey)
	def get_TagRegionId(self): # String
		return self.get_query_params().get('TagRegionId')

	def set_TagRegionId(self, TagRegionId):  # String
		self.add_query_param('TagRegionId', TagRegionId)
