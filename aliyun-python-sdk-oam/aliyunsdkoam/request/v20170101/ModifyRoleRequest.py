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

class ModifyRoleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Oam', '2017-01-01', 'ModifyRole')
		self.set_method('POST')

	def get_NewRoleName(self):
		return self.get_query_params().get('NewRoleName')

	def set_NewRoleName(self,NewRoleName):
		self.add_query_param('NewRoleName',NewRoleName)

	def get_RoleName(self):
		return self.get_query_params().get('RoleName')

	def set_RoleName(self,RoleName):
		self.add_query_param('RoleName',RoleName)

	def get_NewAttribute(self):
		return self.get_query_params().get('NewAttribute')

	def set_NewAttribute(self,NewAttribute):
		self.add_query_param('NewAttribute',NewAttribute)

	def get_NewRoleType(self):
		return self.get_query_params().get('NewRoleType')

	def set_NewRoleType(self,NewRoleType):
		self.add_query_param('NewRoleType',NewRoleType)

	def get_NewDescription(self):
		return self.get_query_params().get('NewDescription')

	def set_NewDescription(self,NewDescription):
		self.add_query_param('NewDescription',NewDescription)