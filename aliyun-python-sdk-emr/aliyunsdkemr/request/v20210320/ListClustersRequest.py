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

class ListClustersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2021-03-20', 'ListClusters','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_IaasTypes(self):
		return self.get_query_params().get('IaasTypes')

	def set_IaasTypes(self,IaasTypes):
		self.add_query_param('IaasTypes',IaasTypes)

	def get_ClusterIds(self):
		return self.get_query_params().get('ClusterIds')

	def set_ClusterIds(self,ClusterIds):
		self.add_query_param('ClusterIds',ClusterIds)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_ClusterStates(self):
		return self.get_query_params().get('ClusterStates')

	def set_ClusterStates(self,ClusterStates):
		self.add_query_param('ClusterStates',ClusterStates)

	def get_PaymentTypes(self):
		return self.get_query_params().get('PaymentTypes')

	def set_PaymentTypes(self,PaymentTypes):
		self.add_query_param('PaymentTypes',PaymentTypes)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_ClusterTypes(self):
		return self.get_query_params().get('ClusterTypes')

	def set_ClusterTypes(self,ClusterTypes):
		self.add_query_param('ClusterTypes',ClusterTypes)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_PaymentStatuses(self):
		return self.get_query_params().get('PaymentStatuses')

	def set_PaymentStatuses(self,PaymentStatuses):
		self.add_query_param('PaymentStatuses',PaymentStatuses)