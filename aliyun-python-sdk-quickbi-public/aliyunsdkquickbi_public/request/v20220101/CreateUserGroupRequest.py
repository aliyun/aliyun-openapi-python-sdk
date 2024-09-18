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

class CreateUserGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'CreateUserGroup','2.2.0')
		self.set_method('POST')

	def get_UserGroupName(self): # String
		return self.get_query_params().get('UserGroupName')

	def set_UserGroupName(self, UserGroupName):  # String
		self.add_query_param('UserGroupName', UserGroupName)
	def get_ParentUserGroupId(self): # String
		return self.get_query_params().get('ParentUserGroupId')

	def set_ParentUserGroupId(self, ParentUserGroupId):  # String
		self.add_query_param('ParentUserGroupId', ParentUserGroupId)
	def get_UserGroupId(self): # String
		return self.get_query_params().get('UserGroupId')

	def set_UserGroupId(self, UserGroupId):  # String
		self.add_query_param('UserGroupId', UserGroupId)
	def get_UserGroupDescription(self): # String
		return self.get_query_params().get('UserGroupDescription')

	def set_UserGroupDescription(self, UserGroupDescription):  # String
		self.add_query_param('UserGroupDescription', UserGroupDescription)
