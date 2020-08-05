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

class PushTradeDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'PushTradeDetail','uniMkt')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SalePrice(self):
		return self.get_body_params().get('SalePrice')

	def set_SalePrice(self,SalePrice):
		self.add_body_params('SalePrice', SalePrice)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_TradeStatus(self):
		return self.get_body_params().get('TradeStatus')

	def set_TradeStatus(self,TradeStatus):
		self.add_body_params('TradeStatus', TradeStatus)

	def get_CommodityId(self):
		return self.get_body_params().get('CommodityId')

	def set_CommodityId(self,CommodityId):
		self.add_body_params('CommodityId', CommodityId)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_TradeOrderId(self):
		return self.get_body_params().get('TradeOrderId')

	def set_TradeOrderId(self,TradeOrderId):
		self.add_body_params('TradeOrderId', TradeOrderId)

	def get_DeviceSn(self):
		return self.get_body_params().get('DeviceSn')

	def set_DeviceSn(self,DeviceSn):
		self.add_body_params('DeviceSn', DeviceSn)

	def get_CommodityName(self):
		return self.get_body_params().get('CommodityName')

	def set_CommodityName(self,CommodityName):
		self.add_body_params('CommodityName', CommodityName)

	def get_VerificationStatus(self):
		return self.get_body_params().get('VerificationStatus')

	def set_VerificationStatus(self,VerificationStatus):
		self.add_body_params('VerificationStatus', VerificationStatus)

	def get_AlipayOrderId(self):
		return self.get_body_params().get('AlipayOrderId')

	def set_AlipayOrderId(self,AlipayOrderId):
		self.add_body_params('AlipayOrderId', AlipayOrderId)

	def get_ChannelId(self):
		return self.get_body_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_body_params('ChannelId', ChannelId)

	def get_OuterTradeId(self):
		return self.get_body_params().get('OuterTradeId')

	def set_OuterTradeId(self,OuterTradeId):
		self.add_body_params('OuterTradeId', OuterTradeId)

	def get_TradeTime(self):
		return self.get_body_params().get('TradeTime')

	def set_TradeTime(self,TradeTime):
		self.add_body_params('TradeTime', TradeTime)

	def get_TradePrice(self):
		return self.get_body_params().get('TradePrice')

	def set_TradePrice(self,TradePrice):
		self.add_body_params('TradePrice', TradePrice)