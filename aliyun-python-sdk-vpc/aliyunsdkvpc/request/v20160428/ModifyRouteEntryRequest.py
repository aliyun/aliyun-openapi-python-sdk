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

class ModifyRouteEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyRouteEntry','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_RouteEntryName(self): # String
		return self.get_query_params().get('RouteEntryName')

	def set_RouteEntryName(self, RouteEntryName):  # String
		self.add_query_param('RouteEntryName', RouteEntryName)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_NewNextHopId(self): # String
		return self.get_query_params().get('NewNextHopId')

	def set_NewNextHopId(self, NewNextHopId):  # String
		self.add_query_param('NewNextHopId', NewNextHopId)
	def get_RouteTableId(self): # String
		return self.get_query_params().get('RouteTableId')

	def set_RouteTableId(self, RouteTableId):  # String
		self.add_query_param('RouteTableId', RouteTableId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_DestinationCidrBlock(self): # String
		return self.get_query_params().get('DestinationCidrBlock')

	def set_DestinationCidrBlock(self, DestinationCidrBlock):  # String
		self.add_query_param('DestinationCidrBlock', DestinationCidrBlock)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_NewNextHopType(self): # String
		return self.get_query_params().get('NewNextHopType')

	def set_NewNextHopType(self, NewNextHopType):  # String
		self.add_query_param('NewNextHopType', NewNextHopType)
	def get_RouteEntryId(self): # String
		return self.get_query_params().get('RouteEntryId')

	def set_RouteEntryId(self, RouteEntryId):  # String
		self.add_query_param('RouteEntryId', RouteEntryId)
