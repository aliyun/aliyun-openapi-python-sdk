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
from aliyunsdkiot.endpoint import endpoint_data

class ModifyOTAFirmwareRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'ModifyOTAFirmware','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FirmwareUdi(self):
		return self.get_query_params().get('FirmwareUdi')

	def set_FirmwareUdi(self,FirmwareUdi):
		self.add_query_param('FirmwareUdi',FirmwareUdi)

	def get_FirmwareDesc(self):
		return self.get_query_params().get('FirmwareDesc')

	def set_FirmwareDesc(self,FirmwareDesc):
		self.add_query_param('FirmwareDesc',FirmwareDesc)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_FirmwareName(self):
		return self.get_query_params().get('FirmwareName')

	def set_FirmwareName(self,FirmwareName):
		self.add_query_param('FirmwareName',FirmwareName)

	def get_FirmwareId(self):
		return self.get_query_params().get('FirmwareId')

	def set_FirmwareId(self,FirmwareId):
		self.add_query_param('FirmwareId',FirmwareId)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)