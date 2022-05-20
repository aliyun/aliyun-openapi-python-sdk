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
from aliyunsdkess.endpoint import endpoint_data

class DescribeScalingRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribeScalingRules','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_ScalingRuleIds(self): # RepeatList
		return self.get_query_params().get('ScalingRuleId')

	def set_ScalingRuleIds(self, ScalingRuleId):  # RepeatList
		for depth1 in range(len(ScalingRuleId)):
			self.add_query_param('ScalingRuleId.' + str(depth1 + 1), ScalingRuleId[depth1])
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ScalingRuleNames(self): # RepeatList
		return self.get_query_params().get('ScalingRuleName')

	def set_ScalingRuleNames(self, ScalingRuleName):  # RepeatList
		for depth1 in range(len(ScalingRuleName)):
			self.add_query_param('ScalingRuleName.' + str(depth1 + 1), ScalingRuleName[depth1])
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ScalingRuleType(self): # String
		return self.get_query_params().get('ScalingRuleType')

	def set_ScalingRuleType(self, ScalingRuleType):  # String
		self.add_query_param('ScalingRuleType', ScalingRuleType)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ScalingRuleAris(self): # RepeatList
		return self.get_query_params().get('ScalingRuleAri')

	def set_ScalingRuleAris(self, ScalingRuleAri):  # RepeatList
		for depth1 in range(len(ScalingRuleAri)):
			self.add_query_param('ScalingRuleAri.' + str(depth1 + 1), ScalingRuleAri[depth1])
	def get_ShowAlarmRules(self): # Boolean
		return self.get_query_params().get('ShowAlarmRules')

	def set_ShowAlarmRules(self, ShowAlarmRules):  # Boolean
		self.add_query_param('ShowAlarmRules', ShowAlarmRules)
