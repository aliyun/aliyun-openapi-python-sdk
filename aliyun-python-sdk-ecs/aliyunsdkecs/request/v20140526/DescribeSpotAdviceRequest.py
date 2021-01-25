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
from aliyunsdkecs.endpoint import endpoint_data

class DescribeSpotAdviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeSpotAdvice','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_GpuSpec(self):
		return self.get_query_params().get('GpuSpec')

	def set_GpuSpec(self,GpuSpec):
		self.add_query_param('GpuSpec',GpuSpec)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Memory(self):
		return self.get_query_params().get('Memory')

	def set_Memory(self,Memory):
		self.add_query_param('Memory',Memory)

	def get_InstanceTypess(self):
		return self.get_query_params().get('InstanceTypes')

	def set_InstanceTypess(self, InstanceTypess):
		for depth1 in range(len(InstanceTypess)):
			if InstanceTypess[depth1] is not None:
				self.add_query_param('InstanceTypes.' + str(depth1 + 1) , InstanceTypess[depth1])

	def get_MinCores(self):
		return self.get_query_params().get('MinCores')

	def set_MinCores(self,MinCores):
		self.add_query_param('MinCores',MinCores)

	def get_Cores(self):
		return self.get_query_params().get('Cores')

	def set_Cores(self,Cores):
		self.add_query_param('Cores',Cores)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_InstanceTypeFamily(self):
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamily(self,InstanceTypeFamily):
		self.add_query_param('InstanceTypeFamily',InstanceTypeFamily)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InstanceFamilyLevel(self):
		return self.get_query_params().get('InstanceFamilyLevel')

	def set_InstanceFamilyLevel(self,InstanceFamilyLevel):
		self.add_query_param('InstanceFamilyLevel',InstanceFamilyLevel)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_GpuAmount(self):
		return self.get_query_params().get('GpuAmount')

	def set_GpuAmount(self,GpuAmount):
		self.add_query_param('GpuAmount',GpuAmount)

	def get_MinMemory(self):
		return self.get_query_params().get('MinMemory')

	def set_MinMemory(self,MinMemory):
		self.add_query_param('MinMemory',MinMemory)