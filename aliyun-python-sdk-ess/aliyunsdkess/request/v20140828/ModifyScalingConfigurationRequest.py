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
from aliyunsdkess.endpoint import endpoint_data

class ModifyScalingConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'ModifyScalingConfiguration','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_HpcClusterId(self): # String
		return self.get_query_params().get('HpcClusterId')

	def set_HpcClusterId(self, HpcClusterId):  # String
		self.add_query_param('HpcClusterId', HpcClusterId)
	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_SpotPriceLimits(self): # RepeatList
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimits(self, SpotPriceLimit):  # RepeatList
		for depth1 in range(len(SpotPriceLimit)):
			if SpotPriceLimit[depth1].get('InstanceType') is not None:
				self.add_query_param('SpotPriceLimit.' + str(depth1 + 1) + '.InstanceType', SpotPriceLimit[depth1].get('InstanceType'))
			if SpotPriceLimit[depth1].get('PriceLimit') is not None:
				self.add_query_param('SpotPriceLimit.' + str(depth1 + 1) + '.PriceLimit', SpotPriceLimit[depth1].get('PriceLimit'))
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_PrivatePoolOptionsMatchCriteria(self): # String
		return self.get_query_params().get('PrivatePoolOptions.MatchCriteria')

	def set_PrivatePoolOptionsMatchCriteria(self, PrivatePoolOptionsMatchCriteria):  # String
		self.add_query_param('PrivatePoolOptions.MatchCriteria', PrivatePoolOptionsMatchCriteria)
	def get_HostName(self): # String
		return self.get_query_params().get('HostName')

	def set_HostName(self, HostName):  # String
		self.add_query_param('HostName', HostName)
	def get_InstanceDescription(self): # String
		return self.get_query_params().get('InstanceDescription')

	def set_InstanceDescription(self, InstanceDescription):  # String
		self.add_query_param('InstanceDescription', InstanceDescription)
	def get_SystemDiskAutoSnapshotPolicyId(self): # String
		return self.get_query_params().get('SystemDisk.AutoSnapshotPolicyId')

	def set_SystemDiskAutoSnapshotPolicyId(self, SystemDiskAutoSnapshotPolicyId):  # String
		self.add_query_param('SystemDisk.AutoSnapshotPolicyId', SystemDiskAutoSnapshotPolicyId)
	def get_PrivatePoolOptionsId(self): # String
		return self.get_query_params().get('PrivatePoolOptions.Id')

	def set_PrivatePoolOptionsId(self, PrivatePoolOptionsId):  # String
		self.add_query_param('PrivatePoolOptions.Id', PrivatePoolOptionsId)
	def get_Ipv6AddressCount(self): # Integer
		return self.get_query_params().get('Ipv6AddressCount')

	def set_Ipv6AddressCount(self, Ipv6AddressCount):  # Integer
		self.add_query_param('Ipv6AddressCount', Ipv6AddressCount)
	def get_Cpu(self): # Integer
		return self.get_query_params().get('Cpu')

	def set_Cpu(self, Cpu):  # Integer
		self.add_query_param('Cpu', Cpu)
	def get_SystemDiskCategoriess(self): # RepeatList
		return self.get_query_params().get('SystemDiskCategories')

	def set_SystemDiskCategoriess(self, SystemDiskCategories):  # RepeatList
		for depth1 in range(len(SystemDiskCategories)):
			self.add_query_param('SystemDiskCategories.' + str(depth1 + 1), SystemDiskCategories[depth1])
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ScalingConfigurationName(self): # String
		return self.get_query_params().get('ScalingConfigurationName')

	def set_ScalingConfigurationName(self, ScalingConfigurationName):  # String
		self.add_query_param('ScalingConfigurationName', ScalingConfigurationName)
	def get_Tags(self): # String
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # String
		self.add_query_param('Tags', Tags)
	def get_ScalingConfigurationId(self): # String
		return self.get_query_params().get('ScalingConfigurationId')

	def set_ScalingConfigurationId(self, ScalingConfigurationId):  # String
		self.add_query_param('ScalingConfigurationId', ScalingConfigurationId)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_SystemDiskBurstingEnabled(self): # Boolean
		return self.get_query_params().get('SystemDisk.BurstingEnabled')

	def set_SystemDiskBurstingEnabled(self, SystemDiskBurstingEnabled):  # Boolean
		self.add_query_param('SystemDisk.BurstingEnabled', SystemDiskBurstingEnabled)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_InstancePatternInfos(self): # RepeatList
		return self.get_query_params().get('InstancePatternInfo')

	def set_InstancePatternInfos(self, InstancePatternInfo):  # RepeatList
		for depth1 in range(len(InstancePatternInfo)):
			if InstancePatternInfo[depth1].get('Cores') is not None:
				self.add_query_param('InstancePatternInfo.' + str(depth1 + 1) + '.Cores', InstancePatternInfo[depth1].get('Cores'))
			if InstancePatternInfo[depth1].get('InstanceFamilyLevel') is not None:
				self.add_query_param('InstancePatternInfo.' + str(depth1 + 1) + '.InstanceFamilyLevel', InstancePatternInfo[depth1].get('InstanceFamilyLevel'))
			if InstancePatternInfo[depth1].get('Memory') is not None:
				self.add_query_param('InstancePatternInfo.' + str(depth1 + 1) + '.Memory', InstancePatternInfo[depth1].get('Memory'))
			if InstancePatternInfo[depth1].get('MaxPrice') is not None:
				self.add_query_param('InstancePatternInfo.' + str(depth1 + 1) + '.MaxPrice', InstancePatternInfo[depth1].get('MaxPrice'))
			if InstancePatternInfo[depth1].get('ExcludedInstanceType') is not None:
				for depth2 in range(len(InstancePatternInfo[depth1].get('ExcludedInstanceType'))):
					self.add_query_param('InstancePatternInfo.' + str(depth1 + 1) + '.ExcludedInstanceType.' + str(depth2 + 1), InstancePatternInfo[depth1].get('ExcludedInstanceType')[depth2])
			if InstancePatternInfo[depth1].get('BurstablePerformance') is not None:
				self.add_query_param('InstancePatternInfo.' + str(depth1 + 1) + '.BurstablePerformance', InstancePatternInfo[depth1].get('BurstablePerformance'))
			if InstancePatternInfo[depth1].get('Architecture') is not None:
				for depth2 in range(len(InstancePatternInfo[depth1].get('Architecture'))):
					self.add_query_param('InstancePatternInfo.' + str(depth1 + 1) + '.Architecture.' + str(depth2 + 1), InstancePatternInfo[depth1].get('Architecture')[depth2])
	def get_Affinity(self): # String
		return self.get_query_params().get('Affinity')

	def set_Affinity(self, Affinity):  # String
		self.add_query_param('Affinity', Affinity)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_Memory(self): # Integer
		return self.get_query_params().get('Memory')

	def set_Memory(self, Memory):  # Integer
		self.add_query_param('Memory', Memory)
	def get_SpotInterruptionBehavior(self): # String
		return self.get_query_params().get('SpotInterruptionBehavior')

	def set_SpotInterruptionBehavior(self, SpotInterruptionBehavior):  # String
		self.add_query_param('SpotInterruptionBehavior', SpotInterruptionBehavior)
	def get_IoOptimized(self): # String
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self, IoOptimized):  # String
		self.add_query_param('IoOptimized', IoOptimized)
	def get_InstanceTypess(self): # RepeatList
		return self.get_query_params().get('InstanceTypes')

	def set_InstanceTypess(self, InstanceTypes):  # RepeatList
		for depth1 in range(len(InstanceTypes)):
			self.add_query_param('InstanceTypes.' + str(depth1 + 1), InstanceTypes[depth1])
	def get_InternetMaxBandwidthOut(self): # Integer
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):  # Integer
		self.add_query_param('InternetMaxBandwidthOut', InternetMaxBandwidthOut)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_SystemDiskKMSKeyId(self): # String
		return self.get_query_params().get('SystemDisk.KMSKeyId')

	def set_SystemDiskKMSKeyId(self, SystemDiskKMSKeyId):  # String
		self.add_query_param('SystemDisk.KMSKeyId', SystemDiskKMSKeyId)
	def get_SystemDiskCategory(self): # String
		return self.get_query_params().get('SystemDisk.Category')

	def set_SystemDiskCategory(self, SystemDiskCategory):  # String
		self.add_query_param('SystemDisk.Category', SystemDiskCategory)
	def get_SystemDiskPerformanceLevel(self): # String
		return self.get_query_params().get('SystemDisk.PerformanceLevel')

	def set_SystemDiskPerformanceLevel(self, SystemDiskPerformanceLevel):  # String
		self.add_query_param('SystemDisk.PerformanceLevel', SystemDiskPerformanceLevel)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_PasswordInherit(self): # Boolean
		return self.get_query_params().get('PasswordInherit')

	def set_PasswordInherit(self, PasswordInherit):  # Boolean
		self.add_query_param('PasswordInherit', PasswordInherit)
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
	def get_Override(self): # Boolean
		return self.get_query_params().get('Override')

	def set_Override(self, Override):  # Boolean
		self.add_query_param('Override', Override)
	def get_SchedulerOptions(self): # Json
		return self.get_query_params().get('SchedulerOptions')

	def set_SchedulerOptions(self, SchedulerOptions):  # Json
		self.add_query_param('SchedulerOptions', SchedulerOptions)
	def get_DeploymentSetId(self): # String
		return self.get_query_params().get('DeploymentSetId')

	def set_DeploymentSetId(self, DeploymentSetId):  # String
		self.add_query_param('DeploymentSetId', DeploymentSetId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_Tenancy(self): # String
		return self.get_query_params().get('Tenancy')

	def set_Tenancy(self, Tenancy):  # String
		self.add_query_param('Tenancy', Tenancy)
	def get_SystemDiskDiskName(self): # String
		return self.get_query_params().get('SystemDisk.DiskName')

	def set_SystemDiskDiskName(self, SystemDiskDiskName):  # String
		self.add_query_param('SystemDisk.DiskName', SystemDiskDiskName)
	def get_RamRoleName(self): # String
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self, RamRoleName):  # String
		self.add_query_param('RamRoleName', RamRoleName)
	def get_SystemDiskEncryptAlgorithm(self): # String
		return self.get_query_params().get('SystemDisk.EncryptAlgorithm')

	def set_SystemDiskEncryptAlgorithm(self, SystemDiskEncryptAlgorithm):  # String
		self.add_query_param('SystemDisk.EncryptAlgorithm', SystemDiskEncryptAlgorithm)
	def get_DedicatedHostId(self): # String
		return self.get_query_params().get('DedicatedHostId')

	def set_DedicatedHostId(self, DedicatedHostId):  # String
		self.add_query_param('DedicatedHostId', DedicatedHostId)
	def get_CreditSpecification(self): # String
		return self.get_query_params().get('CreditSpecification')

	def set_CreditSpecification(self, CreditSpecification):  # String
		self.add_query_param('CreditSpecification', CreditSpecification)
	def get_SpotDuration(self): # Integer
		return self.get_query_params().get('SpotDuration')

	def set_SpotDuration(self, SpotDuration):  # Integer
		self.add_query_param('SpotDuration', SpotDuration)
	def get_SecurityGroupIdss(self): # RepeatList
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIdss(self, SecurityGroupIds):  # RepeatList
		for depth1 in range(len(SecurityGroupIds)):
			self.add_query_param('SecurityGroupIds.' + str(depth1 + 1), SecurityGroupIds[depth1])
	def get_DataDisks(self): # RepeatList
		return self.get_query_params().get('DataDisk')

	def set_DataDisks(self, DataDisk):  # RepeatList
		for depth1 in range(len(DataDisk)):
			if DataDisk[depth1].get('SnapshotId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.SnapshotId', DataDisk[depth1].get('SnapshotId'))
			if DataDisk[depth1].get('PerformanceLevel') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.PerformanceLevel', DataDisk[depth1].get('PerformanceLevel'))
			if DataDisk[depth1].get('AutoSnapshotPolicyId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.AutoSnapshotPolicyId', DataDisk[depth1].get('AutoSnapshotPolicyId'))
			if DataDisk[depth1].get('Description') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Description', DataDisk[depth1].get('Description'))
			if DataDisk[depth1].get('BurstingEnabled') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.BurstingEnabled', DataDisk[depth1].get('BurstingEnabled'))
			if DataDisk[depth1].get('DiskName') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DiskName', DataDisk[depth1].get('DiskName'))
			if DataDisk[depth1].get('ProvisionedIops') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.ProvisionedIops', DataDisk[depth1].get('ProvisionedIops'))
			if DataDisk[depth1].get('Encrypted') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Encrypted', DataDisk[depth1].get('Encrypted'))
			if DataDisk[depth1].get('Size') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Size', DataDisk[depth1].get('Size'))
			if DataDisk[depth1].get('Categories') is not None:
				for depth2 in range(len(DataDisk[depth1].get('Categories'))):
					self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Categories.' + str(depth2 + 1), DataDisk[depth1].get('Categories')[depth2])
			if DataDisk[depth1].get('Category') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Category', DataDisk[depth1].get('Category'))
			if DataDisk[depth1].get('KMSKeyId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.KMSKeyId', DataDisk[depth1].get('KMSKeyId'))
			if DataDisk[depth1].get('Device') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Device', DataDisk[depth1].get('Device'))
			if DataDisk[depth1].get('DeleteWithInstance') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DeleteWithInstance', DataDisk[depth1].get('DeleteWithInstance'))
	def get_InstanceTypeOverrides(self): # RepeatList
		return self.get_query_params().get('InstanceTypeOverride')

	def set_InstanceTypeOverrides(self, InstanceTypeOverride):  # RepeatList
		for depth1 in range(len(InstanceTypeOverride)):
			if InstanceTypeOverride[depth1].get('WeightedCapacity') is not None:
				self.add_query_param('InstanceTypeOverride.' + str(depth1 + 1) + '.WeightedCapacity', InstanceTypeOverride[depth1].get('WeightedCapacity'))
			if InstanceTypeOverride[depth1].get('InstanceType') is not None:
				self.add_query_param('InstanceTypeOverride.' + str(depth1 + 1) + '.InstanceType', InstanceTypeOverride[depth1].get('InstanceType'))
	def get_SystemDiskProvisionedIops(self): # Long
		return self.get_query_params().get('SystemDisk.ProvisionedIops')

	def set_SystemDiskProvisionedIops(self, SystemDiskProvisionedIops):  # Long
		self.add_query_param('SystemDisk.ProvisionedIops', SystemDiskProvisionedIops)
	def get_LoadBalancerWeight(self): # Integer
		return self.get_query_params().get('LoadBalancerWeight')

	def set_LoadBalancerWeight(self, LoadBalancerWeight):  # Integer
		self.add_query_param('LoadBalancerWeight', LoadBalancerWeight)
	def get_SystemDiskSize(self): # Integer
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self, SystemDiskSize):  # Integer
		self.add_query_param('SystemDisk.Size', SystemDiskSize)
	def get_ImageFamily(self): # String
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self, ImageFamily):  # String
		self.add_query_param('ImageFamily', ImageFamily)
	def get_SystemDiskDescription(self): # String
		return self.get_query_params().get('SystemDisk.Description')

	def set_SystemDiskDescription(self, SystemDiskDescription):  # String
		self.add_query_param('SystemDisk.Description', SystemDiskDescription)
	def get_SystemDiskEncrypted(self): # Boolean
		return self.get_query_params().get('SystemDisk.Encrypted')

	def set_SystemDiskEncrypted(self, SystemDiskEncrypted):  # Boolean
		self.add_query_param('SystemDisk.Encrypted', SystemDiskEncrypted)
