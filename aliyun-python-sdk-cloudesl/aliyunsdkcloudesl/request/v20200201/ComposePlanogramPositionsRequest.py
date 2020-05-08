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
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ActionType(self):
		return self.get_body_params().get('ActionType')

	def set_ActionType(self,ActionType):
		self.add_body_params('ActionType', ActionType)

	def get_BeAutoRefresh(self):
		return self.get_body_params().get('BeAutoRefresh')

	def set_BeAutoRefresh(self,BeAutoRefresh):
		self.add_body_params('BeAutoRefresh', BeAutoRefresh)

	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_Layer(self):
		return self.get_body_params().get('Layer')

	def set_Layer(self,Layer):
		self.add_body_params('Layer', Layer)

	def get_Shelf(self):
		return self.get_body_params().get('Shelf')

	def set_Shelf(self,Shelf):
		self.add_body_params('Shelf', Shelf)

	def get_LayerOrigin(self):
		return self.get_body_params().get('LayerOrigin')

	def set_LayerOrigin(self,LayerOrigin):
		self.add_body_params('LayerOrigin', LayerOrigin)

	def get_ShelfPositionInfos(self):
		return self.get_body_params().get('ShelfPositionInfos')

	def set_ShelfPositionInfos(self,ShelfPositionInfos):
		for i in range(len(ShelfPositionInfos)):	
			if ShelfPositionInfos[i].get('OffsetFrom') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(i + 1) + '.OffsetFrom' , ShelfPositionInfos[i].get('OffsetFrom'))
			if ShelfPositionInfos[i].get('Depth') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(i + 1) + '.Depth' , ShelfPositionInfos[i].get('Depth'))
			if ShelfPositionInfos[i].get('Column') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(i + 1) + '.Column' , ShelfPositionInfos[i].get('Column'))
			if ShelfPositionInfos[i].get('Facing') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(i + 1) + '.Facing' , ShelfPositionInfos[i].get('Facing'))
			if ShelfPositionInfos[i].get('OffsetTo') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(i + 1) + '.OffsetTo' , ShelfPositionInfos[i].get('OffsetTo'))
			if ShelfPositionInfos[i].get('ItemBarCode') is not None:
				self.add_body_params('ShelfPositionInfo.' + str(i + 1) + '.ItemBarCode' , ShelfPositionInfos[i].get('ItemBarCode'))
