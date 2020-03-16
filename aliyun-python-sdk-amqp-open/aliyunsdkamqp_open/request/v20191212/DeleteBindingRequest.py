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

class DeleteBindingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'amqp-open', '2019-12-12', 'DeleteBinding','onsproxy')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DestinationName(self):
		return self.get_body_params().get('DestinationName')

	def set_DestinationName(self,DestinationName):
		self.add_body_params('DestinationName', DestinationName)

	def get_SourceExchange(self):
		return self.get_body_params().get('SourceExchange')

	def set_SourceExchange(self,SourceExchange):
		self.add_body_params('SourceExchange', SourceExchange)

	def get_BindingKey(self):
		return self.get_body_params().get('BindingKey')

	def set_BindingKey(self,BindingKey):
		self.add_body_params('BindingKey', BindingKey)

	def get_BindingType(self):
		return self.get_body_params().get('BindingType')

	def set_BindingType(self,BindingType):
		self.add_body_params('BindingType', BindingType)

	def get_InstanceId(self):
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_body_params('InstanceId', InstanceId)

	def get_VirtualHost(self):
		return self.get_body_params().get('VirtualHost')

	def set_VirtualHost(self,VirtualHost):
		self.add_body_params('VirtualHost', VirtualHost)