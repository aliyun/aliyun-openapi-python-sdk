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

class CreateRemediationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Config', '2020-09-07', 'CreateRemediation')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ConfigRuleId(self): # String
		return self.get_body_params().get('ConfigRuleId')

	def set_ConfigRuleId(self, ConfigRuleId):  # String
		self.add_body_params('ConfigRuleId', ConfigRuleId)
	def get_RemediationType(self): # String
		return self.get_body_params().get('RemediationType')

	def set_RemediationType(self, RemediationType):  # String
		self.add_body_params('RemediationType', RemediationType)
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_SourceType(self): # String
		return self.get_body_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_body_params('SourceType', SourceType)
	def get_RemediationTemplateId(self): # String
		return self.get_body_params().get('RemediationTemplateId')

	def set_RemediationTemplateId(self, RemediationTemplateId):  # String
		self.add_body_params('RemediationTemplateId', RemediationTemplateId)
	def get_Params(self): # String
		return self.get_body_params().get('Params')

	def set_Params(self, Params):  # String
		self.add_body_params('Params', Params)
	def get_InvokeType(self): # String
		return self.get_body_params().get('InvokeType')

	def set_InvokeType(self, InvokeType):  # String
		self.add_body_params('InvokeType', InvokeType)
