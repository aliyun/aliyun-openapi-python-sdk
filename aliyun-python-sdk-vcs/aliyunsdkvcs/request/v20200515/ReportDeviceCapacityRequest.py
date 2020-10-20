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
from aliyunsdkvcs.endpoint import endpoint_data

class ReportDeviceCapacityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'ReportDeviceCapacity')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StreamCapacitiess(self):
		return self.get_body_params().get('StreamCapacities')

	def set_StreamCapacitiess(self, StreamCapacitiess):
		for depth1 in range(len(StreamCapacitiess)):
			if StreamCapacitiess[depth1].get('BitrateRange') is not None:
				self.add_body_params('StreamCapacities.' + str(depth1 + 1) + '.BitrateRange', StreamCapacitiess[depth1].get('BitrateRange'))
			if StreamCapacitiess[depth1].get('MaxStream') is not None:
				self.add_body_params('StreamCapacities.' + str(depth1 + 1) + '.MaxStream', StreamCapacitiess[depth1].get('MaxStream'))
			if StreamCapacitiess[depth1].get('EncodeFormat') is not None:
				self.add_body_params('StreamCapacities.' + str(depth1 + 1) + '.EncodeFormat', StreamCapacitiess[depth1].get('EncodeFormat'))
			if StreamCapacitiess[depth1].get('MaxFrameRate') is not None:
				self.add_body_params('StreamCapacities.' + str(depth1 + 1) + '.MaxFrameRate', StreamCapacitiess[depth1].get('MaxFrameRate'))
			if StreamCapacitiess[depth1].get('GovLengthRange') is not None:
				self.add_body_params('StreamCapacities.' + str(depth1 + 1) + '.GovLengthRange', StreamCapacitiess[depth1].get('GovLengthRange'))
			if StreamCapacitiess[depth1].get('Resolution') is not None:
				self.add_body_params('StreamCapacities.' + str(depth1 + 1) + '.Resolution', StreamCapacitiess[depth1].get('Resolution'))

	def get_Latitude(self):
		return self.get_body_params().get('Latitude')

	def set_Latitude(self,Latitude):
		self.add_body_params('Latitude', Latitude)

	def get_PresetNum(self):
		return self.get_body_params().get('PresetNum')

	def set_PresetNum(self,PresetNum):
		self.add_body_params('PresetNum', PresetNum)

	def get_DeviceTimeStamp(self):
		return self.get_body_params().get('DeviceTimeStamp')

	def set_DeviceTimeStamp(self,DeviceTimeStamp):
		self.add_body_params('DeviceTimeStamp', DeviceTimeStamp)

	def get_DeviceSn(self):
		return self.get_body_params().get('DeviceSn')

	def set_DeviceSn(self,DeviceSn):
		self.add_body_params('DeviceSn', DeviceSn)

	def get_AudioFormat(self):
		return self.get_body_params().get('AudioFormat')

	def set_AudioFormat(self,AudioFormat):
		self.add_body_params('AudioFormat', AudioFormat)

	def get_PTZCapacity(self):
		return self.get_body_params().get('PTZCapacity')

	def set_PTZCapacity(self,PTZCapacity):
		self.add_body_params('PTZCapacity', PTZCapacity)

	def get_Longitude(self):
		return self.get_body_params().get('Longitude')

	def set_Longitude(self,Longitude):
		self.add_body_params('Longitude', Longitude)