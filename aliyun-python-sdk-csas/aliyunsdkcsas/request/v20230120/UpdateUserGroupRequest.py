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

class UpdateUserGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'UpdateUserGroup')
		self.set_method('POST')

	def get_UserGroupId(self): # String
		return self.get_body_params().get('UserGroupId')

	def set_UserGroupId(self, UserGroupId):  # String
		self.add_body_params('UserGroupId', UserGroupId)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_ModifyType(self): # String
		return self.get_body_params().get('ModifyType')

	def set_ModifyType(self, ModifyType):  # String
		self.add_body_params('ModifyType', ModifyType)
	def get_Attributes(self): # Array
		return self.get_body_params().get('Attributes')

	def set_Attributes(self, Attributes):  # Array
		for index1, value1 in enumerate(Attributes):
			if value1.get('UserGroupType') is not None:
				self.add_body_params('Attributes.' + str(index1 + 1) + '.UserGroupType', value1.get('UserGroupType'))
			if value1.get('IdpId') is not None:
				self.add_body_params('Attributes.' + str(index1 + 1) + '.IdpId', value1.get('IdpId'))
			if value1.get('Value') is not None:
				self.add_body_params('Attributes.' + str(index1 + 1) + '.Value', value1.get('Value'))
			if value1.get('Relation') is not None:
				self.add_body_params('Attributes.' + str(index1 + 1) + '.Relation', value1.get('Relation'))
