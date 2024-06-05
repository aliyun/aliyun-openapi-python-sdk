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

class RetryDatabaseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-dg', '2023-09-14', 'RetryDatabase')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_Host(self): # String
		return self.get_body_params().get('Host')

	def set_Host(self, Host):  # String
		self.add_body_params('Host', Host)
	def get_DbUserName(self): # String
		return self.get_body_params().get('DbUserName')

	def set_DbUserName(self, DbUserName):  # String
		self.add_body_params('DbUserName', DbUserName)
	def get_DbDescription(self): # String
		return self.get_body_params().get('DbDescription')

	def set_DbDescription(self, DbDescription):  # String
		self.add_body_params('DbDescription', DbDescription)
	def get_GatewayId(self): # String
		return self.get_body_params().get('GatewayId')

	def set_GatewayId(self, GatewayId):  # String
		self.add_body_params('GatewayId', GatewayId)
	def get_DbName(self): # String
		return self.get_body_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_body_params('DbName', DbName)
	def get_Port(self): # Integer
		return self.get_body_params().get('Port')

	def set_Port(self, Port):  # Integer
		self.add_body_params('Port', Port)
	def get_DbPassword(self): # String
		return self.get_body_params().get('DbPassword')

	def set_DbPassword(self, DbPassword):  # String
		self.add_body_params('DbPassword', DbPassword)
	def get_DbType(self): # String
		return self.get_body_params().get('DbType')

	def set_DbType(self, DbType):  # String
		self.add_body_params('DbType', DbType)
