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

class CreateCenRouteMapRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'CreateCenRouteMap','Cbn')
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
		return self.get_query_params().get('DestinationCidrBlockss')

	def set_DestinationCidrBlockss(self,DestinationCidrBlockss):
		for i in range(len(DestinationCidrBlockss)):	
			if DestinationCidrBlockss[i] is not None:
				self.add_query_param('DestinationCidrBlocks.' + str(i + 1) , DestinationCidrBlockss[i]);

	def get_SourceInstanceIdss(self):
		return self.get_query_params().get('SourceInstanceIdss')

	def set_SourceInstanceIdss(self,SourceInstanceIdss):
		for i in range(len(SourceInstanceIdss)):	
			if SourceInstanceIdss[i] is not None:
				self.add_query_param('SourceInstanceIds.' + str(i + 1) , SourceInstanceIdss[i]);

	def get_SourceRegionIdss(self):
		return self.get_query_params().get('SourceRegionIdss')

	def set_SourceRegionIdss(self,SourceRegionIdss):
		for i in range(len(SourceRegionIdss)):	
			if SourceRegionIdss[i] is not None:
				self.add_query_param('SourceRegionIds.' + str(i + 1) , SourceRegionIdss[i]);

	def get_MatchAsnss(self):
		return self.get_query_params().get('MatchAsnss')

	def set_MatchAsnss(self,MatchAsnss):
		for i in range(len(MatchAsnss)):	
			if MatchAsnss[i] is not None:
				self.add_query_param('MatchAsns.' + str(i + 1) , MatchAsnss[i]);

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
		return self.get_query_params().get('DestinationChildInstanceTypess')

	def set_DestinationChildInstanceTypess(self,DestinationChildInstanceTypess):
		for i in range(len(DestinationChildInstanceTypess)):	
			if DestinationChildInstanceTypess[i] is not None:
				self.add_query_param('DestinationChildInstanceTypes.' + str(i + 1) , DestinationChildInstanceTypess[i]);

	def get_SourceRouteTableIdss(self):
		return self.get_query_params().get('SourceRouteTableIdss')

	def set_SourceRouteTableIdss(self,SourceRouteTableIdss):
		for i in range(len(SourceRouteTableIdss)):	
			if SourceRouteTableIdss[i] is not None:
				self.add_query_param('SourceRouteTableIds.' + str(i + 1) , SourceRouteTableIdss[i]);

	def get_SourceChildInstanceTypess(self):
		return self.get_query_params().get('SourceChildInstanceTypess')

	def set_SourceChildInstanceTypess(self,SourceChildInstanceTypess):
		for i in range(len(SourceChildInstanceTypess)):	
			if SourceChildInstanceTypess[i] is not None:
				self.add_query_param('SourceChildInstanceTypes.' + str(i + 1) , SourceChildInstanceTypess[i]);

	def get_CommunityOperateMode(self):
		return self.get_query_params().get('CommunityOperateMode')

	def set_CommunityOperateMode(self,CommunityOperateMode):
		self.add_query_param('CommunityOperateMode',CommunityOperateMode)

	def get_OperateCommunitySets(self):
		return self.get_query_params().get('OperateCommunitySets')

	def set_OperateCommunitySets(self,OperateCommunitySets):
		for i in range(len(OperateCommunitySets)):	
			if OperateCommunitySets[i] is not None:
				self.add_query_param('OperateCommunitySet.' + str(i + 1) , OperateCommunitySets[i]);

	def get_RouteTypess(self):
		return self.get_query_params().get('RouteTypess')

	def set_RouteTypess(self,RouteTypess):
		for i in range(len(RouteTypess)):	
			if RouteTypess[i] is not None:
				self.add_query_param('RouteTypes.' + str(i + 1) , RouteTypess[i]);

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
		return self.get_query_params().get('DestinationRouteTableIdss')

	def set_DestinationRouteTableIdss(self,DestinationRouteTableIdss):
		for i in range(len(DestinationRouteTableIdss)):	
			if DestinationRouteTableIdss[i] is not None:
				self.add_query_param('DestinationRouteTableIds.' + str(i + 1) , DestinationRouteTableIdss[i]);

	def get_TransmitDirection(self):
		return self.get_query_params().get('TransmitDirection')

	def set_TransmitDirection(self,TransmitDirection):
		self.add_query_param('TransmitDirection',TransmitDirection)

	def get_DestinationInstanceIdss(self):
		return self.get_query_params().get('DestinationInstanceIdss')

	def set_DestinationInstanceIdss(self,DestinationInstanceIdss):
		for i in range(len(DestinationInstanceIdss)):	
			if DestinationInstanceIdss[i] is not None:
				self.add_query_param('DestinationInstanceIds.' + str(i + 1) , DestinationInstanceIdss[i]);

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

	def get_PrependAsPaths(self):
		return self.get_query_params().get('PrependAsPaths')

	def set_PrependAsPaths(self,PrependAsPaths):
		for i in range(len(PrependAsPaths)):	
			if PrependAsPaths[i] is not None:
				self.add_query_param('PrependAsPath.' + str(i + 1) , PrependAsPaths[i]);

	def get_AsPathMatchMode(self):
		return self.get_query_params().get('AsPathMatchMode')

	def set_AsPathMatchMode(self,AsPathMatchMode):
		self.add_query_param('AsPathMatchMode',AsPathMatchMode)

	def get_MatchCommunitySets(self):
		return self.get_query_params().get('MatchCommunitySets')

	def set_MatchCommunitySets(self,MatchCommunitySets):
		for i in range(len(MatchCommunitySets)):	
			if MatchCommunitySets[i] is not None:
				self.add_query_param('MatchCommunitySet.' + str(i + 1) , MatchCommunitySets[i]);

	def get_CenRegionId(self):
		return self.get_query_params().get('CenRegionId')

	def set_CenRegionId(self,CenRegionId):
		self.add_query_param('CenRegionId',CenRegionId)