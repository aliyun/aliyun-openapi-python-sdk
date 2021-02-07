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

class CreateDeviceDistributeJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateDeviceDistributeJob','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SourceInstanceId(self):
		return self.get_body_params().get('SourceInstanceId')

	def set_SourceInstanceId(self,SourceInstanceId):
		self.add_body_params('SourceInstanceId', SourceInstanceId)

	def get_TargetAliyunId(self):
		return self.get_body_params().get('TargetAliyunId')

	def set_TargetAliyunId(self,TargetAliyunId):
		self.add_body_params('TargetAliyunId', TargetAliyunId)

	def get_TargetInstanceConfigs(self):
		return self.get_body_params().get('TargetInstanceConfig')

	def set_TargetInstanceConfigs(self, TargetInstanceConfigs):
		for depth1 in range(len(TargetInstanceConfigs)):
			if TargetInstanceConfigs[depth1].get('TargetInstanceId') is not None:
				self.add_body_params('TargetInstanceConfig.' + str(depth1 + 1) + '.TargetInstanceId', TargetInstanceConfigs[depth1].get('TargetInstanceId'))

	def get_ProductKey(self):
		return self.get_body_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_body_params('ProductKey', ProductKey)

	def get_DeviceNames(self):
		return self.get_body_params().get('DeviceName')

	def set_DeviceNames(self, DeviceNames):
		for depth1 in range(len(DeviceNames)):
			if DeviceNames[depth1] is not None:
				self.add_body_params('DeviceName.' + str(depth1 + 1) , DeviceNames[depth1])

	def get_TargetUid(self):
		return self.get_body_params().get('TargetUid')

	def set_TargetUid(self,TargetUid):
		self.add_body_params('TargetUid', TargetUid)

	def get_Strategy(self):
		return self.get_body_params().get('Strategy')

	def set_Strategy(self,Strategy):
		self.add_body_params('Strategy', Strategy)