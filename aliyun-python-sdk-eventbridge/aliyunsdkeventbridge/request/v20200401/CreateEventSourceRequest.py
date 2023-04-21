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
import json

class CreateEventSourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'CreateEventSource')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_EventBusName(self): # String
		return self.get_body_params().get('EventBusName')

	def set_EventBusName(self, EventBusName):  # String
		self.add_body_params('EventBusName', EventBusName)
	def get_SourceMNSParameters(self): # Struct
		return self.get_body_params().get('SourceMNSParameters')

	def set_SourceMNSParameters(self, SourceMNSParameters):  # Struct
		self.add_body_params("SourceMNSParameters", json.dumps(SourceMNSParameters))
	def get_SourceRabbitMQParameters(self): # Struct
		return self.get_body_params().get('SourceRabbitMQParameters')

	def set_SourceRabbitMQParameters(self, SourceRabbitMQParameters):  # Struct
		self.add_body_params("SourceRabbitMQParameters", json.dumps(SourceRabbitMQParameters))
	def get_SourceRocketMQParameters(self): # Struct
		return self.get_body_params().get('SourceRocketMQParameters')

	def set_SourceRocketMQParameters(self, SourceRocketMQParameters):  # Struct
		self.add_body_params("SourceRocketMQParameters", json.dumps(SourceRocketMQParameters))
	def get_SourceSLSParameters(self): # Struct
		return self.get_body_params().get('SourceSLSParameters')

	def set_SourceSLSParameters(self, SourceSLSParameters):  # Struct
		self.add_body_params("SourceSLSParameters", json.dumps(SourceSLSParameters))
	def get_SourceScheduledEventParameters(self): # Struct
		return self.get_body_params().get('SourceScheduledEventParameters')

	def set_SourceScheduledEventParameters(self, SourceScheduledEventParameters):  # Struct
		self.add_body_params("SourceScheduledEventParameters", json.dumps(SourceScheduledEventParameters))
	def get_SourceKafkaParameters(self): # Struct
		return self.get_body_params().get('SourceKafkaParameters')

	def set_SourceKafkaParameters(self, SourceKafkaParameters):  # Struct
		self.add_body_params("SourceKafkaParameters", json.dumps(SourceKafkaParameters))
	def get_SourceHttpEventParameters(self): # Struct
		return self.get_body_params().get('SourceHttpEventParameters')

	def set_SourceHttpEventParameters(self, SourceHttpEventParameters):  # Struct
		self.add_body_params("SourceHttpEventParameters", json.dumps(SourceHttpEventParameters))
	def get_EventSourceName(self): # String
		return self.get_body_params().get('EventSourceName')

	def set_EventSourceName(self, EventSourceName):  # String
		self.add_body_params('EventSourceName', EventSourceName)
