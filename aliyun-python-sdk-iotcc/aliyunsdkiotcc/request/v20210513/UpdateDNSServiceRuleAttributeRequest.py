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

class UpdateDNSServiceRuleAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'UpdateDNSServiceRuleAttribute','IoTCC')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Destination(self): # String
		return self.get_query_params().get('Destination')

	def set_Destination(self, Destination):  # String
		self.add_query_param('Destination', Destination)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_DNSServiceRuleDescription(self): # String
		return self.get_query_params().get('DNSServiceRuleDescription')

	def set_DNSServiceRuleDescription(self, DNSServiceRuleDescription):  # String
		self.add_query_param('DNSServiceRuleDescription', DNSServiceRuleDescription)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_DNSServiceRuleId(self): # String
		return self.get_query_params().get('DNSServiceRuleId')

	def set_DNSServiceRuleId(self, DNSServiceRuleId):  # String
		self.add_query_param('DNSServiceRuleId', DNSServiceRuleId)
	def get_ServiceType(self): # String
		return self.get_query_params().get('ServiceType')

	def set_ServiceType(self, ServiceType):  # String
		self.add_query_param('ServiceType', ServiceType)
	def get_IoTCloudConnectorId(self): # String
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self, IoTCloudConnectorId):  # String
		self.add_query_param('IoTCloudConnectorId', IoTCloudConnectorId)
	def get_DNSServiceRuleName(self): # String
		return self.get_query_params().get('DNSServiceRuleName')

	def set_DNSServiceRuleName(self, DNSServiceRuleName):  # String
		self.add_query_param('DNSServiceRuleName', DNSServiceRuleName)
