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


	def get_RealCostAmount(self):
		return self.get_query_params().get('RealCostAmount')

	def set_RealCostAmount(self,RealCostAmount):
		self.add_query_param('RealCostAmount',RealCostAmount)

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

	def get_DeviceType(self):
		return self.get_query_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_query_param('DeviceType',DeviceType)

	def get_DeviceCode(self):
		return self.get_query_params().get('DeviceCode')

	def set_DeviceCode(self,DeviceCode):
		self.add_query_param('DeviceCode',DeviceCode)

	def get_ApplyPrice(self):
		return self.get_query_params().get('ApplyPrice')

	def set_ApplyPrice(self,ApplyPrice):
		self.add_query_param('ApplyPrice',ApplyPrice)

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)

	def get_OuterCode(self):
		return self.get_query_params().get('OuterCode')

	def set_OuterCode(self,OuterCode):
		self.add_query_param('OuterCode',OuterCode)

	def get_QueryStr(self):
		return self.get_query_params().get('QueryStr')

	def set_QueryStr(self,QueryStr):
		self.add_query_param('QueryStr',QueryStr)

	def get_Phase(self):
		return self.get_query_params().get('Phase')

	def set_Phase(self,Phase):
		self.add_query_param('Phase',Phase)

	def get_BizResult(self):
		return self.get_query_params().get('BizResult')

	def set_BizResult(self,BizResult):
		self.add_query_param('BizResult',BizResult)

	def get_TaskType(self):
		return self.get_query_params().get('TaskType')

	def set_TaskType(self,TaskType):
		self.add_query_param('TaskType',TaskType)

	def get_BrandUserId(self):
		return self.get_query_params().get('BrandUserId')

	def set_BrandUserId(self,BrandUserId):
		self.add_query_param('BrandUserId',BrandUserId)

	def get_Sex(self):
		return self.get_query_params().get('Sex')

	def set_Sex(self,Sex):
		self.add_query_param('Sex',Sex)

	def get_CostDetail(self):
		return self.get_query_params().get('CostDetail')

	def set_CostDetail(self,CostDetail):
		self.add_query_param('CostDetail',CostDetail)

	def get_ProxyUserId(self):
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self,ProxyUserId):
		self.add_query_param('ProxyUserId',ProxyUserId)

	def get_AlipayOpenId(self):
		return self.get_query_params().get('AlipayOpenId')

	def set_AlipayOpenId(self,AlipayOpenId):
		self.add_query_param('AlipayOpenId',AlipayOpenId)

	def get_BizType(self):
		return self.get_query_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_query_param('BizType',BizType)

	def get_BrandNick(self):
		return self.get_query_params().get('BrandNick')

	def set_BrandNick(self,BrandNick):
		self.add_query_param('BrandNick',BrandNick)

	def get_V(self):
		return self.get_query_params().get('V')

	def set_V(self,V):
		self.add_query_param('V',V)

	def get_ChargeTag(self):
		return self.get_query_params().get('ChargeTag')

	def set_ChargeTag(self,ChargeTag):
		self.add_query_param('ChargeTag',ChargeTag)

	def get_Age(self):
		return self.get_query_params().get('Age')

	def set_Age(self,Age):
		self.add_query_param('Age',Age)

	def get_ChannelId(self):
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_query_param('ChannelId',ChannelId)

	def get_Cid(self):
		return self.get_query_params().get('Cid')

	def set_Cid(self,Cid):
		self.add_query_param('Cid',Cid)