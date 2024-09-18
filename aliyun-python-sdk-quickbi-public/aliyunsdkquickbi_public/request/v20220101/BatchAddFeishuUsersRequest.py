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

class BatchAddFeishuUsersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'BatchAddFeishuUsers','2.2.0')
		self.set_method('POST')

	def get_IsAuthAdmin(self): # Boolean
		return self.get_query_params().get('IsAuthAdmin')

	def set_IsAuthAdmin(self, IsAuthAdmin):  # Boolean
		self.add_query_param('IsAuthAdmin', IsAuthAdmin)
	def get_IsAdmin(self): # Boolean
		return self.get_query_params().get('IsAdmin')

	def set_IsAdmin(self, IsAdmin):  # Boolean
		self.add_query_param('IsAdmin', IsAdmin)
	def get_UserType(self): # Integer
		return self.get_query_params().get('UserType')

	def set_UserType(self, UserType):  # Integer
		self.add_query_param('UserType', UserType)
	def get_UserGroupIds(self): # String
		return self.get_query_params().get('UserGroupIds')

	def set_UserGroupIds(self, UserGroupIds):  # String
		self.add_query_param('UserGroupIds', UserGroupIds)
	def get_FeishuUsers(self): # String
		return self.get_query_params().get('FeishuUsers')

	def set_FeishuUsers(self, FeishuUsers):  # String
		self.add_query_param('FeishuUsers', FeishuUsers)
