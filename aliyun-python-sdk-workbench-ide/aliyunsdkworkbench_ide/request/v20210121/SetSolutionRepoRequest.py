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

class SetSolutionRepoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Workbench-ide', '2021-01-21', 'SetSolutionRepo')
		self.set_method('POST')

	def get_RepoCloneUrl(self):
		return self.get_query_params().get('RepoCloneUrl')

	def set_RepoCloneUrl(self,RepoCloneUrl):
		self.add_query_param('RepoCloneUrl',RepoCloneUrl)

	def get_RepoCloneAccount(self):
		return self.get_query_params().get('RepoCloneAccount')

	def set_RepoCloneAccount(self,RepoCloneAccount):
		self.add_query_param('RepoCloneAccount',RepoCloneAccount)

	def get_CurrentOrgId(self):
		return self.get_query_params().get('CurrentOrgId')

	def set_CurrentOrgId(self,CurrentOrgId):
		self.add_query_param('CurrentOrgId',CurrentOrgId)

	def get_SolutionId(self):
		return self.get_query_params().get('SolutionId')

	def set_SolutionId(self,SolutionId):
		self.add_query_param('SolutionId',SolutionId)

	def get_RepoAccessToken(self):
		return self.get_query_params().get('RepoAccessToken')

	def set_RepoAccessToken(self,RepoAccessToken):
		self.add_query_param('RepoAccessToken',RepoAccessToken)