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
from aliyunsdkice.endpoint import endpoint_data
import json

class UpdateLiveTranscodeJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'UpdateLiveTranscodeJob','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StreamInput(self): # Struct
		return self.get_query_params().get('StreamInput')

	def set_StreamInput(self, StreamInput):  # Struct
		self.add_query_param("StreamInput", json.dumps(StreamInput))
	def get_TranscodeOutput(self): # Struct
		return self.get_query_params().get('TranscodeOutput')

	def set_TranscodeOutput(self, TranscodeOutput):  # Struct
		self.add_query_param("TranscodeOutput", json.dumps(TranscodeOutput))
	def get_TimedConfig(self): # Struct
		return self.get_query_params().get('TimedConfig')

	def set_TimedConfig(self, TimedConfig):  # Struct
		self.add_query_param("TimedConfig", json.dumps(TimedConfig))
	def get_JobId(self): # String
		return self.get_query_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_query_param('JobId', JobId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
