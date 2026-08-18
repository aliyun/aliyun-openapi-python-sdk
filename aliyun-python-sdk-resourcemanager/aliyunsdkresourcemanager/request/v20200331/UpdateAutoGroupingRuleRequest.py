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
from aliyunsdkresourcemanager.endpoint import endpoint_data

class UpdateAutoGroupingRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'UpdateAutoGroupingRule','resourcemanager')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RuleDesc(self): # String
		return self.get_query_params().get('RuleDesc')

	def set_RuleDesc(self, RuleDesc):  # String
		self.add_query_param('RuleDesc', RuleDesc)
	def get_ResourceTypesScope(self): # String
		return self.get_query_params().get('ResourceTypesScope')

	def set_ResourceTypesScope(self, ResourceTypesScope):  # String
		self.add_query_param('ResourceTypesScope', ResourceTypesScope)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_ExcludeResourceGroupIdsScope(self): # String
		return self.get_query_params().get('ExcludeResourceGroupIdsScope')

	def set_ExcludeResourceGroupIdsScope(self, ExcludeResourceGroupIdsScope):  # String
		self.add_query_param('ExcludeResourceGroupIdsScope', ExcludeResourceGroupIdsScope)
	def get_RegionIdsScope(self): # String
		return self.get_query_params().get('RegionIdsScope')

	def set_RegionIdsScope(self, RegionIdsScope):  # String
		self.add_query_param('RegionIdsScope', RegionIdsScope)
	def get_ResourceIdsScope(self): # String
		return self.get_query_params().get('ResourceIdsScope')

	def set_ResourceIdsScope(self, ResourceIdsScope):  # String
		self.add_query_param('ResourceIdsScope', ResourceIdsScope)
	def get_RuleContentss(self): # RepeatList
		return self.get_query_params().get('RuleContents')

	def set_RuleContentss(self, RuleContents):  # RepeatList
		for depth1 in range(len(RuleContents)):
			if RuleContents[depth1].get('RuleContentId') is not None:
				self.add_query_param('RuleContents.' + str(depth1 + 1) + '.RuleContentId', RuleContents[depth1].get('RuleContentId'))
			if RuleContents[depth1].get('TargetResourceGroupCondition') is not None:
				self.add_query_param('RuleContents.' + str(depth1 + 1) + '.TargetResourceGroupCondition', RuleContents[depth1].get('TargetResourceGroupCondition'))
			if RuleContents[depth1].get('AutoGroupingScopeCondition') is not None:
				self.add_query_param('RuleContents.' + str(depth1 + 1) + '.AutoGroupingScopeCondition', RuleContents[depth1].get('AutoGroupingScopeCondition'))
	def get_ExcludeResourceTypesScope(self): # String
		return self.get_query_params().get('ExcludeResourceTypesScope')

	def set_ExcludeResourceTypesScope(self, ExcludeResourceTypesScope):  # String
		self.add_query_param('ExcludeResourceTypesScope', ExcludeResourceTypesScope)
	def get_ResourceGroupIdsScope(self): # String
		return self.get_query_params().get('ResourceGroupIdsScope')

	def set_ResourceGroupIdsScope(self, ResourceGroupIdsScope):  # String
		self.add_query_param('ResourceGroupIdsScope', ResourceGroupIdsScope)
	def get_ExcludeRegionIdsScope(self): # String
		return self.get_query_params().get('ExcludeRegionIdsScope')

	def set_ExcludeRegionIdsScope(self, ExcludeRegionIdsScope):  # String
		self.add_query_param('ExcludeRegionIdsScope', ExcludeRegionIdsScope)
	def get_ExcludeResourceIdsScope(self): # String
		return self.get_query_params().get('ExcludeResourceIdsScope')

	def set_ExcludeResourceIdsScope(self, ExcludeResourceIdsScope):  # String
		self.add_query_param('ExcludeResourceIdsScope', ExcludeResourceIdsScope)
	def get_RuleId(self): # String
		return self.get_query_params().get('RuleId')

	def set_RuleId(self, RuleId):  # String
		self.add_query_param('RuleId', RuleId)
