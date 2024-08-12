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

class ModifyFirewallTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SWAS-OPEN', '2020-06-01', 'ModifyFirewallTemplate','SWAS-OPEN')
		self.set_method('POST')

	def get_FirewallTemplateId(self): # String
		return self.get_query_params().get('FirewallTemplateId')

	def set_FirewallTemplateId(self, FirewallTemplateId):  # String
		self.add_query_param('FirewallTemplateId', FirewallTemplateId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_FirewallTemplateRules(self): # RepeatList
		return self.get_query_params().get('FirewallTemplateRule')

	def set_FirewallTemplateRules(self, FirewallTemplateRule):  # RepeatList
		for depth1 in range(len(FirewallTemplateRule)):
			if FirewallTemplateRule[depth1].get('FirewallTemplateRuleId') is not None:
				self.add_query_param('FirewallTemplateRule.' + str(depth1 + 1) + '.FirewallTemplateRuleId', FirewallTemplateRule[depth1].get('FirewallTemplateRuleId'))
			if FirewallTemplateRule[depth1].get('RuleProtocol') is not None:
				self.add_query_param('FirewallTemplateRule.' + str(depth1 + 1) + '.RuleProtocol', FirewallTemplateRule[depth1].get('RuleProtocol'))
			if FirewallTemplateRule[depth1].get('Port') is not None:
				self.add_query_param('FirewallTemplateRule.' + str(depth1 + 1) + '.Port', FirewallTemplateRule[depth1].get('Port'))
			if FirewallTemplateRule[depth1].get('SourceCidrIp') is not None:
				self.add_query_param('FirewallTemplateRule.' + str(depth1 + 1) + '.SourceCidrIp', FirewallTemplateRule[depth1].get('SourceCidrIp'))
			if FirewallTemplateRule[depth1].get('Remark') is not None:
				self.add_query_param('FirewallTemplateRule.' + str(depth1 + 1) + '.Remark', FirewallTemplateRule[depth1].get('Remark'))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
