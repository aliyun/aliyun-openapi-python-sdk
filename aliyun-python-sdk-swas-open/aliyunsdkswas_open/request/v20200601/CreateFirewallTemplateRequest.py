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

class CreateFirewallTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SWAS-OPEN', '2020-06-01', 'CreateFirewallTemplate','SWAS-OPEN')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_FirewallRules(self): # RepeatList
		return self.get_query_params().get('FirewallRule')

	def set_FirewallRules(self, FirewallRule):  # RepeatList
		for depth1 in range(len(FirewallRule)):
			if FirewallRule[depth1].get('RuleProtocol') is not None:
				self.add_query_param('FirewallRule.' + str(depth1 + 1) + '.RuleProtocol', FirewallRule[depth1].get('RuleProtocol'))
			if FirewallRule[depth1].get('Port') is not None:
				self.add_query_param('FirewallRule.' + str(depth1 + 1) + '.Port', FirewallRule[depth1].get('Port'))
			if FirewallRule[depth1].get('SourceCidrIp') is not None:
				self.add_query_param('FirewallRule.' + str(depth1 + 1) + '.SourceCidrIp', FirewallRule[depth1].get('SourceCidrIp'))
			if FirewallRule[depth1].get('Remark') is not None:
				self.add_query_param('FirewallRule.' + str(depth1 + 1) + '.Remark', FirewallRule[depth1].get('Remark'))
