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

class CreatePrivateAccessPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'CreatePrivateAccessPolicy')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_CustomUserAttributes(self): # Array
		return self.get_body_params().get('CustomUserAttributes')

	def set_CustomUserAttributes(self, CustomUserAttributes):  # Array
		self.add_body_params("CustomUserAttributes", json.dumps(CustomUserAttributes))
	def get_TagIds(self): # Array
		return self.get_body_params().get('TagIds')

	def set_TagIds(self, TagIds):  # Array
		self.add_body_params("TagIds", json.dumps(TagIds))
	def get_UserGroupIds(self): # Array
		return self.get_body_params().get('UserGroupIds')

	def set_UserGroupIds(self, UserGroupIds):  # Array
		self.add_body_params("UserGroupIds", json.dumps(UserGroupIds))
	def get_PolicyAction(self): # String
		return self.get_body_params().get('PolicyAction')

	def set_PolicyAction(self, PolicyAction):  # String
		self.add_body_params('PolicyAction', PolicyAction)
	def get_Priority(self): # Integer
		return self.get_body_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_body_params('Priority', Priority)
	def get_ApplicationIds(self): # Array
		return self.get_body_params().get('ApplicationIds')

	def set_ApplicationIds(self, ApplicationIds):  # Array
		self.add_body_params("ApplicationIds", json.dumps(ApplicationIds))
	def get_UserGroupMode(self): # String
		return self.get_body_params().get('UserGroupMode')

	def set_UserGroupMode(self, UserGroupMode):  # String
		self.add_body_params('UserGroupMode', UserGroupMode)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_ApplicationType(self): # String
		return self.get_body_params().get('ApplicationType')

	def set_ApplicationType(self, ApplicationType):  # String
		self.add_body_params('ApplicationType', ApplicationType)
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
