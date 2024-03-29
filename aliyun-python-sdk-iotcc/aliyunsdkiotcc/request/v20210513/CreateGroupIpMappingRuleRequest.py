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

class CreateGroupIpMappingRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'CreateGroupIpMappingRule','IoTCC')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_IoTCloudConnectorGroupId(self): # String
		return self.get_query_params().get('IoTCloudConnectorGroupId')

	def set_IoTCloudConnectorGroupId(self, IoTCloudConnectorGroupId):  # String
		self.add_query_param('IoTCloudConnectorGroupId', IoTCloudConnectorGroupId)
	def get_IpMappingRuleName(self): # String
		return self.get_query_params().get('IpMappingRuleName')

	def set_IpMappingRuleName(self, IpMappingRuleName):  # String
		self.add_query_param('IpMappingRuleName', IpMappingRuleName)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_IpMappingRuleDescription(self): # String
		return self.get_query_params().get('IpMappingRuleDescription')

	def set_IpMappingRuleDescription(self, IpMappingRuleDescription):  # String
		self.add_query_param('IpMappingRuleDescription', IpMappingRuleDescription)
	def get_DestinationIp(self): # String
		return self.get_query_params().get('DestinationIp')

	def set_DestinationIp(self, DestinationIp):  # String
		self.add_query_param('DestinationIp', DestinationIp)
	def get_MappingIp(self): # String
		return self.get_query_params().get('MappingIp')

	def set_MappingIp(self, MappingIp):  # String
		self.add_query_param('MappingIp', MappingIp)
