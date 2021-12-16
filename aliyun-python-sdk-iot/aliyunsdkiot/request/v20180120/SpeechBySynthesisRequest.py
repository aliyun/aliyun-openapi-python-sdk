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

class SpeechBySynthesisRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'SpeechBySynthesis','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Voice(self):
		return self.get_body_params().get('Voice')

	def set_Voice(self,Voice):
		self.add_body_params('Voice', Voice)

	def get_SpeechId(self):
		return self.get_body_params().get('SpeechId')

	def set_SpeechId(self,SpeechId):
		self.add_body_params('SpeechId', SpeechId)

	def get_AudioFormat(self):
		return self.get_body_params().get('AudioFormat')

	def set_AudioFormat(self,AudioFormat):
		self.add_body_params('AudioFormat', AudioFormat)

	def get_IotId(self):
		return self.get_body_params().get('IotId')

	def set_IotId(self,IotId):
		self.add_body_params('IotId', IotId)

	def get_IotInstanceId(self):
		return self.get_body_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_body_params('IotInstanceId', IotInstanceId)

	def get_Text(self):
		return self.get_body_params().get('Text')

	def set_Text(self,Text):
		self.add_body_params('Text', Text)

	def get_ProductKey(self):
		return self.get_body_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_body_params('ProductKey', ProductKey)

	def get_Volume(self):
		return self.get_body_params().get('Volume')

	def set_Volume(self,Volume):
		self.add_body_params('Volume', Volume)

	def get_DeviceName(self):
		return self.get_body_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_body_params('DeviceName', DeviceName)

	def get_SpeechRate(self):
		return self.get_body_params().get('SpeechRate')

	def set_SpeechRate(self,SpeechRate):
		self.add_body_params('SpeechRate', SpeechRate)