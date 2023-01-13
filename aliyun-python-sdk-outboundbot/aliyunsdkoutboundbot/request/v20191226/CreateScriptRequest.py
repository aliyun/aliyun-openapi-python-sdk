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
from aliyunsdkoutboundbot.endpoint import endpoint_data

class CreateScriptRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'CreateScript')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TtsConfig(self): # String
		return self.get_query_params().get('TtsConfig')

	def set_TtsConfig(self, TtsConfig):  # String
		self.add_query_param('TtsConfig', TtsConfig)
	def get_Industry(self): # String
		return self.get_query_params().get('Industry')

	def set_Industry(self, Industry):  # String
		self.add_query_param('Industry', Industry)
	def get_ScriptName(self): # String
		return self.get_query_params().get('ScriptName')

	def set_ScriptName(self, ScriptName):  # String
		self.add_query_param('ScriptName', ScriptName)
	def get_Scene(self): # String
		return self.get_query_params().get('Scene')

	def set_Scene(self, Scene):  # String
		self.add_query_param('Scene', Scene)
	def get_ScriptWaveforms(self): # RepeatList
		return self.get_query_params().get('ScriptWaveform')

	def set_ScriptWaveforms(self, ScriptWaveform):  # RepeatList
		for depth1 in range(len(ScriptWaveform)):
			self.add_query_param('ScriptWaveform.' + str(depth1 + 1), ScriptWaveform[depth1])
	def get_AsrConfig(self): # String
		return self.get_query_params().get('AsrConfig')

	def set_AsrConfig(self, AsrConfig):  # String
		self.add_query_param('AsrConfig', AsrConfig)
	def get_EmotionEnable(self): # Boolean
		return self.get_query_params().get('EmotionEnable')

	def set_EmotionEnable(self, EmotionEnable):  # Boolean
		self.add_query_param('EmotionEnable', EmotionEnable)
	def get_NewBargeInEnable(self): # Boolean
		return self.get_query_params().get('NewBargeInEnable')

	def set_NewBargeInEnable(self, NewBargeInEnable):  # Boolean
		self.add_query_param('NewBargeInEnable', NewBargeInEnable)
	def get_MiniPlaybackEnable(self): # Boolean
		return self.get_query_params().get('MiniPlaybackEnable')

	def set_MiniPlaybackEnable(self, MiniPlaybackEnable):  # Boolean
		self.add_query_param('MiniPlaybackEnable', MiniPlaybackEnable)
	def get_ChatbotId(self): # String
		return self.get_query_params().get('ChatbotId')

	def set_ChatbotId(self, ChatbotId):  # String
		self.add_query_param('ChatbotId', ChatbotId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ScriptDescription(self): # String
		return self.get_query_params().get('ScriptDescription')

	def set_ScriptDescription(self, ScriptDescription):  # String
		self.add_query_param('ScriptDescription', ScriptDescription)
	def get_LongWaitEnable(self): # Boolean
		return self.get_query_params().get('LongWaitEnable')

	def set_LongWaitEnable(self, LongWaitEnable):  # Boolean
		self.add_query_param('LongWaitEnable', LongWaitEnable)
	def get_ScriptContents(self): # RepeatList
		return self.get_query_params().get('ScriptContent')

	def set_ScriptContents(self, ScriptContent):  # RepeatList
		for depth1 in range(len(ScriptContent)):
			self.add_query_param('ScriptContent.' + str(depth1 + 1), ScriptContent[depth1])
