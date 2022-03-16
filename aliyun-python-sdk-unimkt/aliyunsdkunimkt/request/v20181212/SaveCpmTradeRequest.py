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
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'SaveCpmTrade')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TaskType(self): # String
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # String
		self.add_query_param('TaskType', TaskType)
	def get_RealCostAmount(self): # String
		return self.get_query_params().get('RealCostAmount')

	def set_RealCostAmount(self, RealCostAmount):  # String
		self.add_query_param('RealCostAmount', RealCostAmount)
	def get_Sex(self): # String
		return self.get_query_params().get('Sex')

	def set_Sex(self, Sex):  # String
		self.add_query_param('Sex', Sex)
	def get_CostDetail(self): # String
		return self.get_query_params().get('CostDetail')

	def set_CostDetail(self, CostDetail):  # String
		self.add_query_param('CostDetail', CostDetail)
	def get_TaskTag(self): # String
		return self.get_query_params().get('TaskTag')

	def set_TaskTag(self, TaskTag):  # String
		self.add_query_param('TaskTag', TaskTag)
	def get_BizType(self): # String
		return self.get_query_params().get('BizType')

	def set_BizType(self, BizType):  # String
		self.add_query_param('BizType', BizType)
	def get_DeviceCode(self): # String
		return self.get_query_params().get('DeviceCode')

	def set_DeviceCode(self, DeviceCode):  # String
		self.add_query_param('DeviceCode', DeviceCode)
	def get_V(self): # String
		return self.get_query_params().get('V')

	def set_V(self, V):  # String
		self.add_query_param('V', V)
	def get_ApplyPrice(self): # String
		return self.get_query_params().get('ApplyPrice')

	def set_ApplyPrice(self, ApplyPrice):  # String
		self.add_query_param('ApplyPrice', ApplyPrice)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_HoldId(self): # String
		return self.get_query_params().get('HoldId')

	def set_HoldId(self, HoldId):  # String
		self.add_query_param('HoldId', HoldId)
	def get_ExtendString(self): # String
		return self.get_query_params().get('ExtendString')

	def set_ExtendString(self, ExtendString):  # String
		self.add_query_param('ExtendString', ExtendString)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
	def get_Age(self): # Integer
		return self.get_query_params().get('Age')

	def set_Age(self, Age):  # Integer
		self.add_query_param('Age', Age)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_AdvertType(self): # String
		return self.get_query_params().get('AdvertType')

	def set_AdvertType(self, AdvertType):  # String
		self.add_query_param('AdvertType', AdvertType)
	def get_OuterCode(self): # String
		return self.get_query_params().get('OuterCode')

	def set_OuterCode(self, OuterCode):  # String
		self.add_query_param('OuterCode', OuterCode)
	def get_TradeTime(self): # Long
		return self.get_query_params().get('TradeTime')

	def set_TradeTime(self, TradeTime):  # Long
		self.add_query_param('TradeTime', TradeTime)
