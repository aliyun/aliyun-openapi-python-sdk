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

class PutEventRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutEventRule','cms')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_SilenceTime(self): # Long
		return self.get_query_params().get('SilenceTime')

	def set_SilenceTime(self, SilenceTime):  # Long
		self.add_query_param('SilenceTime', SilenceTime)
	def get_State(self): # String
		return self.get_query_params().get('State')

	def set_State(self, State):  # String
		self.add_query_param('State', State)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_EventPatterns(self): # RepeatList
		return self.get_query_params().get('EventPattern')

	def set_EventPatterns(self, EventPattern):  # RepeatList
		for depth1 in range(len(EventPattern)):
			if EventPattern[depth1].get('LevelList') is not None:
				for depth2 in range(len(EventPattern[depth1].get('LevelList'))):
					self.add_query_param('EventPattern.' + str(depth1 + 1) + '.LevelList.' + str(depth2 + 1), EventPattern[depth1].get('LevelList')[depth2])
			if EventPattern[depth1].get('KeywordFilter') is not None:
				if EventPattern[depth1].get('KeywordFilter').get('Keywords') is not None:
					for depth2 in range(len(EventPattern[depth1].get('KeywordFilter').get('Keywords'))):
						self.add_query_param('EventPattern.' + str(depth1 + 1) + '.KeywordFilter.Keywords.' + str(depth2 + 1), EventPattern[depth1].get('KeywordFilter').get('Keywords')[depth2])
				if EventPattern[depth1].get('KeywordFilter').get('Relation') is not None:
					self.add_query_param('EventPattern.' + str(depth1 + 1) + '.KeywordFilter.Relation', EventPattern[depth1].get('KeywordFilter').get('Relation'))
			if EventPattern[depth1].get('Product') is not None:
				self.add_query_param('EventPattern.' + str(depth1 + 1) + '.Product', EventPattern[depth1].get('Product'))
			if EventPattern[depth1].get('StatusList') is not None:
				for depth2 in range(len(EventPattern[depth1].get('StatusList'))):
					self.add_query_param('EventPattern.' + str(depth1 + 1) + '.StatusList.' + str(depth2 + 1), EventPattern[depth1].get('StatusList')[depth2])
			if EventPattern[depth1].get('NameList') is not None:
				for depth2 in range(len(EventPattern[depth1].get('NameList'))):
					self.add_query_param('EventPattern.' + str(depth1 + 1) + '.NameList.' + str(depth2 + 1), EventPattern[depth1].get('NameList')[depth2])
			if EventPattern[depth1].get('CustomFilters') is not None:
				self.add_query_param('EventPattern.' + str(depth1 + 1) + '.CustomFilters', EventPattern[depth1].get('CustomFilters'))
			if EventPattern[depth1].get('EventTypeList') is not None:
				for depth2 in range(len(EventPattern[depth1].get('EventTypeList'))):
					self.add_query_param('EventPattern.' + str(depth1 + 1) + '.EventTypeList.' + str(depth2 + 1), EventPattern[depth1].get('EventTypeList')[depth2])
			if EventPattern[depth1].get('SQLFilter') is not None:
				self.add_query_param('EventPattern.' + str(depth1 + 1) + '.SQLFilter', EventPattern[depth1].get('SQLFilter'))
	def get_EventType(self): # String
		return self.get_query_params().get('EventType')

	def set_EventType(self, EventType):  # String
		self.add_query_param('EventType', EventType)
