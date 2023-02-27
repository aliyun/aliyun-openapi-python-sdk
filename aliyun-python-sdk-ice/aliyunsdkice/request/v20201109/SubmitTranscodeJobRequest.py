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

class SubmitTranscodeJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'SubmitTranscodeJob','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_OutputGroup(self): # Array
		return self.get_query_params().get('OutputGroup')

	def set_OutputGroup(self, OutputGroup):  # Array
		self.add_query_param("OutputGroup", json.dumps(OutputGroup))
	def get_InputGroup(self): # Array
		return self.get_query_params().get('InputGroup')

	def set_InputGroup(self, InputGroup):  # Array
		self.add_query_param("InputGroup", json.dumps(InputGroup))
	def get_ScheduleConfig(self): # Struct
		return self.get_query_params().get('ScheduleConfig')

	def set_ScheduleConfig(self, ScheduleConfig):  # Struct
		self.add_query_param("ScheduleConfig", json.dumps(ScheduleConfig))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
