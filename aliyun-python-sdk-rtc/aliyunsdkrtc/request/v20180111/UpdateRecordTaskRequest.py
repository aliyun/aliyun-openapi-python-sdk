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

class UpdateRecordTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'UpdateRecordTask','rtc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UserPaness(self):
		return self.get_query_params().get('UserPanes')

	def set_UserPaness(self, UserPaness):
		for depth1 in range(len(UserPaness)):
			if UserPaness[depth1].get('PaneId') is not None:
				self.add_query_param('UserPanes.' + str(depth1 + 1) + '.PaneId', UserPaness[depth1].get('PaneId'))
			if UserPaness[depth1].get('UserId') is not None:
				self.add_query_param('UserPanes.' + str(depth1 + 1) + '.UserId', UserPaness[depth1].get('UserId'))
			if UserPaness[depth1].get('SourceType') is not None:
				self.add_query_param('UserPanes.' + str(depth1 + 1) + '.SourceType', UserPaness[depth1].get('SourceType'))
			if UserPaness[depth1].get('Images') is not None:
				for depth2 in range(len(UserPaness[depth1].get('Images'))):
					if UserPaness[depth1].get('Images')[depth2].get('Url') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Images.' + str(depth2 + 1) + '.Url', UserPaness[depth1].get('Images')[depth2].get('Url'))
					if UserPaness[depth1].get('Images')[depth2].get('Display') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Images.' + str(depth2 + 1) + '.Display', UserPaness[depth1].get('Images')[depth2].get('Display'))
					if UserPaness[depth1].get('Images')[depth2].get('X') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Images.' + str(depth2 + 1) + '.X', UserPaness[depth1].get('Images')[depth2].get('X'))
					if UserPaness[depth1].get('Images')[depth2].get('Y') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Images.' + str(depth2 + 1) + '.Y', UserPaness[depth1].get('Images')[depth2].get('Y'))
					if UserPaness[depth1].get('Images')[depth2].get('Width') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Images.' + str(depth2 + 1) + '.Width', UserPaness[depth1].get('Images')[depth2].get('Width'))
					if UserPaness[depth1].get('Images')[depth2].get('Height') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Images.' + str(depth2 + 1) + '.Height', UserPaness[depth1].get('Images')[depth2].get('Height'))
					if UserPaness[depth1].get('Images')[depth2].get('ZOrder') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Images.' + str(depth2 + 1) + '.ZOrder', UserPaness[depth1].get('Images')[depth2].get('ZOrder'))
			if UserPaness[depth1].get('Texts') is not None:
				for depth2 in range(len(UserPaness[depth1].get('Texts'))):
					if UserPaness[depth1].get('Texts')[depth2].get('Text') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Texts.' + str(depth2 + 1) + '.Text', UserPaness[depth1].get('Texts')[depth2].get('Text'))
					if UserPaness[depth1].get('Texts')[depth2].get('X') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Texts.' + str(depth2 + 1) + '.X', UserPaness[depth1].get('Texts')[depth2].get('X'))
					if UserPaness[depth1].get('Texts')[depth2].get('Y') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Texts.' + str(depth2 + 1) + '.Y', UserPaness[depth1].get('Texts')[depth2].get('Y'))
					if UserPaness[depth1].get('Texts')[depth2].get('FontType') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Texts.' + str(depth2 + 1) + '.FontType', UserPaness[depth1].get('Texts')[depth2].get('FontType'))
					if UserPaness[depth1].get('Texts')[depth2].get('FontSize') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Texts.' + str(depth2 + 1) + '.FontSize', UserPaness[depth1].get('Texts')[depth2].get('FontSize'))
					if UserPaness[depth1].get('Texts')[depth2].get('FontColor') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Texts.' + str(depth2 + 1) + '.FontColor', UserPaness[depth1].get('Texts')[depth2].get('FontColor'))
					if UserPaness[depth1].get('Texts')[depth2].get('ZOrder') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + '.Texts.' + str(depth2 + 1) + '.ZOrder', UserPaness[depth1].get('Texts')[depth2].get('ZOrder'))

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TemplateId(self):
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_query_param('TemplateId',TemplateId)

	def get_SubSpecUserss(self):
		return self.get_query_params().get('SubSpecUsers')

	def set_SubSpecUserss(self, SubSpecUserss):
		for depth1 in range(len(SubSpecUserss)):
			if SubSpecUserss[depth1] is not None:
				self.add_query_param('SubSpecUsers.' + str(depth1 + 1) , SubSpecUserss[depth1])

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_ChannelId(self):
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_query_param('ChannelId',ChannelId)