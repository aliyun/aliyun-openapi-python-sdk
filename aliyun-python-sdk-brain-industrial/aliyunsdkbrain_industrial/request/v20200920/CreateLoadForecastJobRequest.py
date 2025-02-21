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
from aliyunsdkbrain_industrial.endpoint import endpoint_data
import json

class CreateLoadForecastJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'brain-industrial', '2020-09-20', 'CreateLoadForecastJob','aistudio')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TimeZone(self): # String
		return self.get_body_params().get('TimeZone')

	def set_TimeZone(self, TimeZone):  # String
		self.add_body_params('TimeZone', TimeZone)
	def get_Freq(self): # String
		return self.get_body_params().get('Freq')

	def set_Freq(self, Freq):  # String
		self.add_body_params('Freq', Freq)
	def get_SystemType(self): # String
		return self.get_body_params().get('SystemType')

	def set_SystemType(self, SystemType):  # String
		self.add_body_params('SystemType', SystemType)
	def get_DeviceType(self): # String
		return self.get_body_params().get('DeviceType')

	def set_DeviceType(self, DeviceType):  # String
		self.add_body_params('DeviceType', DeviceType)
	def get_Duration(self): # Integer
		return self.get_body_params().get('Duration')

	def set_Duration(self, Duration):  # Integer
		self.add_body_params('Duration', Duration)
	def get_RunDate(self): # String
		return self.get_body_params().get('RunDate')

	def set_RunDate(self, RunDate):  # String
		self.add_body_params('RunDate', RunDate)
	def get_HistoryData(self): # Array
		return self.get_body_params().get('HistoryData')

	def set_HistoryData(self, HistoryData):  # Array
		self.add_body_params("HistoryData", json.dumps(HistoryData))
	def get_ModelVersion(self): # String
		return self.get_body_params().get('ModelVersion')

	def set_ModelVersion(self, ModelVersion):  # String
		self.add_body_params('ModelVersion', ModelVersion)
