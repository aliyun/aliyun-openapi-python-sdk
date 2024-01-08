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
from aliyunsdkresourcesharing.endpoint import endpoint_data

class ListSharedResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceSharing', '2020-01-10', 'ListSharedResources','ressharing')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ResourceShareIdss(self): # RepeatList
		return self.get_query_params().get('ResourceShareIds')

	def set_ResourceShareIdss(self, ResourceShareIds):  # RepeatList
		for depth1 in range(len(ResourceShareIds)):
			self.add_query_param('ResourceShareIds.' + str(depth1 + 1), ResourceShareIds[depth1])
	def get_ResourceOwner(self): # String
		return self.get_query_params().get('ResourceOwner')

	def set_ResourceOwner(self, ResourceOwner):  # String
		self.add_query_param('ResourceOwner', ResourceOwner)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_Target(self): # String
		return self.get_query_params().get('Target')

	def set_Target(self, Target):  # String
		self.add_query_param('Target', Target)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_ResourceIdss(self): # RepeatList
		return self.get_query_params().get('ResourceIds')

	def set_ResourceIdss(self, ResourceIds):  # RepeatList
		for depth1 in range(len(ResourceIds)):
			self.add_query_param('ResourceIds.' + str(depth1 + 1), ResourceIds[depth1])
