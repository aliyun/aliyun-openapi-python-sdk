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
from aliyunsdkidrsservice.endpoint import endpoint_data

class UpdateSlrConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idrsservice', '2020-06-30', 'UpdateSlrConfiguration','idrsservice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MqInstanceId(self):
		return self.get_query_params().get('MqInstanceId')

	def set_MqInstanceId(self,MqInstanceId):
		self.add_query_param('MqInstanceId',MqInstanceId)

	def get_MqGroupId(self):
		return self.get_query_params().get('MqGroupId')

	def set_MqGroupId(self,MqGroupId):
		self.add_query_param('MqGroupId',MqGroupId)

	def get_MqEvents(self):
		return self.get_query_params().get('MqEvent')

	def set_MqEvents(self, MqEvents):
		for depth1 in range(len(MqEvents)):
			if MqEvents[depth1] is not None:
				self.add_query_param('MqEvent.' + str(depth1 + 1) , MqEvents[depth1])

	def get_MqEndpoint(self):
		return self.get_query_params().get('MqEndpoint')

	def set_MqEndpoint(self,MqEndpoint):
		self.add_query_param('MqEndpoint',MqEndpoint)

	def get_MqTopic(self):
		return self.get_query_params().get('MqTopic')

	def set_MqTopic(self,MqTopic):
		self.add_query_param('MqTopic',MqTopic)

	def get_MqSubscribe(self):
		return self.get_query_params().get('MqSubscribe')

	def set_MqSubscribe(self,MqSubscribe):
		self.add_query_param('MqSubscribe',MqSubscribe)