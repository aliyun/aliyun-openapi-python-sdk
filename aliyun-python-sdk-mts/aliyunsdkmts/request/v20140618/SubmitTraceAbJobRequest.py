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
from aliyunsdkmts.endpoint import endpoint_data

class SubmitTraceAbJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'SubmitTraceAbJob','mts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_Output(self): # String
		return self.get_query_params().get('Output')

	def set_Output(self, Output):  # String
		self.add_query_param('Output', Output)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_CipherBase64ed(self): # String
		return self.get_query_params().get('CipherBase64ed')

	def set_CipherBase64ed(self, CipherBase64ed):  # String
		self.add_query_param('CipherBase64ed', CipherBase64ed)
	def get_Level(self): # Long
		return self.get_query_params().get('Level')

	def set_Level(self, Level):  # Long
		self.add_query_param('Level', Level)
	def get_Url(self): # String
		return self.get_query_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_query_param('Url', Url)
	def get_Input(self): # String
		return self.get_query_params().get('Input')

	def set_Input(self, Input):  # String
		self.add_query_param('Input', Input)
	def get_TotalTime(self): # Long
		return self.get_query_params().get('TotalTime')

	def set_TotalTime(self, TotalTime):  # Long
		self.add_query_param('TotalTime', TotalTime)
	def get_CallBack(self): # String
		return self.get_query_params().get('CallBack')

	def set_CallBack(self, CallBack):  # String
		self.add_query_param('CallBack', CallBack)
