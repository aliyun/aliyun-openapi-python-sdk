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

class ListMetaDataSourceClusterForOuterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ListMetaDataSourceClusterForOuter','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterIds(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterIds(self, ClusterIds):
		for depth1 in range(len(ClusterIds)):
			if ClusterIds[depth1] is not None:
				self.add_query_param('ClusterId.' + str(depth1 + 1) , ClusterIds[depth1])

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_DataSourceIds(self):
		return self.get_query_params().get('DataSourceId')

	def set_DataSourceIds(self, DataSourceIds):
		for depth1 in range(len(DataSourceIds)):
			if DataSourceIds[depth1] is not None:
				self.add_query_param('DataSourceId.' + str(depth1 + 1) , DataSourceIds[depth1])

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)