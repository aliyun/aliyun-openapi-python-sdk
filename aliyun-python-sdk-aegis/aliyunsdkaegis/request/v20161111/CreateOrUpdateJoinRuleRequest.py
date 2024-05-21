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
class CreateOrUpdateJoinRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'CreateOrUpdateJoinRule','vipaegis')

	def get_WarnLevel(self):
		return self.get_query_params().get('WarnLevel')

	def set_WarnLevel(self,WarnLevel):
		self.add_query_param('WarnLevel',WarnLevel)

	def get_DataSourceId2(self):
		return self.get_query_params().get('DataSourceId2')

	def set_DataSourceId2(self,DataSourceId2):
		self.add_query_param('DataSourceId2',DataSourceId2)

	def get_DataSourceId1(self):
		return self.get_query_params().get('DataSourceId1')

	def set_DataSourceId1(self,DataSourceId1):
		self.add_query_param('DataSourceId1',DataSourceId1)

	def get_TimeWindow(self):
		return self.get_query_params().get('TimeWindow')

	def set_TimeWindow(self,TimeWindow):
		self.add_query_param('TimeWindow',TimeWindow)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_Expression2(self):
		return self.get_query_params().get('Expression2')

	def set_Expression2(self,Expression2):
		self.add_query_param('Expression2',Expression2)

	def get_Expression1(self):
		return self.get_query_params().get('Expression1')

	def set_Expression1(self,Expression1):
		self.add_query_param('Expression1',Expression1)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_StatisticsRules(self):
		return self.get_query_params().get('StatisticsRules')

	def set_StatisticsRules(self,StatisticsRules):
		self.add_query_param('StatisticsRules',StatisticsRules)

	def get_JoinRelation(self):
		return self.get_query_params().get('JoinRelation')

	def set_JoinRelation(self,JoinRelation):
		self.add_query_param('JoinRelation',JoinRelation)

	def get_RuleId(self):
		return self.get_query_params().get('RuleId')

	def set_RuleId(self,RuleId):
		self.add_query_param('RuleId',RuleId)

	def get_Actions(self):
		return self.get_query_params().get('Actions')

	def set_Actions(self,Actions):
		self.add_query_param('Actions',Actions)