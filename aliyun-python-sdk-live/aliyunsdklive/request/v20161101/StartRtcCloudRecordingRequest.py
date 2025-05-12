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
import json

class StartRtcCloudRecordingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'StartRtcCloudRecording','live')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StorageParams(self): # Struct
		return self.get_query_params().get('StorageParams')

	def set_StorageParams(self, StorageParams):  # Struct
		self.add_query_param("StorageParams", json.dumps(StorageParams))
	def get_NotifyUrl(self): # String
		return self.get_query_params().get('NotifyUrl')

	def set_NotifyUrl(self, NotifyUrl):  # String
		self.add_query_param('NotifyUrl', NotifyUrl)
	def get_SubscribeParams(self): # Struct
		return self.get_query_params().get('SubscribeParams')

	def set_SubscribeParams(self, SubscribeParams):  # Struct
		self.add_query_param("SubscribeParams", json.dumps(SubscribeParams))
	def get_RecordParams(self): # Struct
		return self.get_query_params().get('RecordParams')

	def set_RecordParams(self, RecordParams):  # Struct
		self.add_query_param("RecordParams", json.dumps(RecordParams))
	def get_MixTranscodeParams(self): # Struct
		return self.get_query_params().get('MixTranscodeParams')

	def set_MixTranscodeParams(self, MixTranscodeParams):  # Struct
		self.add_query_param("MixTranscodeParams", json.dumps(MixTranscodeParams))
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
	def get_MixLayoutParams(self): # Struct
		return self.get_query_params().get('MixLayoutParams')

	def set_MixLayoutParams(self, MixLayoutParams):  # Struct
		self.add_query_param("MixLayoutParams", json.dumps(MixLayoutParams))
