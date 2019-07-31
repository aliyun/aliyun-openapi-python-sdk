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
class UpdateServerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateServer','hbr')
		self.set_protocol_type('https')

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_ServerType(self):
		return self.get_query_params().get('ServerType')

	def set_ServerType(self,ServerType):
		self.add_query_param('ServerType',ServerType)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_ServerStatus(self):
		return self.get_query_params().get('ServerStatus')

	def set_ServerStatus(self,ServerStatus):
		self.add_query_param('ServerStatus',ServerStatus)

	def get_Host(self):
		return self.get_query_params().get('Host')

	def set_Host(self,Host):
		self.add_query_param('Host',Host)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_DetailInfo(self):
		return self.get_query_params().get('DetailInfo')

	def set_DetailInfo(self,DetailInfo):
		self.add_query_param('DetailInfo',DetailInfo)

	def get_ServerId(self):
		return self.get_query_params().get('ServerId')

	def set_ServerId(self,ServerId):
		self.add_query_param('ServerId',ServerId)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_Username(self):
		return self.get_query_params().get('Username')

	def set_Username(self,Username):
		self.add_query_param('Username',Username)