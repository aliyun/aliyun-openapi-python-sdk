# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateFleetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateFleet','ecs')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_FleetType(self):
		return self.get_query_params().get('FleetType')

	def set_FleetType(self,FleetType):
		self.add_query_param('FleetType',FleetType)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_TerminateInstancesWithExpiration(self):
		return self.get_query_params().get('TerminateInstancesWithExpiration')

	def set_TerminateInstancesWithExpiration(self,TerminateInstancesWithExpiration):
		self.add_query_param('TerminateInstancesWithExpiration',TerminateInstancesWithExpiration)

	def get_OnDemandTargetCapacity(self):
		return self.get_query_params().get('OnDemandTargetCapacity')

	def set_OnDemandTargetCapacity(self,OnDemandTargetCapacity):
		self.add_query_param('OnDemandTargetCapacity',OnDemandTargetCapacity)

	def get_FleetName(self):
		return self.get_query_params().get('FleetName')

	def set_FleetName(self,FleetName):
		self.add_query_param('FleetName',FleetName)

	def get_SpotAllocationStrategy(self):
		return self.get_query_params().get('SpotAllocationStrategy')

	def set_SpotAllocationStrategy(self,SpotAllocationStrategy):
		self.add_query_param('SpotAllocationStrategy',SpotAllocationStrategy)

	def get_TerminateInstances(self):
		return self.get_query_params().get('TerminateInstances')

	def set_TerminateInstances(self,TerminateInstances):
		self.add_query_param('TerminateInstances',TerminateInstances)

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

	def set_LaunchTemplateConfigs(self,LaunchTemplateConfigs):
		for i in range(len(LaunchTemplateConfigs)):	
			if LaunchTemplateConfigs[i].get('InstanceType') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(i + 1) + '.InstanceType' , LaunchTemplateConfigs[i].get('InstanceType'))
			if LaunchTemplateConfigs[i].get('MaxPrice') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(i + 1) + '.MaxPrice' , LaunchTemplateConfigs[i].get('MaxPrice'))
			if LaunchTemplateConfigs[i].get('VSwitchId') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(i + 1) + '.VSwitchId' , LaunchTemplateConfigs[i].get('VSwitchId'))
			if LaunchTemplateConfigs[i].get('WeightedCapacity') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(i + 1) + '.WeightedCapacity' , LaunchTemplateConfigs[i].get('WeightedCapacity'))
			if LaunchTemplateConfigs[i].get('Priority') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(i + 1) + '.Priority' , LaunchTemplateConfigs[i].get('Priority'))


	def get_ValidUntil(self):
		return self.get_query_params().get('ValidUntil')

	def set_ValidUntil(self,ValidUntil):
		self.add_query_param('ValidUntil',ValidUntil)

	def get_FillGapWithOnDemand(self):
		return self.get_query_params().get('FillGapWithOnDemand')

	def set_FillGapWithOnDemand(self,FillGapWithOnDemand):
		self.add_query_param('FillGapWithOnDemand',FillGapWithOnDemand)

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

	def get_TotalTargetCapacity(self):
		return self.get_query_params().get('TotalTargetCapacity')

	def set_TotalTargetCapacity(self,TotalTargetCapacity):
		self.add_query_param('TotalTargetCapacity',TotalTargetCapacity)

	def get_OnDemandAllocationStrategy(self):
		return self.get_query_params().get('OnDemandAllocationStrategy')

	def set_OnDemandAllocationStrategy(self,OnDemandAllocationStrategy):
		self.add_query_param('OnDemandAllocationStrategy',OnDemandAllocationStrategy)

	def get_SpotTargetCapacity(self):
		return self.get_query_params().get('SpotTargetCapacity')

	def set_SpotTargetCapacity(self,SpotTargetCapacity):
		self.add_query_param('SpotTargetCapacity',SpotTargetCapacity)

	def get_ValidFrom(self):
		return self.get_query_params().get('ValidFrom')

	def set_ValidFrom(self,ValidFrom):
		self.add_query_param('ValidFrom',ValidFrom)

	def get_MaxSpotPrice(self):
		return self.get_query_params().get('MaxSpotPrice')

	def set_MaxSpotPrice(self,MaxSpotPrice):
		self.add_query_param('MaxSpotPrice',MaxSpotPrice)