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
class InsertTmMonitorRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'InsertTmMonitorRule','trademark')

	def get_StartApplyDate(self):
		return self.get_query_params().get('StartApplyDate')

	def set_StartApplyDate(self,StartApplyDate):
		self.add_query_param('StartApplyDate',StartApplyDate)

	def get_NotifyStatus(self):
		return self.get_query_params().get('NotifyStatus')

	def set_NotifyStatus(self,NotifyStatus):
		self.add_query_param('NotifyStatus',NotifyStatus)

	def get_RuleType(self):
		return self.get_query_params().get('RuleType')

	def set_RuleType(self,RuleType):
		self.add_query_param('RuleType',RuleType)

	def get_RuleSource(self):
		return self.get_query_params().get('RuleSource')

	def set_RuleSource(self,RuleSource):
		self.add_query_param('RuleSource',RuleSource)

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_EndApplyDate(self):
		return self.get_query_params().get('EndApplyDate')

	def set_EndApplyDate(self,EndApplyDate):
		self.add_query_param('EndApplyDate',EndApplyDate)

	def get_Classification(self):
		return self.get_query_params().get('Classification')

	def set_Classification(self,Classification):
		self.add_query_param('Classification',Classification)

	def get_RuleKeyword(self):
		return self.get_query_params().get('RuleKeyword')

	def set_RuleKeyword(self,RuleKeyword):
		self.add_query_param('RuleKeyword',RuleKeyword)