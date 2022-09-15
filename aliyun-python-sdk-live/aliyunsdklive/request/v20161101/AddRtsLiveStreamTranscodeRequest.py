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
from aliyunsdklive.endpoint import endpoint_data

class AddRtsLiveStreamTranscodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddRtsLiveStreamTranscode','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Template(self): # String
		return self.get_query_params().get('Template')

	def set_Template(self, Template):  # String
		self.add_query_param('Template', Template)
	def get_DeleteBframes(self): # Boolean
		return self.get_query_params().get('DeleteBframes')

	def set_DeleteBframes(self, DeleteBframes):  # Boolean
		self.add_query_param('DeleteBframes', DeleteBframes)
	def get_Lazy(self): # String
		return self.get_query_params().get('Lazy')

	def set_Lazy(self, Lazy):  # String
		self.add_query_param('Lazy', Lazy)
	def get_Gop(self): # String
		return self.get_query_params().get('Gop')

	def set_Gop(self, Gop):  # String
		self.add_query_param('Gop', Gop)
	def get_Opus(self): # Boolean
		return self.get_query_params().get('Opus')

	def set_Opus(self, Opus):  # Boolean
		self.add_query_param('Opus', Opus)
	def get_AudioCodec(self): # String
		return self.get_query_params().get('AudioCodec')

	def set_AudioCodec(self, AudioCodec):  # String
		self.add_query_param('AudioCodec', AudioCodec)
	def get_TemplateType(self): # String
		return self.get_query_params().get('TemplateType')

	def set_TemplateType(self, TemplateType):  # String
		self.add_query_param('TemplateType', TemplateType)
	def get_AudioProfile(self): # String
		return self.get_query_params().get('AudioProfile')

	def set_AudioProfile(self, AudioProfile):  # String
		self.add_query_param('AudioProfile', AudioProfile)
	def get_Height(self): # Integer
		return self.get_query_params().get('Height')

	def set_Height(self, Height):  # Integer
		self.add_query_param('Height', Height)
	def get_App(self): # String
		return self.get_query_params().get('App')

	def set_App(self, App):  # String
		self.add_query_param('App', App)
	def get_AudioChannelNum(self): # Integer
		return self.get_query_params().get('AudioChannelNum')

	def set_AudioChannelNum(self, AudioChannelNum):  # Integer
		self.add_query_param('AudioChannelNum', AudioChannelNum)
	def get_Profile(self): # Integer
		return self.get_query_params().get('Profile')

	def set_Profile(self, Profile):  # Integer
		self.add_query_param('Profile', Profile)
	def get_FPS(self): # Integer
		return self.get_query_params().get('FPS')

	def set_FPS(self, FPS):  # Integer
		self.add_query_param('FPS', FPS)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_AudioRate(self): # Integer
		return self.get_query_params().get('AudioRate')

	def set_AudioRate(self, AudioRate):  # Integer
		self.add_query_param('AudioRate', AudioRate)
	def get_AudioBitrate(self): # Integer
		return self.get_query_params().get('AudioBitrate')

	def set_AudioBitrate(self, AudioBitrate):  # Integer
		self.add_query_param('AudioBitrate', AudioBitrate)
	def get_Domain(self): # String
		return self.get_query_params().get('Domain')

	def set_Domain(self, Domain):  # String
		self.add_query_param('Domain', Domain)
	def get_Width(self): # Integer
		return self.get_query_params().get('Width')

	def set_Width(self, Width):  # Integer
		self.add_query_param('Width', Width)
	def get_VideoBitrate(self): # Integer
		return self.get_query_params().get('VideoBitrate')

	def set_VideoBitrate(self, VideoBitrate):  # Integer
		self.add_query_param('VideoBitrate', VideoBitrate)
