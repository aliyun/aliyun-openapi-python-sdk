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

class ScanCodeNotificationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'ScanCodeNotification')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RealCostAmount(self): # String
		return self.get_query_params().get('RealCostAmount')

	def set_RealCostAmount(self, RealCostAmount):  # String
		self.add_query_param('RealCostAmount', RealCostAmount)
	def get_SalePrice(self): # Integer
		return self.get_query_params().get('SalePrice')

	def set_SalePrice(self, SalePrice):  # Integer
		self.add_query_param('SalePrice', SalePrice)
	def get_CommodityId(self): # String
		return self.get_query_params().get('CommodityId')

	def set_CommodityId(self, CommodityId):  # String
		self.add_query_param('CommodityId', CommodityId)
	def get_TradeTimeStr(self): # String
		return self.get_query_params().get('TradeTimeStr')

	def set_TradeTimeStr(self, TradeTimeStr):  # String
		self.add_query_param('TradeTimeStr', TradeTimeStr)
	def get_HolderId(self): # String
		return self.get_query_params().get('HolderId')

	def set_HolderId(self, HolderId):  # String
		self.add_query_param('HolderId', HolderId)
	def get_DeviceType(self): # String
		return self.get_query_params().get('DeviceType')

	def set_DeviceType(self, DeviceType):  # String
		self.add_query_param('DeviceType', DeviceType)
	def get_DeviceCode(self): # String
		return self.get_query_params().get('DeviceCode')

	def set_DeviceCode(self, DeviceCode):  # String
		self.add_query_param('DeviceCode', DeviceCode)
	def get_ApplyPrice(self): # Integer
		return self.get_query_params().get('ApplyPrice')

	def set_ApplyPrice(self, ApplyPrice):  # Integer
		self.add_query_param('ApplyPrice', ApplyPrice)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_OuterCode(self): # String
		return self.get_query_params().get('OuterCode')

	def set_OuterCode(self, OuterCode):  # String
		self.add_query_param('OuterCode', OuterCode)
	def get_QueryStr(self): # String
		return self.get_query_params().get('QueryStr')

	def set_QueryStr(self, QueryStr):  # String
		self.add_query_param('QueryStr', QueryStr)
	def get_Phase(self): # String
		return self.get_query_params().get('Phase')

	def set_Phase(self, Phase):  # String
		self.add_query_param('Phase', Phase)
	def get_BizResult(self): # String
		return self.get_query_params().get('BizResult')

	def set_BizResult(self, BizResult):  # String
		self.add_query_param('BizResult', BizResult)
	def get_TaskType(self): # String
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # String
		self.add_query_param('TaskType', TaskType)
	def get_BrandUserId(self): # String
		return self.get_query_params().get('BrandUserId')

	def set_BrandUserId(self, BrandUserId):  # String
		self.add_query_param('BrandUserId', BrandUserId)
	def get_Sex(self): # String
		return self.get_query_params().get('Sex')

	def set_Sex(self, Sex):  # String
		self.add_query_param('Sex', Sex)
	def get_CostDetail(self): # String
		return self.get_query_params().get('CostDetail')

	def set_CostDetail(self, CostDetail):  # String
		self.add_query_param('CostDetail', CostDetail)
	def get_ProxyUserId(self): # String
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self, ProxyUserId):  # String
		self.add_query_param('ProxyUserId', ProxyUserId)
	def get_AlipayOpenId(self): # String
		return self.get_query_params().get('AlipayOpenId')

	def set_AlipayOpenId(self, AlipayOpenId):  # String
		self.add_query_param('AlipayOpenId', AlipayOpenId)
	def get_BizType(self): # String
		return self.get_query_params().get('BizType')

	def set_BizType(self, BizType):  # String
		self.add_query_param('BizType', BizType)
	def get_BrandNick(self): # String
		return self.get_query_params().get('BrandNick')

	def set_BrandNick(self, BrandNick):  # String
		self.add_query_param('BrandNick', BrandNick)
	def get_V(self): # String
		return self.get_query_params().get('V')

	def set_V(self, V):  # String
		self.add_query_param('V', V)
	def get_ChargeTag(self): # String
		return self.get_query_params().get('ChargeTag')

	def set_ChargeTag(self, ChargeTag):  # String
		self.add_query_param('ChargeTag', ChargeTag)
	def get_Age(self): # Integer
		return self.get_query_params().get('Age')

	def set_Age(self, Age):  # Integer
		self.add_query_param('Age', Age)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
	def get_Cid(self): # String
		return self.get_query_params().get('Cid')

	def set_Cid(self, Cid):  # String
		self.add_query_param('Cid', Cid)
