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

class UpdateAuthorizationRuleAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'UpdateAuthorizationRuleAttribute','cciot')
		self.set_method('POST')

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_DestinationType(self):
		return self.get_query_params().get('DestinationType')

	def set_DestinationType(self,DestinationType):
		self.add_query_param('DestinationType',DestinationType)

	def get_Destination(self):
		return self.get_query_params().get('Destination')

	def set_Destination(self,Destination):
		self.add_query_param('Destination',Destination)

	def get_AuthorizationRuleDescription(self):
		return self.get_query_params().get('AuthorizationRuleDescription')

	def set_AuthorizationRuleDescription(self,AuthorizationRuleDescription):
		self.add_query_param('AuthorizationRuleDescription',AuthorizationRuleDescription)

	def get_Policy(self):
		return self.get_query_params().get('Policy')

	def set_Policy(self,Policy):
		self.add_query_param('Policy',Policy)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_SourceCidrss(self):
		return self.get_query_params().get('SourceCidrs')

	def set_SourceCidrss(self, SourceCidrss):
		for depth1 in range(len(SourceCidrss)):
			if SourceCidrss[depth1] is not None:
				self.add_query_param('SourceCidrs.' + str(depth1 + 1) , SourceCidrss[depth1])

	def get_AuthorizationRuleId(self):
		return self.get_query_params().get('AuthorizationRuleId')

	def set_AuthorizationRuleId(self,AuthorizationRuleId):
		self.add_query_param('AuthorizationRuleId',AuthorizationRuleId)

	def get_AuthorizationRuleName(self):
		return self.get_query_params().get('AuthorizationRuleName')

	def set_AuthorizationRuleName(self,AuthorizationRuleName):
		self.add_query_param('AuthorizationRuleName',AuthorizationRuleName)

	def get_IoTCloudConnectorId(self):
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self,IoTCloudConnectorId):
		self.add_query_param('IoTCloudConnectorId',IoTCloudConnectorId)