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
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'ModifyCenRouteMap','cbn')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_CommunityMatchMode(self):
		return self.get_query_params().get('CommunityMatchMode')

	def set_CommunityMatchMode(self,CommunityMatchMode):
		self.add_query_param('CommunityMatchMode',CommunityMatchMode)

	def get_MapResult(self):
		return self.get_query_params().get('MapResult')

	def set_MapResult(self,MapResult):
		self.add_query_param('MapResult',MapResult)

	def get_NextPriority(self):
		return self.get_query_params().get('NextPriority')

	def set_NextPriority(self,NextPriority):
		self.add_query_param('NextPriority',NextPriority)

	def get_DestinationCidrBlockss(self):
		return self.get_query_params().get('DestinationCidrBlocks')

	def set_DestinationCidrBlockss(self, DestinationCidrBlockss):
		for depth1 in range(len(DestinationCidrBlockss)):
			if DestinationCidrBlockss[depth1] is not None:
				self.add_query_param('DestinationCidrBlocks.' + str(depth1 + 1) , DestinationCidrBlockss[depth1])

	def get_SourceInstanceIdss(self):
		return self.get_query_params().get('SourceInstanceIds')

	def set_SourceInstanceIdss(self, SourceInstanceIdss):
		for depth1 in range(len(SourceInstanceIdss)):
			if SourceInstanceIdss[depth1] is not None:
				self.add_query_param('SourceInstanceIds.' + str(depth1 + 1) , SourceInstanceIdss[depth1])

	def get_SourceRegionIdss(self):
		return self.get_query_params().get('SourceRegionIds')

	def set_SourceRegionIdss(self, SourceRegionIdss):
		for depth1 in range(len(SourceRegionIdss)):
			if SourceRegionIdss[depth1] is not None:
				self.add_query_param('SourceRegionIds.' + str(depth1 + 1) , SourceRegionIdss[depth1])

	def get_MatchAsnss(self):
		return self.get_query_params().get('MatchAsns')

	def set_MatchAsnss(self, MatchAsnss):
		for depth1 in range(len(MatchAsnss)):
			if MatchAsnss[depth1] is not None:
				self.add_query_param('MatchAsns.' + str(depth1 + 1) , MatchAsnss[depth1])

	def get_Preference(self):
		return self.get_query_params().get('Preference')

	def set_Preference(self,Preference):
		self.add_query_param('Preference',Preference)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_DestinationChildInstanceTypess(self):
		return self.get_query_params().get('DestinationChildInstanceTypes')

	def set_DestinationChildInstanceTypess(self, DestinationChildInstanceTypess):
		for depth1 in range(len(DestinationChildInstanceTypess)):
			if DestinationChildInstanceTypess[depth1] is not None:
				self.add_query_param('DestinationChildInstanceTypes.' + str(depth1 + 1) , DestinationChildInstanceTypess[depth1])

	def get_SourceRouteTableIdss(self):
		return self.get_query_params().get('SourceRouteTableIds')

	def set_SourceRouteTableIdss(self, SourceRouteTableIdss):
		for depth1 in range(len(SourceRouteTableIdss)):
			if SourceRouteTableIdss[depth1] is not None:
				self.add_query_param('SourceRouteTableIds.' + str(depth1 + 1) , SourceRouteTableIdss[depth1])

	def get_SourceChildInstanceTypess(self):
		return self.get_query_params().get('SourceChildInstanceTypes')

	def set_SourceChildInstanceTypess(self, SourceChildInstanceTypess):
		for depth1 in range(len(SourceChildInstanceTypess)):
			if SourceChildInstanceTypess[depth1] is not None:
				self.add_query_param('SourceChildInstanceTypes.' + str(depth1 + 1) , SourceChildInstanceTypess[depth1])

	def get_CommunityOperateMode(self):
		return self.get_query_params().get('CommunityOperateMode')

	def set_CommunityOperateMode(self,CommunityOperateMode):
		self.add_query_param('CommunityOperateMode',CommunityOperateMode)

	def get_OperateCommunitySets(self):
		return self.get_query_params().get('OperateCommunitySet')

	def set_OperateCommunitySets(self, OperateCommunitySets):
		for depth1 in range(len(OperateCommunitySets)):
			if OperateCommunitySets[depth1] is not None:
				self.add_query_param('OperateCommunitySet.' + str(depth1 + 1) , OperateCommunitySets[depth1])

	def get_RouteTypess(self):
		return self.get_query_params().get('RouteTypes')

	def set_RouteTypess(self, RouteTypess):
		for depth1 in range(len(RouteTypess)):
			if RouteTypess[depth1] is not None:
				self.add_query_param('RouteTypes.' + str(depth1 + 1) , RouteTypess[depth1])

	def get_CidrMatchMode(self):
		return self.get_query_params().get('CidrMatchMode')

	def set_CidrMatchMode(self,CidrMatchMode):
		self.add_query_param('CidrMatchMode',CidrMatchMode)

	def get_CenId(self):
		return self.get_query_params().get('CenId')

	def set_CenId(self,CenId):
		self.add_query_param('CenId',CenId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_SourceInstanceIdsReverseMatch(self):
		return self.get_query_params().get('SourceInstanceIdsReverseMatch')

	def set_SourceInstanceIdsReverseMatch(self,SourceInstanceIdsReverseMatch):
		self.add_query_param('SourceInstanceIdsReverseMatch',SourceInstanceIdsReverseMatch)

	def get_DestinationRouteTableIdss(self):
		return self.get_query_params().get('DestinationRouteTableIds')

	def set_DestinationRouteTableIdss(self, DestinationRouteTableIdss):
		for depth1 in range(len(DestinationRouteTableIdss)):
			if DestinationRouteTableIdss[depth1] is not None:
				self.add_query_param('DestinationRouteTableIds.' + str(depth1 + 1) , DestinationRouteTableIdss[depth1])

	def get_DestinationInstanceIdss(self):
		return self.get_query_params().get('DestinationInstanceIds')

	def set_DestinationInstanceIdss(self, DestinationInstanceIdss):
		for depth1 in range(len(DestinationInstanceIdss)):
			if DestinationInstanceIdss[depth1] is not None:
				self.add_query_param('DestinationInstanceIds.' + str(depth1 + 1) , DestinationInstanceIdss[depth1])

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_DestinationInstanceIdsReverseMatch(self):
		return self.get_query_params().get('DestinationInstanceIdsReverseMatch')

	def set_DestinationInstanceIdsReverseMatch(self,DestinationInstanceIdsReverseMatch):
		self.add_query_param('DestinationInstanceIdsReverseMatch',DestinationInstanceIdsReverseMatch)

	def get_RouteMapId(self):
		return self.get_query_params().get('RouteMapId')

	def set_RouteMapId(self,RouteMapId):
		self.add_query_param('RouteMapId',RouteMapId)

	def get_PrependAsPaths(self):
		return self.get_query_params().get('PrependAsPath')

	def set_PrependAsPaths(self, PrependAsPaths):
		for depth1 in range(len(PrependAsPaths)):
			if PrependAsPaths[depth1] is not None:
				self.add_query_param('PrependAsPath.' + str(depth1 + 1) , PrependAsPaths[depth1])

	def get_AsPathMatchMode(self):
		return self.get_query_params().get('AsPathMatchMode')

	def set_AsPathMatchMode(self,AsPathMatchMode):
		self.add_query_param('AsPathMatchMode',AsPathMatchMode)

	def get_MatchCommunitySets(self):
		return self.get_query_params().get('MatchCommunitySet')

	def set_MatchCommunitySets(self, MatchCommunitySets):
		for depth1 in range(len(MatchCommunitySets)):
			if MatchCommunitySets[depth1] is not None:
				self.add_query_param('MatchCommunitySet.' + str(depth1 + 1) , MatchCommunitySets[depth1])

	def get_CenRegionId(self):
		return self.get_query_params().get('CenRegionId')

	def set_CenRegionId(self,CenRegionId):
		self.add_query_param('CenRegionId',CenRegionId)