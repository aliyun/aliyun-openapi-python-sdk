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
from aliyunsdkdyvmsapi.endpoint import endpoint_data

class SmartCallRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'SmartCall','dyvms')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_VoiceCodeParam(self):
		return self.get_query_params().get('VoiceCodeParam')

	def set_VoiceCodeParam(self,VoiceCodeParam):
		self.add_query_param('VoiceCodeParam',VoiceCodeParam)

	def get_EarlyMediaAsr(self):
		return self.get_query_params().get('EarlyMediaAsr')

	def set_EarlyMediaAsr(self,EarlyMediaAsr):
		self.add_query_param('EarlyMediaAsr',EarlyMediaAsr)

	def get_Speed(self):
		return self.get_query_params().get('Speed')

	def set_Speed(self,Speed):
		self.add_query_param('Speed',Speed)

	def get_AsrBaseId(self):
		return self.get_query_params().get('AsrBaseId')

	def set_AsrBaseId(self,AsrBaseId):
		self.add_query_param('AsrBaseId',AsrBaseId)

	def get_SessionTimeout(self):
		return self.get_query_params().get('SessionTimeout')

	def set_SessionTimeout(self,SessionTimeout):
		self.add_query_param('SessionTimeout',SessionTimeout)

	def get_DynamicId(self):
		return self.get_query_params().get('DynamicId')

	def set_DynamicId(self,DynamicId):
		self.add_query_param('DynamicId',DynamicId)

	def get_CalledNumber(self):
		return self.get_query_params().get('CalledNumber')

	def set_CalledNumber(self,CalledNumber):
		self.add_query_param('CalledNumber',CalledNumber)

	def get_TtsSpeed(self):
		return self.get_query_params().get('TtsSpeed')

	def set_TtsSpeed(self,TtsSpeed):
		self.add_query_param('TtsSpeed',TtsSpeed)

	def get_VoiceCode(self):
		return self.get_query_params().get('VoiceCode')

	def set_VoiceCode(self,VoiceCode):
		self.add_query_param('VoiceCode',VoiceCode)

	def get_CalledShowNumber(self):
		return self.get_query_params().get('CalledShowNumber')

	def set_CalledShowNumber(self,CalledShowNumber):
		self.add_query_param('CalledShowNumber',CalledShowNumber)

	def get_ActionCodeTimeBreak(self):
		return self.get_query_params().get('ActionCodeTimeBreak')

	def set_ActionCodeTimeBreak(self,ActionCodeTimeBreak):
		self.add_query_param('ActionCodeTimeBreak',ActionCodeTimeBreak)

	def get_TtsConf(self):
		return self.get_query_params().get('TtsConf')

	def set_TtsConf(self,TtsConf):
		self.add_query_param('TtsConf',TtsConf)

	def get_ActionCodeBreak(self):
		return self.get_query_params().get('ActionCodeBreak')

	def set_ActionCodeBreak(self,ActionCodeBreak):
		self.add_query_param('ActionCodeBreak',ActionCodeBreak)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_RecordFlag(self):
		return self.get_query_params().get('RecordFlag')

	def set_RecordFlag(self,RecordFlag):
		self.add_query_param('RecordFlag',RecordFlag)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TtsVolume(self):
		return self.get_query_params().get('TtsVolume')

	def set_TtsVolume(self,TtsVolume):
		self.add_query_param('TtsVolume',TtsVolume)

	def get_Volume(self):
		return self.get_query_params().get('Volume')

	def set_Volume(self,Volume):
		self.add_query_param('Volume',Volume)

	def get_MuteTime(self):
		return self.get_query_params().get('MuteTime')

	def set_MuteTime(self,MuteTime):
		self.add_query_param('MuteTime',MuteTime)

	def get_OutId(self):
		return self.get_query_params().get('OutId')

	def set_OutId(self,OutId):
		self.add_query_param('OutId',OutId)

	def get_AsrModelId(self):
		return self.get_query_params().get('AsrModelId')

	def set_AsrModelId(self,AsrModelId):
		self.add_query_param('AsrModelId',AsrModelId)

	def get_PauseTime(self):
		return self.get_query_params().get('PauseTime')

	def set_PauseTime(self,PauseTime):
		self.add_query_param('PauseTime',PauseTime)

	def get_TtsStyle(self):
		return self.get_query_params().get('TtsStyle')

	def set_TtsStyle(self,TtsStyle):
		self.add_query_param('TtsStyle',TtsStyle)