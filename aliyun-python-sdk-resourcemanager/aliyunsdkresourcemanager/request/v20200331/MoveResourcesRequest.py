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

class MoveResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'MoveResources')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Resources(self): # Array
		return self.get_query_params().get('Resources')

	def set_Resources(self, Resources):  # Array
		for index1, value1 in enumerate(Resources):
			if value1.get('ResourceId') is not None:
				self.add_query_param('Resources.' + str(index1 + 1) + '.ResourceId', value1.get('ResourceId'))
			if value1.get('RegionId') is not None:
				self.add_query_param('Resources.' + str(index1 + 1) + '.RegionId', value1.get('RegionId'))
			if value1.get('Service') is not None:
				self.add_query_param('Resources.' + str(index1 + 1) + '.Service', value1.get('Service'))
			if value1.get('ResourceType') is not None:
				self.add_query_param('Resources.' + str(index1 + 1) + '.ResourceType', value1.get('ResourceType'))
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
