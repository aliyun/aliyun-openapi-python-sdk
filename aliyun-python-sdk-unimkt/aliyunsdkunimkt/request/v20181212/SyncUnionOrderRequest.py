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

class SyncUnionOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'SyncUnionOrder')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProxyChannelId(self): # String
		return self.get_query_params().get('ProxyChannelId')

	def set_ProxyChannelId(self, ProxyChannelId):  # String
		self.add_query_param('ProxyChannelId', ProxyChannelId)
	def get_TaskType(self): # String
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # String
		self.add_query_param('TaskType', TaskType)
	def get_RealCostAmount(self): # Long
		return self.get_query_params().get('RealCostAmount')

	def set_RealCostAmount(self, RealCostAmount):  # Long
		self.add_query_param('RealCostAmount', RealCostAmount)
	def get_TaskBizType(self): # String
		return self.get_query_params().get('TaskBizType')

	def set_TaskBizType(self, TaskBizType):  # String
		self.add_query_param('TaskBizType', TaskBizType)
	def get_Sex(self): # String
		return self.get_query_params().get('Sex')

	def set_Sex(self, Sex):  # String
		self.add_query_param('Sex', Sex)
	def get_BrandUserId(self): # Long
		return self.get_query_params().get('BrandUserId')

	def set_BrandUserId(self, BrandUserId):  # Long
		self.add_query_param('BrandUserId', BrandUserId)
	def get_BrandName(self): # String
		return self.get_query_params().get('BrandName')

	def set_BrandName(self, BrandName):  # String
		self.add_query_param('BrandName', BrandName)
	def get_ProxyUserId(self): # Long
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self, ProxyUserId):  # Long
		self.add_query_param('ProxyUserId', ProxyUserId)
	def get_DeviceId(self): # String
		return self.get_query_params().get('DeviceId')

	def set_DeviceId(self, DeviceId):  # String
		self.add_query_param('DeviceId', DeviceId)
	def get_HolderId(self): # String
		return self.get_query_params().get('HolderId')

	def set_HolderId(self, HolderId):  # String
		self.add_query_param('HolderId', HolderId)
	def get_BizSerialNumber(self): # String
		return self.get_query_params().get('BizSerialNumber')

	def set_BizSerialNumber(self, BizSerialNumber):  # String
		self.add_query_param('BizSerialNumber', BizSerialNumber)
	def get_TaskRuleType(self): # String
		return self.get_query_params().get('TaskRuleType')

	def set_TaskRuleType(self, TaskRuleType):  # String
		self.add_query_param('TaskRuleType', TaskRuleType)
	def get_V(self): # String
		return self.get_query_params().get('V')

	def set_V(self, V):  # String
		self.add_query_param('V', V)
	def get_IndustryLabelBagId(self): # Integer
		return self.get_query_params().get('IndustryLabelBagId')

	def set_IndustryLabelBagId(self, IndustryLabelBagId):  # Integer
		self.add_query_param('IndustryLabelBagId', IndustryLabelBagId)
	def get_ApplyPrice(self): # Long
		return self.get_query_params().get('ApplyPrice')

	def set_ApplyPrice(self, ApplyPrice):  # Long
		self.add_query_param('ApplyPrice', ApplyPrice)
	def get_TradeTimeString(self): # String
		return self.get_query_params().get('TradeTimeString')

	def set_TradeTimeString(self, TradeTimeString):  # String
		self.add_query_param('TradeTimeString', TradeTimeString)
	def get_ExtendInfo(self): # String
		return self.get_query_params().get('ExtendInfo')

	def set_ExtendInfo(self, ExtendInfo):  # String
		self.add_query_param('ExtendInfo', ExtendInfo)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
	def get_Age(self): # Integer
		return self.get_query_params().get('Age')

	def set_Age(self, Age):  # Integer
		self.add_query_param('Age', Age)
	def get_TaskId(self): # Long
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # Long
		self.add_query_param('TaskId', TaskId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
