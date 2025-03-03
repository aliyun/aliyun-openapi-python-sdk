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
from aliyunsdkresourcemanager.endpoint import endpoint_data

class UntagResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'UntagResources','resourcemanager')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_All(self): # Boolean
		return self.get_query_params().get('All')

	def set_All(self, All):  # Boolean
		self.add_query_param('All', All)
	def get_ResourceId(self): # Array
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # Array
		for index1, value1 in enumerate(ResourceId):
			self.add_query_param('ResourceId.' + str(index1 + 1), value1)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_TagKey(self): # Array
		return self.get_query_params().get('TagKey')

	def set_TagKey(self, TagKey):  # Array
		for index1, value1 in enumerate(TagKey):
			self.add_query_param('TagKey.' + str(index1 + 1), value1)
