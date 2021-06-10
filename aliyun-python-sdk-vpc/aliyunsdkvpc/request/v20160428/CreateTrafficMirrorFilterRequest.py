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
from aliyunsdkvpc.endpoint import endpoint_data

class CreateTrafficMirrorFilterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateTrafficMirrorFilter','vpc')
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

	def get_IngressRuless(self):
		return self.get_query_params().get('IngressRules')

	def set_IngressRuless(self, IngressRuless):
		for depth1 in range(len(IngressRuless)):
			if IngressRuless[depth1].get('Priority') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.Priority', IngressRuless[depth1].get('Priority'))
			if IngressRuless[depth1].get('Action') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.Action', IngressRuless[depth1].get('Action'))
			if IngressRuless[depth1].get('Protocol') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.Protocol', IngressRuless[depth1].get('Protocol'))
			if IngressRuless[depth1].get('DestinationCidrBlock') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.DestinationCidrBlock', IngressRuless[depth1].get('DestinationCidrBlock'))
			if IngressRuless[depth1].get('SourceCidrBlock') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.SourceCidrBlock', IngressRuless[depth1].get('SourceCidrBlock'))
			if IngressRuless[depth1].get('DestinationPortRange') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.DestinationPortRange', IngressRuless[depth1].get('DestinationPortRange'))
			if IngressRuless[depth1].get('SourcePortRange') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.SourcePortRange', IngressRuless[depth1].get('SourcePortRange'))

	def get_TrafficMirrorFilterName(self):
		return self.get_query_params().get('TrafficMirrorFilterName')

	def set_TrafficMirrorFilterName(self,TrafficMirrorFilterName):
		self.add_query_param('TrafficMirrorFilterName',TrafficMirrorFilterName)

	def get_EgressRuless(self):
		return self.get_query_params().get('EgressRules')

	def set_EgressRuless(self, EgressRuless):
		for depth1 in range(len(EgressRuless)):
			if EgressRuless[depth1].get('Priority') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.Priority', EgressRuless[depth1].get('Priority'))
			if EgressRuless[depth1].get('Action') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.Action', EgressRuless[depth1].get('Action'))
			if EgressRuless[depth1].get('Protocol') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.Protocol', EgressRuless[depth1].get('Protocol'))
			if EgressRuless[depth1].get('DestinationCidrBlock') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.DestinationCidrBlock', EgressRuless[depth1].get('DestinationCidrBlock'))
			if EgressRuless[depth1].get('SourceCidrBlock') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.SourceCidrBlock', EgressRuless[depth1].get('SourceCidrBlock'))
			if EgressRuless[depth1].get('DestinationPortRange') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.DestinationPortRange', EgressRuless[depth1].get('DestinationPortRange'))
			if EgressRuless[depth1].get('SourcePortRange') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.SourcePortRange', EgressRuless[depth1].get('SourcePortRange'))

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

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

	def get_TrafficMirrorFilterDescription(self):
		return self.get_query_params().get('TrafficMirrorFilterDescription')

	def set_TrafficMirrorFilterDescription(self,TrafficMirrorFilterDescription):
		self.add_query_param('TrafficMirrorFilterDescription',TrafficMirrorFilterDescription)