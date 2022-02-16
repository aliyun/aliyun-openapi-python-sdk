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

class CreateOnAckClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2021-03-20', 'CreateOnAckCluster','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_AckNodePools(self):
		return self.get_query_params().get('AckNodePools')

	def set_AckNodePools(self,AckNodePools):
		self.add_query_param('AckNodePools',AckNodePools)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_OssPath(self):
		return self.get_query_params().get('OssPath')

	def set_OssPath(self,OssPath):
		self.add_query_param('OssPath',OssPath)

	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_AckClusterId(self):
		return self.get_query_params().get('AckClusterId')

	def set_AckClusterId(self,AckClusterId):
		self.add_query_param('AckClusterId',AckClusterId)

	def get_AckNamespace(self):
		return self.get_query_params().get('AckNamespace')

	def set_AckNamespace(self,AckNamespace):
		self.add_query_param('AckNamespace',AckNamespace)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_AckNodes(self):
		return self.get_query_params().get('AckNodes')

	def set_AckNodes(self,AckNodes):
		self.add_query_param('AckNodes',AckNodes)

	def get_ProductRoleName(self):
		return self.get_query_params().get('ProductRoleName')

	def set_ProductRoleName(self,ProductRoleName):
		self.add_query_param('ProductRoleName',ProductRoleName)

	def get_Applications(self):
		return self.get_query_params().get('Applications')

	def set_Applications(self,Applications):
		self.add_query_param('Applications',Applications)