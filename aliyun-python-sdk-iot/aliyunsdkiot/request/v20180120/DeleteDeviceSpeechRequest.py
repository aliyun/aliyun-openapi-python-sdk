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

class DeleteDeviceSpeechRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'DeleteDeviceSpeech','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IotId(self):
		return self.get_body_params().get('IotId')

	def set_IotId(self,IotId):
		self.add_body_params('IotId', IotId)

	def get_IotInstanceId(self):
		return self.get_body_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_body_params('IotInstanceId', IotInstanceId)

	def get_DeviceSpeechLists(self):
		return self.get_body_params().get('DeviceSpeechList')

	def set_DeviceSpeechLists(self, DeviceSpeechLists):
		for depth1 in range(len(DeviceSpeechLists)):
			if DeviceSpeechLists[depth1].get('BizCode') is not None:
				self.add_body_params('DeviceSpeechList.' + str(depth1 + 1) + '.BizCode', DeviceSpeechLists[depth1].get('BizCode'))
			if DeviceSpeechLists[depth1].get('AudioFormat') is not None:
				self.add_body_params('DeviceSpeechList.' + str(depth1 + 1) + '.AudioFormat', DeviceSpeechLists[depth1].get('AudioFormat'))