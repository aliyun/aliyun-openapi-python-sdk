# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class PutContactRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutContact','cms')

	def get_ContactName(self):
		return self.get_query_params().get('ContactName')

	def set_ContactName(self,ContactName):
		self.add_query_param('ContactName',ContactName)

	def get_ChannelsMail(self):
		return self.get_query_params().get('Channels.Mail')

	def set_ChannelsMail(self,ChannelsMail):
		self.add_query_param('Channels.Mail',ChannelsMail)

	def get_ChannelsAliIM(self):
		return self.get_query_params().get('Channels.AliIM')

	def set_ChannelsAliIM(self,ChannelsAliIM):
		self.add_query_param('Channels.AliIM',ChannelsAliIM)

	def get_ChannelsDingWebHook(self):
		return self.get_query_params().get('Channels.DingWebHook')

	def set_ChannelsDingWebHook(self,ChannelsDingWebHook):
		self.add_query_param('Channels.DingWebHook',ChannelsDingWebHook)

	def get_Describe(self):
		return self.get_query_params().get('Describe')

	def set_Describe(self,Describe):
		self.add_query_param('Describe',Describe)

	def get_ChannelsSMS(self):
		return self.get_query_params().get('Channels.SMS')

	def set_ChannelsSMS(self,ChannelsSMS):
		self.add_query_param('Channels.SMS',ChannelsSMS)