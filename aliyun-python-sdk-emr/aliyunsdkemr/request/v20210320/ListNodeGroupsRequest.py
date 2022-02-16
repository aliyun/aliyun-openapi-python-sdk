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

class ListNodeGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2021-03-20', 'ListNodeGroups','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NodeGroupIds(self):
		return self.get_query_params().get('NodeGroupIds')

	def set_NodeGroupIds(self,NodeGroupIds):
		self.add_query_param('NodeGroupIds',NodeGroupIds)

	def get_NodeGroupTypes(self):
		return self.get_query_params().get('NodeGroupTypes')

	def set_NodeGroupTypes(self,NodeGroupTypes):
		self.add_query_param('NodeGroupTypes',NodeGroupTypes)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_NodeGroupStatuses(self):
		return self.get_query_params().get('NodeGroupStatuses')

	def set_NodeGroupStatuses(self,NodeGroupStatuses):
		self.add_query_param('NodeGroupStatuses',NodeGroupStatuses)

	def get_NodeGroupNames(self):
		return self.get_query_params().get('NodeGroupNames')

	def set_NodeGroupNames(self,NodeGroupNames):
		self.add_query_param('NodeGroupNames',NodeGroupNames)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_Statuses(self):
		return self.get_query_params().get('Statuses')

	def set_Statuses(self,Statuses):
		self.add_query_param('Statuses',Statuses)