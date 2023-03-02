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

class UpdateRouteRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'lto', '2021-07-07', 'UpdateRouteRule')
		self.set_method('POST')

	def get_ContractTemplateId(self): # String
		return self.get_query_params().get('ContractTemplateId')

	def set_ContractTemplateId(self, ContractTemplateId):  # String
		self.add_query_param('ContractTemplateId', ContractTemplateId)
	def get_ContractName(self): # String
		return self.get_query_params().get('ContractName')

	def set_ContractName(self, ContractName):  # String
		self.add_query_param('ContractName', ContractName)
	def get_PrivacyRuleId(self): # String
		return self.get_query_params().get('PrivacyRuleId')

	def set_PrivacyRuleId(self, PrivacyRuleId):  # String
		self.add_query_param('PrivacyRuleId', PrivacyRuleId)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_BizChainId(self): # String
		return self.get_query_params().get('BizChainId')

	def set_BizChainId(self, BizChainId):  # String
		self.add_query_param('BizChainId', BizChainId)
	def get_InvokeType(self): # String
		return self.get_query_params().get('InvokeType')

	def set_InvokeType(self, InvokeType):  # String
		self.add_query_param('InvokeType', InvokeType)
	def get_RouteRuleId(self): # String
		return self.get_query_params().get('RouteRuleId')

	def set_RouteRuleId(self, RouteRuleId):  # String
		self.add_query_param('RouteRuleId', RouteRuleId)
