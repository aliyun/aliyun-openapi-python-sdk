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
from aliyunsdkwaf_openapi.endpoint import endpoint_data

class DescribeRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'waf-openapi', '2019-09-10', 'DescribeRules','waf')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RuleGroupId(self): # Long
		return self.get_query_params().get('RuleGroupId')

	def set_RuleGroupId(self, RuleGroupId):  # Long
		self.add_query_param('RuleGroupId', RuleGroupId)
	def get_ProtectionType(self): # Integer
		return self.get_query_params().get('ProtectionType')

	def set_ProtectionType(self, ProtectionType):  # Integer
		self.add_query_param('ProtectionType', ProtectionType)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_CveIdKey(self): # String
		return self.get_query_params().get('CveIdKey')

	def set_CveIdKey(self, CveIdKey):  # String
		self.add_query_param('CveIdKey', CveIdKey)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_RiskLevel(self): # Integer
		return self.get_query_params().get('RiskLevel')

	def set_RiskLevel(self, RiskLevel):  # Integer
		self.add_query_param('RiskLevel', RiskLevel)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_RuleIdKey(self): # String
		return self.get_query_params().get('RuleIdKey')

	def set_RuleIdKey(self, RuleIdKey):  # String
		self.add_query_param('RuleIdKey', RuleIdKey)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
	def get_ApplicationType(self): # Integer
		return self.get_query_params().get('ApplicationType')

	def set_ApplicationType(self, ApplicationType):  # Integer
		self.add_query_param('ApplicationType', ApplicationType)
