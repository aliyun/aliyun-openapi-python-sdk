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
from aliyunsdkcbn.endpoint import endpoint_data

class CreateTrafficMarkingPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'CreateTrafficMarkingPolicy')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TrafficMarkingPolicyDescription(self): # String
		return self.get_query_params().get('TrafficMarkingPolicyDescription')

	def set_TrafficMarkingPolicyDescription(self, TrafficMarkingPolicyDescription):  # String
		self.add_query_param('TrafficMarkingPolicyDescription', TrafficMarkingPolicyDescription)
	def get_TrafficMarkingPolicyName(self): # String
		return self.get_query_params().get('TrafficMarkingPolicyName')

	def set_TrafficMarkingPolicyName(self, TrafficMarkingPolicyName):  # String
		self.add_query_param('TrafficMarkingPolicyName', TrafficMarkingPolicyName)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_TrafficMatchRuless(self): # RepeatList
		return self.get_query_params().get('TrafficMatchRules')

	def set_TrafficMatchRuless(self, TrafficMatchRules):  # RepeatList
		for depth1 in range(len(TrafficMatchRules)):
			if TrafficMatchRules[depth1].get('DstPortRange') is not None:
				for depth2 in range(len(TrafficMatchRules[depth1].get('DstPortRange'))):
					self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.DstPortRange.' + str(depth2 + 1), TrafficMatchRules[depth1].get('DstPortRange')[depth2])
			if TrafficMatchRules[depth1].get('MatchDscp') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.MatchDscp', TrafficMatchRules[depth1].get('MatchDscp'))
			if TrafficMatchRules[depth1].get('Protocol') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.Protocol', TrafficMatchRules[depth1].get('Protocol'))
			if TrafficMatchRules[depth1].get('TrafficMatchRuleDescription') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.TrafficMatchRuleDescription', TrafficMatchRules[depth1].get('TrafficMatchRuleDescription'))
			if TrafficMatchRules[depth1].get('SrcPortRange') is not None:
				for depth2 in range(len(TrafficMatchRules[depth1].get('SrcPortRange'))):
					self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.SrcPortRange.' + str(depth2 + 1), TrafficMatchRules[depth1].get('SrcPortRange')[depth2])
			if TrafficMatchRules[depth1].get('DstCidr') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.DstCidr', TrafficMatchRules[depth1].get('DstCidr'))
			if TrafficMatchRules[depth1].get('TrafficMatchRuleName') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.TrafficMatchRuleName', TrafficMatchRules[depth1].get('TrafficMatchRuleName'))
			if TrafficMatchRules[depth1].get('SrcCidr') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.SrcCidr', TrafficMatchRules[depth1].get('SrcCidr'))
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
	def get_TransitRouterId(self): # String
		return self.get_query_params().get('TransitRouterId')

	def set_TransitRouterId(self, TransitRouterId):  # String
		self.add_query_param('TransitRouterId', TransitRouterId)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_MarkingDscp(self): # Integer
		return self.get_query_params().get('MarkingDscp')

	def set_MarkingDscp(self, MarkingDscp):  # Integer
		self.add_query_param('MarkingDscp', MarkingDscp)
