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
class PutEventRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutEventRule','cms')

	def get_EventPatterns(self):
		return self.get_query_params().get('EventPatterns')

	def set_EventPatterns(self,EventPatterns):
		for i in range(len(EventPatterns)):	
			for j in range(len(EventPatterns[i].get('LevelLists'))):
				if EventPatterns[i].get('LevelLists')[j] is not None:
					self.add_query_param('EventPattern.' + str(i + 1) + '.LevelList.'+str(j + 1), EventPatterns[i].get('LevelLists')[j])
			if EventPatterns[i].get('Product') is not None:
				self.add_query_param('EventPattern.' + str(i + 1) + '.Product' , EventPatterns[i].get('Product'))
			for j in range(len(EventPatterns[i].get('StatusLists'))):
				if EventPatterns[i].get('StatusLists')[j] is not None:
					self.add_query_param('EventPattern.' + str(i + 1) + '.StatusList.'+str(j + 1), EventPatterns[i].get('StatusLists')[j])
			for j in range(len(EventPatterns[i].get('NameLists'))):
				if EventPatterns[i].get('NameLists')[j] is not None:
					self.add_query_param('EventPattern.' + str(i + 1) + '.NameList.'+str(j + 1), EventPatterns[i].get('NameLists')[j])
			for j in range(len(EventPatterns[i].get('EventTypeLists'))):
				if EventPatterns[i].get('EventTypeLists')[j] is not None:
					self.add_query_param('EventPattern.' + str(i + 1) + '.EventTypeList.'+str(j + 1), EventPatterns[i].get('EventTypeLists')[j])


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

	def get_EventType(self):
		return self.get_query_params().get('EventType')

	def set_EventType(self,EventType):
		self.add_query_param('EventType',EventType)

	def get_State(self):
		return self.get_query_params().get('State')

	def set_State(self,State):
		self.add_query_param('State',State)