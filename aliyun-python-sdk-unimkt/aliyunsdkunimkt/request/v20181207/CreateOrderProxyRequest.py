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
from aliyunsdkunimkt.endpoint import endpoint_data

class CreateOrderProxyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-07', 'CreateOrderProxy','uniMkt')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SalePrice(self):
		return self.get_query_params().get('SalePrice')

	def set_SalePrice(self,SalePrice):
		self.add_query_param('SalePrice',SalePrice)

	def get_CommodityId(self):
		return self.get_query_params().get('CommodityId')

	def set_CommodityId(self,CommodityId):
		self.add_query_param('CommodityId',CommodityId)

	def get_HolderId(self):
		return self.get_query_params().get('HolderId')

	def set_HolderId(self,HolderId):
		self.add_query_param('HolderId',HolderId)

	def get_PromotionId(self):
		return self.get_query_params().get('PromotionId')

	def set_PromotionId(self,PromotionId):
		self.add_query_param('PromotionId',PromotionId)

	def get_DeviceType(self):
		return self.get_query_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_query_param('DeviceType',DeviceType)

	def get_AlipayUid(self):
		return self.get_query_params().get('AlipayUid')

	def set_AlipayUid(self,AlipayUid):
		self.add_query_param('AlipayUid',AlipayUid)

	def get_DeviceCode(self):
		return self.get_query_params().get('DeviceCode')

	def set_DeviceCode(self,DeviceCode):
		self.add_query_param('DeviceCode',DeviceCode)

	def get_V(self):
		return self.get_query_params().get('V')

	def set_V(self,V):
		self.add_query_param('V',V)

	def get_ChannelId(self):
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_query_param('ChannelId',ChannelId)

	def get_OuterCode(self):
		return self.get_query_params().get('OuterCode')

	def set_OuterCode(self,OuterCode):
		self.add_query_param('OuterCode',OuterCode)

	def get_QueryStr(self):
		return self.get_query_params().get('QueryStr')

	def set_QueryStr(self,QueryStr):
		self.add_query_param('QueryStr',QueryStr)