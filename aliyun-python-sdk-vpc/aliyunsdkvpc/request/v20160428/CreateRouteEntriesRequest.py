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

class CreateRouteEntriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateRouteEntries','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
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
	def get_RouteEntriess(self): # RepeatList
		return self.get_query_params().get('RouteEntries')

	def set_RouteEntriess(self, RouteEntries):  # RepeatList
		for depth1 in range(len(RouteEntries)):
			if RouteEntries[depth1].get('DstCidrBlock') is not None:
				self.add_query_param('RouteEntries.' + str(depth1 + 1) + '.DstCidrBlock', RouteEntries[depth1].get('DstCidrBlock'))
			if RouteEntries[depth1].get('RouteTableId') is not None:
				self.add_query_param('RouteEntries.' + str(depth1 + 1) + '.RouteTableId', RouteEntries[depth1].get('RouteTableId'))
			if RouteEntries[depth1].get('IpVersion') is not None:
				self.add_query_param('RouteEntries.' + str(depth1 + 1) + '.IpVersion', RouteEntries[depth1].get('IpVersion'))
			if RouteEntries[depth1].get('NextHop') is not None:
				self.add_query_param('RouteEntries.' + str(depth1 + 1) + '.NextHop', RouteEntries[depth1].get('NextHop'))
			if RouteEntries[depth1].get('NextHopType') is not None:
				self.add_query_param('RouteEntries.' + str(depth1 + 1) + '.NextHopType', RouteEntries[depth1].get('NextHopType'))
			if RouteEntries[depth1].get('Name') is not None:
				self.add_query_param('RouteEntries.' + str(depth1 + 1) + '.Name', RouteEntries[depth1].get('Name'))
			if RouteEntries[depth1].get('Describption') is not None:
				self.add_query_param('RouteEntries.' + str(depth1 + 1) + '.Describption', RouteEntries[depth1].get('Describption'))
