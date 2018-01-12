# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateRouteEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateRouteEntry','ecs')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_DestinationCidrBlock(self):
		return self.get_query_params().get('DestinationCidrBlock')

	def set_DestinationCidrBlock(self,DestinationCidrBlock):
		self.add_query_param('DestinationCidrBlock',DestinationCidrBlock)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_NextHopId(self):
		return self.get_query_params().get('NextHopId')

	def set_NextHopId(self,NextHopId):
		self.add_query_param('NextHopId',NextHopId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_NextHopType(self):
		return self.get_query_params().get('NextHopType')

	def set_NextHopType(self,NextHopType):
		self.add_query_param('NextHopType',NextHopType)

	def get_NextHopLists(self):
		return self.get_query_params().get('NextHopLists')

	def set_NextHopLists(self,NextHopLists):
		for i in range(len(NextHopLists)):	
			if NextHopLists[i].get('NextHopType') is not None:
				self.add_query_param('NextHopList.' + str(i + 1) + '.NextHopType' , NextHopLists[i].get('NextHopType'))
			if NextHopLists[i].get('NextHopId') is not None:
				self.add_query_param('NextHopList.' + str(i + 1) + '.NextHopId' , NextHopLists[i].get('NextHopId'))


	def get_RouteTableId(self):
		return self.get_query_params().get('RouteTableId')

	def set_RouteTableId(self,RouteTableId):
		self.add_query_param('RouteTableId',RouteTableId)