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
from aliyunsdkcomputenest.endpoint import endpoint_data

class ListServiceInstanceResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ComputeNest', '2021-06-01', 'ListServiceInstanceResources','computenest')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ExpireTimeEnd(self): # String
		return self.get_query_params().get('ExpireTimeEnd')

	def set_ExpireTimeEnd(self, ExpireTimeEnd):  # String
		self.add_query_param('ExpireTimeEnd', ExpireTimeEnd)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ServiceInstanceResourceType(self): # String
		return self.get_query_params().get('ServiceInstanceResourceType')

	def set_ServiceInstanceResourceType(self, ServiceInstanceResourceType):  # String
		self.add_query_param('ServiceInstanceResourceType', ServiceInstanceResourceType)
	def get_ResourceARNs(self): # RepeatList
		return self.get_query_params().get('ResourceARN')

	def set_ResourceARNs(self, ResourceARN):  # RepeatList
		for depth1 in range(len(ResourceARN)):
			self.add_query_param('ResourceARN.' + str(depth1 + 1), ResourceARN[depth1])
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_ServiceInstanceId(self): # String
		return self.get_query_params().get('ServiceInstanceId')

	def set_ServiceInstanceId(self, ServiceInstanceId):  # String
		self.add_query_param('ServiceInstanceId', ServiceInstanceId)
	def get_ExpireTimeStart(self): # String
		return self.get_query_params().get('ExpireTimeStart')

	def set_ExpireTimeStart(self, ExpireTimeStart):  # String
		self.add_query_param('ExpireTimeStart', ExpireTimeStart)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
