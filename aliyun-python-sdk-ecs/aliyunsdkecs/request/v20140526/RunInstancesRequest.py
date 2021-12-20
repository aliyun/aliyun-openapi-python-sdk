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

class RunInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'RunInstances','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UniqueSuffix(self): # Boolean
		return self.get_query_params().get('UniqueSuffix')

	def set_UniqueSuffix(self, UniqueSuffix):  # Boolean
		self.add_query_param('UniqueSuffix', UniqueSuffix)
	def get_SecurityEnhancementStrategy(self): # String
		return self.get_query_params().get('SecurityEnhancementStrategy')

	def set_SecurityEnhancementStrategy(self, SecurityEnhancementStrategy):  # String
		self.add_query_param('SecurityEnhancementStrategy', SecurityEnhancementStrategy)
	def get_MinAmount(self): # Integer
		return self.get_query_params().get('MinAmount')

	def set_MinAmount(self, MinAmount):  # Integer
		self.add_query_param('MinAmount', MinAmount)
	def get_DeletionProtection(self): # Boolean
		return self.get_query_params().get('DeletionProtection')

	def set_DeletionProtection(self, DeletionProtection):  # Boolean
		self.add_query_param('DeletionProtection', DeletionProtection)
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
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_SystemDisk(self): # Struct
		return self.get_query_params().get('SystemDisk')

	def set_SystemDisk(self, SystemDisk):  # Struct
		if SystemDisk.get('StorageClusterId') is not None:
			self.add_query_param('SystemDisk.StorageClusterId', SystemDisk.get('StorageClusterId'))
	def get_DeploymentSetGroupNo(self): # Integer
		return self.get_query_params().get('DeploymentSetGroupNo')

	def set_DeploymentSetGroupNo(self, DeploymentSetGroupNo):  # Integer
		self.add_query_param('DeploymentSetGroupNo', DeploymentSetGroupNo)
	def get_SystemDiskAutoSnapshotPolicyId(self): # String
		return self.get_query_params().get('SystemDisk.AutoSnapshotPolicyId')

	def set_SystemDiskAutoSnapshotPolicyId(self, SystemDiskAutoSnapshotPolicyId):  # String
		self.add_query_param('SystemDisk.AutoSnapshotPolicyId', SystemDiskAutoSnapshotPolicyId)
	def get_CpuOptionsCore(self): # Integer
		return self.get_query_params().get('CpuOptions.Core')

	def set_CpuOptionsCore(self, CpuOptionsCore):  # Integer
		self.add_query_param('CpuOptions.Core', CpuOptionsCore)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_CpuOptionsNuma(self): # String
		return self.get_query_params().get('CpuOptions.Numa')

	def set_CpuOptionsNuma(self, CpuOptionsNuma):  # String
		self.add_query_param('CpuOptions.Numa', CpuOptionsNuma)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_PrivateIpAddress(self): # String
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self, PrivateIpAddress):  # String
		self.add_query_param('PrivateIpAddress', PrivateIpAddress)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_InternetMaxBandwidthIn(self): # Integer
		return self.get_query_params().get('InternetMaxBandwidthIn')

	def set_InternetMaxBandwidthIn(self, InternetMaxBandwidthIn):  # Integer
		self.add_query_param('InternetMaxBandwidthIn', InternetMaxBandwidthIn)
	def get_Affinity(self): # String
		return self.get_query_params().get('Affinity')

	def set_Affinity(self, Affinity):  # String
		self.add_query_param('Affinity', Affinity)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_SpotInterruptionBehavior(self): # String
		return self.get_query_params().get('SpotInterruptionBehavior')

	def set_SpotInterruptionBehavior(self, SpotInterruptionBehavior):  # String
		self.add_query_param('SpotInterruptionBehavior', SpotInterruptionBehavior)
	def get_NetworkInterfaceQueueNumber(self): # Integer
		return self.get_query_params().get('NetworkInterfaceQueueNumber')

	def set_NetworkInterfaceQueueNumber(self, NetworkInterfaceQueueNumber):  # Integer
		self.add_query_param('NetworkInterfaceQueueNumber', NetworkInterfaceQueueNumber)
	def get_IoOptimized(self): # String
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self, IoOptimized):  # String
		self.add_query_param('IoOptimized', IoOptimized)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_HibernationOptionsConfigured(self): # Boolean
		return self.get_query_params().get('HibernationOptions.Configured')

	def set_HibernationOptionsConfigured(self, HibernationOptionsConfigured):  # Boolean
		self.add_query_param('HibernationOptions.Configured', HibernationOptionsConfigured)
	def get_SystemDiskPerformanceLevel(self): # String
		return self.get_query_params().get('SystemDisk.PerformanceLevel')

	def set_SystemDiskPerformanceLevel(self, SystemDiskPerformanceLevel):  # String
		self.add_query_param('SystemDisk.PerformanceLevel', SystemDiskPerformanceLevel)
	def get_PasswordInherit(self): # Boolean
		return self.get_query_params().get('PasswordInherit')

	def set_PasswordInherit(self, PasswordInherit):  # Boolean
		self.add_query_param('PasswordInherit', PasswordInherit)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_Arns(self): # RepeatList
		return self.get_query_params().get('Arn')

	def set_Arns(self, Arn):  # RepeatList
		for depth1 in range(len(Arn)):
			if Arn[depth1].get('RoleType') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.RoleType', Arn[depth1].get('RoleType'))
			if Arn[depth1].get('Rolearn') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.Rolearn', Arn[depth1].get('Rolearn'))
			if Arn[depth1].get('AssumeRoleFor') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.AssumeRoleFor', Arn[depth1].get('AssumeRoleFor'))
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_SchedulerOptionsDedicatedHostClusterId(self): # String
		return self.get_query_params().get('SchedulerOptions.DedicatedHostClusterId')

	def set_SchedulerOptionsDedicatedHostClusterId(self, SchedulerOptionsDedicatedHostClusterId):  # String
		self.add_query_param('SchedulerOptions.DedicatedHostClusterId', SchedulerOptionsDedicatedHostClusterId)
	def get_SystemDiskDiskName(self): # String
		return self.get_query_params().get('SystemDisk.DiskName')

	def set_SystemDiskDiskName(self, SystemDiskDiskName):  # String
		self.add_query_param('SystemDisk.DiskName', SystemDiskDiskName)
	def get_DedicatedHostId(self): # String
		return self.get_query_params().get('DedicatedHostId')

	def set_DedicatedHostId(self, DedicatedHostId):  # String
		self.add_query_param('DedicatedHostId', DedicatedHostId)
	def get_SpotDuration(self): # Integer
		return self.get_query_params().get('SpotDuration')

	def set_SpotDuration(self, SpotDuration):  # Integer
		self.add_query_param('SpotDuration', SpotDuration)
	def get_SecurityGroupIdss(self): # RepeatList
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIdss(self, SecurityGroupIds):  # RepeatList
		for depth1 in range(len(SecurityGroupIds)):
			self.add_query_param('SecurityGroupIds.' + str(depth1 + 1), SecurityGroupIds[depth1])
	def get_SystemDiskSize(self): # String
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self, SystemDiskSize):  # String
		self.add_query_param('SystemDisk.Size', SystemDiskSize)
	def get_ImageFamily(self): # String
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self, ImageFamily):  # String
		self.add_query_param('ImageFamily', ImageFamily)
	def get_LaunchTemplateName(self): # String
		return self.get_query_params().get('LaunchTemplateName')

	def set_LaunchTemplateName(self, LaunchTemplateName):  # String
		self.add_query_param('LaunchTemplateName', LaunchTemplateName)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_HpcClusterId(self): # String
		return self.get_query_params().get('HpcClusterId')

	def set_HpcClusterId(self, HpcClusterId):  # String
		self.add_query_param('HpcClusterId', HpcClusterId)
	def get_HttpPutResponseHopLimit(self): # Integer
		return self.get_query_params().get('HttpPutResponseHopLimit')

	def set_HttpPutResponseHopLimit(self, HttpPutResponseHopLimit):  # Integer
		self.add_query_param('HttpPutResponseHopLimit', HttpPutResponseHopLimit)
	def get_Isp(self): # String
		return self.get_query_params().get('Isp')

	def set_Isp(self, Isp):  # String
		self.add_query_param('Isp', Isp)
	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_SpotPriceLimit(self): # Float
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self, SpotPriceLimit):  # Float
		self.add_query_param('SpotPriceLimit', SpotPriceLimit)
	def get_StorageSetPartitionNumber(self): # Integer
		return self.get_query_params().get('StorageSetPartitionNumber')

	def set_StorageSetPartitionNumber(self, StorageSetPartitionNumber):  # Integer
		self.add_query_param('StorageSetPartitionNumber', StorageSetPartitionNumber)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
	def get_PrivatePoolOptionsId(self): # String
		return self.get_query_params().get('PrivatePoolOptions.Id')

	def set_PrivatePoolOptionsId(self, PrivatePoolOptionsId):  # String
		self.add_query_param('PrivatePoolOptions.Id', PrivatePoolOptionsId)
	def get_AutoRenewPeriod(self): # Integer
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self, AutoRenewPeriod):  # Integer
		self.add_query_param('AutoRenewPeriod', AutoRenewPeriod)
	def get_LaunchTemplateId(self): # String
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self, LaunchTemplateId):  # String
		self.add_query_param('LaunchTemplateId', LaunchTemplateId)
	def get_Ipv6AddressCount(self): # Integer
		return self.get_query_params().get('Ipv6AddressCount')

	def set_Ipv6AddressCount(self, Ipv6AddressCount):  # Integer
		self.add_query_param('Ipv6AddressCount', Ipv6AddressCount)
	def get_HostNamess(self): # RepeatList
		return self.get_query_params().get('HostNames')

	def set_HostNamess(self, HostNames):  # RepeatList
		for depth1 in range(len(HostNames)):
			self.add_query_param('HostNames.' + str(depth1 + 1), HostNames[depth1])
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_Ipv6Addresss(self): # RepeatList
		return self.get_query_params().get('Ipv6Address')

	def set_Ipv6Addresss(self, Ipv6Address):  # RepeatList
		for depth1 in range(len(Ipv6Address)):
			self.add_query_param('Ipv6Address.' + str(depth1 + 1), Ipv6Address[depth1])
	def get_SecurityOptionsConfidentialComputingMode(self): # String
		return self.get_query_params().get('SecurityOptions.ConfidentialComputingMode')

	def set_SecurityOptionsConfidentialComputingMode(self, SecurityOptionsConfidentialComputingMode):  # String
		self.add_query_param('SecurityOptions.ConfidentialComputingMode', SecurityOptionsConfidentialComputingMode)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_InternetMaxBandwidthOut(self): # Integer
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):  # Integer
		self.add_query_param('InternetMaxBandwidthOut', InternetMaxBandwidthOut)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_CpuOptionsThreadsPerCore(self): # Integer
		return self.get_query_params().get('CpuOptions.ThreadsPerCore')

	def set_CpuOptionsThreadsPerCore(self, CpuOptionsThreadsPerCore):  # Integer
		self.add_query_param('CpuOptions.ThreadsPerCore', CpuOptionsThreadsPerCore)
	def get_SystemDiskCategory(self): # String
		return self.get_query_params().get('SystemDisk.Category')

	def set_SystemDiskCategory(self, SystemDiskCategory):  # String
		self.add_query_param('SystemDisk.Category', SystemDiskCategory)
	def get_SecurityOptionsTrustedSystemMode(self): # String
		return self.get_query_params().get('SecurityOptions.TrustedSystemMode')

	def set_SecurityOptionsTrustedSystemMode(self, SecurityOptionsTrustedSystemMode):  # String
		self.add_query_param('SecurityOptions.TrustedSystemMode', SecurityOptionsTrustedSystemMode)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_HttpEndpoint(self): # String
		return self.get_query_params().get('HttpEndpoint')

	def set_HttpEndpoint(self, HttpEndpoint):  # String
		self.add_query_param('HttpEndpoint', HttpEndpoint)
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_DeploymentSetId(self): # String
		return self.get_query_params().get('DeploymentSetId')

	def set_DeploymentSetId(self, DeploymentSetId):  # String
		self.add_query_param('DeploymentSetId', DeploymentSetId)
	def get_NetworkInterfaces(self): # RepeatList
		return self.get_query_params().get('NetworkInterface')

	def set_NetworkInterfaces(self, NetworkInterface):  # RepeatList
		for depth1 in range(len(NetworkInterface)):
			if NetworkInterface[depth1].get('VSwitchId') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.VSwitchId', NetworkInterface[depth1].get('VSwitchId'))
			if NetworkInterface[depth1].get('NetworkInterfaceName') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.NetworkInterfaceName', NetworkInterface[depth1].get('NetworkInterfaceName'))
			if NetworkInterface[depth1].get('Description') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.Description', NetworkInterface[depth1].get('Description'))
			if NetworkInterface[depth1].get('SecurityGroupId') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.SecurityGroupId', NetworkInterface[depth1].get('SecurityGroupId'))
			if NetworkInterface[depth1].get('PrimaryIpAddress') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.PrimaryIpAddress', NetworkInterface[depth1].get('PrimaryIpAddress'))
			if NetworkInterface[depth1].get('QueueNumber') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.QueueNumber', NetworkInterface[depth1].get('QueueNumber'))
			if NetworkInterface[depth1].get('SecurityGroupIds') is not None:
				for depth2 in range(len(NetworkInterface[depth1].get('SecurityGroupIds'))):
					self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.SecurityGroupIds' + str(depth2 + 1), NetworkInterface[depth1].get('SecurityGroupIds')[depth2])
			if NetworkInterface[depth1].get('NetworkInterfaceTrafficMode') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.NetworkInterfaceTrafficMode', NetworkInterface[depth1].get('NetworkInterfaceTrafficMode'))
			if NetworkInterface[depth1].get('QueuePairNumber') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.QueuePairNumber', NetworkInterface[depth1].get('QueuePairNumber'))
			if NetworkInterface[depth1].get('InstanceType') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.InstanceType', NetworkInterface[depth1].get('InstanceType'))
			if NetworkInterface[depth1].get('Ipv6AddressCount') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.Ipv6AddressCount', NetworkInterface[depth1].get('Ipv6AddressCount'))
			if NetworkInterface[depth1].get('Ipv6Address') is not None:
				for depth2 in range(len(NetworkInterface[depth1].get('Ipv6Address'))):
					self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.Ipv6Address' + str(depth2 + 1), NetworkInterface[depth1].get('Ipv6Address')[depth2])
	def get_Amount(self): # Integer
		return self.get_query_params().get('Amount')

	def set_Amount(self, Amount):  # Integer
		self.add_query_param('Amount', Amount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_Tenancy(self): # String
		return self.get_query_params().get('Tenancy')

	def set_Tenancy(self, Tenancy):  # String
		self.add_query_param('Tenancy', Tenancy)
	def get_RamRoleName(self): # String
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self, RamRoleName):  # String
		self.add_query_param('RamRoleName', RamRoleName)
	def get_AutoReleaseTime(self): # String
		return self.get_query_params().get('AutoReleaseTime')

	def set_AutoReleaseTime(self, AutoReleaseTime):  # String
		self.add_query_param('AutoReleaseTime', AutoReleaseTime)
	def get_CreditSpecification(self): # String
		return self.get_query_params().get('CreditSpecification')

	def set_CreditSpecification(self, CreditSpecification):  # String
		self.add_query_param('CreditSpecification', CreditSpecification)
	def get_LaunchTemplateVersion(self): # Long
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self, LaunchTemplateVersion):  # Long
		self.add_query_param('LaunchTemplateVersion', LaunchTemplateVersion)
	def get_DataDisks(self): # RepeatList
		return self.get_query_params().get('DataDisk')

	def set_DataDisks(self, DataDisk):  # RepeatList
		for depth1 in range(len(DataDisk)):
			if DataDisk[depth1].get('PerformanceLevel') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.PerformanceLevel', DataDisk[depth1].get('PerformanceLevel'))
			if DataDisk[depth1].get('AutoSnapshotPolicyId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.AutoSnapshotPolicyId', DataDisk[depth1].get('AutoSnapshotPolicyId'))
			if DataDisk[depth1].get('Encrypted') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Encrypted', DataDisk[depth1].get('Encrypted'))
			if DataDisk[depth1].get('Description') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Description', DataDisk[depth1].get('Description'))
			if DataDisk[depth1].get('SnapshotId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.SnapshotId', DataDisk[depth1].get('SnapshotId'))
			if DataDisk[depth1].get('Device') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Device', DataDisk[depth1].get('Device'))
			if DataDisk[depth1].get('Size') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Size', DataDisk[depth1].get('Size'))
			if DataDisk[depth1].get('DiskName') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DiskName', DataDisk[depth1].get('DiskName'))
			if DataDisk[depth1].get('Category') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Category', DataDisk[depth1].get('Category'))
			if DataDisk[depth1].get('EncryptAlgorithm') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.EncryptAlgorithm', DataDisk[depth1].get('EncryptAlgorithm'))
			if DataDisk[depth1].get('DeleteWithInstance') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DeleteWithInstance', DataDisk[depth1].get('DeleteWithInstance'))
			if DataDisk[depth1].get('KMSKeyId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.KMSKeyId', DataDisk[depth1].get('KMSKeyId'))
			if DataDisk[depth1].get('StorageClusterId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.StorageClusterId', DataDisk[depth1].get('StorageClusterId'))
	def get_StorageSetId(self): # String
		return self.get_query_params().get('StorageSetId')

	def set_StorageSetId(self, StorageSetId):  # String
		self.add_query_param('StorageSetId', StorageSetId)
	def get_HttpTokens(self): # String
		return self.get_query_params().get('HttpTokens')

	def set_HttpTokens(self, HttpTokens):  # String
		self.add_query_param('HttpTokens', HttpTokens)
	def get_SystemDiskDescription(self): # String
		return self.get_query_params().get('SystemDisk.Description')

	def set_SystemDiskDescription(self, SystemDiskDescription):  # String
		self.add_query_param('SystemDisk.Description', SystemDiskDescription)
