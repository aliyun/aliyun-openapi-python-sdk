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

class SaveCpmTradeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'SaveCpmTrade','uniMkt')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TaskType(self):
		return self.get_query_params().get('TaskType')

	def set_TaskType(self,TaskType):
		self.add_query_param('TaskType',TaskType)

	def get_RealCostAmount(self):
		return self.get_query_params().get('RealCostAmount')

	def set_RealCostAmount(self,RealCostAmount):
		self.add_query_param('RealCostAmount',RealCostAmount)

	def get_Sex(self):
		return self.get_query_params().get('Sex')

	def set_Sex(self,Sex):
		self.add_query_param('Sex',Sex)

	def get_CostDetail(self):
		return self.get_query_params().get('CostDetail')

	def set_CostDetail(self,CostDetail):
		self.add_query_param('CostDetail',CostDetail)

	def get_TaskTag(self):
		return self.get_query_params().get('TaskTag')

	def set_TaskTag(self,TaskTag):
		self.add_query_param('TaskTag',TaskTag)

	def get_BizType(self):
		return self.get_query_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_query_param('BizType',BizType)

	def get_DeviceCode(self):
		return self.get_query_params().get('DeviceCode')

	def set_DeviceCode(self,DeviceCode):
		self.add_query_param('DeviceCode',DeviceCode)

	def get_V(self):
		return self.get_query_params().get('V')

	def set_V(self,V):
		self.add_query_param('V',V)

	def get_ApplyPrice(self):
		return self.get_query_params().get('ApplyPrice')

	def set_ApplyPrice(self,ApplyPrice):
		self.add_query_param('ApplyPrice',ApplyPrice)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_HoldId(self):
		return self.get_query_params().get('HoldId')

	def set_HoldId(self,HoldId):
		self.add_query_param('HoldId',HoldId)

	def get_ExtendString(self):
		return self.get_query_params().get('ExtendString')

	def set_ExtendString(self,ExtendString):
		self.add_query_param('ExtendString',ExtendString)

	def get_ChannelId(self):
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_query_param('ChannelId',ChannelId)

	def get_Age(self):
		return self.get_query_params().get('Age')

	def set_Age(self,Age):
		self.add_query_param('Age',Age)

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)

	def get_AdvertType(self):
		return self.get_query_params().get('AdvertType')

	def set_AdvertType(self,AdvertType):
		self.add_query_param('AdvertType',AdvertType)

	def get_OuterCode(self):
		return self.get_query_params().get('OuterCode')

	def set_OuterCode(self,OuterCode):
		self.add_query_param('OuterCode',OuterCode)

	def get_TradeTime(self):
		return self.get_query_params().get('TradeTime')

	def set_TradeTime(self,TradeTime):
		self.add_query_param('TradeTime',TradeTime)