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
import json

class CreateDeviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imarketing', '2022-07-04', 'CreateDevice')
		self.set_method('POST')

	def get_FirstScene(self): # String
		return self.get_body_params().get('FirstScene')

	def set_FirstScene(self, FirstScene):  # String
		self.add_body_params('FirstScene', FirstScene)
	def get_ExtraMap(self): # Map
		return self.get_body_params().get('ExtraMap')

	def set_ExtraMap(self, ExtraMap):  # Map
		self.add_body_params("ExtraMap", json.dumps(ExtraMap))
	def get_City(self): # String
		return self.get_body_params().get('City')

	def set_City(self, City):  # String
		self.add_body_params('City', City)
	def get_MediaId(self): # String
		return self.get_body_params().get('MediaId')

	def set_MediaId(self, MediaId):  # String
		self.add_body_params('MediaId', MediaId)
	def get_DeviceType(self): # String
		return self.get_body_params().get('DeviceType')

	def set_DeviceType(self, DeviceType):  # String
		self.add_body_params('DeviceType', DeviceType)
	def get_LocationName(self): # String
		return self.get_body_params().get('LocationName')

	def set_LocationName(self, LocationName):  # String
		self.add_body_params('LocationName', LocationName)
	def get_Province(self): # String
		return self.get_body_params().get('Province')

	def set_Province(self, Province):  # String
		self.add_body_params('Province', Province)
	def get_District(self): # String
		return self.get_body_params().get('District')

	def set_District(self, District):  # String
		self.add_body_params('District', District)
	def get_DeviceName(self): # String
		return self.get_body_params().get('DeviceName')

	def set_DeviceName(self, DeviceName):  # String
		self.add_body_params('DeviceName', DeviceName)
	def get_DeviceModelNumber(self): # String
		return self.get_body_params().get('DeviceModelNumber')

	def set_DeviceModelNumber(self, DeviceModelNumber):  # String
		self.add_body_params('DeviceModelNumber', DeviceModelNumber)
	def get_SecondScene(self): # String
		return self.get_body_params().get('SecondScene')

	def set_SecondScene(self, SecondScene):  # String
		self.add_body_params('SecondScene', SecondScene)
	def get_Floor(self): # String
		return self.get_body_params().get('Floor')

	def set_Floor(self, Floor):  # String
		self.add_body_params('Floor', Floor)
	def get_ChannelId(self): # String
		return self.get_body_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_body_params('ChannelId', ChannelId)
	def get_OuterCode(self): # String
		return self.get_body_params().get('OuterCode')

	def set_OuterCode(self, OuterCode):  # String
		self.add_body_params('OuterCode', OuterCode)
