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

class CreateAutoProvisioningGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateAutoProvisioningGroup','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_AutoProvisioningGroupType(self):
		return self.get_query_params().get('AutoProvisioningGroupType')

	def set_AutoProvisioningGroupType(self,AutoProvisioningGroupType):
		self.add_query_param('AutoProvisioningGroupType',AutoProvisioningGroupType)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_TerminateInstancesWithExpiration(self):
		return self.get_query_params().get('TerminateInstancesWithExpiration')

	def set_TerminateInstancesWithExpiration(self,TerminateInstancesWithExpiration):
		self.add_query_param('TerminateInstancesWithExpiration',TerminateInstancesWithExpiration)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_SpotAllocationStrategy(self):
		return self.get_query_params().get('SpotAllocationStrategy')

	def set_SpotAllocationStrategy(self,SpotAllocationStrategy):
		self.add_query_param('SpotAllocationStrategy',SpotAllocationStrategy)

	def get_TerminateInstances(self):
		return self.get_query_params().get('TerminateInstances')

	def set_TerminateInstances(self,TerminateInstances):
		self.add_query_param('TerminateInstances',TerminateInstances)

	def get_PayAsYouGoAllocationStrategy(self):
		return self.get_query_params().get('PayAsYouGoAllocationStrategy')

	def set_PayAsYouGoAllocationStrategy(self,PayAsYouGoAllocationStrategy):
		self.add_query_param('PayAsYouGoAllocationStrategy',PayAsYouGoAllocationStrategy)

	def get_DefaultTargetCapacityType(self):
		return self.get_query_params().get('DefaultTargetCapacityType')

	def set_DefaultTargetCapacityType(self,DefaultTargetCapacityType):
		self.add_query_param('DefaultTargetCapacityType',DefaultTargetCapacityType)

	def get_ExcessCapacityTerminationPolicy(self):
		return self.get_query_params().get('ExcessCapacityTerminationPolicy')

	def set_ExcessCapacityTerminationPolicy(self,ExcessCapacityTerminationPolicy):
		self.add_query_param('ExcessCapacityTerminationPolicy',ExcessCapacityTerminationPolicy)

	def get_LaunchTemplateConfigs(self):
		return self.get_query_params().get('LaunchTemplateConfigs')

	def set_LaunchTemplateConfigs(self, LaunchTemplateConfigs):
		for depth1 in range(len(LaunchTemplateConfigs)):
			if LaunchTemplateConfigs[depth1].get('InstanceType') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.InstanceType', LaunchTemplateConfigs[depth1].get('InstanceType'))
			if LaunchTemplateConfigs[depth1].get('MaxPrice') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.MaxPrice', LaunchTemplateConfigs[depth1].get('MaxPrice'))
			if LaunchTemplateConfigs[depth1].get('VSwitchId') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.VSwitchId', LaunchTemplateConfigs[depth1].get('VSwitchId'))
			if LaunchTemplateConfigs[depth1].get('WeightedCapacity') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.WeightedCapacity', LaunchTemplateConfigs[depth1].get('WeightedCapacity'))
			if LaunchTemplateConfigs[depth1].get('Priority') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.Priority', LaunchTemplateConfigs[depth1].get('Priority'))

	def get_ValidUntil(self):
		return self.get_query_params().get('ValidUntil')

	def set_ValidUntil(self,ValidUntil):
		self.add_query_param('ValidUntil',ValidUntil)

	def get_SpotInstanceInterruptionBehavior(self):
		return self.get_query_params().get('SpotInstanceInterruptionBehavior')

	def set_SpotInstanceInterruptionBehavior(self,SpotInstanceInterruptionBehavior):
		self.add_query_param('SpotInstanceInterruptionBehavior',SpotInstanceInterruptionBehavior)

	def get_LaunchTemplateId(self):
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self,LaunchTemplateId):
		self.add_query_param('LaunchTemplateId',LaunchTemplateId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_SpotInstancePoolsToUseCount(self):
		return self.get_query_params().get('SpotInstancePoolsToUseCount')

	def set_SpotInstancePoolsToUseCount(self,SpotInstancePoolsToUseCount):
		self.add_query_param('SpotInstancePoolsToUseCount',SpotInstancePoolsToUseCount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_LaunchTemplateVersion(self):
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self,LaunchTemplateVersion):
		self.add_query_param('LaunchTemplateVersion',LaunchTemplateVersion)

	def get_PayAsYouGoTargetCapacity(self):
		return self.get_query_params().get('PayAsYouGoTargetCapacity')

	def set_PayAsYouGoTargetCapacity(self,PayAsYouGoTargetCapacity):
		self.add_query_param('PayAsYouGoTargetCapacity',PayAsYouGoTargetCapacity)

	def get_TotalTargetCapacity(self):
		return self.get_query_params().get('TotalTargetCapacity')

	def set_TotalTargetCapacity(self,TotalTargetCapacity):
		self.add_query_param('TotalTargetCapacity',TotalTargetCapacity)

	def get_SpotTargetCapacity(self):
		return self.get_query_params().get('SpotTargetCapacity')

	def set_SpotTargetCapacity(self,SpotTargetCapacity):
		self.add_query_param('SpotTargetCapacity',SpotTargetCapacity)

	def get_ValidFrom(self):
		return self.get_query_params().get('ValidFrom')

	def set_ValidFrom(self,ValidFrom):
		self.add_query_param('ValidFrom',ValidFrom)

	def get_AutoProvisioningGroupName(self):
		return self.get_query_params().get('AutoProvisioningGroupName')

	def set_AutoProvisioningGroupName(self,AutoProvisioningGroupName):
		self.add_query_param('AutoProvisioningGroupName',AutoProvisioningGroupName)

	def get_MaxSpotPrice(self):
		return self.get_query_params().get('MaxSpotPrice')

	def set_MaxSpotPrice(self,MaxSpotPrice):
		self.add_query_param('MaxSpotPrice',MaxSpotPrice)