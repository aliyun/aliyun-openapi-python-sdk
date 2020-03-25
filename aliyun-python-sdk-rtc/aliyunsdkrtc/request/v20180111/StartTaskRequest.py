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
from aliyunsdkrtc.endpoint import endpoint_data

class StartTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'StartTask','rtc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MixPaness(self):
		return self.get_query_params().get('MixPaness')

	def set_MixPaness(self,MixPaness):
		for i in range(len(MixPaness)):	
			if MixPaness[i].get('PaneId') is not None:
				self.add_query_param('MixPanes.' + str(i + 1) + '.PaneId' , MixPaness[i].get('PaneId'))
			if MixPaness[i].get('UserId') is not None:
				self.add_query_param('MixPanes.' + str(i + 1) + '.UserId' , MixPaness[i].get('UserId'))
			if MixPaness[i].get('SourceType') is not None:
				self.add_query_param('MixPanes.' + str(i + 1) + '.SourceType' , MixPaness[i].get('SourceType'))


	def get_IdempotentId(self):
		return self.get_query_params().get('IdempotentId')

	def set_IdempotentId(self,IdempotentId):
		self.add_query_param('IdempotentId',IdempotentId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TemplateId(self):
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_query_param('TemplateId',TemplateId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_ChannelId(self):
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_query_param('ChannelId',ChannelId)