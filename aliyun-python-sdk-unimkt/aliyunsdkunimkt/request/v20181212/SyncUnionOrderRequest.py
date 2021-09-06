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


	def get_ProxyChannelId(self):
		return self.get_query_params().get('ProxyChannelId')

	def set_ProxyChannelId(self,ProxyChannelId):
		self.add_query_param('ProxyChannelId',ProxyChannelId)

	def get_TaskType(self):
		return self.get_query_params().get('TaskType')

	def set_TaskType(self,TaskType):
		self.add_query_param('TaskType',TaskType)

	def get_RealCostAmount(self):
		return self.get_query_params().get('RealCostAmount')

	def set_RealCostAmount(self,RealCostAmount):
		self.add_query_param('RealCostAmount',RealCostAmount)

	def get_TaskBizType(self):
		return self.get_query_params().get('TaskBizType')

	def set_TaskBizType(self,TaskBizType):
		self.add_query_param('TaskBizType',TaskBizType)

	def get_Sex(self):
		return self.get_query_params().get('Sex')

	def set_Sex(self,Sex):
		self.add_query_param('Sex',Sex)

	def get_BrandUserId(self):
		return self.get_query_params().get('BrandUserId')

	def set_BrandUserId(self,BrandUserId):
		self.add_query_param('BrandUserId',BrandUserId)

	def get_BrandName(self):
		return self.get_query_params().get('BrandName')

	def set_BrandName(self,BrandName):
		self.add_query_param('BrandName',BrandName)

	def get_ProxyUserId(self):
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self,ProxyUserId):
		self.add_query_param('ProxyUserId',ProxyUserId)

	def get_DeviceId(self):
		return self.get_query_params().get('DeviceId')

	def set_DeviceId(self,DeviceId):
		self.add_query_param('DeviceId',DeviceId)

	def get_HolderId(self):
		return self.get_query_params().get('HolderId')

	def set_HolderId(self,HolderId):
		self.add_query_param('HolderId',HolderId)

	def get_BizSerialNumber(self):
		return self.get_query_params().get('BizSerialNumber')

	def set_BizSerialNumber(self,BizSerialNumber):
		self.add_query_param('BizSerialNumber',BizSerialNumber)

	def get_TaskRuleType(self):
		return self.get_query_params().get('TaskRuleType')

	def set_TaskRuleType(self,TaskRuleType):
		self.add_query_param('TaskRuleType',TaskRuleType)

	def get_V(self):
		return self.get_query_params().get('V')

	def set_V(self,V):
		self.add_query_param('V',V)

	def get_IndustryLabelBagId(self):
		return self.get_query_params().get('IndustryLabelBagId')

	def set_IndustryLabelBagId(self,IndustryLabelBagId):
		self.add_query_param('IndustryLabelBagId',IndustryLabelBagId)

	def get_ApplyPrice(self):
		return self.get_query_params().get('ApplyPrice')

	def set_ApplyPrice(self,ApplyPrice):
		self.add_query_param('ApplyPrice',ApplyPrice)

	def get_ExtendInfo(self):
		return self.get_query_params().get('ExtendInfo')

	def set_ExtendInfo(self,ExtendInfo):
		self.add_query_param('ExtendInfo',ExtendInfo)

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

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)