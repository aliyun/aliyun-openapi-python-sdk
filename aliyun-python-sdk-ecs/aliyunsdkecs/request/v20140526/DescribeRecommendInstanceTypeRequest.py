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

class DescribeRecommendInstanceTypeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeRecommendInstanceType','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Memory(self):
		return self.get_query_params().get('Memory')

	def set_Memory(self,Memory):
		self.add_query_param('Memory',Memory)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_NetworkType(self):
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_query_param('NetworkType',NetworkType)

	def get_Scene(self):
		return self.get_query_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_query_param('Scene',Scene)

	def get_Cores(self):
		return self.get_query_params().get('Cores')

	def set_Cores(self,Cores):
		self.add_query_param('Cores',Cores)

	def get_SystemDiskCategory(self):
		return self.get_query_params().get('SystemDiskCategory')

	def set_SystemDiskCategory(self,SystemDiskCategory):
		self.add_query_param('SystemDiskCategory',SystemDiskCategory)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_MaxPrice(self):
		return self.get_query_params().get('MaxPrice')

	def set_MaxPrice(self,MaxPrice):
		self.add_query_param('MaxPrice',MaxPrice)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_InstanceTypeFamilys(self):
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamilys(self, InstanceTypeFamilys):
		for depth1 in range(len(InstanceTypeFamilys)):
			if InstanceTypeFamilys[depth1] is not None:
				self.add_query_param('InstanceTypeFamily.' + str(depth1 + 1) , InstanceTypeFamilys[depth1])

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SpotStrategy(self):
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self,SpotStrategy):
		self.add_query_param('SpotStrategy',SpotStrategy)

	def get_PriorityStrategy(self):
		return self.get_query_params().get('PriorityStrategy')

	def set_PriorityStrategy(self,PriorityStrategy):
		self.add_query_param('PriorityStrategy',PriorityStrategy)

	def get_InstanceFamilyLevel(self):
		return self.get_query_params().get('InstanceFamilyLevel')

	def set_InstanceFamilyLevel(self,InstanceFamilyLevel):
		self.add_query_param('InstanceFamilyLevel',InstanceFamilyLevel)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)