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

class AuthorizeMenuRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'AuthorizeMenu','2.2.0')
		self.set_method('POST')

	def get_DataPortalId(self): # String
		return self.get_query_params().get('DataPortalId')

	def set_DataPortalId(self, DataPortalId):  # String
		self.add_query_param('DataPortalId', DataPortalId)
	def get_AuthPointsValue(self): # Integer
		return self.get_query_params().get('AuthPointsValue')

	def set_AuthPointsValue(self, AuthPointsValue):  # Integer
		self.add_query_param('AuthPointsValue', AuthPointsValue)
	def get_MenuIds(self): # String
		return self.get_query_params().get('MenuIds')

	def set_MenuIds(self, MenuIds):  # String
		self.add_query_param('MenuIds', MenuIds)
	def get_UserGroupIds(self): # String
		return self.get_query_params().get('UserGroupIds')

	def set_UserGroupIds(self, UserGroupIds):  # String
		self.add_query_param('UserGroupIds', UserGroupIds)
	def get_UserIds(self): # String
		return self.get_query_params().get('UserIds')

	def set_UserIds(self, UserIds):  # String
		self.add_query_param('UserIds', UserIds)
