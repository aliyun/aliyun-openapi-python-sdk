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

class StartMPUTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'StartMPUTask')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PayloadType(self): # Integer
		return self.get_query_params().get('PayloadType')

	def set_PayloadType(self, PayloadType):  # Integer
		self.add_query_param('PayloadType', PayloadType)
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
			if UserPanes[depth1].get('SegmentType') is not None:
				self.add_query_param('UserPanes.' + str(depth1 + 1) + '.SegmentType', UserPanes[depth1].get('SegmentType'))
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
	def get_BackgroundColor(self): # Integer
		return self.get_query_params().get('BackgroundColor')

	def set_BackgroundColor(self, BackgroundColor):  # Integer
		self.add_query_param('BackgroundColor', BackgroundColor)
	def get_ReportVad(self): # Integer
		return self.get_query_params().get('ReportVad')

	def set_ReportVad(self, ReportVad):  # Integer
		self.add_query_param('ReportVad', ReportVad)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_ClockWidgetss(self): # RepeatList
		return self.get_query_params().get('ClockWidgets')

	def set_ClockWidgetss(self, ClockWidgets):  # RepeatList
		for depth1 in range(len(ClockWidgets)):
			if ClockWidgets[depth1].get('FontType') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.FontType', ClockWidgets[depth1].get('FontType'))
			if ClockWidgets[depth1].get('FontColor') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.FontColor', ClockWidgets[depth1].get('FontColor'))
			if ClockWidgets[depth1].get('Y') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.Y', ClockWidgets[depth1].get('Y'))
			if ClockWidgets[depth1].get('ZOrder') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.ZOrder', ClockWidgets[depth1].get('ZOrder'))
			if ClockWidgets[depth1].get('X') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.X', ClockWidgets[depth1].get('X'))
			if ClockWidgets[depth1].get('FontSize') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.FontSize', ClockWidgets[depth1].get('FontSize'))
	def get_UnsubSpecCameraUserss(self): # RepeatList
		return self.get_query_params().get('UnsubSpecCameraUsers')

	def set_UnsubSpecCameraUserss(self, UnsubSpecCameraUsers):  # RepeatList
		for depth1 in range(len(UnsubSpecCameraUsers)):
			self.add_query_param('UnsubSpecCameraUsers.' + str(depth1 + 1), UnsubSpecCameraUsers[depth1])
	def get_TaskType(self): # Integer
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # Integer
		self.add_query_param('TaskType', TaskType)
	def get_UnsubSpecAudioUserss(self): # RepeatList
		return self.get_query_params().get('UnsubSpecAudioUsers')

	def set_UnsubSpecAudioUserss(self, UnsubSpecAudioUsers):  # RepeatList
		for depth1 in range(len(UnsubSpecAudioUsers)):
			self.add_query_param('UnsubSpecAudioUsers.' + str(depth1 + 1), UnsubSpecAudioUsers[depth1])
	def get_VadInterval(self): # Long
		return self.get_query_params().get('VadInterval')

	def set_VadInterval(self, VadInterval):  # Long
		self.add_query_param('VadInterval', VadInterval)
	def get_Watermarkss(self): # RepeatList
		return self.get_query_params().get('Watermarks')

	def set_Watermarkss(self, Watermarks):  # RepeatList
		for depth1 in range(len(Watermarks)):
			if Watermarks[depth1].get('Alpha') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Alpha', Watermarks[depth1].get('Alpha'))
			if Watermarks[depth1].get('Width') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Width', Watermarks[depth1].get('Width'))
			if Watermarks[depth1].get('Height') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Height', Watermarks[depth1].get('Height'))
			if Watermarks[depth1].get('Y') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Y', Watermarks[depth1].get('Y'))
			if Watermarks[depth1].get('Url') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Url', Watermarks[depth1].get('Url'))
			if Watermarks[depth1].get('Display') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Display', Watermarks[depth1].get('Display'))
			if Watermarks[depth1].get('ZOrder') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.ZOrder', Watermarks[depth1].get('ZOrder'))
			if Watermarks[depth1].get('X') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.X', Watermarks[depth1].get('X'))
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SubSpecAudioUserss(self): # RepeatList
		return self.get_query_params().get('SubSpecAudioUsers')

	def set_SubSpecAudioUserss(self, SubSpecAudioUsers):  # RepeatList
		for depth1 in range(len(SubSpecAudioUsers)):
			self.add_query_param('SubSpecAudioUsers.' + str(depth1 + 1), SubSpecAudioUsers[depth1])
	def get_MediaEncode(self): # Integer
		return self.get_query_params().get('MediaEncode')

	def set_MediaEncode(self, MediaEncode):  # Integer
		self.add_query_param('MediaEncode', MediaEncode)
	def get_EnhancedParam(self): # Struct
		return self.get_body_params().get('EnhancedParam')

	def set_EnhancedParam(self, EnhancedParam):  # Struct
		if EnhancedParam.get('EnablePortraitSegmentation') is not None:
			self.add_body_params('EnhancedParam.EnablePortraitSegmentation', EnhancedParam.get('EnablePortraitSegmentation'))
		if EnhancedParam.get('EnableVirtualConference') is not None:
			self.add_body_params('EnhancedParam.EnableVirtualConference', EnhancedParam.get('EnableVirtualConference'))
		if EnhancedParam.get('EnableCartoonPortrait') is not None:
			self.add_body_params('EnhancedParam.EnableCartoonPortrait', EnhancedParam.get('EnableCartoonPortrait'))
		if EnhancedParam.get('EnableVoiceChanger') is not None:
			self.add_body_params('EnhancedParam.EnableVoiceChanger', EnhancedParam.get('EnableVoiceChanger'))
		if EnhancedParam.get('EnableUserPaneBackground') is not None:
			self.add_body_params('EnhancedParam.EnableUserPaneBackground', EnhancedParam.get('EnableUserPaneBackground'))
		if EnhancedParam.get('BackgroundPath') is not None:
			self.add_body_params('EnhancedParam.BackgroundPath', EnhancedParam.get('BackgroundPath'))
	def get_RtpExtInfo(self): # Integer
		return self.get_query_params().get('RtpExtInfo')

	def set_RtpExtInfo(self, RtpExtInfo):  # Integer
		self.add_query_param('RtpExtInfo', RtpExtInfo)
	def get_CropMode(self): # Integer
		return self.get_query_params().get('CropMode')

	def set_CropMode(self, CropMode):  # Integer
		self.add_query_param('CropMode', CropMode)
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
	def get_StreamURL(self): # String
		return self.get_query_params().get('StreamURL')

	def set_StreamURL(self, StreamURL):  # String
		self.add_query_param('StreamURL', StreamURL)
	def get_StreamType(self): # Integer
		return self.get_query_params().get('StreamType')

	def set_StreamType(self, StreamType):  # Integer
		self.add_query_param('StreamType', StreamType)
	def get_UnsubSpecShareScreenUserss(self): # RepeatList
		return self.get_query_params().get('UnsubSpecShareScreenUsers')

	def set_UnsubSpecShareScreenUserss(self, UnsubSpecShareScreenUsers):  # RepeatList
		for depth1 in range(len(UnsubSpecShareScreenUsers)):
			self.add_query_param('UnsubSpecShareScreenUsers.' + str(depth1 + 1), UnsubSpecShareScreenUsers[depth1])
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
	def get_Backgroundss(self): # RepeatList
		return self.get_query_params().get('Backgrounds')

	def set_Backgroundss(self, Backgrounds):  # RepeatList
		for depth1 in range(len(Backgrounds)):
			if Backgrounds[depth1].get('Width') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Width', Backgrounds[depth1].get('Width'))
			if Backgrounds[depth1].get('Height') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Height', Backgrounds[depth1].get('Height'))
			if Backgrounds[depth1].get('Y') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Y', Backgrounds[depth1].get('Y'))
			if Backgrounds[depth1].get('Url') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Url', Backgrounds[depth1].get('Url'))
			if Backgrounds[depth1].get('Display') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Display', Backgrounds[depth1].get('Display'))
			if Backgrounds[depth1].get('ZOrder') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.ZOrder', Backgrounds[depth1].get('ZOrder'))
			if Backgrounds[depth1].get('X') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.X', Backgrounds[depth1].get('X'))
	def get_TimeStampRef(self): # Long
		return self.get_query_params().get('TimeStampRef')

	def set_TimeStampRef(self, TimeStampRef):  # Long
		self.add_query_param('TimeStampRef', TimeStampRef)
	def get_MixMode(self): # Integer
		return self.get_query_params().get('MixMode')

	def set_MixMode(self, MixMode):  # Integer
		self.add_query_param('MixMode', MixMode)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
