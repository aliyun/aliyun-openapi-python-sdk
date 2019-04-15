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
class CreateOrUpdateRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'CreateOrUpdateRule','vipaegis')

	def get_WarnLevel(self):
		return self.get_query_params().get('WarnLevel')

	def set_WarnLevel(self,WarnLevel):
		self.add_query_param('WarnLevel',WarnLevel)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_StatisticsRules(self):
		return self.get_query_params().get('StatisticsRules')

	def set_StatisticsRules(self,StatisticsRules):
		self.add_query_param('StatisticsRules',StatisticsRules)

	def get_DataSourceId(self):
		return self.get_query_params().get('DataSourceId')

	def set_DataSourceId(self,DataSourceId):
		self.add_query_param('DataSourceId',DataSourceId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Expressions(self):
		return self.get_query_params().get('Expressions')

	def set_Expressions(self,Expressions):
		self.add_query_param('Expressions',Expressions)

	def get_Actions(self):
		return self.get_query_params().get('Actions')

	def set_Actions(self,Actions):
		self.add_query_param('Actions',Actions)

	def get_RuleGroupIds(self):
		return self.get_query_params().get('RuleGroupIds')

	def set_RuleGroupIds(self,RuleGroupIds):
		self.add_query_param('RuleGroupIds',RuleGroupIds)