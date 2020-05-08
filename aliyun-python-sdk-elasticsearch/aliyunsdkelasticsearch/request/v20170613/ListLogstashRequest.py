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
from aliyunsdkelasticsearch.endpoint import endpoint_data

class ListLogstashRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'ListLogstash','elasticsearch')
		self.set_uri_pattern('/openapi/logstashes')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_resourceGroupId(self):
		return self.get_query_params().get('resourceGroupId')

	def set_resourceGroupId(self,resourceGroupId):
		self.add_query_param('resourceGroupId',resourceGroupId)

	def get_instanceId(self):
		return self.get_query_params().get('instanceId')

	def set_instanceId(self,instanceId):
		self.add_query_param('instanceId',instanceId)

	def get_size(self):
		return self.get_query_params().get('size')

	def set_size(self,size):
		self.add_query_param('size',size)

	def get_description(self):
		return self.get_query_params().get('description')

	def set_description(self,description):
		self.add_query_param('description',description)

	def get_page(self):
		return self.get_query_params().get('page')

	def set_page(self,page):
		self.add_query_param('page',page)

	def get_ownerId(self):
		return self.get_query_params().get('ownerId')

	def set_ownerId(self,ownerId):
		self.add_query_param('ownerId',ownerId)

	def get_version(self):
		return self.get_query_params().get('version')

	def set_version(self,version):
		self.add_query_param('version',version)