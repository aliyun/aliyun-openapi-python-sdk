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

from aliyunsdkcore.request import RoaRequest

class CreateRepositoryRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'codeup', '2020-04-14', 'CreateRepository')
		self.set_uri_pattern('/api/v3/projects')
		self.set_method('POST')

	def get_OrganizationId(self):
		return self.get_query_params().get('OrganizationId')

	def set_OrganizationId(self,OrganizationId):
		self.add_query_param('OrganizationId',OrganizationId)

	def get_SubUserId(self):
		return self.get_query_params().get('SubUserId')

	def set_SubUserId(self,SubUserId):
		self.add_query_param('SubUserId',SubUserId)

	def get_AccessToken(self):
		return self.get_query_params().get('AccessToken')

	def set_AccessToken(self,AccessToken):
		self.add_query_param('AccessToken',AccessToken)

	def get_Sync(self):
		return self.get_query_params().get('Sync')

	def set_Sync(self,Sync):
		self.add_query_param('Sync',Sync)

	def get_CreateParentPath(self):
		return self.get_query_params().get('CreateParentPath')

	def set_CreateParentPath(self,CreateParentPath):
		self.add_query_param('CreateParentPath',CreateParentPath)