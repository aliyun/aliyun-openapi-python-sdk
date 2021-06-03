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

class InsertDevopsUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'devops-rdc', '2020-03-03', 'InsertDevopsUser')
		self.set_method('POST')

	def get_Phone(self):
		return self.get_body_params().get('Phone')

	def set_Phone(self,Phone):
		self.add_body_params('Phone', Phone)

	def get_UserPk(self):
		return self.get_body_params().get('UserPk')

	def set_UserPk(self,UserPk):
		self.add_body_params('UserPk', UserPk)

	def get_Email(self):
		return self.get_body_params().get('Email')

	def set_Email(self,Email):
		self.add_body_params('Email', Email)

	def get_UserName(self):
		return self.get_body_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_body_params('UserName', UserName)