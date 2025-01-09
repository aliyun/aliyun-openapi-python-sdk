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

class RunSynchronizationJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'RunSynchronizationJob','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_TargetId(self): # String
		return self.get_query_params().get('TargetId')

	def set_TargetId(self, TargetId):  # String
		self.add_query_param('TargetId', TargetId)
	def get_TargetType(self): # String
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_query_param('TargetType', TargetType)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_SynchronizationScopeConfig(self): # Struct
		return self.get_query_params().get('SynchronizationScopeConfig')

	def set_SynchronizationScopeConfig(self, SynchronizationScopeConfig):  # Struct
		if SynchronizationScopeConfig.get('OrganizationalUnitIds') is not None:
			for index1, value1 in enumerate(SynchronizationScopeConfig.get('OrganizationalUnitIds')):
				self.add_query_param('SynchronizationScopeConfig.OrganizationalUnitIds.' + str(index1 + 1), value1)
		if SynchronizationScopeConfig.get('UserIds') is not None:
			for index1, value1 in enumerate(SynchronizationScopeConfig.get('UserIds')):
				self.add_query_param('SynchronizationScopeConfig.UserIds.' + str(index1 + 1), value1)
		if SynchronizationScopeConfig.get('GroupIds') is not None:
			for index1, value1 in enumerate(SynchronizationScopeConfig.get('GroupIds')):
				self.add_query_param('SynchronizationScopeConfig.GroupIds.' + str(index1 + 1), value1)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_PasswordInitialization(self): # Boolean
		return self.get_query_params().get('PasswordInitialization')

	def set_PasswordInitialization(self, PasswordInitialization):  # Boolean
		self.add_query_param('PasswordInitialization', PasswordInitialization)
	def get_UserIdentityTypes(self): # Array
		return self.get_query_params().get('UserIdentityTypes')

	def set_UserIdentityTypes(self, UserIdentityTypes):  # Array
		for index1, value1 in enumerate(UserIdentityTypes):
			self.add_query_param('UserIdentityTypes.' + str(index1 + 1), value1)
