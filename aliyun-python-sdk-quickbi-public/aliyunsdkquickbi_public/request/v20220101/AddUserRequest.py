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

class AddUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'AddUser','2.2.0')
		self.set_method('POST')

	def get_AdminUser(self): # Boolean
		return self.get_query_params().get('AdminUser')

	def set_AdminUser(self, AdminUser):  # Boolean
		self.add_query_param('AdminUser', AdminUser)
	def get_AccountId(self): # String
		return self.get_query_params().get('AccountId')

	def set_AccountId(self, AccountId):  # String
		self.add_query_param('AccountId', AccountId)
	def get_RoleIds(self): # String
		return self.get_body_params().get('RoleIds')

	def set_RoleIds(self, RoleIds):  # String
		self.add_body_params('RoleIds', RoleIds)
	def get_AccountName(self): # String
		return self.get_query_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_query_param('AccountName', AccountName)
	def get_NickName(self): # String
		return self.get_query_params().get('NickName')

	def set_NickName(self, NickName):  # String
		self.add_query_param('NickName', NickName)
	def get_AuthAdminUser(self): # Boolean
		return self.get_query_params().get('AuthAdminUser')

	def set_AuthAdminUser(self, AuthAdminUser):  # Boolean
		self.add_query_param('AuthAdminUser', AuthAdminUser)
	def get_UserType(self): # Integer
		return self.get_query_params().get('UserType')

	def set_UserType(self, UserType):  # Integer
		self.add_query_param('UserType', UserType)
