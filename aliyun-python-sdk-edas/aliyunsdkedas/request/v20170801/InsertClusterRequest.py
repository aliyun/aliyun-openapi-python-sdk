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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class InsertClusterRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'InsertCluster','Edas')
		self.set_uri_pattern('/pop/v5/resource/cluster')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_IaasProvider(self):
		return self.get_query_params().get('IaasProvider')

	def set_IaasProvider(self,IaasProvider):
		self.add_query_param('IaasProvider',IaasProvider)

	def get_LogicalRegionId(self):
		return self.get_query_params().get('LogicalRegionId')

	def set_LogicalRegionId(self,LogicalRegionId):
		self.add_query_param('LogicalRegionId',LogicalRegionId)

	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_NetworkMode(self):
		return self.get_query_params().get('NetworkMode')

	def set_NetworkMode(self,NetworkMode):
		self.add_query_param('NetworkMode',NetworkMode)

	def get_OversoldFactor(self):
		return self.get_query_params().get('OversoldFactor')

	def set_OversoldFactor(self,OversoldFactor):
		self.add_query_param('OversoldFactor',OversoldFactor)