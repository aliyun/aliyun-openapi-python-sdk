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

class ListAuthorizationRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListAuthorizationRules','cciot')
		self.set_method('POST')

	def get_DestinationTypes(self):
		return self.get_query_params().get('DestinationType')

	def set_DestinationTypes(self, DestinationTypes):
		for depth1 in range(len(DestinationTypes)):
			if DestinationTypes[depth1] is not None:
				self.add_query_param('DestinationType.' + str(depth1 + 1) , DestinationTypes[depth1])

	def get_AuthorizationRuleIdss(self):
		return self.get_query_params().get('AuthorizationRuleIds')

	def set_AuthorizationRuleIdss(self, AuthorizationRuleIdss):
		for depth1 in range(len(AuthorizationRuleIdss)):
			if AuthorizationRuleIdss[depth1] is not None:
				self.add_query_param('AuthorizationRuleIds.' + str(depth1 + 1) , AuthorizationRuleIdss[depth1])

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_Policys(self):
		return self.get_query_params().get('Policy')

	def set_Policys(self, Policys):
		for depth1 in range(len(Policys)):
			if Policys[depth1] is not None:
				self.add_query_param('Policy.' + str(depth1 + 1) , Policys[depth1])

	def get_AuthorizationRuleStatuss(self):
		return self.get_query_params().get('AuthorizationRuleStatus')

	def set_AuthorizationRuleStatuss(self, AuthorizationRuleStatuss):
		for depth1 in range(len(AuthorizationRuleStatuss)):
			if AuthorizationRuleStatuss[depth1] is not None:
				self.add_query_param('AuthorizationRuleStatus.' + str(depth1 + 1) , AuthorizationRuleStatuss[depth1])

	def get_AuthorizationRuleNames(self):
		return self.get_query_params().get('AuthorizationRuleName')

	def set_AuthorizationRuleNames(self, AuthorizationRuleNames):
		for depth1 in range(len(AuthorizationRuleNames)):
			if AuthorizationRuleNames[depth1] is not None:
				self.add_query_param('AuthorizationRuleName.' + str(depth1 + 1) , AuthorizationRuleNames[depth1])

	def get_IoTCloudConnectorId(self):
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self,IoTCloudConnectorId):
		self.add_query_param('IoTCloudConnectorId',IoTCloudConnectorId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)