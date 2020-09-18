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

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_EventPatterns(self):
		return self.get_query_params().get('EventPattern')

	def set_EventPatterns(self, EventPatterns):
		for depth1 in range(len(EventPatterns)):
			if EventPatterns[depth1].get('LevelList') is not None:
				for depth2 in range(len(EventPatterns[depth1].get('LevelList'))):
					if EventPatterns[depth1].get('LevelList')[depth2] is not None:
						self.add_query_param('EventPattern.' + str(depth1 + 1) + '.LevelList.' + str(depth2 + 1) , EventPatterns[depth1].get('LevelList')[depth2])
			if EventPatterns[depth1].get('Product') is not None:
				self.add_query_param('EventPattern.' + str(depth1 + 1) + '.Product', EventPatterns[depth1].get('Product'))
			if EventPatterns[depth1].get('StatusList') is not None:
				for depth2 in range(len(EventPatterns[depth1].get('StatusList'))):
					if EventPatterns[depth1].get('StatusList')[depth2] is not None:
						self.add_query_param('EventPattern.' + str(depth1 + 1) + '.StatusList.' + str(depth2 + 1) , EventPatterns[depth1].get('StatusList')[depth2])
			if EventPatterns[depth1].get('NameList') is not None:
				for depth2 in range(len(EventPatterns[depth1].get('NameList'))):
					if EventPatterns[depth1].get('NameList')[depth2] is not None:
						self.add_query_param('EventPattern.' + str(depth1 + 1) + '.NameList.' + str(depth2 + 1) , EventPatterns[depth1].get('NameList')[depth2])
			if EventPatterns[depth1].get('EventTypeList') is not None:
				for depth2 in range(len(EventPatterns[depth1].get('EventTypeList'))):
					if EventPatterns[depth1].get('EventTypeList')[depth2] is not None:
						self.add_query_param('EventPattern.' + str(depth1 + 1) + '.EventTypeList.' + str(depth2 + 1) , EventPatterns[depth1].get('EventTypeList')[depth2])

	def get_EventType(self):
		return self.get_query_params().get('EventType')

	def set_EventType(self,EventType):
		self.add_query_param('EventType',EventType)

	def get_State(self):
		return self.get_query_params().get('State')

	def set_State(self,State):
		self.add_query_param('State',State)