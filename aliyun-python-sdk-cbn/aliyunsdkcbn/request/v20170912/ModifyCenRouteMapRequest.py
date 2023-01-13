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

class ModifyCenRouteMapRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'ModifyCenRouteMap')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_CommunityMatchMode(self): # String
		return self.get_query_params().get('CommunityMatchMode')

	def set_CommunityMatchMode(self, CommunityMatchMode):  # String
		self.add_query_param('CommunityMatchMode', CommunityMatchMode)
	def get_MapResult(self): # String
		return self.get_query_params().get('MapResult')

	def set_MapResult(self, MapResult):  # String
		self.add_query_param('MapResult', MapResult)
	def get_NextPriority(self): # Integer
		return self.get_query_params().get('NextPriority')

	def set_NextPriority(self, NextPriority):  # Integer
		self.add_query_param('NextPriority', NextPriority)
	def get_DestinationCidrBlockss(self): # RepeatList
		return self.get_query_params().get('DestinationCidrBlocks')

	def set_DestinationCidrBlockss(self, DestinationCidrBlocks):  # RepeatList
		for depth1 in range(len(DestinationCidrBlocks)):
			self.add_query_param('DestinationCidrBlocks.' + str(depth1 + 1), DestinationCidrBlocks[depth1])
	def get_SourceInstanceIdss(self): # RepeatList
		return self.get_query_params().get('SourceInstanceIds')

	def set_SourceInstanceIdss(self, SourceInstanceIds):  # RepeatList
		for depth1 in range(len(SourceInstanceIds)):
			self.add_query_param('SourceInstanceIds.' + str(depth1 + 1), SourceInstanceIds[depth1])
	def get_SourceRegionIdss(self): # RepeatList
		return self.get_query_params().get('SourceRegionIds')

	def set_SourceRegionIdss(self, SourceRegionIds):  # RepeatList
		for depth1 in range(len(SourceRegionIds)):
			self.add_query_param('SourceRegionIds.' + str(depth1 + 1), SourceRegionIds[depth1])
	def get_MatchAsnss(self): # RepeatList
		return self.get_query_params().get('MatchAsns')

	def set_MatchAsnss(self, MatchAsns):  # RepeatList
		for depth1 in range(len(MatchAsns)):
			self.add_query_param('MatchAsns.' + str(depth1 + 1), MatchAsns[depth1])
	def get_Preference(self): # Integer
		return self.get_query_params().get('Preference')

	def set_Preference(self, Preference):  # Integer
		self.add_query_param('Preference', Preference)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_DestinationChildInstanceTypess(self): # RepeatList
		return self.get_query_params().get('DestinationChildInstanceTypes')

	def set_DestinationChildInstanceTypess(self, DestinationChildInstanceTypes):  # RepeatList
		for depth1 in range(len(DestinationChildInstanceTypes)):
			self.add_query_param('DestinationChildInstanceTypes.' + str(depth1 + 1), DestinationChildInstanceTypes[depth1])
	def get_SourceRouteTableIdss(self): # RepeatList
		return self.get_query_params().get('SourceRouteTableIds')

	def set_SourceRouteTableIdss(self, SourceRouteTableIds):  # RepeatList
		for depth1 in range(len(SourceRouteTableIds)):
			self.add_query_param('SourceRouteTableIds.' + str(depth1 + 1), SourceRouteTableIds[depth1])
	def get_SourceChildInstanceTypess(self): # RepeatList
		return self.get_query_params().get('SourceChildInstanceTypes')

	def set_SourceChildInstanceTypess(self, SourceChildInstanceTypes):  # RepeatList
		for depth1 in range(len(SourceChildInstanceTypes)):
			self.add_query_param('SourceChildInstanceTypes.' + str(depth1 + 1), SourceChildInstanceTypes[depth1])
	def get_CommunityOperateMode(self): # String
		return self.get_query_params().get('CommunityOperateMode')

	def set_CommunityOperateMode(self, CommunityOperateMode):  # String
		self.add_query_param('CommunityOperateMode', CommunityOperateMode)
	def get_OperateCommunitySets(self): # RepeatList
		return self.get_query_params().get('OperateCommunitySet')

	def set_OperateCommunitySets(self, OperateCommunitySet):  # RepeatList
		for depth1 in range(len(OperateCommunitySet)):
			self.add_query_param('OperateCommunitySet.' + str(depth1 + 1), OperateCommunitySet[depth1])
	def get_RouteTypess(self): # RepeatList
		return self.get_query_params().get('RouteTypes')

	def set_RouteTypess(self, RouteTypes):  # RepeatList
		for depth1 in range(len(RouteTypes)):
			self.add_query_param('RouteTypes.' + str(depth1 + 1), RouteTypes[depth1])
	def get_MatchAddressType(self): # String
		return self.get_query_params().get('MatchAddressType')

	def set_MatchAddressType(self, MatchAddressType):  # String
		self.add_query_param('MatchAddressType', MatchAddressType)
	def get_CidrMatchMode(self): # String
		return self.get_query_params().get('CidrMatchMode')

	def set_CidrMatchMode(self, CidrMatchMode):  # String
		self.add_query_param('CidrMatchMode', CidrMatchMode)
	def get_CenId(self): # String
		return self.get_query_params().get('CenId')

	def set_CenId(self, CenId):  # String
		self.add_query_param('CenId', CenId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_SourceInstanceIdsReverseMatch(self): # Boolean
		return self.get_query_params().get('SourceInstanceIdsReverseMatch')

	def set_SourceInstanceIdsReverseMatch(self, SourceInstanceIdsReverseMatch):  # Boolean
		self.add_query_param('SourceInstanceIdsReverseMatch', SourceInstanceIdsReverseMatch)
	def get_DestinationRouteTableIdss(self): # RepeatList
		return self.get_query_params().get('DestinationRouteTableIds')

	def set_DestinationRouteTableIdss(self, DestinationRouteTableIds):  # RepeatList
		for depth1 in range(len(DestinationRouteTableIds)):
			self.add_query_param('DestinationRouteTableIds.' + str(depth1 + 1), DestinationRouteTableIds[depth1])
	def get_DestinationInstanceIdss(self): # RepeatList
		return self.get_query_params().get('DestinationInstanceIds')

	def set_DestinationInstanceIdss(self, DestinationInstanceIds):  # RepeatList
		for depth1 in range(len(DestinationInstanceIds)):
			self.add_query_param('DestinationInstanceIds.' + str(depth1 + 1), DestinationInstanceIds[depth1])
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_DestinationInstanceIdsReverseMatch(self): # Boolean
		return self.get_query_params().get('DestinationInstanceIdsReverseMatch')

	def set_DestinationInstanceIdsReverseMatch(self, DestinationInstanceIdsReverseMatch):  # Boolean
		self.add_query_param('DestinationInstanceIdsReverseMatch', DestinationInstanceIdsReverseMatch)
	def get_RouteMapId(self): # String
		return self.get_query_params().get('RouteMapId')

	def set_RouteMapId(self, RouteMapId):  # String
		self.add_query_param('RouteMapId', RouteMapId)
	def get_PrependAsPaths(self): # RepeatList
		return self.get_query_params().get('PrependAsPath')

	def set_PrependAsPaths(self, PrependAsPath):  # RepeatList
		for depth1 in range(len(PrependAsPath)):
			self.add_query_param('PrependAsPath.' + str(depth1 + 1), PrependAsPath[depth1])
	def get_AsPathMatchMode(self): # String
		return self.get_query_params().get('AsPathMatchMode')

	def set_AsPathMatchMode(self, AsPathMatchMode):  # String
		self.add_query_param('AsPathMatchMode', AsPathMatchMode)
	def get_MatchCommunitySets(self): # RepeatList
		return self.get_query_params().get('MatchCommunitySet')

	def set_MatchCommunitySets(self, MatchCommunitySet):  # RepeatList
		for depth1 in range(len(MatchCommunitySet)):
			self.add_query_param('MatchCommunitySet.' + str(depth1 + 1), MatchCommunitySet[depth1])
	def get_CenRegionId(self): # String
		return self.get_query_params().get('CenRegionId')

	def set_CenRegionId(self, CenRegionId):  # String
		self.add_query_param('CenRegionId', CenRegionId)
