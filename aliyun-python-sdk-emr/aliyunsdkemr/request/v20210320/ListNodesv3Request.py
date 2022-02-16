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

class ListNodesv3Request(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2021-03-20', 'ListNodesv3','emr')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NodeNames(self):
		return self.get_query_params().get('NodeNames')

	def set_NodeNames(self,NodeNames):
		self.add_query_param('NodeNames',NodeNames)

	def get_PublicIp(self):
		return self.get_query_params().get('PublicIp')

	def set_PublicIp(self,PublicIp):
		self.add_query_param('PublicIp',PublicIp)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_PrivateIp(self):
		return self.get_query_params().get('PrivateIp')

	def set_PrivateIp(self,PrivateIp):
		self.add_query_param('PrivateIp',PrivateIp)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_NodeGroupId(self):
		return self.get_query_params().get('NodeGroupId')

	def set_NodeGroupId(self,NodeGroupId):
		self.add_query_param('NodeGroupId',NodeGroupId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_NodeIds(self):
		return self.get_query_params().get('NodeIds')

	def set_NodeIds(self,NodeIds):
		self.add_query_param('NodeIds',NodeIds)