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
from aliyunsdkedas.endpoint import endpoint_data

class GetK8sClusterRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'GetK8sCluster','Edas')
		self.set_uri_pattern('/pop/v5/k8s_clusters')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClusterType(self): # Integer
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self, ClusterType):  # Integer
		self.add_query_param('ClusterType', ClusterType)
	def get_RegionTag(self): # String
		return self.get_query_params().get('RegionTag')

	def set_RegionTag(self, RegionTag):  # String
		self.add_query_param('RegionTag', RegionTag)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_SubClusterType(self): # String
		return self.get_query_params().get('SubClusterType')

	def set_SubClusterType(self, SubClusterType):  # String
		self.add_query_param('SubClusterType', SubClusterType)
