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

class SubmitIProductionJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'SubmitIProductionJob','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_JobParams(self): # String
		return self.get_query_params().get('JobParams')

	def set_JobParams(self, JobParams):  # String
		self.add_query_param('JobParams', JobParams)
	def get_Output(self): # Struct
		return self.get_query_params().get('Output')

	def set_Output(self, Output):  # Struct
		self.add_query_param("Output", json.dumps(Output))
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_FunctionName(self): # String
		return self.get_query_params().get('FunctionName')

	def set_FunctionName(self, FunctionName):  # String
		self.add_query_param('FunctionName', FunctionName)
	def get_ScheduleConfig(self): # Struct
		return self.get_query_params().get('ScheduleConfig')

	def set_ScheduleConfig(self, ScheduleConfig):  # Struct
		self.add_query_param("ScheduleConfig", json.dumps(ScheduleConfig))
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_Input(self): # Struct
		return self.get_query_params().get('Input')

	def set_Input(self, Input):  # Struct
		self.add_query_param("Input", json.dumps(Input))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
