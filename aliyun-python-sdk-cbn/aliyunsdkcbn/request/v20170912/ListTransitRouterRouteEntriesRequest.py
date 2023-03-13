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

class ListTransitRouterRouteEntriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'ListTransitRouterRouteEntries')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TransitRouterRouteEntryType(self): # String
		return self.get_query_params().get('TransitRouterRouteEntryType')

	def set_TransitRouterRouteEntryType(self, TransitRouterRouteEntryType):  # String
		self.add_query_param('TransitRouterRouteEntryType', TransitRouterRouteEntryType)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_TransitRouterRouteEntryNextHopResourceType(self): # String
		return self.get_query_params().get('TransitRouterRouteEntryNextHopResourceType')

	def set_TransitRouterRouteEntryNextHopResourceType(self, TransitRouterRouteEntryNextHopResourceType):  # String
		self.add_query_param('TransitRouterRouteEntryNextHopResourceType', TransitRouterRouteEntryNextHopResourceType)
	def get_TransitRouterRouteEntryNextHopType(self): # String
		return self.get_query_params().get('TransitRouterRouteEntryNextHopType')

	def set_TransitRouterRouteEntryNextHopType(self, TransitRouterRouteEntryNextHopType):  # String
		self.add_query_param('TransitRouterRouteEntryNextHopType', TransitRouterRouteEntryNextHopType)
	def get_TransitRouterRouteEntryDestinationCidrBlock(self): # String
		return self.get_query_params().get('TransitRouterRouteEntryDestinationCidrBlock')

	def set_TransitRouterRouteEntryDestinationCidrBlock(self, TransitRouterRouteEntryDestinationCidrBlock):  # String
		self.add_query_param('TransitRouterRouteEntryDestinationCidrBlock', TransitRouterRouteEntryDestinationCidrBlock)
	def get_TransitRouterRouteTableId(self): # String
		return self.get_query_params().get('TransitRouterRouteTableId')

	def set_TransitRouterRouteTableId(self, TransitRouterRouteTableId):  # String
		self.add_query_param('TransitRouterRouteTableId', TransitRouterRouteTableId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_PrefixListId(self): # String
		return self.get_query_params().get('PrefixListId')

	def set_PrefixListId(self, PrefixListId):  # String
		self.add_query_param('PrefixListId', PrefixListId)
	def get_TransitRouterRouteEntryNextHopId(self): # String
		return self.get_query_params().get('TransitRouterRouteEntryNextHopId')

	def set_TransitRouterRouteEntryNextHopId(self, TransitRouterRouteEntryNextHopId):  # String
		self.add_query_param('TransitRouterRouteEntryNextHopId', TransitRouterRouteEntryNextHopId)
	def get_TransitRouterRouteEntryStatus(self): # String
		return self.get_query_params().get('TransitRouterRouteEntryStatus')

	def set_TransitRouterRouteEntryStatus(self, TransitRouterRouteEntryStatus):  # String
		self.add_query_param('TransitRouterRouteEntryStatus', TransitRouterRouteEntryStatus)
	def get_RouteFilters(self): # RepeatList
		return self.get_query_params().get('RouteFilter')

	def set_RouteFilters(self, RouteFilter):  # RepeatList
		for depth1 in range(len(RouteFilter)):
			if RouteFilter[depth1].get('Value') is not None:
				for depth2 in range(len(RouteFilter[depth1].get('Value'))):
					self.add_query_param('RouteFilter.' + str(depth1 + 1) + '.Value.' + str(depth2 + 1), RouteFilter[depth1].get('Value')[depth2])
			if RouteFilter[depth1].get('Key') is not None:
				self.add_query_param('RouteFilter.' + str(depth1 + 1) + '.Key', RouteFilter[depth1].get('Key'))
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_TransitRouterRouteEntryNamess(self): # RepeatList
		return self.get_query_params().get('TransitRouterRouteEntryNames')

	def set_TransitRouterRouteEntryNamess(self, TransitRouterRouteEntryNames):  # RepeatList
		for depth1 in range(len(TransitRouterRouteEntryNames)):
			self.add_query_param('TransitRouterRouteEntryNames.' + str(depth1 + 1), TransitRouterRouteEntryNames[depth1])
	def get_TransitRouterRouteEntryIdss(self): # RepeatList
		return self.get_query_params().get('TransitRouterRouteEntryIds')

	def set_TransitRouterRouteEntryIdss(self, TransitRouterRouteEntryIds):  # RepeatList
		for depth1 in range(len(TransitRouterRouteEntryIds)):
			self.add_query_param('TransitRouterRouteEntryIds.' + str(depth1 + 1), TransitRouterRouteEntryIds[depth1])
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TransitRouterRouteEntryOriginResourceType(self): # String
		return self.get_query_params().get('TransitRouterRouteEntryOriginResourceType')

	def set_TransitRouterRouteEntryOriginResourceType(self, TransitRouterRouteEntryOriginResourceType):  # String
		self.add_query_param('TransitRouterRouteEntryOriginResourceType', TransitRouterRouteEntryOriginResourceType)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_TransitRouterRouteEntryOriginResourceId(self): # String
		return self.get_query_params().get('TransitRouterRouteEntryOriginResourceId')

	def set_TransitRouterRouteEntryOriginResourceId(self, TransitRouterRouteEntryOriginResourceId):  # String
		self.add_query_param('TransitRouterRouteEntryOriginResourceId', TransitRouterRouteEntryOriginResourceId)
	def get_TransitRouterRouteEntryNextHopResourceId(self): # String
		return self.get_query_params().get('TransitRouterRouteEntryNextHopResourceId')

	def set_TransitRouterRouteEntryNextHopResourceId(self, TransitRouterRouteEntryNextHopResourceId):  # String
		self.add_query_param('TransitRouterRouteEntryNextHopResourceId', TransitRouterRouteEntryNextHopResourceId)
