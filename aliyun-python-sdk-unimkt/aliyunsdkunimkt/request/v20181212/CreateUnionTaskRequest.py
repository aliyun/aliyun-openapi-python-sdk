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

	def get_TaskType(self): # String
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # String
		self.add_query_param('TaskType', TaskType)
	def get_CustomCreativeType(self): # String
		return self.get_query_params().get('CustomCreativeType')

	def set_CustomCreativeType(self, CustomCreativeType):  # String
		self.add_query_param('CustomCreativeType', CustomCreativeType)
	def get_TaskBizType(self): # String
		return self.get_query_params().get('TaskBizType')

	def set_TaskBizType(self, TaskBizType):  # String
		self.add_query_param('TaskBizType', TaskBizType)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_BrandUserId(self): # Long
		return self.get_query_params().get('BrandUserId')

	def set_BrandUserId(self, BrandUserId):  # Long
		self.add_query_param('BrandUserId', BrandUserId)
	def get_ContentId(self): # Long
		return self.get_query_params().get('ContentId')

	def set_ContentId(self, ContentId):  # Long
		self.add_query_param('ContentId', ContentId)
	def get_Channel(self): # String
		return self.get_query_params().get('Channel')

	def set_Channel(self, Channel):  # String
		self.add_query_param('Channel', Channel)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_BrandUserNick(self): # String
		return self.get_query_params().get('BrandUserNick')

	def set_BrandUserNick(self, BrandUserNick):  # String
		self.add_query_param('BrandUserNick', BrandUserNick)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_ProxyUserId(self): # Long
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self, ProxyUserId):  # Long
		self.add_query_param('ProxyUserId', ProxyUserId)
	def get_ContentUrl(self): # String
		return self.get_query_params().get('ContentUrl')

	def set_ContentUrl(self, ContentUrl):  # String
		self.add_query_param('ContentUrl', ContentUrl)
	def get_TaskRuleType(self): # String
		return self.get_query_params().get('TaskRuleType')

	def set_TaskRuleType(self, TaskRuleType):  # String
		self.add_query_param('TaskRuleType', TaskRuleType)
	def get_Quota(self): # Long
		return self.get_query_params().get('Quota')

	def set_Quota(self, Quota):  # Long
		self.add_query_param('Quota', Quota)
	def get_IndustryLabelBagId(self): # Integer
		return self.get_query_params().get('IndustryLabelBagId')

	def set_IndustryLabelBagId(self, IndustryLabelBagId):  # Integer
		self.add_query_param('IndustryLabelBagId', IndustryLabelBagId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_QuotaDay(self): # Long
		return self.get_query_params().get('QuotaDay')

	def set_QuotaDay(self, QuotaDay):  # Long
		self.add_query_param('QuotaDay', QuotaDay)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
