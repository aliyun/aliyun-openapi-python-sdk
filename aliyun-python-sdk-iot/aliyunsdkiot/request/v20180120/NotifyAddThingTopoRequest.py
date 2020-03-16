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

class NotifyAddThingTopoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'NotifyAddThingTopo','Iot')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_GwProductKey(self):
		return self.get_query_params().get('GwProductKey')

	def set_GwProductKey(self,GwProductKey):
		self.add_query_param('GwProductKey',GwProductKey)

	def get_DeviceListStr(self):
		return self.get_query_params().get('DeviceListStr')

	def set_DeviceListStr(self,DeviceListStr):
		self.add_query_param('DeviceListStr',DeviceListStr)

	def get_GwDeviceName(self):
		return self.get_query_params().get('GwDeviceName')

	def set_GwDeviceName(self,GwDeviceName):
		self.add_query_param('GwDeviceName',GwDeviceName)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_GwIotId(self):
		return self.get_query_params().get('GwIotId')

	def set_GwIotId(self,GwIotId):
		self.add_query_param('GwIotId',GwIotId)