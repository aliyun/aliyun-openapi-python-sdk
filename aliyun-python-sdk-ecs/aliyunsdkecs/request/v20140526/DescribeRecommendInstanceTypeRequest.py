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

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Memory(self): # Float
		return self.get_query_params().get('Memory')

	def set_Memory(self, Memory):  # Float
		self.add_query_param('Memory', Memory)
	def get_IoOptimized(self): # String
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self, IoOptimized):  # String
		self.add_query_param('IoOptimized', IoOptimized)
	def get_NetworkType(self): # String
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self, NetworkType):  # String
		self.add_query_param('NetworkType', NetworkType)
	def get_Scene(self): # String
		return self.get_query_params().get('Scene')

	def set_Scene(self, Scene):  # String
		self.add_query_param('Scene', Scene)
	def get_Cores(self): # Integer
		return self.get_query_params().get('Cores')

	def set_Cores(self, Cores):  # Integer
		self.add_query_param('Cores', Cores)
	def get_SystemDiskCategory(self): # String
		return self.get_query_params().get('SystemDiskCategory')

	def set_SystemDiskCategory(self, SystemDiskCategory):  # String
		self.add_query_param('SystemDiskCategory', SystemDiskCategory)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_MaxPrice(self): # Float
		return self.get_query_params().get('MaxPrice')

	def set_MaxPrice(self, MaxPrice):  # Float
		self.add_query_param('MaxPrice', MaxPrice)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_ZoneMatchMode(self): # String
		return self.get_query_params().get('ZoneMatchMode')

	def set_ZoneMatchMode(self, ZoneMatchMode):  # String
		self.add_query_param('ZoneMatchMode', ZoneMatchMode)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_InstanceTypeFamilys(self): # RepeatList
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamilys(self, InstanceTypeFamily):  # RepeatList
		for depth1 in range(len(InstanceTypeFamily)):
			self.add_query_param('InstanceTypeFamily.' + str(depth1 + 1), InstanceTypeFamily[depth1])
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_PriorityStrategy(self): # String
		return self.get_query_params().get('PriorityStrategy')

	def set_PriorityStrategy(self, PriorityStrategy):  # String
		self.add_query_param('PriorityStrategy', PriorityStrategy)
	def get_InstanceFamilyLevel(self): # String
		return self.get_query_params().get('InstanceFamilyLevel')

	def set_InstanceFamilyLevel(self, InstanceFamilyLevel):  # String
		self.add_query_param('InstanceFamilyLevel', InstanceFamilyLevel)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
