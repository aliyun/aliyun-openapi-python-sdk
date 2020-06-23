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
from aliyunsdkcs.endpoint import endpoint_data

class ListTagResourcesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'CS', '2015-12-15', 'ListTagResources')
		self.set_uri_pattern('/tags')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_resource_type(self):
		return self.get_query_params().get('resource_type')

	def set_resource_type(self,resource_type):
		self.add_query_param('resource_type',resource_type)

	def get_next_token(self):
		return self.get_query_params().get('next_token')

	def set_next_token(self,next_token):
		self.add_query_param('next_token',next_token)

	def get_resource_ids(self):
		return self.get_query_params().get('resource_ids')

	def set_resource_ids(self,resource_ids):
		self.add_query_param('resource_ids',resource_ids)

	def get_tags(self):
		return self.get_query_params().get('tags')

	def set_tags(self,tags):
		self.add_query_param('tags',tags)