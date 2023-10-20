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
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeImageListWithBaselineName','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Pod(self): # String
		return self.get_query_params().get('Pod')

	def set_Pod(self, Pod):  # String
		self.add_query_param('Pod', Pod)
	def get_ClusterName(self): # String
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self, ClusterName):  # String
		self.add_query_param('ClusterName', ClusterName)
	def get_Criteria(self): # String
		return self.get_query_params().get('Criteria')

	def set_Criteria(self, Criteria):  # String
		self.add_query_param('Criteria', Criteria)
	def get_RepoNamespace(self): # String
		return self.get_query_params().get('RepoNamespace')

	def set_RepoNamespace(self, RepoNamespace):  # String
		self.add_query_param('RepoNamespace', RepoNamespace)
	def get_ImageDigest(self): # String
		return self.get_query_params().get('ImageDigest')

	def set_ImageDigest(self, ImageDigest):  # String
		self.add_query_param('ImageDigest', ImageDigest)
	def get_ScanRanges(self): # RepeatList
		return self.get_query_params().get('ScanRange')

	def set_ScanRanges(self, ScanRange):  # RepeatList
		for depth1 in range(len(ScanRange)):
			self.add_query_param('ScanRange.' + str(depth1 + 1), ScanRange[depth1])
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_CriteriaType(self): # String
		return self.get_query_params().get('CriteriaType')

	def set_CriteriaType(self, CriteriaType):  # String
		self.add_query_param('CriteriaType', CriteriaType)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Image(self): # String
		return self.get_query_params().get('Image')

	def set_Image(self, Image):  # String
		self.add_query_param('Image', Image)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_RepoName(self): # String
		return self.get_query_params().get('RepoName')

	def set_RepoName(self, RepoName):  # String
		self.add_query_param('RepoName', RepoName)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_BaselineNameKey(self): # String
		return self.get_query_params().get('BaselineNameKey')

	def set_BaselineNameKey(self, BaselineNameKey):  # String
		self.add_query_param('BaselineNameKey', BaselineNameKey)
	def get_RepoInstanceId(self): # String
		return self.get_query_params().get('RepoInstanceId')

	def set_RepoInstanceId(self, RepoInstanceId):  # String
		self.add_query_param('RepoInstanceId', RepoInstanceId)
	def get_ContainerId(self): # String
		return self.get_query_params().get('ContainerId')

	def set_ContainerId(self, ContainerId):  # String
		self.add_query_param('ContainerId', ContainerId)
