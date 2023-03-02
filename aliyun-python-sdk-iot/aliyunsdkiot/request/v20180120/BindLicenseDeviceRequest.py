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

class BindLicenseDeviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'BindLicenseDevice','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DeviceNameLists(self):
		return self.get_body_params().get('DeviceNameList')

	def set_DeviceNameLists(self, DeviceNameLists):
		for depth1 in range(len(DeviceNameLists)):
			if DeviceNameLists[depth1] is not None:
				self.add_body_params('DeviceNameList.' + str(depth1 + 1) , DeviceNameLists[depth1])

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_IotIdLists(self):
		return self.get_body_params().get('IotIdList')

	def set_IotIdLists(self, IotIdLists):
		for depth1 in range(len(IotIdLists)):
			if IotIdLists[depth1] is not None:
				self.add_body_params('IotIdList.' + str(depth1 + 1) , IotIdLists[depth1])

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_LicenseCode(self):
		return self.get_query_params().get('LicenseCode')

	def set_LicenseCode(self,LicenseCode):
		self.add_query_param('LicenseCode',LicenseCode)