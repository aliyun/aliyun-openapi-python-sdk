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

class CreateVpnPbrRouteEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateVpnPbrRouteEntry','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RouteSource(self): # String
		return self.get_query_params().get('RouteSource')

	def set_RouteSource(self, RouteSource):  # String
		self.add_query_param('RouteSource', RouteSource)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_PublishVpc(self): # Boolean
		return self.get_query_params().get('PublishVpc')

	def set_PublishVpc(self, PublishVpc):  # Boolean
		self.add_query_param('PublishVpc', PublishVpc)
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
	def get_Weight(self): # Integer
		return self.get_query_params().get('Weight')

	def set_Weight(self, Weight):  # Integer
		self.add_query_param('Weight', Weight)
	def get_VpnGatewayId(self): # String
		return self.get_query_params().get('VpnGatewayId')

	def set_VpnGatewayId(self, VpnGatewayId):  # String
		self.add_query_param('VpnGatewayId', VpnGatewayId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_RouteDest(self): # String
		return self.get_query_params().get('RouteDest')

	def set_RouteDest(self, RouteDest):  # String
		self.add_query_param('RouteDest', RouteDest)
	def get_NextHop(self): # String
		return self.get_query_params().get('NextHop')

	def set_NextHop(self, NextHop):  # String
		self.add_query_param('NextHop', NextHop)
	def get_OverlayMode(self): # String
		return self.get_query_params().get('OverlayMode')

	def set_OverlayMode(self, OverlayMode):  # String
		self.add_query_param('OverlayMode', OverlayMode)
