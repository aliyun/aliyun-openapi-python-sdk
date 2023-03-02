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

class BatchCheckImportDeviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'BatchCheckImportDevice','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_DeviceLists(self):
		return self.get_query_params().get('DeviceList')

	def set_DeviceLists(self, DeviceLists):
		for depth1 in range(len(DeviceLists)):
			if DeviceLists[depth1].get('DeviceSecret') is not None:
				self.add_query_param('DeviceList.' + str(depth1 + 1) + '.DeviceSecret', DeviceLists[depth1].get('DeviceSecret'))
			if DeviceLists[depth1].get('DeviceName') is not None:
				self.add_query_param('DeviceList.' + str(depth1 + 1) + '.DeviceName', DeviceLists[depth1].get('DeviceName'))
			if DeviceLists[depth1].get('Sn') is not None:
				self.add_query_param('DeviceList.' + str(depth1 + 1) + '.Sn', DeviceLists[depth1].get('Sn'))