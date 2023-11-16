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

class UpdateRegistrationPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'UpdateRegistrationPolicy')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_MatchMode(self): # String
		return self.get_body_params().get('MatchMode')

	def set_MatchMode(self, MatchMode):  # String
		self.add_body_params('MatchMode', MatchMode)
	def get_PolicyId(self): # String
		return self.get_body_params().get('PolicyId')

	def set_PolicyId(self, PolicyId):  # String
		self.add_body_params('PolicyId', PolicyId)
	def get_CompanyLimitCount(self): # Struct
		return self.get_body_params().get('CompanyLimitCount')

	def set_CompanyLimitCount(self, CompanyLimitCount):  # Struct
		self.add_body_params("CompanyLimitCount", json.dumps(CompanyLimitCount))
	def get_PersonalLimitCount(self): # Struct
		return self.get_body_params().get('PersonalLimitCount')

	def set_PersonalLimitCount(self, PersonalLimitCount):  # Struct
		self.add_body_params("PersonalLimitCount", json.dumps(PersonalLimitCount))
	def get_UserGroupIds(self): # Array
		return self.get_body_params().get('UserGroupIds')

	def set_UserGroupIds(self, UserGroupIds):  # Array
		for index1, value1 in enumerate(UserGroupIds):
			self.add_body_params('UserGroupIds.' + str(index1 + 1), value1)
	def get_Whitelist(self): # Array
		return self.get_body_params().get('Whitelist')

	def set_Whitelist(self, Whitelist):  # Array
		for index1, value1 in enumerate(Whitelist):
			self.add_body_params('Whitelist.' + str(index1 + 1), value1)
	def get_Priority(self): # Long
		return self.get_body_params().get('Priority')

	def set_Priority(self, Priority):  # Long
		self.add_body_params('Priority', Priority)
	def get_PersonalLimitType(self): # String
		return self.get_body_params().get('PersonalLimitType')

	def set_PersonalLimitType(self, PersonalLimitType):  # String
		self.add_body_params('PersonalLimitType', PersonalLimitType)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_CompanyLimitType(self): # String
		return self.get_body_params().get('CompanyLimitType')

	def set_CompanyLimitType(self, CompanyLimitType):  # String
		self.add_body_params('CompanyLimitType', CompanyLimitType)
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
