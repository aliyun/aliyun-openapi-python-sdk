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
from aliyunsdksas.endpoint import endpoint_data

class DescribeImageListWithBaselineNameRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeImageListWithBaselineName')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Criteria(self):
		return self.get_query_params().get('Criteria')

	def set_Criteria(self,Criteria):
		self.add_query_param('Criteria',Criteria)

	def get_RepoNamespace(self):
		return self.get_query_params().get('RepoNamespace')

	def set_RepoNamespace(self,RepoNamespace):
		self.add_query_param('RepoNamespace',RepoNamespace)

	def get_ImageDigest(self):
		return self.get_query_params().get('ImageDigest')

	def set_ImageDigest(self,ImageDigest):
		self.add_query_param('ImageDigest',ImageDigest)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CriteriaType(self):
		return self.get_query_params().get('CriteriaType')

	def set_CriteriaType(self,CriteriaType):
		self.add_query_param('CriteriaType',CriteriaType)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_RepoName(self):
		return self.get_query_params().get('RepoName')

	def set_RepoName(self,RepoName):
		self.add_query_param('RepoName',RepoName)

	def get_BaselineNameKey(self):
		return self.get_query_params().get('BaselineNameKey')

	def set_BaselineNameKey(self,BaselineNameKey):
		self.add_query_param('BaselineNameKey',BaselineNameKey)

	def get_RepoInstanceId(self):
		return self.get_query_params().get('RepoInstanceId')

	def set_RepoInstanceId(self,RepoInstanceId):
		self.add_query_param('RepoInstanceId',RepoInstanceId)