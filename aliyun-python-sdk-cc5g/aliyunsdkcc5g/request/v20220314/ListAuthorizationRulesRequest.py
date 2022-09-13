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
		RpcRequest.__init__(self, 'CC5G', '2022-03-14', 'ListAuthorizationRules','fivegcc')
		self.set_method('GET')

	def get_DestinationType(self): # String
		return self.get_query_params().get('DestinationType')

	def set_DestinationType(self, DestinationType):  # String
		self.add_query_param('DestinationType', DestinationType)
	def get_Destination(self): # String
		return self.get_query_params().get('Destination')

	def set_Destination(self, Destination):  # String
		self.add_query_param('Destination', Destination)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Protocol(self): # String
		return self.get_query_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_query_param('Protocol', Protocol)
	def get_AuthorizationRuleIds(self): # Array
		return self.get_query_params().get('AuthorizationRuleIds')

	def set_AuthorizationRuleIds(self, AuthorizationRuleIds):  # Array
		for index1, value1 in enumerate(AuthorizationRuleIds):
			self.add_query_param('AuthorizationRuleIds.' + str(index1 + 1), value1)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Policy(self): # String
		return self.get_query_params().get('Policy')

	def set_Policy(self, Policy):  # String
		self.add_query_param('Policy', Policy)
	def get_Dns(self): # Boolean
		return self.get_query_params().get('Dns')

	def set_Dns(self, Dns):  # Boolean
		self.add_query_param('Dns', Dns)
	def get_DestinationPort(self): # String
		return self.get_query_params().get('DestinationPort')

	def set_DestinationPort(self, DestinationPort):  # String
		self.add_query_param('DestinationPort', DestinationPort)
	def get_Names(self): # Array
		return self.get_query_params().get('Names')

	def set_Names(self, Names):  # Array
		for index1, value1 in enumerate(Names):
			self.add_query_param('Names.' + str(index1 + 1), value1)
	def get_WirelessCloudConnectorId(self): # String
		return self.get_query_params().get('WirelessCloudConnectorId')

	def set_WirelessCloudConnectorId(self, WirelessCloudConnectorId):  # String
		self.add_query_param('WirelessCloudConnectorId', WirelessCloudConnectorId)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
	def get_Statuses(self): # Array
		return self.get_query_params().get('Statuses')

	def set_Statuses(self, Statuses):  # Array
		for index1, value1 in enumerate(Statuses):
			self.add_query_param('Statuses.' + str(index1 + 1), value1)
