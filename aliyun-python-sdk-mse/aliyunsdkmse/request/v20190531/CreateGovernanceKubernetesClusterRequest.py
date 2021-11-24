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
from aliyunsdkmse.endpoint import endpoint_data

class CreateGovernanceKubernetesClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'CreateGovernanceKubernetesCluster')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClusterName(self): # String
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self, ClusterName):  # String
		self.add_query_param('ClusterName', ClusterName)
	def get_NameSpaceInfos(self): # String
		return self.get_query_params().get('NameSpaceInfos')

	def set_NameSpaceInfos(self, NameSpaceInfos):  # String
		self.add_query_param('NameSpaceInfos', NameSpaceInfos)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_K8sVersion(self): # String
		return self.get_query_params().get('K8sVersion')

	def set_K8sVersion(self, K8sVersion):  # String
		self.add_query_param('K8sVersion', K8sVersion)
	def get_PilotStartTime(self): # Long
		return self.get_query_params().get('PilotStartTime')

	def set_PilotStartTime(self, PilotStartTime):  # Long
		self.add_query_param('PilotStartTime', PilotStartTime)
