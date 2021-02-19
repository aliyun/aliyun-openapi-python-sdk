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

class UpdateMPULayoutRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'UpdateMPULayout','rtc')
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
			if UserPaness[depth1].get('SegmentType') is not None:
				self.add_query_param('UserPanes.' + str(depth1 + 1) + '.SegmentType', UserPaness[depth1].get('SegmentType'))
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

	def get_BackgroundColor(self):
		return self.get_query_params().get('BackgroundColor')

	def set_BackgroundColor(self,BackgroundColor):
		self.add_query_param('BackgroundColor',BackgroundColor)

	def get_CropMode(self):
		return self.get_query_params().get('CropMode')

	def set_CropMode(self,CropMode):
		self.add_query_param('CropMode',CropMode)

	def get_LayoutIdss(self):
		return self.get_query_params().get('LayoutIds')

	def set_LayoutIdss(self, LayoutIdss):
		for depth1 in range(len(LayoutIdss)):
			if LayoutIdss[depth1] is not None:
				self.add_query_param('LayoutIds.' + str(depth1 + 1) , LayoutIdss[depth1])

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)

	def get_ClockWidgetss(self):
		return self.get_query_params().get('ClockWidgets')

	def set_ClockWidgetss(self, ClockWidgetss):
		for depth1 in range(len(ClockWidgetss)):
			if ClockWidgetss[depth1].get('X') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.X', ClockWidgetss[depth1].get('X'))
			if ClockWidgetss[depth1].get('Y') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.Y', ClockWidgetss[depth1].get('Y'))
			if ClockWidgetss[depth1].get('FontType') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.FontType', ClockWidgetss[depth1].get('FontType'))
			if ClockWidgetss[depth1].get('FontSize') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.FontSize', ClockWidgetss[depth1].get('FontSize'))
			if ClockWidgetss[depth1].get('FontColor') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.FontColor', ClockWidgetss[depth1].get('FontColor'))
			if ClockWidgetss[depth1].get('ZOrder') is not None:
				self.add_query_param('ClockWidgets.' + str(depth1 + 1) + '.ZOrder', ClockWidgetss[depth1].get('ZOrder'))

	def get_Watermarkss(self):
		return self.get_query_params().get('Watermarks')

	def set_Watermarkss(self, Watermarkss):
		for depth1 in range(len(Watermarkss)):
			if Watermarkss[depth1].get('Url') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Url', Watermarkss[depth1].get('Url'))
			if Watermarkss[depth1].get('Alpha') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Alpha', Watermarkss[depth1].get('Alpha'))
			if Watermarkss[depth1].get('Display') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Display', Watermarkss[depth1].get('Display'))
			if Watermarkss[depth1].get('X') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.X', Watermarkss[depth1].get('X'))
			if Watermarkss[depth1].get('Y') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Y', Watermarkss[depth1].get('Y'))
			if Watermarkss[depth1].get('Width') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Width', Watermarkss[depth1].get('Width'))
			if Watermarkss[depth1].get('Height') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.Height', Watermarkss[depth1].get('Height'))
			if Watermarkss[depth1].get('ZOrder') is not None:
				self.add_query_param('Watermarks.' + str(depth1 + 1) + '.ZOrder', Watermarkss[depth1].get('ZOrder'))

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_Backgroundss(self):
		return self.get_query_params().get('Backgrounds')

	def set_Backgroundss(self, Backgroundss):
		for depth1 in range(len(Backgroundss)):
			if Backgroundss[depth1].get('Url') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Url', Backgroundss[depth1].get('Url'))
			if Backgroundss[depth1].get('Display') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Display', Backgroundss[depth1].get('Display'))
			if Backgroundss[depth1].get('X') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.X', Backgroundss[depth1].get('X'))
			if Backgroundss[depth1].get('Y') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Y', Backgroundss[depth1].get('Y'))
			if Backgroundss[depth1].get('Width') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Width', Backgroundss[depth1].get('Width'))
			if Backgroundss[depth1].get('Height') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.Height', Backgroundss[depth1].get('Height'))
			if Backgroundss[depth1].get('ZOrder') is not None:
				self.add_query_param('Backgrounds.' + str(depth1 + 1) + '.ZOrder', Backgroundss[depth1].get('ZOrder'))