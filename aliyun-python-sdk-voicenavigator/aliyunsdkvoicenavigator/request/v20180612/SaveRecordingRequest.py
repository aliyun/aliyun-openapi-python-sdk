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
from aliyunsdkvoicenavigator.endpoint import endpoint_data

class SaveRecordingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'VoiceNavigator', '2018-06-12', 'SaveRecording','voicebot')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_VoiceSliceRecordingList(self): # String
		return self.get_query_params().get('VoiceSliceRecordingList')

	def set_VoiceSliceRecordingList(self, VoiceSliceRecordingList):  # String
		self.add_query_param('VoiceSliceRecordingList', VoiceSliceRecordingList)
	def get_ConversationId(self): # String
		return self.get_query_params().get('ConversationId')

	def set_ConversationId(self, ConversationId):  # String
		self.add_query_param('ConversationId', ConversationId)
	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Duration(self): # String
		return self.get_query_params().get('Duration')

	def set_Duration(self, Duration):  # String
		self.add_query_param('Duration', Duration)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_FileName(self): # String
		return self.get_query_params().get('FileName')

	def set_FileName(self, FileName):  # String
		self.add_query_param('FileName', FileName)
	def get_FilePath(self): # String
		return self.get_query_params().get('FilePath')

	def set_FilePath(self, FilePath):  # String
		self.add_query_param('FilePath', FilePath)
	def get_InstanceOwnerId(self): # Long
		return self.get_query_params().get('InstanceOwnerId')

	def set_InstanceOwnerId(self, InstanceOwnerId):  # Long
		self.add_query_param('InstanceOwnerId', InstanceOwnerId)
