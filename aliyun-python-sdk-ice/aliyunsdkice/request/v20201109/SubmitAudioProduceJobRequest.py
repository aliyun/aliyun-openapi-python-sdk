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

class SubmitAudioProduceJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'SubmitAudioProduceJob','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OutputConfig(self): # String
		return self.get_query_params().get('OutputConfig')

	def set_OutputConfig(self, OutputConfig):  # String
		self.add_query_param('OutputConfig', OutputConfig)
	def get_EditingConfig(self): # String
		return self.get_query_params().get('EditingConfig')

	def set_EditingConfig(self, EditingConfig):  # String
		self.add_query_param('EditingConfig', EditingConfig)
	def get_InputConfig(self): # String
		return self.get_query_params().get('InputConfig')

	def set_InputConfig(self, InputConfig):  # String
		self.add_query_param('InputConfig', InputConfig)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Title(self): # String
		return self.get_query_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_query_param('Title', Title)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_Overwrite(self): # Boolean
		return self.get_query_params().get('Overwrite')

	def set_Overwrite(self, Overwrite):  # Boolean
		self.add_query_param('Overwrite', Overwrite)
