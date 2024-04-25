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

class CreateClientUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'CreateClientUser')
		self.set_method('POST')

	def get_MobileNumber(self): # String
		return self.get_query_params().get('MobileNumber')

	def set_MobileNumber(self, MobileNumber):  # String
		self.add_query_param('MobileNumber', MobileNumber)
	def get_DepartmentId(self): # String
		return self.get_query_params().get('DepartmentId')

	def set_DepartmentId(self, DepartmentId):  # String
		self.add_query_param('DepartmentId', DepartmentId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_IdpConfigId(self): # String
		return self.get_query_params().get('IdpConfigId')

	def set_IdpConfigId(self, IdpConfigId):  # String
		self.add_query_param('IdpConfigId', IdpConfigId)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
