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
from aliyunsdkconfig.endpoint import endpoint_data

class ListDiscoveredResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Config', '2020-09-07', 'ListDiscoveredResources')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceDeleted(self): # Integer
		return self.get_query_params().get('ResourceDeleted')

	def set_ResourceDeleted(self, ResourceDeleted):  # Integer
		self.add_query_param('ResourceDeleted', ResourceDeleted)
	def get_ResourceId(self): # String
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_query_param('ResourceId', ResourceId)
	def get_Regions(self): # String
		return self.get_query_params().get('Regions')

	def set_Regions(self, Regions):  # String
		self.add_query_param('Regions', Regions)
	def get_ResourceTypes(self): # String
		return self.get_query_params().get('ResourceTypes')

	def set_ResourceTypes(self, ResourceTypes):  # String
		self.add_query_param('ResourceTypes', ResourceTypes)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
