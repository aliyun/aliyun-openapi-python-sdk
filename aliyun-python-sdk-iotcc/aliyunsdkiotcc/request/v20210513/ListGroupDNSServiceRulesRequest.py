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

class ListGroupDNSServiceRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListGroupDNSServiceRules','IoTCC')
		self.set_method('POST')

	def get_Destinations(self): # RepeatList
		return self.get_query_params().get('Destination')

	def set_Destinations(self, Destination):  # RepeatList
		for depth1 in range(len(Destination)):
			self.add_query_param('Destination.' + str(depth1 + 1), Destination[depth1])
	def get_Sources(self): # RepeatList
		return self.get_query_params().get('Source')

	def set_Sources(self, Source):  # RepeatList
		for depth1 in range(len(Source)):
			self.add_query_param('Source.' + str(depth1 + 1), Source[depth1])
	def get_DNSServiceRuleStatuss(self): # RepeatList
		return self.get_query_params().get('DNSServiceRuleStatus')

	def set_DNSServiceRuleStatuss(self, DNSServiceRuleStatus):  # RepeatList
		for depth1 in range(len(DNSServiceRuleStatus)):
			self.add_query_param('DNSServiceRuleStatus.' + str(depth1 + 1), DNSServiceRuleStatus[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_IoTCloudConnectorGroupId(self): # String
		return self.get_query_params().get('IoTCloudConnectorGroupId')

	def set_IoTCloudConnectorGroupId(self, IoTCloudConnectorGroupId):  # String
		self.add_query_param('IoTCloudConnectorGroupId', IoTCloudConnectorGroupId)
	def get_ServiceType(self): # String
		return self.get_query_params().get('ServiceType')

	def set_ServiceType(self, ServiceType):  # String
		self.add_query_param('ServiceType', ServiceType)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_DNSServiceRuleIdss(self): # RepeatList
		return self.get_query_params().get('DNSServiceRuleIds')

	def set_DNSServiceRuleIdss(self, DNSServiceRuleIds):  # RepeatList
		for depth1 in range(len(DNSServiceRuleIds)):
			self.add_query_param('DNSServiceRuleIds.' + str(depth1 + 1), DNSServiceRuleIds[depth1])
	def get_DNSServiceRuleNames(self): # RepeatList
		return self.get_query_params().get('DNSServiceRuleName')

	def set_DNSServiceRuleNames(self, DNSServiceRuleName):  # RepeatList
		for depth1 in range(len(DNSServiceRuleName)):
			self.add_query_param('DNSServiceRuleName.' + str(depth1 + 1), DNSServiceRuleName[depth1])
