# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class SetRemoteReqAuthConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2014-11-11', 'SetRemoteReqAuthConfig')

	def get_AuthPath(self):
		return self.get_query_params().get('AuthPath')

	def set_AuthPath(self,AuthPath):
		self.add_query_param('AuthPath',AuthPath)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_AuthEnable(self):
		return self.get_query_params().get('AuthEnable')

	def set_AuthEnable(self,AuthEnable):
		self.add_query_param('AuthEnable',AuthEnable)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TimeOut(self):
		return self.get_query_params().get('TimeOut')

	def set_TimeOut(self,TimeOut):
		self.add_query_param('TimeOut',TimeOut)

	def get_AuthType(self):
		return self.get_query_params().get('AuthType')

	def set_AuthType(self,AuthType):
		self.add_query_param('AuthType',AuthType)

	def get_AuthProvider(self):
		return self.get_query_params().get('AuthProvider')

	def set_AuthProvider(self,AuthProvider):
		self.add_query_param('AuthProvider',AuthProvider)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_AuthCrash(self):
		return self.get_query_params().get('AuthCrash')

	def set_AuthCrash(self,AuthCrash):
		self.add_query_param('AuthCrash',AuthCrash)

	def get_AuthAddr(self):
		return self.get_query_params().get('AuthAddr')

	def set_AuthAddr(self,AuthAddr):
		self.add_query_param('AuthAddr',AuthAddr)

	def get_AuthFileType(self):
		return self.get_query_params().get('AuthFileType')

	def set_AuthFileType(self,AuthFileType):
		self.add_query_param('AuthFileType',AuthFileType)