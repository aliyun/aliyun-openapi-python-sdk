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

class ListIpMappingRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListIpMappingRules','IoTCC')
		self.set_method('POST')

	def get_MappingIpss(self): # RepeatList
		return self.get_query_params().get('MappingIps')

	def set_MappingIpss(self, MappingIps):  # RepeatList
		for depth1 in range(len(MappingIps)):
			self.add_query_param('MappingIps.' + str(depth1 + 1), MappingIps[depth1])
	def get_IpMappingRuleIdss(self): # RepeatList
		return self.get_query_params().get('IpMappingRuleIds')

	def set_IpMappingRuleIdss(self, IpMappingRuleIds):  # RepeatList
		for depth1 in range(len(IpMappingRuleIds)):
			self.add_query_param('IpMappingRuleIds.' + str(depth1 + 1), IpMappingRuleIds[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_IpMappingRuleStatusess(self): # RepeatList
		return self.get_query_params().get('IpMappingRuleStatuses')

	def set_IpMappingRuleStatusess(self, IpMappingRuleStatuses):  # RepeatList
		for depth1 in range(len(IpMappingRuleStatuses)):
			self.add_query_param('IpMappingRuleStatuses.' + str(depth1 + 1), IpMappingRuleStatuses[depth1])
	def get_IpMappingRuleNamess(self): # RepeatList
		return self.get_query_params().get('IpMappingRuleNames')

	def set_IpMappingRuleNamess(self, IpMappingRuleNames):  # RepeatList
		for depth1 in range(len(IpMappingRuleNames)):
			self.add_query_param('IpMappingRuleNames.' + str(depth1 + 1), IpMappingRuleNames[depth1])
	def get_IoTCloudConnectorId(self): # String
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self, IoTCloudConnectorId):  # String
		self.add_query_param('IoTCloudConnectorId', IoTCloudConnectorId)
	def get_DestinationIpss(self): # RepeatList
		return self.get_query_params().get('DestinationIps')

	def set_DestinationIpss(self, DestinationIps):  # RepeatList
		for depth1 in range(len(DestinationIps)):
			self.add_query_param('DestinationIps.' + str(depth1 + 1), DestinationIps[depth1])
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
