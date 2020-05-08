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
from aliyunsdkemr.endpoint import endpoint_data

class UpdateWorkspaceRepoSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'UpdateWorkspaceRepoSetting','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RepoMavens(self):
		return self.get_query_params().get('RepoMavens')

	def set_RepoMavens(self,RepoMavens):
		for i in range(len(RepoMavens)):	
			if RepoMavens[i].get('GroupId') is not None:
				self.add_query_param('RepoMaven.' + str(i + 1) + '.GroupId' , RepoMavens[i].get('GroupId'))
			if RepoMavens[i].get('ArtifactId') is not None:
				self.add_query_param('RepoMaven.' + str(i + 1) + '.ArtifactId' , RepoMavens[i].get('ArtifactId'))
			if RepoMavens[i].get('Version') is not None:
				self.add_query_param('RepoMaven.' + str(i + 1) + '.Version' , RepoMavens[i].get('Version'))


	def get_RepoPips(self):
		return self.get_query_params().get('RepoPips')

	def set_RepoPips(self,RepoPips):
		for i in range(len(RepoPips)):	
			if RepoPips[i].get('PackageName') is not None:
				self.add_query_param('RepoPip.' + str(i + 1) + '.PackageName' , RepoPips[i].get('PackageName'))
			if RepoPips[i].get('Version') is not None:
				self.add_query_param('RepoPip.' + str(i + 1) + '.Version' , RepoPips[i].get('Version'))


	def get_WorkspaceId(self):
		return self.get_query_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_query_param('WorkspaceId',WorkspaceId)