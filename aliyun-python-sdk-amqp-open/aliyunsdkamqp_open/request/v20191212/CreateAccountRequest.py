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

class CreateAccountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'amqp-open', '2019-12-12', 'CreateAccount')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_signature(self): # String
		return self.get_query_params().get('signature')

	def set_signature(self, signature):  # String
		self.add_query_param('signature', signature)
	def get_secretSign(self): # String
		return self.get_query_params().get('secretSign')

	def set_secretSign(self, secretSign):  # String
		self.add_query_param('secretSign', secretSign)
	def get_accountAccessKey(self): # String
		return self.get_query_params().get('accountAccessKey')

	def set_accountAccessKey(self, accountAccessKey):  # String
		self.add_query_param('accountAccessKey', accountAccessKey)
	def get_instanceId(self): # String
		return self.get_query_params().get('instanceId')

	def set_instanceId(self, instanceId):  # String
		self.add_query_param('instanceId', instanceId)
	def get_createTimestamp(self): # Long
		return self.get_query_params().get('createTimestamp')

	def set_createTimestamp(self, createTimestamp):  # Long
		self.add_query_param('createTimestamp', createTimestamp)
	def get_userName(self): # String
		return self.get_query_params().get('userName')

	def set_userName(self, userName):  # String
		self.add_query_param('userName', userName)
