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

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_IngressRuless(self): # RepeatList
		return self.get_query_params().get('IngressRules')

	def set_IngressRuless(self, IngressRules):  # RepeatList
		for depth1 in range(len(IngressRules)):
			if IngressRules[depth1].get('Action') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.Action', IngressRules[depth1].get('Action'))
			if IngressRules[depth1].get('SourceCidrBlock') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.SourceCidrBlock', IngressRules[depth1].get('SourceCidrBlock'))
			if IngressRules[depth1].get('Protocol') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.Protocol', IngressRules[depth1].get('Protocol'))
			if IngressRules[depth1].get('IpVersion') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.IpVersion', IngressRules[depth1].get('IpVersion'))
			if IngressRules[depth1].get('DestinationPortRange') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.DestinationPortRange', IngressRules[depth1].get('DestinationPortRange'))
			if IngressRules[depth1].get('Priority') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.Priority', IngressRules[depth1].get('Priority'))
			if IngressRules[depth1].get('DestinationCidrBlock') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.DestinationCidrBlock', IngressRules[depth1].get('DestinationCidrBlock'))
			if IngressRules[depth1].get('SourcePortRange') is not None:
				self.add_query_param('IngressRules.' + str(depth1 + 1) + '.SourcePortRange', IngressRules[depth1].get('SourcePortRange'))
	def get_TrafficMirrorFilterName(self): # String
		return self.get_query_params().get('TrafficMirrorFilterName')

	def set_TrafficMirrorFilterName(self, TrafficMirrorFilterName):  # String
		self.add_query_param('TrafficMirrorFilterName', TrafficMirrorFilterName)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
	def get_EgressRuless(self): # RepeatList
		return self.get_query_params().get('EgressRules')

	def set_EgressRuless(self, EgressRules):  # RepeatList
		for depth1 in range(len(EgressRules)):
			if EgressRules[depth1].get('Action') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.Action', EgressRules[depth1].get('Action'))
			if EgressRules[depth1].get('SourceCidrBlock') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.SourceCidrBlock', EgressRules[depth1].get('SourceCidrBlock'))
			if EgressRules[depth1].get('Protocol') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.Protocol', EgressRules[depth1].get('Protocol'))
			if EgressRules[depth1].get('IpVersion') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.IpVersion', EgressRules[depth1].get('IpVersion'))
			if EgressRules[depth1].get('DestinationPortRange') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.DestinationPortRange', EgressRules[depth1].get('DestinationPortRange'))
			if EgressRules[depth1].get('Priority') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.Priority', EgressRules[depth1].get('Priority'))
			if EgressRules[depth1].get('DestinationCidrBlock') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.DestinationCidrBlock', EgressRules[depth1].get('DestinationCidrBlock'))
			if EgressRules[depth1].get('SourcePortRange') is not None:
				self.add_query_param('EgressRules.' + str(depth1 + 1) + '.SourcePortRange', EgressRules[depth1].get('SourcePortRange'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
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
	def get_TrafficMirrorFilterDescription(self): # String
		return self.get_query_params().get('TrafficMirrorFilterDescription')

	def set_TrafficMirrorFilterDescription(self, TrafficMirrorFilterDescription):  # String
		self.add_query_param('TrafficMirrorFilterDescription', TrafficMirrorFilterDescription)
