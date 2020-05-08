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

class CreateMAURuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'CreateMAURule','rtc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UseridPrefix(self):
		return self.get_query_params().get('UseridPrefix')

	def set_UseridPrefix(self,UseridPrefix):
		self.add_query_param('UseridPrefix',UseridPrefix)

	def get_ChannelPrefix(self):
		return self.get_query_params().get('ChannelPrefix')

	def set_ChannelPrefix(self,ChannelPrefix):
		self.add_query_param('ChannelPrefix',ChannelPrefix)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_MauTemplateId(self):
		return self.get_query_params().get('MauTemplateId')

	def set_MauTemplateId(self,MauTemplateId):
		self.add_query_param('MauTemplateId',MauTemplateId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_CallBack(self):
		return self.get_query_params().get('CallBack')

	def set_CallBack(self,CallBack):
		self.add_query_param('CallBack',CallBack)