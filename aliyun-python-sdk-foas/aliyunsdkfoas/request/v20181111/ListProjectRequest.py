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
from aliyunsdkfoas.endpoint import endpoint_data

class ListProjectRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'foas', '2018-11-11', 'ListProject','foas')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v2/projects')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_name(self):
		return self.get_query_params().get('name')

	def set_name(self,name):
		self.add_query_param('name',name)

	def get_pageSize(self):
		return self.get_query_params().get('pageSize')

	def set_pageSize(self,pageSize):
		self.add_query_param('pageSize',pageSize)

	def get_pageIndex(self):
		return self.get_query_params().get('pageIndex')

	def set_pageIndex(self,pageIndex):
		self.add_query_param('pageIndex',pageIndex)

	def get_clusterId(self):
		return self.get_query_params().get('clusterId')

	def set_clusterId(self,clusterId):
		self.add_query_param('clusterId',clusterId)

	def get_region(self):
		return self.get_query_params().get('region')

	def set_region(self,region):
		self.add_query_param('region',region)

	def get_deployType(self):
		return self.get_query_params().get('deployType')

	def set_deployType(self,deployType):
		self.add_query_param('deployType',deployType)