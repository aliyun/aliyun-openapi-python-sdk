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

class GetFileBlobsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'codeup', '2020-04-14', 'GetFileBlobs')
		self.set_uri_pattern('/api/v4/projects/[ProjectId]/repository/blobs')
		self.set_method('GET')

	def get_AccessToken(self):
		return self.get_query_params().get('AccessToken')

	def set_AccessToken(self,AccessToken):
		self.add_query_param('AccessToken',AccessToken)

	def get_OrganizationId(self):
		return self.get_query_params().get('OrganizationId')

	def set_OrganizationId(self,OrganizationId):
		self.add_query_param('OrganizationId',OrganizationId)

	def get_Ref(self):
		return self.get_query_params().get('Ref')

	def set_Ref(self,Ref):
		self.add_query_param('Ref',Ref)

	def get_SubUserId(self):
		return self.get_query_params().get('SubUserId')

	def set_SubUserId(self,SubUserId):
		self.add_query_param('SubUserId',SubUserId)

	def get_FilePath(self):
		return self.get_query_params().get('FilePath')

	def set_FilePath(self,FilePath):
		self.add_query_param('FilePath',FilePath)

	def get_From(self):
		return self.get_query_params().get('From')

	def set_From(self,_From):
		self.add_query_param('From',_From)

	def get_To(self):
		return self.get_query_params().get('To')

	def set_To(self,To):
		self.add_query_param('To',To)

	def get_ProjectId(self):
		return self.get_path_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_path_param('ProjectId',ProjectId)