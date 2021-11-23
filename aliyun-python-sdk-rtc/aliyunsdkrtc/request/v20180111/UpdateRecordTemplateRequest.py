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

class UpdateRecordTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'UpdateRecordTemplate')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Formatss(self): # RepeatList
		return self.get_query_params().get('Formats')

	def set_Formatss(self, Formats):  # RepeatList
		for depth1 in range(len(Formats)):
			self.add_query_param('Formats.' + str(depth1 + 1), Formats[depth1])
	def get_OssFilePrefix(self): # String
		return self.get_query_params().get('OssFilePrefix')

	def set_OssFilePrefix(self, OssFilePrefix):  # String
		self.add_query_param('OssFilePrefix', OssFilePrefix)
	def get_BackgroundColor(self): # Integer
		return self.get_query_params().get('BackgroundColor')

	def set_BackgroundColor(self, BackgroundColor):  # Integer
		self.add_query_param('BackgroundColor', BackgroundColor)
	def get_TaskProfile(self): # String
		return self.get_query_params().get('TaskProfile')

	def set_TaskProfile(self, TaskProfile):  # String
		self.add_query_param('TaskProfile', TaskProfile)
	def get_LayoutIdss(self): # RepeatList
		return self.get_query_params().get('LayoutIds')

	def set_LayoutIdss(self, LayoutIds):  # RepeatList
		for depth1 in range(len(LayoutIds)):
			self.add_query_param('LayoutIds.' + str(depth1 + 1), LayoutIds[depth1])
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
	def get_OssBucket(self): # String
		return self.get_query_params().get('OssBucket')

	def set_OssBucket(self, OssBucket):  # String
		self.add_query_param('OssBucket', OssBucket)
	def get_DelayStopTime(self): # Integer
		return self.get_query_params().get('DelayStopTime')

	def set_DelayStopTime(self, DelayStopTime):  # Integer
		self.add_query_param('DelayStopTime', DelayStopTime)
	def get_MnsQueue(self): # String
		return self.get_query_params().get('MnsQueue')

	def set_MnsQueue(self, MnsQueue):  # String
		self.add_query_param('MnsQueue', MnsQueue)
	def get_FileSplitInterval(self): # Integer
		return self.get_query_params().get('FileSplitInterval')

	def set_FileSplitInterval(self, FileSplitInterval):  # Integer
		self.add_query_param('FileSplitInterval', FileSplitInterval)
	def get_HttpCallbackUrl(self): # String
		return self.get_query_params().get('HttpCallbackUrl')

	def set_HttpCallbackUrl(self, HttpCallbackUrl):  # String
		self.add_query_param('HttpCallbackUrl', HttpCallbackUrl)
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
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_EnableM3u8DateTime(self): # Boolean
		return self.get_query_params().get('EnableM3u8DateTime')

	def set_EnableM3u8DateTime(self, EnableM3u8DateTime):  # Boolean
		self.add_query_param('EnableM3u8DateTime', EnableM3u8DateTime)
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
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_MediaEncode(self): # Integer
		return self.get_query_params().get('MediaEncode')

	def set_MediaEncode(self, MediaEncode):  # Integer
		self.add_query_param('MediaEncode', MediaEncode)
