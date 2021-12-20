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

	def get_LaunchConfigurationDataDisks(self): # RepeatList
		return self.get_query_params().get('LaunchConfiguration.DataDisk')

	def set_LaunchConfigurationDataDisks(self, LaunchConfigurationDataDisk):  # RepeatList
		for depth1 in range(len(LaunchConfigurationDataDisk)):
			if LaunchConfigurationDataDisk[depth1].get('PerformanceLevel') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.PerformanceLevel', LaunchConfigurationDataDisk[depth1].get('PerformanceLevel'))
			if LaunchConfigurationDataDisk[depth1].get('KmsKeyId') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.KmsKeyId', LaunchConfigurationDataDisk[depth1].get('KmsKeyId'))
			if LaunchConfigurationDataDisk[depth1].get('Description') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Description', LaunchConfigurationDataDisk[depth1].get('Description'))
			if LaunchConfigurationDataDisk[depth1].get('SnapshotId') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.SnapshotId', LaunchConfigurationDataDisk[depth1].get('SnapshotId'))
			if LaunchConfigurationDataDisk[depth1].get('Size') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Size', LaunchConfigurationDataDisk[depth1].get('Size'))
			if LaunchConfigurationDataDisk[depth1].get('Device') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Device', LaunchConfigurationDataDisk[depth1].get('Device'))
			if LaunchConfigurationDataDisk[depth1].get('DiskName') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.DiskName', LaunchConfigurationDataDisk[depth1].get('DiskName'))
			if LaunchConfigurationDataDisk[depth1].get('Category') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Category', LaunchConfigurationDataDisk[depth1].get('Category'))
			if LaunchConfigurationDataDisk[depth1].get('DeleteWithInstance') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.DeleteWithInstance', LaunchConfigurationDataDisk[depth1].get('DeleteWithInstance'))
			if LaunchConfigurationDataDisk[depth1].get('Encrypted') is not None:
				self.add_query_param('LaunchConfiguration.DataDisk.' + str(depth1 + 1) + '.Encrypted', LaunchConfigurationDataDisk[depth1].get('Encrypted'))
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_LaunchConfigurationSystemDiskCategory(self): # String
		return self.get_query_params().get('LaunchConfiguration.SystemDiskCategory')

	def set_LaunchConfigurationSystemDiskCategory(self, LaunchConfigurationSystemDiskCategory):  # String
		self.add_query_param('LaunchConfiguration.SystemDiskCategory', LaunchConfigurationSystemDiskCategory)
	def get_AutoProvisioningGroupType(self): # String
		return self.get_query_params().get('AutoProvisioningGroupType')

	def set_AutoProvisioningGroupType(self, AutoProvisioningGroupType):  # String
		self.add_query_param('AutoProvisioningGroupType', AutoProvisioningGroupType)
	def get_LaunchConfigurationSystemDiskPerformanceLevel(self): # String
		return self.get_query_params().get('LaunchConfiguration.SystemDiskPerformanceLevel')

	def set_LaunchConfigurationSystemDiskPerformanceLevel(self, LaunchConfigurationSystemDiskPerformanceLevel):  # String
		self.add_query_param('LaunchConfiguration.SystemDiskPerformanceLevel', LaunchConfigurationSystemDiskPerformanceLevel)
	def get_LaunchConfigurationHostNamess(self): # RepeatList
		return self.get_query_params().get('LaunchConfiguration.HostNames')

	def set_LaunchConfigurationHostNamess(self, LaunchConfigurationHostNames):  # RepeatList
		for depth1 in range(len(LaunchConfigurationHostNames)):
			self.add_query_param('LaunchConfiguration.HostNames.' + str(depth1 + 1), LaunchConfigurationHostNames[depth1])
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_LaunchConfigurationImageId(self): # String
		return self.get_query_params().get('LaunchConfiguration.ImageId')

	def set_LaunchConfigurationImageId(self, LaunchConfigurationImageId):  # String
		self.add_query_param('LaunchConfiguration.ImageId', LaunchConfigurationImageId)
	def get_LaunchConfigurationResourceGroupId(self): # String
		return self.get_query_params().get('LaunchConfiguration.ResourceGroupId')

	def set_LaunchConfigurationResourceGroupId(self, LaunchConfigurationResourceGroupId):  # String
		self.add_query_param('LaunchConfiguration.ResourceGroupId', LaunchConfigurationResourceGroupId)
	def get_PayAsYouGoAllocationStrategy(self): # String
		return self.get_query_params().get('PayAsYouGoAllocationStrategy')

	def set_PayAsYouGoAllocationStrategy(self, PayAsYouGoAllocationStrategy):  # String
		self.add_query_param('PayAsYouGoAllocationStrategy', PayAsYouGoAllocationStrategy)
	def get_DefaultTargetCapacityType(self): # String
		return self.get_query_params().get('DefaultTargetCapacityType')

	def set_DefaultTargetCapacityType(self, DefaultTargetCapacityType):  # String
		self.add_query_param('DefaultTargetCapacityType', DefaultTargetCapacityType)
	def get_LaunchConfigurationKeyPairName(self): # String
		return self.get_query_params().get('LaunchConfiguration.KeyPairName')

	def set_LaunchConfigurationKeyPairName(self, LaunchConfigurationKeyPairName):  # String
		self.add_query_param('LaunchConfiguration.KeyPairName', LaunchConfigurationKeyPairName)
	def get_SystemDiskConfigs(self): # RepeatList
		return self.get_query_params().get('SystemDiskConfig')

	def set_SystemDiskConfigs(self, SystemDiskConfig):  # RepeatList
		for depth1 in range(len(SystemDiskConfig)):
			if SystemDiskConfig[depth1].get('DiskCategory') is not None:
				self.add_query_param('SystemDiskConfig.' + str(depth1 + 1) + '.DiskCategory', SystemDiskConfig[depth1].get('DiskCategory'))
	def get_DataDiskConfigs(self): # RepeatList
		return self.get_query_params().get('DataDiskConfig')

	def set_DataDiskConfigs(self, DataDiskConfig):  # RepeatList
		for depth1 in range(len(DataDiskConfig)):
			if DataDiskConfig[depth1].get('DiskCategory') is not None:
				self.add_query_param('DataDiskConfig.' + str(depth1 + 1) + '.DiskCategory', DataDiskConfig[depth1].get('DiskCategory'))
	def get_ValidUntil(self): # String
		return self.get_query_params().get('ValidUntil')

	def set_ValidUntil(self, ValidUntil):  # String
		self.add_query_param('ValidUntil', ValidUntil)
	def get_LaunchTemplateId(self): # String
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self, LaunchTemplateId):  # String
		self.add_query_param('LaunchTemplateId', LaunchTemplateId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_LaunchConfigurationSystemDiskSize(self): # Integer
		return self.get_query_params().get('LaunchConfiguration.SystemDiskSize')

	def set_LaunchConfigurationSystemDiskSize(self, LaunchConfigurationSystemDiskSize):  # Integer
		self.add_query_param('LaunchConfiguration.SystemDiskSize', LaunchConfigurationSystemDiskSize)
	def get_LaunchConfigurationInternetMaxBandwidthOut(self): # Integer
		return self.get_query_params().get('LaunchConfiguration.InternetMaxBandwidthOut')

	def set_LaunchConfigurationInternetMaxBandwidthOut(self, LaunchConfigurationInternetMaxBandwidthOut):  # Integer
		self.add_query_param('LaunchConfiguration.InternetMaxBandwidthOut', LaunchConfigurationInternetMaxBandwidthOut)
	def get_LaunchConfigurationHostName(self): # String
		return self.get_query_params().get('LaunchConfiguration.HostName')

	def set_LaunchConfigurationHostName(self, LaunchConfigurationHostName):  # String
		self.add_query_param('LaunchConfiguration.HostName', LaunchConfigurationHostName)
	def get_MinTargetCapacity(self): # String
		return self.get_query_params().get('MinTargetCapacity')

	def set_MinTargetCapacity(self, MinTargetCapacity):  # String
		self.add_query_param('MinTargetCapacity', MinTargetCapacity)
	def get_MaxSpotPrice(self): # Float
		return self.get_query_params().get('MaxSpotPrice')

	def set_MaxSpotPrice(self, MaxSpotPrice):  # Float
		self.add_query_param('MaxSpotPrice', MaxSpotPrice)
	def get_LaunchConfigurationPasswordInherit(self): # Boolean
		return self.get_query_params().get('LaunchConfiguration.PasswordInherit')

	def set_LaunchConfigurationPasswordInherit(self, LaunchConfigurationPasswordInherit):  # Boolean
		self.add_query_param('LaunchConfiguration.PasswordInherit', LaunchConfigurationPasswordInherit)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_LaunchConfigurationSecurityGroupId(self): # String
		return self.get_query_params().get('LaunchConfiguration.SecurityGroupId')

	def set_LaunchConfigurationSecurityGroupId(self, LaunchConfigurationSecurityGroupId):  # String
		self.add_query_param('LaunchConfiguration.SecurityGroupId', LaunchConfigurationSecurityGroupId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_TerminateInstancesWithExpiration(self): # Boolean
		return self.get_query_params().get('TerminateInstancesWithExpiration')

	def set_TerminateInstancesWithExpiration(self, TerminateInstancesWithExpiration):  # Boolean
		self.add_query_param('TerminateInstancesWithExpiration', TerminateInstancesWithExpiration)
	def get_LaunchConfigurationUserData(self): # String
		return self.get_query_params().get('LaunchConfiguration.UserData')

	def set_LaunchConfigurationUserData(self, LaunchConfigurationUserData):  # String
		self.add_query_param('LaunchConfiguration.UserData', LaunchConfigurationUserData)
	def get_LaunchConfigurationCreditSpecification(self): # String
		return self.get_query_params().get('LaunchConfiguration.CreditSpecification')

	def set_LaunchConfigurationCreditSpecification(self, LaunchConfigurationCreditSpecification):  # String
		self.add_query_param('LaunchConfiguration.CreditSpecification', LaunchConfigurationCreditSpecification)
	def get_LaunchConfigurationInstanceName(self): # String
		return self.get_query_params().get('LaunchConfiguration.InstanceName')

	def set_LaunchConfigurationInstanceName(self, LaunchConfigurationInstanceName):  # String
		self.add_query_param('LaunchConfiguration.InstanceName', LaunchConfigurationInstanceName)
	def get_LaunchConfigurationInstanceDescription(self): # String
		return self.get_query_params().get('LaunchConfiguration.InstanceDescription')

	def set_LaunchConfigurationInstanceDescription(self, LaunchConfigurationInstanceDescription):  # String
		self.add_query_param('LaunchConfiguration.InstanceDescription', LaunchConfigurationInstanceDescription)
	def get_SpotAllocationStrategy(self): # String
		return self.get_query_params().get('SpotAllocationStrategy')

	def set_SpotAllocationStrategy(self, SpotAllocationStrategy):  # String
		self.add_query_param('SpotAllocationStrategy', SpotAllocationStrategy)
	def get_TerminateInstances(self): # Boolean
		return self.get_query_params().get('TerminateInstances')

	def set_TerminateInstances(self, TerminateInstances):  # Boolean
		self.add_query_param('TerminateInstances', TerminateInstances)
	def get_LaunchConfigurationSystemDiskName(self): # String
		return self.get_query_params().get('LaunchConfiguration.SystemDiskName')

	def set_LaunchConfigurationSystemDiskName(self, LaunchConfigurationSystemDiskName):  # String
		self.add_query_param('LaunchConfiguration.SystemDiskName', LaunchConfigurationSystemDiskName)
	def get_LaunchConfigurationSystemDiskDescription(self): # String
		return self.get_query_params().get('LaunchConfiguration.SystemDiskDescription')

	def set_LaunchConfigurationSystemDiskDescription(self, LaunchConfigurationSystemDiskDescription):  # String
		self.add_query_param('LaunchConfiguration.SystemDiskDescription', LaunchConfigurationSystemDiskDescription)
	def get_ExcessCapacityTerminationPolicy(self): # String
		return self.get_query_params().get('ExcessCapacityTerminationPolicy')

	def set_ExcessCapacityTerminationPolicy(self, ExcessCapacityTerminationPolicy):  # String
		self.add_query_param('ExcessCapacityTerminationPolicy', ExcessCapacityTerminationPolicy)
	def get_LaunchTemplateConfigs(self): # RepeatList
		return self.get_query_params().get('LaunchTemplateConfig')

	def set_LaunchTemplateConfigs(self, LaunchTemplateConfig):  # RepeatList
		for depth1 in range(len(LaunchTemplateConfig)):
			if LaunchTemplateConfig[depth1].get('VSwitchId') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.VSwitchId', LaunchTemplateConfig[depth1].get('VSwitchId'))
			if LaunchTemplateConfig[depth1].get('MaxPrice') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.MaxPrice', LaunchTemplateConfig[depth1].get('MaxPrice'))
			if LaunchTemplateConfig[depth1].get('Priority') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.Priority', LaunchTemplateConfig[depth1].get('Priority'))
			if LaunchTemplateConfig[depth1].get('InstanceType') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.InstanceType', LaunchTemplateConfig[depth1].get('InstanceType'))
			if LaunchTemplateConfig[depth1].get('WeightedCapacity') is not None:
				self.add_query_param('LaunchTemplateConfig.' + str(depth1 + 1) + '.WeightedCapacity', LaunchTemplateConfig[depth1].get('WeightedCapacity'))
	def get_LaunchConfigurationRamRoleName(self): # String
		return self.get_query_params().get('LaunchConfiguration.RamRoleName')

	def set_LaunchConfigurationRamRoleName(self, LaunchConfigurationRamRoleName):  # String
		self.add_query_param('LaunchConfiguration.RamRoleName', LaunchConfigurationRamRoleName)
	def get_LaunchConfigurationInternetMaxBandwidthIn(self): # Integer
		return self.get_query_params().get('LaunchConfiguration.InternetMaxBandwidthIn')

	def set_LaunchConfigurationInternetMaxBandwidthIn(self, LaunchConfigurationInternetMaxBandwidthIn):  # Integer
		self.add_query_param('LaunchConfiguration.InternetMaxBandwidthIn', LaunchConfigurationInternetMaxBandwidthIn)
	def get_SpotInstanceInterruptionBehavior(self): # String
		return self.get_query_params().get('SpotInstanceInterruptionBehavior')

	def set_SpotInstanceInterruptionBehavior(self, SpotInstanceInterruptionBehavior):  # String
		self.add_query_param('SpotInstanceInterruptionBehavior', SpotInstanceInterruptionBehavior)
	def get_LaunchConfigurationSecurityEnhancementStrategy(self): # String
		return self.get_query_params().get('LaunchConfiguration.SecurityEnhancementStrategy')

	def set_LaunchConfigurationSecurityEnhancementStrategy(self, LaunchConfigurationSecurityEnhancementStrategy):  # String
		self.add_query_param('LaunchConfiguration.SecurityEnhancementStrategy', LaunchConfigurationSecurityEnhancementStrategy)
	def get_LaunchConfigurationTags(self): # RepeatList
		return self.get_query_params().get('LaunchConfiguration.Tag')

	def set_LaunchConfigurationTags(self, LaunchConfigurationTag):  # RepeatList
		for depth1 in range(len(LaunchConfigurationTag)):
			if LaunchConfigurationTag[depth1].get('Key') is not None:
				self.add_query_param('LaunchConfiguration.Tag.' + str(depth1 + 1) + '.Key', LaunchConfigurationTag[depth1].get('Key'))
			if LaunchConfigurationTag[depth1].get('Value') is not None:
				self.add_query_param('LaunchConfiguration.Tag.' + str(depth1 + 1) + '.Value', LaunchConfigurationTag[depth1].get('Value'))
	def get_LaunchConfigurationDeploymentSetId(self): # String
		return self.get_query_params().get('LaunchConfiguration.DeploymentSetId')

	def set_LaunchConfigurationDeploymentSetId(self, LaunchConfigurationDeploymentSetId):  # String
		self.add_query_param('LaunchConfiguration.DeploymentSetId', LaunchConfigurationDeploymentSetId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_SpotInstancePoolsToUseCount(self): # Integer
		return self.get_query_params().get('SpotInstancePoolsToUseCount')

	def set_SpotInstancePoolsToUseCount(self, SpotInstancePoolsToUseCount):  # Integer
		self.add_query_param('SpotInstancePoolsToUseCount', SpotInstancePoolsToUseCount)
	def get_LaunchConfigurationInternetChargeType(self): # String
		return self.get_query_params().get('LaunchConfiguration.InternetChargeType')

	def set_LaunchConfigurationInternetChargeType(self, LaunchConfigurationInternetChargeType):  # String
		self.add_query_param('LaunchConfiguration.InternetChargeType', LaunchConfigurationInternetChargeType)
	def get_LaunchTemplateVersion(self): # String
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self, LaunchTemplateVersion):  # String
		self.add_query_param('LaunchTemplateVersion', LaunchTemplateVersion)
	def get_LaunchConfigurationIoOptimized(self): # String
		return self.get_query_params().get('LaunchConfiguration.IoOptimized')

	def set_LaunchConfigurationIoOptimized(self, LaunchConfigurationIoOptimized):  # String
		self.add_query_param('LaunchConfiguration.IoOptimized', LaunchConfigurationIoOptimized)
	def get_PayAsYouGoTargetCapacity(self): # String
		return self.get_query_params().get('PayAsYouGoTargetCapacity')

	def set_PayAsYouGoTargetCapacity(self, PayAsYouGoTargetCapacity):  # String
		self.add_query_param('PayAsYouGoTargetCapacity', PayAsYouGoTargetCapacity)
	def get_TotalTargetCapacity(self): # String
		return self.get_query_params().get('TotalTargetCapacity')

	def set_TotalTargetCapacity(self, TotalTargetCapacity):  # String
		self.add_query_param('TotalTargetCapacity', TotalTargetCapacity)
	def get_SpotTargetCapacity(self): # String
		return self.get_query_params().get('SpotTargetCapacity')

	def set_SpotTargetCapacity(self, SpotTargetCapacity):  # String
		self.add_query_param('SpotTargetCapacity', SpotTargetCapacity)
	def get_ValidFrom(self): # String
		return self.get_query_params().get('ValidFrom')

	def set_ValidFrom(self, ValidFrom):  # String
		self.add_query_param('ValidFrom', ValidFrom)
	def get_AutoProvisioningGroupName(self): # String
		return self.get_query_params().get('AutoProvisioningGroupName')

	def set_AutoProvisioningGroupName(self, AutoProvisioningGroupName):  # String
		self.add_query_param('AutoProvisioningGroupName', AutoProvisioningGroupName)
