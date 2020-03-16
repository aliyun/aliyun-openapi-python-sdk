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

class CreateQueueRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'amqp-open', '2019-12-12', 'CreateQueue','onsproxy')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_QueueName(self):
		return self.get_body_params().get('QueueName')

	def set_QueueName(self,QueueName):
		self.add_body_params('QueueName', QueueName)

	def get_DeadLetterRoutingKey(self):
		return self.get_body_params().get('DeadLetterRoutingKey')

	def set_DeadLetterRoutingKey(self,DeadLetterRoutingKey):
		self.add_body_params('DeadLetterRoutingKey', DeadLetterRoutingKey)

	def get_MaxLength(self):
		return self.get_body_params().get('MaxLength')

	def set_MaxLength(self,MaxLength):
		self.add_body_params('MaxLength', MaxLength)

	def get_AutoExpireState(self):
		return self.get_body_params().get('AutoExpireState')

	def set_AutoExpireState(self,AutoExpireState):
		self.add_body_params('AutoExpireState', AutoExpireState)

	def get_DeadLetterExchange(self):
		return self.get_body_params().get('DeadLetterExchange')

	def set_DeadLetterExchange(self,DeadLetterExchange):
		self.add_body_params('DeadLetterExchange', DeadLetterExchange)

	def get_InstanceId(self):
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_body_params('InstanceId', InstanceId)

	def get_ExclusiveState(self):
		return self.get_body_params().get('ExclusiveState')

	def set_ExclusiveState(self,ExclusiveState):
		self.add_body_params('ExclusiveState', ExclusiveState)

	def get_AutoDeleteState(self):
		return self.get_body_params().get('AutoDeleteState')

	def set_AutoDeleteState(self,AutoDeleteState):
		self.add_body_params('AutoDeleteState', AutoDeleteState)

	def get_MessageTTL(self):
		return self.get_body_params().get('MessageTTL')

	def set_MessageTTL(self,MessageTTL):
		self.add_body_params('MessageTTL', MessageTTL)

	def get_VirtualHost(self):
		return self.get_body_params().get('VirtualHost')

	def set_VirtualHost(self,VirtualHost):
		self.add_body_params('VirtualHost', VirtualHost)

	def get_MaximumPriority(self):
		return self.get_body_params().get('MaximumPriority')

	def set_MaximumPriority(self,MaximumPriority):
		self.add_body_params('MaximumPriority', MaximumPriority)