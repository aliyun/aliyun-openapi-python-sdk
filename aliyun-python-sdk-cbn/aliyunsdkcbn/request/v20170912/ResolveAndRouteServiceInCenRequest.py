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

class ResolveAndRouteServiceInCenRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'ResolveAndRouteServiceInCen','Cbn')
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

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Host(self):
		return self.get_query_params().get('Host')

	def set_Host(self,Host):
		self.add_query_param('Host',Host)

	def get_HostRegionId(self):
		return self.get_query_params().get('HostRegionId')

	def set_HostRegionId(self,HostRegionId):
		self.add_query_param('HostRegionId',HostRegionId)

	def get_HostVpcId(self):
		return self.get_query_params().get('HostVpcId')

	def set_HostVpcId(self,HostVpcId):
		self.add_query_param('HostVpcId',HostVpcId)

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

	def get_AccessRegionIdss(self):
		return self.get_query_params().get('AccessRegionIdss')

	def set_AccessRegionIdss(self,AccessRegionIdss):
		for i in range(len(AccessRegionIdss)):	
			if AccessRegionIdss[i] is not None:
				self.add_query_param('AccessRegionIds.' + str(i + 1) , AccessRegionIdss[i]);