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
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'UpdateRecordTask')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserPaness(self): # RepeatList
		return self.get_query_params().get('UserPanes')

	def set_UserPaness(self, UserPanes):  # RepeatList
		for depth1 in range(len(UserPanes)):
			if UserPanes[depth1].get('Images') is not None:
				for depth2 in range(len(UserPanes[depth1].get('Images'))):
					if UserPanes[depth1].get('Images')[depth2].get('Width') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.Width', UserPanes[depth1].get('Images')[depth2].get('Width'))
					if UserPanes[depth1].get('Images')[depth2].get('Height') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.Height', UserPanes[depth1].get('Images')[depth2].get('Height'))
					if UserPanes[depth1].get('Images')[depth2].get('Y') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.Y', UserPanes[depth1].get('Images')[depth2].get('Y'))
					if UserPanes[depth1].get('Images')[depth2].get('Url') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.Url', UserPanes[depth1].get('Images')[depth2].get('Url'))
					if UserPanes[depth1].get('Images')[depth2].get('Display') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.Display', UserPanes[depth1].get('Images')[depth2].get('Display'))
					if UserPanes[depth1].get('Images')[depth2].get('ZOrder') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.ZOrder', UserPanes[depth1].get('Images')[depth2].get('ZOrder'))
					if UserPanes[depth1].get('Images')[depth2].get('X') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.X', UserPanes[depth1].get('Images')[depth2].get('X'))
			if UserPanes[depth1].get('UserId') is not None:
				self.add_query_param('UserPanes.' + str(depth1 + 1) + '.UserId', UserPanes[depth1].get('UserId'))
			if UserPanes[depth1].get('Texts') is not None:
				for depth2 in range(len(UserPanes[depth1].get('Texts'))):
					if UserPanes[depth1].get('Texts')[depth2].get('FontType') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.FontType', UserPanes[depth1].get('Texts')[depth2].get('FontType'))
					if UserPanes[depth1].get('Texts')[depth2].get('FontColor') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.FontColor', UserPanes[depth1].get('Texts')[depth2].get('FontColor'))
					if UserPanes[depth1].get('Texts')[depth2].get('Y') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.Y', UserPanes[depth1].get('Texts')[depth2].get('Y'))
					if UserPanes[depth1].get('Texts')[depth2].get('Text') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.Text', UserPanes[depth1].get('Texts')[depth2].get('Text'))
					if UserPanes[depth1].get('Texts')[depth2].get('ZOrder') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.ZOrder', UserPanes[depth1].get('Texts')[depth2].get('ZOrder'))
					if UserPanes[depth1].get('Texts')[depth2].get('X') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.X', UserPanes[depth1].get('Texts')[depth2].get('X'))
					if UserPanes[depth1].get('Texts')[depth2].get('FontSize') is not None:
						self.add_query_param('UserPanes.' + str(depth1 + 1) + str(depth2 + 1) + '.FontSize', UserPanes[depth1].get('Texts')[depth2].get('FontSize'))
			if UserPanes[depth1].get('SourceType') is not None:
				self.add_query_param('UserPanes.' + str(depth1 + 1) + '.SourceType', UserPanes[depth1].get('SourceType'))
			if UserPanes[depth1].get('PaneId') is not None:
				self.add_query_param('UserPanes.' + str(depth1 + 1) + '.PaneId', UserPanes[depth1].get('PaneId'))
	def get_SubSpecCameraUserss(self): # RepeatList
		return self.get_query_params().get('SubSpecCameraUsers')

	def set_SubSpecCameraUserss(self, SubSpecCameraUsers):  # RepeatList
		for depth1 in range(len(SubSpecCameraUsers)):
			self.add_query_param('SubSpecCameraUsers.' + str(depth1 + 1), SubSpecCameraUsers[depth1])
	def get_LayoutIdss(self): # RepeatList
		return self.get_query_params().get('LayoutIds')

	def set_LayoutIdss(self, LayoutIds):  # RepeatList
		for depth1 in range(len(LayoutIds)):
			self.add_query_param('LayoutIds.' + str(depth1 + 1), LayoutIds[depth1])
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_UnsubSpecCameraUserss(self): # RepeatList
		return self.get_query_params().get('UnsubSpecCameraUsers')

	def set_UnsubSpecCameraUserss(self, UnsubSpecCameraUsers):  # RepeatList
		for depth1 in range(len(UnsubSpecCameraUsers)):
			self.add_query_param('UnsubSpecCameraUsers.' + str(depth1 + 1), UnsubSpecCameraUsers[depth1])
	def get_UnsubSpecAudioUserss(self): # RepeatList
		return self.get_query_params().get('UnsubSpecAudioUsers')

	def set_UnsubSpecAudioUserss(self, UnsubSpecAudioUsers):  # RepeatList
		for depth1 in range(len(UnsubSpecAudioUsers)):
			self.add_query_param('UnsubSpecAudioUsers.' + str(depth1 + 1), UnsubSpecAudioUsers[depth1])
	def get_UnsubSpecShareScreenUserss(self): # RepeatList
		return self.get_query_params().get('UnsubSpecShareScreenUsers')

	def set_UnsubSpecShareScreenUserss(self, UnsubSpecShareScreenUsers):  # RepeatList
		for depth1 in range(len(UnsubSpecShareScreenUsers)):
			self.add_query_param('UnsubSpecShareScreenUsers.' + str(depth1 + 1), UnsubSpecShareScreenUsers[depth1])
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_SubSpecAudioUserss(self): # RepeatList
		return self.get_query_params().get('SubSpecAudioUsers')

	def set_SubSpecAudioUserss(self, SubSpecAudioUsers):  # RepeatList
		for depth1 in range(len(SubSpecAudioUsers)):
			self.add_query_param('SubSpecAudioUsers.' + str(depth1 + 1), SubSpecAudioUsers[depth1])
	def get_SubSpecShareScreenUserss(self): # RepeatList
		return self.get_query_params().get('SubSpecShareScreenUsers')

	def set_SubSpecShareScreenUserss(self, SubSpecShareScreenUsers):  # RepeatList
		for depth1 in range(len(SubSpecShareScreenUsers)):
			self.add_query_param('SubSpecShareScreenUsers.' + str(depth1 + 1), SubSpecShareScreenUsers[depth1])
	def get_SubSpecUserss(self): # RepeatList
		return self.get_query_params().get('SubSpecUsers')

	def set_SubSpecUserss(self, SubSpecUsers):  # RepeatList
		for depth1 in range(len(SubSpecUsers)):
			self.add_query_param('SubSpecUsers.' + str(depth1 + 1), SubSpecUsers[depth1])
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
