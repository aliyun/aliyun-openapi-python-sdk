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

class UpdateDeviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'UpdateDevice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DeviceSite(self):
		return self.get_body_params().get('DeviceSite')

	def set_DeviceSite(self,DeviceSite):
		self.add_body_params('DeviceSite', DeviceSite)

	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_GbId(self):
		return self.get_body_params().get('GbId')

	def set_GbId(self,GbId):
		self.add_body_params('GbId', GbId)

	def get_BitRate(self):
		return self.get_body_params().get('BitRate')

	def set_BitRate(self,BitRate):
		self.add_body_params('BitRate', BitRate)

	def get_DeviceDirection(self):
		return self.get_body_params().get('DeviceDirection')

	def set_DeviceDirection(self,DeviceDirection):
		self.add_body_params('DeviceDirection', DeviceDirection)

	def get_DeviceAddress(self):
		return self.get_body_params().get('DeviceAddress')

	def set_DeviceAddress(self,DeviceAddress):
		self.add_body_params('DeviceAddress', DeviceAddress)

	def get_DeviceType(self):
		return self.get_body_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_body_params('DeviceType', DeviceType)

	def get_DeviceResolution(self):
		return self.get_body_params().get('DeviceResolution')

	def set_DeviceResolution(self,DeviceResolution):
		self.add_body_params('DeviceResolution', DeviceResolution)

	def get_Vendor(self):
		return self.get_body_params().get('Vendor')

	def set_Vendor(self,Vendor):
		self.add_body_params('Vendor', Vendor)

	def get_DeviceName(self):
		return self.get_body_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_body_params('DeviceName', DeviceName)