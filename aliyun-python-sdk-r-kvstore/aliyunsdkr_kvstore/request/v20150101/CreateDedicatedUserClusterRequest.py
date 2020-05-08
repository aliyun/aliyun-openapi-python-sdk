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
from aliyunsdkr_kvstore.endpoint import endpoint_data

class CreateDedicatedUserClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'R-kvstore', '2015-01-01', 'CreateDedicatedUserCluster','redisa')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_DiskOverAllocationRatio(self):
		return self.get_query_params().get('DiskOverAllocationRatio')

	def set_DiskOverAllocationRatio(self,DiskOverAllocationRatio):
		self.add_query_param('DiskOverAllocationRatio',DiskOverAllocationRatio)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_MemoryOverAllocationRatio(self):
		return self.get_query_params().get('MemoryOverAllocationRatio')

	def set_MemoryOverAllocationRatio(self,MemoryOverAllocationRatio):
		self.add_query_param('MemoryOverAllocationRatio',MemoryOverAllocationRatio)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_HostReplacePolicy(self):
		return self.get_query_params().get('HostReplacePolicy')

	def set_HostReplacePolicy(self,HostReplacePolicy):
		self.add_query_param('HostReplacePolicy',HostReplacePolicy)

	def get_AllocationPolicy(self):
		return self.get_query_params().get('AllocationPolicy')

	def set_AllocationPolicy(self,AllocationPolicy):
		self.add_query_param('AllocationPolicy',AllocationPolicy)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_CpuOverAllocationRatio(self):
		return self.get_query_params().get('CpuOverAllocationRatio')

	def set_CpuOverAllocationRatio(self,CpuOverAllocationRatio):
		self.add_query_param('CpuOverAllocationRatio',CpuOverAllocationRatio)