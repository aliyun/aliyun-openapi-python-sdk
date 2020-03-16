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
from aliyunsdkamqp_open.endpoint import endpoint_data

class CreateExchangeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'amqp-open', '2019-12-12', 'CreateExchange','onsproxy')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Internal(self):
		return self.get_body_params().get('Internal')

	def set_Internal(self,Internal):
		self.add_body_params('Internal', Internal)

	def get_ExchangeName(self):
		return self.get_body_params().get('ExchangeName')

	def set_ExchangeName(self,ExchangeName):
		self.add_body_params('ExchangeName', ExchangeName)

	def get_InstanceId(self):
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_body_params('InstanceId', InstanceId)

	def get_AlternateExchange(self):
		return self.get_body_params().get('AlternateExchange')

	def set_AlternateExchange(self,AlternateExchange):
		self.add_body_params('AlternateExchange', AlternateExchange)

	def get_AutoDeleteState(self):
		return self.get_body_params().get('AutoDeleteState')

	def set_AutoDeleteState(self,AutoDeleteState):
		self.add_body_params('AutoDeleteState', AutoDeleteState)

	def get_ExchangeType(self):
		return self.get_body_params().get('ExchangeType')

	def set_ExchangeType(self,ExchangeType):
		self.add_body_params('ExchangeType', ExchangeType)

	def get_VirtualHost(self):
		return self.get_body_params().get('VirtualHost')

	def set_VirtualHost(self,VirtualHost):
		self.add_body_params('VirtualHost', VirtualHost)