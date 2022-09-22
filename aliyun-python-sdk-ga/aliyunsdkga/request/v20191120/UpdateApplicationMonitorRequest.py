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
from aliyunsdkga.endpoint import endpoint_data

class UpdateApplicationMonitorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'UpdateApplicationMonitor','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DetectEnable(self): # Boolean
		return self.get_query_params().get('DetectEnable')

	def set_DetectEnable(self, DetectEnable):  # Boolean
		self.add_query_param('DetectEnable', DetectEnable)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_SilenceTime(self): # Integer
		return self.get_query_params().get('SilenceTime')

	def set_SilenceTime(self, SilenceTime):  # Integer
		self.add_query_param('SilenceTime', SilenceTime)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_Address(self): # String
		return self.get_query_params().get('Address')

	def set_Address(self, Address):  # String
		self.add_query_param('Address', Address)
	def get_DetectThreshold(self): # Integer
		return self.get_query_params().get('DetectThreshold')

	def set_DetectThreshold(self, DetectThreshold):  # Integer
		self.add_query_param('DetectThreshold', DetectThreshold)
	def get_OptionsJson(self): # String
		return self.get_query_params().get('OptionsJson')

	def set_OptionsJson(self, OptionsJson):  # String
		self.add_query_param('OptionsJson', OptionsJson)
	def get_DetectTimes(self): # Integer
		return self.get_query_params().get('DetectTimes')

	def set_DetectTimes(self, DetectTimes):  # Integer
		self.add_query_param('DetectTimes', DetectTimes)
