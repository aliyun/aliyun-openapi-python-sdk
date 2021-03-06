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
from aliyunsdkonsmqtt.endpoint import endpoint_data

class SendMessageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OnsMqtt', '2020-04-20', 'SendMessage','onsmqtt')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MqttTopic(self):
		return self.get_query_params().get('MqttTopic')

	def set_MqttTopic(self,MqttTopic):
		self.add_query_param('MqttTopic',MqttTopic)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Payload(self):
		return self.get_query_params().get('Payload')

	def set_Payload(self,Payload):
		self.add_query_param('Payload',Payload)