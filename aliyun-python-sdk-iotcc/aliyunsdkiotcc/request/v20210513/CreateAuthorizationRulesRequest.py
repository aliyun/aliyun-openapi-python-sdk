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

class CreateAuthorizationRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'CreateAuthorizationRules','IoTCC')
		self.set_method('POST')

	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_AuthorizationRuless(self): # RepeatList
		return self.get_query_params().get('AuthorizationRules')

	def set_AuthorizationRuless(self, AuthorizationRules):  # RepeatList
		for depth1 in range(len(AuthorizationRules)):
			if AuthorizationRules[depth1].get('Name') is not None:
				self.add_query_param('AuthorizationRules.' + str(depth1 + 1) + '.Name', AuthorizationRules[depth1].get('Name'))
			if AuthorizationRules[depth1].get('Description') is not None:
				self.add_query_param('AuthorizationRules.' + str(depth1 + 1) + '.Description', AuthorizationRules[depth1].get('Description'))
			if AuthorizationRules[depth1].get('SourceCidr') is not None:
				self.add_query_param('AuthorizationRules.' + str(depth1 + 1) + '.SourceCidr', AuthorizationRules[depth1].get('SourceCidr'))
			if AuthorizationRules[depth1].get('DestinationType') is not None:
				self.add_query_param('AuthorizationRules.' + str(depth1 + 1) + '.DestinationType', AuthorizationRules[depth1].get('DestinationType'))
			if AuthorizationRules[depth1].get('DestinationPort') is not None:
				self.add_query_param('AuthorizationRules.' + str(depth1 + 1) + '.DestinationPort', AuthorizationRules[depth1].get('DestinationPort'))
			if AuthorizationRules[depth1].get('Protocol') is not None:
				self.add_query_param('AuthorizationRules.' + str(depth1 + 1) + '.Protocol', AuthorizationRules[depth1].get('Protocol'))
			if AuthorizationRules[depth1].get('Destination') is not None:
				self.add_query_param('AuthorizationRules.' + str(depth1 + 1) + '.Destination', AuthorizationRules[depth1].get('Destination'))
			if AuthorizationRules[depth1].get('Policy') is not None:
				self.add_query_param('AuthorizationRules.' + str(depth1 + 1) + '.Policy', AuthorizationRules[depth1].get('Policy'))
	def get_IoTCloudConnectorId(self): # String
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self, IoTCloudConnectorId):  # String
		self.add_query_param('IoTCloudConnectorId', IoTCloudConnectorId)
