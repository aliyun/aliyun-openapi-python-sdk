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
from aliyunsdkecs.endpoint import endpoint_data

class CreateRouteEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateRouteEntry','ecs')
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
	def get_NextHopId(self): # String
		return self.get_query_params().get('NextHopId')

	def set_NextHopId(self, NextHopId):  # String
		self.add_query_param('NextHopId', NextHopId)
	def get_NextHopType(self): # String
		return self.get_query_params().get('NextHopType')

	def set_NextHopType(self, NextHopType):  # String
		self.add_query_param('NextHopType', NextHopType)
	def get_RouteTableId(self): # String
		return self.get_query_params().get('RouteTableId')

	def set_RouteTableId(self, RouteTableId):  # String
		self.add_query_param('RouteTableId', RouteTableId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DestinationCidrBlock(self): # String
		return self.get_query_params().get('DestinationCidrBlock')

	def set_DestinationCidrBlock(self, DestinationCidrBlock):  # String
		self.add_query_param('DestinationCidrBlock', DestinationCidrBlock)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_NextHopLists(self): # RepeatList
		return self.get_query_params().get('NextHopList')

	def set_NextHopLists(self, NextHopList):  # RepeatList
		for depth1 in range(len(NextHopList)):
			if NextHopList[depth1].get('NextHopId') is not None:
				self.add_query_param('NextHopList.' + str(depth1 + 1) + '.NextHopId', NextHopList[depth1].get('NextHopId'))
			if NextHopList[depth1].get('NextHopType') is not None:
				self.add_query_param('NextHopList.' + str(depth1 + 1) + '.NextHopType', NextHopList[depth1].get('NextHopType'))
