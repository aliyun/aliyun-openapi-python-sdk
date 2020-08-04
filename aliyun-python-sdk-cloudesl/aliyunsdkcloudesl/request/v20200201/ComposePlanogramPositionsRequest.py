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
from aliyunsdkcloudesl.endpoint import endpoint_data

class ComposePlanogramPositionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'ComposePlanogramPositions','cloudesl')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ActionType(self):
		return self.get_body_params().get('ActionType')

	def set_ActionType(self,ActionType):
		self.add_body_params('ActionType', ActionType)

	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_Layer(self):
		return self.get_body_params().get('Layer')

	def set_Layer(self,Layer):
		self.add_body_params('Layer', Layer)

	def get_LayerOrigin(self):
		return self.get_body_params().get('LayerOrigin')

	def set_LayerOrigin(self,LayerOrigin):
		self.add_body_params('LayerOrigin', LayerOrigin)

	def get_BeAutoRefresh(self):
		return self.get_body_params().get('BeAutoRefresh')

	def set_BeAutoRefresh(self,BeAutoRefresh):
		self.add_body_params('BeAutoRefresh', BeAutoRefresh)

	def get_Shelf(self):
		return self.get_body_params().get('Shelf')

	def set_Shelf(self,Shelf):
		self.add_body_params('Shelf', Shelf)

	def get_ShelfPositionInfos(self):
		return self.get_body_params().get('ShelfPositionInfos')

	def set_ShelfPositionInfos(self, ShelfPositionInfos):
		for depth1 in range(len(ShelfPositionInfos)):
			if ShelfPositionInfos[depth1].get('OffsetFrom') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(depth1 + 1) + '.OffsetFrom', ShelfPositionInfos[depth1].get('OffsetFrom'))
			if ShelfPositionInfos[depth1].get('Depth') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(depth1 + 1) + '.Depth', ShelfPositionInfos[depth1].get('Depth'))
			if ShelfPositionInfos[depth1].get('Column') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(depth1 + 1) + '.Column', ShelfPositionInfos[depth1].get('Column'))
			if ShelfPositionInfos[depth1].get('Facing') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(depth1 + 1) + '.Facing', ShelfPositionInfos[depth1].get('Facing'))
			if ShelfPositionInfos[depth1].get('OffsetTo') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(depth1 + 1) + '.OffsetTo', ShelfPositionInfos[depth1].get('OffsetTo'))
			if ShelfPositionInfos[depth1].get('ItemBarCode') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(depth1 + 1) + '.ItemBarCode', ShelfPositionInfos[depth1].get('ItemBarCode'))