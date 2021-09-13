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
from aliyunsdklinkwan.endpoint import endpoint_data

class SendUnicastCommandRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2019-03-01', 'SendUnicastCommand','linkwan')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Confirmed(self):
		return self.get_query_params().get('Confirmed')

	def set_Confirmed(self,Confirmed):
		self.add_query_param('Confirmed',Confirmed)

	def get_Content(self):
		return self.get_query_params().get('Content')

	def set_Content(self,Content):
		self.add_query_param('Content',Content)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_MaxRetries(self):
		return self.get_query_params().get('MaxRetries')

	def set_MaxRetries(self,MaxRetries):
		self.add_query_param('MaxRetries',MaxRetries)

	def get_DevEui(self):
		return self.get_query_params().get('DevEui')

	def set_DevEui(self,DevEui):
		self.add_query_param('DevEui',DevEui)

	def get_CleanUp(self):
		return self.get_query_params().get('CleanUp')

	def set_CleanUp(self,CleanUp):
		self.add_query_param('CleanUp',CleanUp)

	def get_FPort(self):
		return self.get_query_params().get('FPort')

	def set_FPort(self,FPort):
		self.add_query_param('FPort',FPort)