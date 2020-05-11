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
from aliyunsdklinkedmall.endpoint import endpoint_data

class AddItemLimitRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'linkedmall', '2018-01-16', 'AddItemLimitRule','linkedmall')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UpperNum(self):
		return self.get_query_params().get('UpperNum')

	def set_UpperNum(self,UpperNum):
		self.add_query_param('UpperNum',UpperNum)

	def get_LmActivityId(self):
		return self.get_query_params().get('LmActivityId')

	def set_LmActivityId(self,LmActivityId):
		self.add_query_param('LmActivityId',LmActivityId)

	def get_RuleType(self):
		return self.get_query_params().get('RuleType')

	def set_RuleType(self,RuleType):
		self.add_query_param('RuleType',RuleType)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_LmItemId(self):
		return self.get_query_params().get('LmItemId')

	def set_LmItemId(self,LmItemId):
		self.add_query_param('LmItemId',LmItemId)

	def get_BeginTime(self):
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self,BeginTime):
		self.add_query_param('BeginTime',BeginTime)

	def get_SubBizCode(self):
		return self.get_query_params().get('SubBizCode')

	def set_SubBizCode(self,SubBizCode):
		self.add_query_param('SubBizCode',SubBizCode)

	def get_ItemId(self):
		return self.get_query_params().get('ItemId')

	def set_ItemId(self,ItemId):
		self.add_query_param('ItemId',ItemId)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)