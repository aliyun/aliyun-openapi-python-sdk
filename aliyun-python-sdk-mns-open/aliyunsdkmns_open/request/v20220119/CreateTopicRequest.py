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
from aliyunsdkmns_open.endpoint import endpoint_data

class CreateTopicRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mns-open', '2022-01-19', 'CreateTopic','mns')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TopicName(self): # String
		return self.get_body_params().get('TopicName')

	def set_TopicName(self, TopicName):  # String
		self.add_body_params('TopicName', TopicName)
	def get_MaxMessageSize(self): # Long
		return self.get_body_params().get('MaxMessageSize')

	def set_MaxMessageSize(self, MaxMessageSize):  # Long
		self.add_body_params('MaxMessageSize', MaxMessageSize)
	def get_EnableLogging(self): # Boolean
		return self.get_body_params().get('EnableLogging')

	def set_EnableLogging(self, EnableLogging):  # Boolean
		self.add_body_params('EnableLogging', EnableLogging)
