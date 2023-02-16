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

class CreateConnectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'CreateConnection')
		self.set_method('POST')

	def get_ConnectionName(self): # String
		return self.get_query_params().get('ConnectionName')

	def set_ConnectionName(self, ConnectionName):  # String
		self.add_query_param('ConnectionName', ConnectionName)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_NetworkParameters(self): # Struct
		return self.get_query_params().get('NetworkParameters')

	def set_NetworkParameters(self, NetworkParameters):  # Struct
		self.add_query_param("NetworkParameters", json.dumps(NetworkParameters))
	def get_AuthParameters(self): # Struct
		return self.get_query_params().get('AuthParameters')

	def set_AuthParameters(self, AuthParameters):  # Struct
		self.add_query_param("AuthParameters", json.dumps(AuthParameters))
