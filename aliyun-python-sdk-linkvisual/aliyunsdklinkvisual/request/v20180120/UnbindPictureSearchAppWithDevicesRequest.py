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
from aliyunsdklinkvisual.endpoint import endpoint_data

class UnbindPictureSearchAppWithDevicesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Linkvisual', '2018-01-20', 'UnbindPictureSearchAppWithDevices','Linkvisual')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IotInstanceId(self): # String
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self, IotInstanceId):  # String
		self.add_query_param('IotInstanceId', IotInstanceId)
	def get_DeviceIotIdss(self): # RepeatList
		return self.get_query_params().get('DeviceIotIds')

	def set_DeviceIotIdss(self, DeviceIotIds):  # RepeatList
		for depth1 in range(len(DeviceIotIds)):
			self.add_query_param('DeviceIotIds.' + str(depth1 + 1), DeviceIotIds[depth1])
	def get_AppInstanceId(self): # String
		return self.get_query_params().get('AppInstanceId')

	def set_AppInstanceId(self, AppInstanceId):  # String
		self.add_query_param('AppInstanceId', AppInstanceId)
