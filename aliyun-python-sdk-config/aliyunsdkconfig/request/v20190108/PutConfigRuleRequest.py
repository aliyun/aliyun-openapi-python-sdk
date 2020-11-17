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
from aliyunsdkconfig.endpoint import endpoint_data

class PutConfigRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Config', '2019-01-08', 'PutConfigRule','Config')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConfigRuleId(self):
		return self.get_body_params().get('ConfigRuleId')

	def set_ConfigRuleId(self,ConfigRuleId):
		self.add_body_params('ConfigRuleId', ConfigRuleId)

	def get_MultiAccount(self):
		return self.get_query_params().get('MultiAccount')

	def set_MultiAccount(self,MultiAccount):
		self.add_query_param('MultiAccount',MultiAccount)

	def get_ClientToken(self):
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_body_params('ClientToken', ClientToken)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_SourceIdentifier(self):
		return self.get_body_params().get('SourceIdentifier')

	def set_SourceIdentifier(self,SourceIdentifier):
		self.add_body_params('SourceIdentifier', SourceIdentifier)

	def get_SourceMaximumExecutionFrequency(self):
		return self.get_body_params().get('SourceMaximumExecutionFrequency')

	def set_SourceMaximumExecutionFrequency(self,SourceMaximumExecutionFrequency):
		self.add_body_params('SourceMaximumExecutionFrequency', SourceMaximumExecutionFrequency)

	def get_ScopeComplianceResourceTypes(self):
		return self.get_body_params().get('ScopeComplianceResourceTypes')

	def set_ScopeComplianceResourceTypes(self,ScopeComplianceResourceTypes):
		self.add_body_params('ScopeComplianceResourceTypes', ScopeComplianceResourceTypes)

	def get_SourceDetailMessageType(self):
		return self.get_body_params().get('SourceDetailMessageType')

	def set_SourceDetailMessageType(self,SourceDetailMessageType):
		self.add_body_params('SourceDetailMessageType', SourceDetailMessageType)

	def get_RiskLevel(self):
		return self.get_body_params().get('RiskLevel')

	def set_RiskLevel(self,RiskLevel):
		self.add_body_params('RiskLevel', RiskLevel)

	def get_SourceOwner(self):
		return self.get_body_params().get('SourceOwner')

	def set_SourceOwner(self,SourceOwner):
		self.add_body_params('SourceOwner', SourceOwner)

	def get_InputParameters(self):
		return self.get_body_params().get('InputParameters')

	def set_InputParameters(self,InputParameters):
		self.add_body_params('InputParameters', InputParameters)

	def get_ConfigRuleName(self):
		return self.get_body_params().get('ConfigRuleName')

	def set_ConfigRuleName(self,ConfigRuleName):
		self.add_body_params('ConfigRuleName', ConfigRuleName)

	def get_ScopeComplianceResourceId(self):
		return self.get_body_params().get('ScopeComplianceResourceId')

	def set_ScopeComplianceResourceId(self,ScopeComplianceResourceId):
		self.add_body_params('ScopeComplianceResourceId', ScopeComplianceResourceId)

	def get_MemberId(self):
		return self.get_query_params().get('MemberId')

	def set_MemberId(self,MemberId):
		self.add_query_param('MemberId',MemberId)