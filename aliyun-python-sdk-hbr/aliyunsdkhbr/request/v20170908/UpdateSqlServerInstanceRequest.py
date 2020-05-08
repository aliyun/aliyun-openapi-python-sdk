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
class UpdateSqlServerInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateSqlServerInstance','hbr')

	def get_WindowsLogin(self):
		return self.get_query_params().get('WindowsLogin')

	def set_WindowsLogin(self,WindowsLogin):
		self.add_query_param('WindowsLogin',WindowsLogin)

	def get_WindowsPassword(self):
		return self.get_query_params().get('WindowsPassword')

	def set_WindowsPassword(self,WindowsPassword):
		self.add_query_param('WindowsPassword',WindowsPassword)

	def get_SqlLogin(self):
		return self.get_query_params().get('SqlLogin')

	def set_SqlLogin(self,SqlLogin):
		self.add_query_param('SqlLogin',SqlLogin)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_UseWindowsAuth(self):
		return self.get_query_params().get('UseWindowsAuth')

	def set_UseWindowsAuth(self,UseWindowsAuth):
		self.add_query_param('UseWindowsAuth',UseWindowsAuth)

	def get_SqlPassword(self):
		return self.get_query_params().get('SqlPassword')

	def set_SqlPassword(self,SqlPassword):
		self.add_query_param('SqlPassword',SqlPassword)

	def get_ServerName(self):
		return self.get_query_params().get('ServerName')

	def set_ServerName(self,ServerName):
		self.add_query_param('ServerName',ServerName)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)