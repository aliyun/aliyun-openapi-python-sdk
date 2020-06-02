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

class GetRepoBuildListRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'cr', '2016-06-07', 'GetRepoBuildList','acr')
		self.set_uri_pattern('/repos/[RepoNamespace]/[RepoName]/build')
		self.set_method('GET')

	def get_RepoNamespace(self):
		return self.get_path_params().get('RepoNamespace')

	def set_RepoNamespace(self,RepoNamespace):
		self.add_path_param('RepoNamespace',RepoNamespace)

	def get_RepoName(self):
		return self.get_path_params().get('RepoName')

	def set_RepoName(self,RepoName):
		self.add_path_param('RepoName',RepoName)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Page(self):
		return self.get_query_params().get('Page')

	def set_Page(self,Page):
		self.add_query_param('Page',Page)