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


	def get_LaunchConfigurationDataDisks(self):
		return self.get_query_params().get('LaunchConfiguration.DataDisk')

	def set_LaunchConfigurationDataDisks(self, LaunchConfigurationDataDisks):
		for depth1 in range(len(LaunchConfigurationDataDisks)):
			if LaunchConfigurationDataDisks[depth1].get('Size') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Size', LaunchConfigurationDataDisks[depth1].get('Size'))
			if LaunchConfigurationDataDisks[depth1].get('Category') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Category', LaunchConfigurationDataDisks[depth1].get('Category'))
			if LaunchConfigurationDataDisks[depth1].get('PerformanceLevel') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.PerformanceLevel', LaunchConfigurationDataDisks[depth1].get('PerformanceLevel'))
			if LaunchConfigurationDataDisks[depth1].get('Device') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Device', LaunchConfigurationDataDisks[depth1].get('Device'))
			if LaunchConfigurationDataDisks[depth1].get('SnapshotId') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.SnapshotId', LaunchConfigurationDataDisks[depth1].get('SnapshotId'))
			if LaunchConfigurationDataDisks[depth1].get('DeleteWithInstance') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.DeleteWithInstance', LaunchConfigurationDataDisks[depth1].get('DeleteWithInstance'))
			if LaunchConfigurationDataDisks[depth1].get('Encrypted') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Encrypted', LaunchConfigurationDataDisks[depth1].get('Encrypted'))
			if LaunchConfigurationDataDisks[depth1].get('KmsKeyId') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.KmsKeyId', LaunchConfigurationDataDisks[depth1].get('KmsKeyId'))
			if LaunchConfigurationDataDisks[depth1].get('DiskName') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.DiskName', LaunchConfigurationDataDisks[depth1].get('DiskName'))
			if LaunchConfigurationDataDisks[depth1].get('Description') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Description', LaunchConfigurationDataDisks[depth1].get('Description'))

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_LaunchConfigurationSystemDiskCategory(self):
		return self.get_query_params().get('LaunchConfiguration.SystemDiskCategory')

	def set_LaunchConfigurationSystemDiskCategory(self,LaunchConfigurationSystemDiskCategory):
		self.add_query_param('LaunchConfiguration.SystemDiskCategory',LaunchConfigurationSystemDiskCategory)

	def get_AutoProvisioningGroupType(self):
		return self.get_query_params().get('AutoProvisioningGroupType')

	def set_AutoProvisioningGroupType(self,AutoProvisioningGroupType):
		self.add_query_param('AutoProvisioningGroupType',AutoProvisioningGroupType)

	def get_LaunchConfigurationSystemDiskPerformanceLevel(self):
		return self.get_query_params().get('LaunchConfiguration.SystemDiskPerformanceLevel')

	def set_LaunchConfigurationSystemDiskPerformanceLevel(self,LaunchConfigurationSystemDiskPerformanceLevel):
		self.add_query_param('LaunchConfiguration.SystemDiskPerformanceLevel',LaunchConfigurationSystemDiskPerformanceLevel)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_LaunchConfigurationImageId(self):
		return self.get_query_params().get('LaunchConfiguration.ImageId')

	def set_LaunchConfigurationImageId(self,LaunchConfigurationImageId):
		self.add_query_param('LaunchConfiguration.ImageId',LaunchConfigurationImageId)

	def get_LaunchConfigurationResourceGroupId(self):
		return self.get_query_params().get('LaunchConfiguration.ResourceGroupId')

	def set_LaunchConfigurationResourceGroupId(self,LaunchConfigurationResourceGroupId):
		self.add_query_param('LaunchConfiguration.ResourceGroupId',LaunchConfigurationResourceGroupId)

	def get_PayAsYouGoAllocationStrategy(self):
		return self.get_query_params().get('PayAsYouGoAllocationStrategy')

	def set_PayAsYouGoAllocationStrategy(self,PayAsYouGoAllocationStrategy):
		self.add_query_param('PayAsYouGoAllocationStrategy',PayAsYouGoAllocationStrategy)

	def get_DefaultTargetCapacityType(self):
		return self.get_query_params().get('DefaultTargetCapacityType')

	def set_DefaultTargetCapacityType(self,DefaultTargetCapacityType):
		self.add_query_param('DefaultTargetCapacityType',DefaultTargetCapacityType)

	def get_LaunchConfigurationKeyPairName(self):
		return self.get_query_params().get('LaunchConfiguration.KeyPairName')

	def set_LaunchConfigurationKeyPairName(self,LaunchConfigurationKeyPairName):
		self.add_query_param('LaunchConfiguration.KeyPairName',LaunchConfigurationKeyPairName)

	def get_SystemDiskConfigs(self):
		return self.get_query_params().get('SystemDiskConfig')

	def set_SystemDiskConfigs(self, SystemDiskConfigs):
		for depth1 in range(len(SystemDiskConfigs)):
			if SystemDiskConfigs[depth1].get('DiskCategory') is not None:
				self.add_query_param('SystemDiskConfig.' + str(depth1 + 1) + '.DiskCategory', SystemDiskConfigs[depth1].get('DiskCategory'))

	def get_DataDiskConfigs(self):
		return self.get_query_params().get('DataDiskConfig')

	def set_DataDiskConfigs(self, DataDiskConfigs):
		for depth1 in range(len(DataDiskConfigs)):
			if DataDiskConfigs[depth1].get('DiskCategory') is not None:
				self.add_query_param('DataDiskConfig.' + str(depth1 + 1) + '.DiskCategory', DataDiskConfigs[depth1].get('DiskCategory'))

	def get_ValidUntil(self):
		return self.get_query_params().get('ValidUntil')

	def set_ValidUntil(self,ValidUntil):
		self.add_query_param('ValidUntil',ValidUntil)

	def get_LaunchTemplateId(self):
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self,LaunchTemplateId):
		self.add_query_param('LaunchTemplateId',LaunchTemplateId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_LaunchConfigurationSystemDiskSize(self):
		return self.get_query_params().get('LaunchConfiguration.SystemDiskSize')

	def set_LaunchConfigurationSystemDiskSize(self,LaunchConfigurationSystemDiskSize):
		self.add_query_param('LaunchConfiguration.SystemDiskSize',LaunchConfigurationSystemDiskSize)

	def get_LaunchConfigurationInternetMaxBandwidthOut(self):
		return self.get_query_params().get('LaunchConfiguration.InternetMaxBandwidthOut')

	def set_LaunchConfigurationInternetMaxBandwidthOut(self,LaunchConfigurationInternetMaxBandwidthOut):
		self.add_query_param('LaunchConfiguration.InternetMaxBandwidthOut',LaunchConfigurationInternetMaxBandwidthOut)

	def get_LaunchConfigurationHostName(self):
		return self.get_query_params().get('LaunchConfiguration.HostName')

	def set_LaunchConfigurationHostName(self,LaunchConfigurationHostName):
		self.add_query_param('LaunchConfiguration.HostName',LaunchConfigurationHostName)

	def get_MaxSpotPrice(self):
		return self.get_query_params().get('MaxSpotPrice')

	def set_MaxSpotPrice(self,MaxSpotPrice):
		self.add_query_param('MaxSpotPrice',MaxSpotPrice)

	def get_LaunchConfigurationPasswordInherit(self):
		return self.get_query_params().get('LaunchConfiguration.PasswordInherit')

	def set_LaunchConfigurationPasswordInherit(self,LaunchConfigurationPasswordInherit):
		self.add_query_param('LaunchConfiguration.PasswordInherit',LaunchConfigurationPasswordInherit)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_LaunchConfigurationSecurityGroupId(self):
		return self.get_query_params().get('LaunchConfiguration.SecurityGroupId')

	def set_LaunchConfigurationSecurityGroupId(self,LaunchConfigurationSecurityGroupId):
		self.add_query_param('LaunchConfiguration.SecurityGroupId',LaunchConfigurationSecurityGroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_TerminateInstancesWithExpiration(self):
		return self.get_query_params().get('TerminateInstancesWithExpiration')

	def set_TerminateInstancesWithExpiration(self,TerminateInstancesWithExpiration):
		self.add_query_param('TerminateInstancesWithExpiration',TerminateInstancesWithExpiration)

	def get_LaunchConfigurationUserData(self):
		return self.get_query_params().get('LaunchConfiguration.UserData')

	def set_LaunchConfigurationUserData(self,LaunchConfigurationUserData):
		self.add_query_param('LaunchConfiguration.UserData',LaunchConfigurationUserData)

	def get_LaunchConfigurationCreditSpecification(self):
		return self.get_query_params().get('LaunchConfiguration.CreditSpecification')

	def set_LaunchConfigurationCreditSpecification(self,LaunchConfigurationCreditSpecification):
		self.add_query_param('LaunchConfiguration.CreditSpecification',LaunchConfigurationCreditSpecification)

	def get_LaunchConfigurationInstanceName(self):
		return self.get_query_params().get('LaunchConfiguration.InstanceName')

	def set_LaunchConfigurationInstanceName(self,LaunchConfigurationInstanceName):
		self.add_query_param('LaunchConfiguration.InstanceName',LaunchConfigurationInstanceName)

	def get_LaunchConfigurationInstanceDescription(self):
		return self.get_query_params().get('LaunchConfiguration.InstanceDescription')

	def set_LaunchConfigurationInstanceDescription(self,LaunchConfigurationInstanceDescription):
		self.add_query_param('LaunchConfiguration.InstanceDescription',LaunchConfigurationInstanceDescription)

	def get_SpotAllocationStrategy(self):
		return self.get_query_params().get('SpotAllocationStrategy')

	def set_SpotAllocationStrategy(self,SpotAllocationStrategy):
		self.add_query_param('SpotAllocationStrategy',SpotAllocationStrategy)

	def get_TerminateInstances(self):
		return self.get_query_params().get('TerminateInstances')

	def set_TerminateInstances(self,TerminateInstances):
		self.add_query_param('TerminateInstances',TerminateInstances)

	def get_LaunchConfigurationSystemDiskName(self):
		return self.get_query_params().get('LaunchConfiguration.SystemDiskName')

	def set_LaunchConfigurationSystemDiskName(self,LaunchConfigurationSystemDiskName):
		self.add_query_param('LaunchConfiguration.SystemDiskName',LaunchConfigurationSystemDiskName)

	def get_LaunchConfigurationSystemDiskDescription(self):
		return self.get_query_params().get('LaunchConfiguration.SystemDiskDescription')

	def set_LaunchConfigurationSystemDiskDescription(self,LaunchConfigurationSystemDiskDescription):
		self.add_query_param('LaunchConfiguration.SystemDiskDescription',LaunchConfigurationSystemDiskDescription)

	def get_ExcessCapacityTerminationPolicy(self):
		return self.get_query_params().get('ExcessCapacityTerminationPolicy')

	def set_ExcessCapacityTerminationPolicy(self,ExcessCapacityTerminationPolicy):
		self.add_query_param('ExcessCapacityTerminationPolicy',ExcessCapacityTerminationPolicy)

	def get_LaunchTemplateConfigs(self):
		return self.get_query_params().get('LaunchTemplateConfig')

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

	def get_LaunchConfigurationRamRoleName(self):
		return self.get_query_params().get('LaunchConfiguration.RamRoleName')

	def set_LaunchConfigurationRamRoleName(self,LaunchConfigurationRamRoleName):
		self.add_query_param('LaunchConfiguration.RamRoleName',LaunchConfigurationRamRoleName)

	def get_LaunchConfigurationInternetMaxBandwidthIn(self):
		return self.get_query_params().get('LaunchConfiguration.InternetMaxBandwidthIn')

	def set_LaunchConfigurationInternetMaxBandwidthIn(self,LaunchConfigurationInternetMaxBandwidthIn):
		self.add_query_param('LaunchConfiguration.InternetMaxBandwidthIn',LaunchConfigurationInternetMaxBandwidthIn)

	def get_SpotInstanceInterruptionBehavior(self):
		return self.get_query_params().get('SpotInstanceInterruptionBehavior')

	def set_SpotInstanceInterruptionBehavior(self,SpotInstanceInterruptionBehavior):
		self.add_query_param('SpotInstanceInterruptionBehavior',SpotInstanceInterruptionBehavior)

	def get_LaunchConfigurationSecurityEnhancementStrategy(self):
		return self.get_query_params().get('LaunchConfiguration.SecurityEnhancementStrategy')

	def set_LaunchConfigurationSecurityEnhancementStrategy(self,LaunchConfigurationSecurityEnhancementStrategy):
		self.add_query_param('LaunchConfiguration.SecurityEnhancementStrategy',LaunchConfigurationSecurityEnhancementStrategy)

	def get_LaunchConfigurationTags(self):
		return self.get_query_params().get('LaunchConfiguration.Tag')

	def set_LaunchConfigurationTags(self, LaunchConfigurationTags):
		for depth1 in range(len(LaunchConfigurationTags)):
			if LaunchConfigurationTags[depth1].get('Key') is not None:
				self.add_query_param('LaunchConfiguration.Tag.' + str(depth1 + 1) + '.Key', LaunchConfigurationTags[depth1].get('Key'))
			if LaunchConfigurationTags[depth1].get('Value') is not None:
				self.add_query_param('LaunchConfiguration.Tag.' + str(depth1 + 1) + '.Value', LaunchConfigurationTags[depth1].get('Value'))

	def get_LaunchConfigurationDeploymentSetId(self):
		return self.get_query_params().get('LaunchConfiguration.DeploymentSetId')

	def set_LaunchConfigurationDeploymentSetId(self,LaunchConfigurationDeploymentSetId):
		self.add_query_param('LaunchConfiguration.DeploymentSetId',LaunchConfigurationDeploymentSetId)

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

	def get_LaunchConfigurationInternetChargeType(self):
		return self.get_query_params().get('LaunchConfiguration.InternetChargeType')

	def set_LaunchConfigurationInternetChargeType(self,LaunchConfigurationInternetChargeType):
		self.add_query_param('LaunchConfiguration.InternetChargeType',LaunchConfigurationInternetChargeType)

	def get_LaunchTemplateVersion(self):
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self,LaunchTemplateVersion):
		self.add_query_param('LaunchTemplateVersion',LaunchTemplateVersion)

	def get_LaunchConfigurationIoOptimized(self):
		return self.get_query_params().get('LaunchConfiguration.IoOptimized')

	def set_LaunchConfigurationIoOptimized(self,LaunchConfigurationIoOptimized):
		self.add_query_param('LaunchConfiguration.IoOptimized',LaunchConfigurationIoOptimized)

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