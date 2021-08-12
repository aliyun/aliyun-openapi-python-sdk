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

class CreateTransitRouterPeerAttachmentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'CreateTransitRouterPeerAttachment','cbn')
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

	def get_CenId(self):
		return self.get_query_params().get('CenId')

	def set_CenId(self,CenId):
		self.add_query_param('CenId',CenId)

	def get_TransitRouterAttachmentName(self):
		return self.get_query_params().get('TransitRouterAttachmentName')

	def set_TransitRouterAttachmentName(self,TransitRouterAttachmentName):
		self.add_query_param('TransitRouterAttachmentName',TransitRouterAttachmentName)

	def get_AutoPublishRouteEnabled(self):
		return self.get_query_params().get('AutoPublishRouteEnabled')

	def set_AutoPublishRouteEnabled(self,AutoPublishRouteEnabled):
		self.add_query_param('AutoPublishRouteEnabled',AutoPublishRouteEnabled)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

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

	def get_TransitRouterAttachmentDescription(self):
		return self.get_query_params().get('TransitRouterAttachmentDescription')

	def set_TransitRouterAttachmentDescription(self,TransitRouterAttachmentDescription):
		self.add_query_param('TransitRouterAttachmentDescription',TransitRouterAttachmentDescription)

	def get_PeerTransitRouterRegionId(self):
		return self.get_query_params().get('PeerTransitRouterRegionId')

	def set_PeerTransitRouterRegionId(self,PeerTransitRouterRegionId):
		self.add_query_param('PeerTransitRouterRegionId',PeerTransitRouterRegionId)

	def get_CenBandwidthPackageId(self):
		return self.get_query_params().get('CenBandwidthPackageId')

	def set_CenBandwidthPackageId(self,CenBandwidthPackageId):
		self.add_query_param('CenBandwidthPackageId',CenBandwidthPackageId)

	def get_PeerTransitRouterId(self):
		return self.get_query_params().get('PeerTransitRouterId')

	def set_PeerTransitRouterId(self,PeerTransitRouterId):
		self.add_query_param('PeerTransitRouterId',PeerTransitRouterId)