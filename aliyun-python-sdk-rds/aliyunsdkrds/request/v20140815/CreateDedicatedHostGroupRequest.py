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
from aliyunsdkrds.endpoint import endpoint_data

class CreateDedicatedHostGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateDedicatedHostGroup','rds')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_CpuAllocationRatio(self):
		return self.get_query_params().get('CpuAllocationRatio')

	def set_CpuAllocationRatio(self,CpuAllocationRatio):
		self.add_query_param('CpuAllocationRatio',CpuAllocationRatio)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Engine(self):
		return self.get_query_params().get('Engine')

	def set_Engine(self,Engine):
		self.add_query_param('Engine',Engine)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_DiskAllocationRatio(self):
		return self.get_query_params().get('DiskAllocationRatio')

	def set_DiskAllocationRatio(self,DiskAllocationRatio):
		self.add_query_param('DiskAllocationRatio',DiskAllocationRatio)

	def get_MemAllocationRatio(self):
		return self.get_query_params().get('MemAllocationRatio')

	def set_MemAllocationRatio(self,MemAllocationRatio):
		self.add_query_param('MemAllocationRatio',MemAllocationRatio)

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

	def get_VPCId(self):
		return self.get_query_params().get('VPCId')

	def set_VPCId(self,VPCId):
		self.add_query_param('VPCId',VPCId)