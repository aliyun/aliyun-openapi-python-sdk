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

class ModifyScriptRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'ModifyScript','outboundbot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TtsConfig(self):
		return self.get_query_params().get('TtsConfig')

	def set_TtsConfig(self,TtsConfig):
		self.add_query_param('TtsConfig',TtsConfig)

	def get_Industry(self):
		return self.get_query_params().get('Industry')

	def set_Industry(self,Industry):
		self.add_query_param('Industry',Industry)

	def get_ScriptName(self):
		return self.get_query_params().get('ScriptName')

	def set_ScriptName(self,ScriptName):
		self.add_query_param('ScriptName',ScriptName)

	def get_Scene(self):
		return self.get_query_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_query_param('Scene',Scene)

	def get_ScriptId(self):
		return self.get_query_params().get('ScriptId')

	def set_ScriptId(self,ScriptId):
		self.add_query_param('ScriptId',ScriptId)

	def get_ScriptWaveforms(self):
		return self.get_query_params().get('ScriptWaveform')

	def set_ScriptWaveforms(self, ScriptWaveforms):
		for depth1 in range(len(ScriptWaveforms)):
			if ScriptWaveforms[depth1] is not None:
				self.add_query_param('ScriptWaveform.' + str(depth1 + 1) , ScriptWaveforms[depth1])

	def get_AsrConfig(self):
		return self.get_query_params().get('AsrConfig')

	def set_AsrConfig(self,AsrConfig):
		self.add_query_param('AsrConfig',AsrConfig)

	def get_NlsConfig(self):
		return self.get_query_params().get('NlsConfig')

	def set_NlsConfig(self,NlsConfig):
		self.add_query_param('NlsConfig',NlsConfig)

	def get_MiniPlaybackEnabled(self):
		return self.get_query_params().get('MiniPlaybackEnabled')

	def set_MiniPlaybackEnabled(self,MiniPlaybackEnabled):
		self.add_query_param('MiniPlaybackEnabled',MiniPlaybackEnabled)

	def get_ChatbotId(self):
		return self.get_query_params().get('ChatbotId')

	def set_ChatbotId(self,ChatbotId):
		self.add_query_param('ChatbotId',ChatbotId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_ScriptDescription(self):
		return self.get_query_params().get('ScriptDescription')

	def set_ScriptDescription(self,ScriptDescription):
		self.add_query_param('ScriptDescription',ScriptDescription)

	def get_ScriptContents(self):
		return self.get_query_params().get('ScriptContent')

	def set_ScriptContents(self, ScriptContents):
		for depth1 in range(len(ScriptContents)):
			if ScriptContents[depth1] is not None:
				self.add_query_param('ScriptContent.' + str(depth1 + 1) , ScriptContents[depth1])