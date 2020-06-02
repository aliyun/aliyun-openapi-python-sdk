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

class ListRepoSyncRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cr', '2018-12-01', 'ListRepoSyncRule','acr')
		self.set_method('POST')

	def get_NamespaceName(self):
		return self.get_query_params().get('NamespaceName')

	def set_NamespaceName(self,NamespaceName):
		self.add_query_param('NamespaceName',NamespaceName)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_TargetInstanceId(self):
		return self.get_query_params().get('TargetInstanceId')

	def set_TargetInstanceId(self,TargetInstanceId):
		self.add_query_param('TargetInstanceId',TargetInstanceId)

	def get_RepoName(self):
		return self.get_query_params().get('RepoName')

	def set_RepoName(self,RepoName):
		self.add_query_param('RepoName',RepoName)

	def get_PageNo(self):
		return self.get_query_params().get('PageNo')

	def set_PageNo(self,PageNo):
		self.add_query_param('PageNo',PageNo)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_TargetRegionId(self):
		return self.get_query_params().get('TargetRegionId')

	def set_TargetRegionId(self,TargetRegionId):
		self.add_query_param('TargetRegionId',TargetRegionId)