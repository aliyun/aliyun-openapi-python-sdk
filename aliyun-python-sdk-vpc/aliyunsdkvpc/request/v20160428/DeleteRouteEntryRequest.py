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
class DeleteRouteEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DeleteRouteEntry','vpc')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RouteTableId(self):
		return self.get_query_params().get('RouteTableId')

	def set_RouteTableId(self,RouteTableId):
		self.add_query_param('RouteTableId',RouteTableId)

	def get_DestinationCidrBlock(self):
		return self.get_query_params().get('DestinationCidrBlock')

	def set_DestinationCidrBlock(self,DestinationCidrBlock):
		self.add_query_param('DestinationCidrBlock',DestinationCidrBlock)

	def get_NextHopId(self):
		return self.get_query_params().get('NextHopId')

	def set_NextHopId(self,NextHopId):
		self.add_query_param('NextHopId',NextHopId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)
	def  set_NextHopList_1_NextHopType(self, NextHopList_1_NextHopType):
		self.add_query_param('NextHopList.1.NextHopType', NextHopList_1_NextHopType)

	def  get_NextHopList_1_NextHopType(self):
		self.get_query_params().get('NextHopList.1.NextHopType')

	def  set_NextHopList_2_NextHopType(self, NextHopList_2_NextHopType):
		self.add_query_param('NextHopList.2.NextHopType', NextHopList_2_NextHopType)

	def  get_NextHopList_2_NextHopType(self):
		self.get_query_params().get('NextHopList.2.NextHopType')

	def  set_NextHopList_3_NextHopType(self, NextHopList_3_NextHopType):
		self.add_query_param('NextHopList.3.NextHopType', NextHopList_3_NextHopType)

	def  get_NextHopList_3_NextHopType(self):
		self.get_query_params().get('NextHopList.3.NextHopType')

	def  set_NextHopList_4_NextHopType(self, NextHopList_4_NextHopType):
		self.add_query_param('NextHopList.4.NextHopType', NextHopList_4_NextHopType)

	def  get_NextHopList_4_NextHopType(self):
		self.get_query_params().get('NextHopList.4.NextHopType')

	def  set_NextHopList_1_NextHopId(self, NextHopList_1_NextHopId):
		self.add_query_param('NextHopList.1.NextHopId', NextHopList_1_NextHopId)

	def  get_NextHopList_1_NextHopId(self):
		self.get_query_params().get('NextHopList.1.NextHopId')

	def  set_NextHopList_2_NextHopId(self, NextHopList_2_NextHopId):
		self.add_query_param('NextHopList.2.NextHopId', NextHopList_2_NextHopId)

	def  get_NextHopList_2_NextHopId(self):
		self.get_query_params().get('NextHopList.2.NextHopId')

	def  set_NextHopList_3_NextHopId(self, NextHopList_3_NextHopId):
		self.add_query_param('NextHopList.3.NextHopId', NextHopList_3_NextHopId)

	def  get_NextHopList_3_NextHopId(self):
		self.get_query_params().get('NextHopList.3.NextHopId')

	def  set_NextHopList_4_NextHopId(self, NextHopList_4_NextHopId):
		self.add_query_param('NextHopList.4.NextHopId', NextHopList_4_NextHopId)

	def  get_NextHopList_4_NextHopId(self):
		self.get_query_params().get('NextHopList.4.NextHopId')



