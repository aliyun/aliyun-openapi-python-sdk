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

class UpdateLiveStreamMonitorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'UpdateLiveStreamMonitor','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MonitorId(self): # String
		return self.get_query_params().get('MonitorId')

	def set_MonitorId(self, MonitorId):  # String
		self.add_query_param('MonitorId', MonitorId)
	def get_MonitorConfig(self): # String
		return self.get_query_params().get('MonitorConfig')

	def set_MonitorConfig(self, MonitorConfig):  # String
		self.add_query_param('MonitorConfig', MonitorConfig)
	def get_MonitorName(self): # String
		return self.get_query_params().get('MonitorName')

	def set_MonitorName(self, MonitorName):  # String
		self.add_query_param('MonitorName', MonitorName)
	def get_Stream(self): # String
		return self.get_query_params().get('Stream')

	def set_Stream(self, Stream):  # String
		self.add_query_param('Stream', Stream)
	def get_OutputTemplate(self): # String
		return self.get_query_params().get('OutputTemplate')

	def set_OutputTemplate(self, OutputTemplate):  # String
		self.add_query_param('OutputTemplate', OutputTemplate)
	def get_App(self): # String
		return self.get_query_params().get('App')

	def set_App(self, App):  # String
		self.add_query_param('App', App)
	def get_InputList(self): # String
		return self.get_query_params().get('InputList')

	def set_InputList(self, InputList):  # String
		self.add_query_param('InputList', InputList)
	def get_DingTalkWebHookUrl(self): # String
		return self.get_query_params().get('DingTalkWebHookUrl')

	def set_DingTalkWebHookUrl(self, DingTalkWebHookUrl):  # String
		self.add_query_param('DingTalkWebHookUrl', DingTalkWebHookUrl)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Domain(self): # String
		return self.get_query_params().get('Domain')

	def set_Domain(self, Domain):  # String
		self.add_query_param('Domain', Domain)
	def get_CallbackUrl(self): # String
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self, CallbackUrl):  # String
		self.add_query_param('CallbackUrl', CallbackUrl)
