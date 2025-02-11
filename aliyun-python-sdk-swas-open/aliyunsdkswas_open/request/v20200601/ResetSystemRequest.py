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

class ResetSystemRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SWAS-OPEN', '2020-06-01', 'ResetSystem','SWAS-OPEN')
		self.set_method('POST')

	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_LoginCredentials(self): # Struct
		return self.get_query_params().get('LoginCredentials')

	def set_LoginCredentials(self, LoginCredentials):  # Struct
		if LoginCredentials.get('Password') is not None:
			self.add_query_param('LoginCredentials.Password', LoginCredentials.get('Password'))
		if LoginCredentials.get('KeyPairName') is not None:
			self.add_query_param('LoginCredentials.KeyPairName', LoginCredentials.get('KeyPairName'))
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
