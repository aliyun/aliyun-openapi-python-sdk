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

class DescribeTTSDemoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'DescribeTTSDemo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Voice(self): # String
		return self.get_query_params().get('Voice')

	def set_Voice(self, Voice):  # String
		self.add_query_param('Voice', Voice)
	def get_Volume(self): # Integer
		return self.get_query_params().get('Volume')

	def set_Volume(self, Volume):  # Integer
		self.add_query_param('Volume', Volume)
	def get_ScriptId(self): # String
		return self.get_query_params().get('ScriptId')

	def set_ScriptId(self, ScriptId):  # String
		self.add_query_param('ScriptId', ScriptId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Text(self): # String
		return self.get_query_params().get('Text')

	def set_Text(self, Text):  # String
		self.add_query_param('Text', Text)
	def get_SpeechRate(self): # Integer
		return self.get_query_params().get('SpeechRate')

	def set_SpeechRate(self, SpeechRate):  # Integer
		self.add_query_param('SpeechRate', SpeechRate)
	def get_PitchRate(self): # Integer
		return self.get_query_params().get('PitchRate')

	def set_PitchRate(self, PitchRate):  # Integer
		self.add_query_param('PitchRate', PitchRate)
