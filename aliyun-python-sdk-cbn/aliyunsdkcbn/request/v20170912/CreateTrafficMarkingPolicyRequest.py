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
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'CreateTrafficMarkingPolicy','cbn')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_TrafficMarkingPolicyDescription(self):
		return self.get_query_params().get('TrafficMarkingPolicyDescription')

	def set_TrafficMarkingPolicyDescription(self,TrafficMarkingPolicyDescription):
		self.add_query_param('TrafficMarkingPolicyDescription',TrafficMarkingPolicyDescription)

	def get_TrafficMarkingPolicyName(self):
		return self.get_query_params().get('TrafficMarkingPolicyName')

	def set_TrafficMarkingPolicyName(self,TrafficMarkingPolicyName):
		self.add_query_param('TrafficMarkingPolicyName',TrafficMarkingPolicyName)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_TrafficMatchRuless(self):
		return self.get_query_params().get('TrafficMatchRules')

	def set_TrafficMatchRuless(self, TrafficMatchRuless):
		for depth1 in range(len(TrafficMatchRuless)):
			if TrafficMatchRuless[depth1].get('DstPortRange') is not None:
				for depth2 in range(len(TrafficMatchRuless[depth1].get('DstPortRange'))):
					if TrafficMatchRuless[depth1].get('DstPortRange')[depth2] is not None:
						self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.DstPortRange.' + str(depth2 + 1) , TrafficMatchRuless[depth1].get('DstPortRange')[depth2])
			if TrafficMatchRuless[depth1].get('MatchDscp') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.MatchDscp', TrafficMatchRuless[depth1].get('MatchDscp'))
			if TrafficMatchRuless[depth1].get('Protocol') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.Protocol', TrafficMatchRuless[depth1].get('Protocol'))
			if TrafficMatchRuless[depth1].get('TrafficMatchRuleDescription') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.TrafficMatchRuleDescription', TrafficMatchRuless[depth1].get('TrafficMatchRuleDescription'))
			if TrafficMatchRuless[depth1].get('SrcPortRange') is not None:
				for depth2 in range(len(TrafficMatchRuless[depth1].get('SrcPortRange'))):
					if TrafficMatchRuless[depth1].get('SrcPortRange')[depth2] is not None:
						self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.SrcPortRange.' + str(depth2 + 1) , TrafficMatchRuless[depth1].get('SrcPortRange')[depth2])
			if TrafficMatchRuless[depth1].get('DstCidr') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.DstCidr', TrafficMatchRuless[depth1].get('DstCidr'))
			if TrafficMatchRuless[depth1].get('TrafficMatchRuleName') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.TrafficMatchRuleName', TrafficMatchRuless[depth1].get('TrafficMatchRuleName'))
			if TrafficMatchRuless[depth1].get('SrcCidr') is not None:
				self.add_query_param('TrafficMatchRules.' + str(depth1 + 1) + '.SrcCidr', TrafficMatchRuless[depth1].get('SrcCidr'))

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TransitRouterId(self):
		return self.get_query_params().get('TransitRouterId')

	def set_TransitRouterId(self,TransitRouterId):
		self.add_query_param('TransitRouterId',TransitRouterId)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_MarkingDscp(self):
		return self.get_query_params().get('MarkingDscp')

	def set_MarkingDscp(self,MarkingDscp):
		self.add_query_param('MarkingDscp',MarkingDscp)