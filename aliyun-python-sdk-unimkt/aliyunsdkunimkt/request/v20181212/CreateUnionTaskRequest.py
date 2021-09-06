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

class CreateUnionTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'CreateUnionTask')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TaskType(self):
		return self.get_query_params().get('TaskType')

	def set_TaskType(self,TaskType):
		self.add_query_param('TaskType',TaskType)

	def get_CustomCreativeType(self):
		return self.get_query_params().get('CustomCreativeType')

	def set_CustomCreativeType(self,CustomCreativeType):
		self.add_query_param('CustomCreativeType',CustomCreativeType)

	def get_TaskBizType(self):
		return self.get_query_params().get('TaskBizType')

	def set_TaskBizType(self,TaskBizType):
		self.add_query_param('TaskBizType',TaskBizType)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_BrandUserId(self):
		return self.get_query_params().get('BrandUserId')

	def set_BrandUserId(self,BrandUserId):
		self.add_query_param('BrandUserId',BrandUserId)

	def get_ContentId(self):
		return self.get_query_params().get('ContentId')

	def set_ContentId(self,ContentId):
		self.add_query_param('ContentId',ContentId)

	def get_Channel(self):
		return self.get_query_params().get('Channel')

	def set_Channel(self,Channel):
		self.add_query_param('Channel',Channel)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_BrandUserNick(self):
		return self.get_query_params().get('BrandUserNick')

	def set_BrandUserNick(self,BrandUserNick):
		self.add_query_param('BrandUserNick',BrandUserNick)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_ProxyUserId(self):
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self,ProxyUserId):
		self.add_query_param('ProxyUserId',ProxyUserId)

	def get_ContentUrl(self):
		return self.get_query_params().get('ContentUrl')

	def set_ContentUrl(self,ContentUrl):
		self.add_query_param('ContentUrl',ContentUrl)

	def get_TaskRuleType(self):
		return self.get_query_params().get('TaskRuleType')

	def set_TaskRuleType(self,TaskRuleType):
		self.add_query_param('TaskRuleType',TaskRuleType)

	def get_Quota(self):
		return self.get_query_params().get('Quota')

	def set_Quota(self,Quota):
		self.add_query_param('Quota',Quota)

	def get_IndustryLabelBagId(self):
		return self.get_query_params().get('IndustryLabelBagId')

	def set_IndustryLabelBagId(self,IndustryLabelBagId):
		self.add_query_param('IndustryLabelBagId',IndustryLabelBagId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_QuotaDay(self):
		return self.get_query_params().get('QuotaDay')

	def set_QuotaDay(self,QuotaDay):
		self.add_query_param('QuotaDay',QuotaDay)

	def get_ChannelId(self):
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_query_param('ChannelId',ChannelId)