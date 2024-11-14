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

class StartLiveMPUTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'StartLiveMPUTask','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SingleSubParams(self): # Struct
		return self.get_query_params().get('SingleSubParams')

	def set_SingleSubParams(self, SingleSubParams):  # Struct
		self.add_query_param("SingleSubParams", json.dumps(SingleSubParams))
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_StreamURL(self): # String
		return self.get_query_params().get('StreamURL')

	def set_StreamURL(self, StreamURL):  # String
		self.add_query_param('StreamURL', StreamURL)
	def get_MultiStreamURL(self): # Array
		return self.get_query_params().get('MultiStreamURL')

	def set_MultiStreamURL(self, MultiStreamURL):  # Array
		self.add_query_param("MultiStreamURL", json.dumps(MultiStreamURL))
	def get_MaxIdleTime(self): # String
		return self.get_query_params().get('MaxIdleTime')

	def set_MaxIdleTime(self, MaxIdleTime):  # String
		self.add_query_param('MaxIdleTime', MaxIdleTime)
	def get_SeiParams(self): # Struct
		return self.get_query_params().get('SeiParams')

	def set_SeiParams(self, SeiParams):  # Struct
		self.add_query_param("SeiParams", json.dumps(SeiParams))
	def get_TranscodeParams(self): # Struct
		return self.get_query_params().get('TranscodeParams')

	def set_TranscodeParams(self, TranscodeParams):  # Struct
		self.add_query_param("TranscodeParams", json.dumps(TranscodeParams))
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
	def get_MixMode(self): # String
		return self.get_query_params().get('MixMode')

	def set_MixMode(self, MixMode):  # String
		self.add_query_param('MixMode', MixMode)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
