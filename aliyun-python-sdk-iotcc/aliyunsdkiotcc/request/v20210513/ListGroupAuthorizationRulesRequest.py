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

class ListGroupAuthorizationRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListGroupAuthorizationRules','IoTCC')
		self.set_method('POST')

	def get_DestinationTypes(self): # RepeatList
		return self.get_query_params().get('DestinationType')

	def set_DestinationTypes(self, DestinationType):  # RepeatList
		for depth1 in range(len(DestinationType)):
			self.add_query_param('DestinationType.' + str(depth1 + 1), DestinationType[depth1])
	def get_Destinations(self): # RepeatList
		return self.get_query_params().get('Destination')

	def set_Destinations(self, Destination):  # RepeatList
		for depth1 in range(len(Destination)):
			self.add_query_param('Destination.' + str(depth1 + 1), Destination[depth1])
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_AuthorizationRuleIdss(self): # RepeatList
		return self.get_query_params().get('AuthorizationRuleIds')

	def set_AuthorizationRuleIdss(self, AuthorizationRuleIds):  # RepeatList
		for depth1 in range(len(AuthorizationRuleIds)):
			self.add_query_param('AuthorizationRuleIds.' + str(depth1 + 1), AuthorizationRuleIds[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Policys(self): # RepeatList
		return self.get_query_params().get('Policy')

	def set_Policys(self, Policy):  # RepeatList
		for depth1 in range(len(Policy)):
			self.add_query_param('Policy.' + str(depth1 + 1), Policy[depth1])
	def get_AuthorizationRuleStatuss(self): # RepeatList
		return self.get_query_params().get('AuthorizationRuleStatus')

	def set_AuthorizationRuleStatuss(self, AuthorizationRuleStatus):  # RepeatList
		for depth1 in range(len(AuthorizationRuleStatus)):
			self.add_query_param('AuthorizationRuleStatus.' + str(depth1 + 1), AuthorizationRuleStatus[depth1])
	def get_IoTCloudConnectorGroupId(self): # String
		return self.get_query_params().get('IoTCloudConnectorGroupId')

	def set_IoTCloudConnectorGroupId(self, IoTCloudConnectorGroupId):  # String
		self.add_query_param('IoTCloudConnectorGroupId', IoTCloudConnectorGroupId)
	def get_AuthorizationRuleNames(self): # RepeatList
		return self.get_query_params().get('AuthorizationRuleName')

	def set_AuthorizationRuleNames(self, AuthorizationRuleName):  # RepeatList
		for depth1 in range(len(AuthorizationRuleName)):
			self.add_query_param('AuthorizationRuleName.' + str(depth1 + 1), AuthorizationRuleName[depth1])
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
