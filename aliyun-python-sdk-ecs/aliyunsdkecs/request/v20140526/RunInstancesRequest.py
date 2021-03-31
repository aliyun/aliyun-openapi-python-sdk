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


	def get_UniqueSuffix(self):
		return self.get_query_params().get('UniqueSuffix')

	def set_UniqueSuffix(self,UniqueSuffix):
		self.add_query_param('UniqueSuffix',UniqueSuffix)

	def get_SecurityEnhancementStrategy(self):
		return self.get_query_params().get('SecurityEnhancementStrategy')

	def set_SecurityEnhancementStrategy(self,SecurityEnhancementStrategy):
		self.add_query_param('SecurityEnhancementStrategy',SecurityEnhancementStrategy)

	def get_MinAmount(self):
		return self.get_query_params().get('MinAmount')

	def set_MinAmount(self,MinAmount):
		self.add_query_param('MinAmount',MinAmount)

	def get_DeletionProtection(self):
		return self.get_query_params().get('DeletionProtection')

	def set_DeletionProtection(self,DeletionProtection):
		self.add_query_param('DeletionProtection',DeletionProtection)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_PrivatePoolOptionsMatchCriteria(self):
		return self.get_query_params().get('PrivatePoolOptions.MatchCriteria')

	def set_PrivatePoolOptionsMatchCriteria(self,PrivatePoolOptionsMatchCriteria):
		self.add_query_param('PrivatePoolOptions.MatchCriteria',PrivatePoolOptionsMatchCriteria)

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_DeploymentSetGroupNo(self):
		return self.get_query_params().get('DeploymentSetGroupNo')

	def set_DeploymentSetGroupNo(self,DeploymentSetGroupNo):
		self.add_query_param('DeploymentSetGroupNo',DeploymentSetGroupNo)

	def get_SystemDiskAutoSnapshotPolicyId(self):
		return self.get_query_params().get('SystemDisk.AutoSnapshotPolicyId')

	def set_SystemDiskAutoSnapshotPolicyId(self,SystemDiskAutoSnapshotPolicyId):
		self.add_query_param('SystemDisk.AutoSnapshotPolicyId',SystemDiskAutoSnapshotPolicyId)

	def get_CpuOptionsCore(self):
		return self.get_query_params().get('CpuOptions.Core')

	def set_CpuOptionsCore(self,CpuOptionsCore):
		self.add_query_param('CpuOptions.Core',CpuOptionsCore)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_CpuOptionsNuma(self):
		return self.get_query_params().get('CpuOptions.Numa')

	def set_CpuOptionsNuma(self,CpuOptionsNuma):
		self.add_query_param('CpuOptions.Numa',CpuOptionsNuma)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SpotStrategy(self):
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self,SpotStrategy):
		self.add_query_param('SpotStrategy',SpotStrategy)

	def get_PrivateIpAddress(self):
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self,PrivateIpAddress):
		self.add_query_param('PrivateIpAddress',PrivateIpAddress)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_InternetMaxBandwidthIn(self):
		return self.get_query_params().get('InternetMaxBandwidthIn')

	def set_InternetMaxBandwidthIn(self,InternetMaxBandwidthIn):
		self.add_query_param('InternetMaxBandwidthIn',InternetMaxBandwidthIn)

	def get_Affinity(self):
		return self.get_query_params().get('Affinity')

	def set_Affinity(self,Affinity):
		self.add_query_param('Affinity',Affinity)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_SpotInterruptionBehavior(self):
		return self.get_query_params().get('SpotInterruptionBehavior')

	def set_SpotInterruptionBehavior(self,SpotInterruptionBehavior):
		self.add_query_param('SpotInterruptionBehavior',SpotInterruptionBehavior)

	def get_NetworkInterfaceQueueNumber(self):
		return self.get_query_params().get('NetworkInterfaceQueueNumber')

	def set_NetworkInterfaceQueueNumber(self,NetworkInterfaceQueueNumber):
		self.add_query_param('NetworkInterfaceQueueNumber',NetworkInterfaceQueueNumber)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_HibernationOptionsConfigured(self):
		return self.get_query_params().get('HibernationOptions.Configured')

	def set_HibernationOptionsConfigured(self,HibernationOptionsConfigured):
		self.add_query_param('HibernationOptions.Configured',HibernationOptionsConfigured)

	def get_SystemDiskPerformanceLevel(self):
		return self.get_query_params().get('SystemDisk.PerformanceLevel')

	def set_SystemDiskPerformanceLevel(self,SystemDiskPerformanceLevel):
		self.add_query_param('SystemDisk.PerformanceLevel',SystemDiskPerformanceLevel)

	def get_PasswordInherit(self):
		return self.get_query_params().get('PasswordInherit')

	def set_PasswordInherit(self,PasswordInherit):
		self.add_query_param('PasswordInherit',PasswordInherit)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_Arns(self):
		return self.get_query_params().get('Arn')

	def set_Arns(self, Arns):
		for depth1 in range(len(Arns)):
			if Arns[depth1].get('AssumeRoleFor') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.AssumeRoleFor', Arns[depth1].get('AssumeRoleFor'))
			if Arns[depth1].get('Rolearn') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.Rolearn', Arns[depth1].get('Rolearn'))
			if Arns[depth1].get('RoleType') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.RoleType', Arns[depth1].get('RoleType'))

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_SchedulerOptionsDedicatedHostClusterId(self):
		return self.get_query_params().get('SchedulerOptions.DedicatedHostClusterId')

	def set_SchedulerOptionsDedicatedHostClusterId(self,SchedulerOptionsDedicatedHostClusterId):
		self.add_query_param('SchedulerOptions.DedicatedHostClusterId',SchedulerOptionsDedicatedHostClusterId)

	def get_SystemDiskDiskName(self):
		return self.get_query_params().get('SystemDisk.DiskName')

	def set_SystemDiskDiskName(self,SystemDiskDiskName):
		self.add_query_param('SystemDisk.DiskName',SystemDiskDiskName)

	def get_DedicatedHostId(self):
		return self.get_query_params().get('DedicatedHostId')

	def set_DedicatedHostId(self,DedicatedHostId):
		self.add_query_param('DedicatedHostId',DedicatedHostId)

	def get_SecurityGroupIdss(self):
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIdss(self, SecurityGroupIdss):
		for depth1 in range(len(SecurityGroupIdss)):
			if SecurityGroupIdss[depth1] is not None:
				self.add_query_param('SecurityGroupIds.' + str(depth1 + 1) , SecurityGroupIdss[depth1])

	def get_SpotDuration(self):
		return self.get_query_params().get('SpotDuration')

	def set_SpotDuration(self,SpotDuration):
		self.add_query_param('SpotDuration',SpotDuration)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDisk.Size',SystemDiskSize)

	def get_ImageFamily(self):
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self,ImageFamily):
		self.add_query_param('ImageFamily',ImageFamily)

	def get_LaunchTemplateName(self):
		return self.get_query_params().get('LaunchTemplateName')

	def set_LaunchTemplateName(self,LaunchTemplateName):
		self.add_query_param('LaunchTemplateName',LaunchTemplateName)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_HpcClusterId(self):
		return self.get_query_params().get('HpcClusterId')

	def set_HpcClusterId(self,HpcClusterId):
		self.add_query_param('HpcClusterId',HpcClusterId)

	def get_HttpPutResponseHopLimit(self):
		return self.get_query_params().get('HttpPutResponseHopLimit')

	def set_HttpPutResponseHopLimit(self,HttpPutResponseHopLimit):
		self.add_query_param('HttpPutResponseHopLimit',HttpPutResponseHopLimit)

	def get_Isp(self):
		return self.get_query_params().get('Isp')

	def set_Isp(self,Isp):
		self.add_query_param('Isp',Isp)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_SpotPriceLimit(self):
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self,SpotPriceLimit):
		self.add_query_param('SpotPriceLimit',SpotPriceLimit)

	def get_StorageSetPartitionNumber(self):
		return self.get_query_params().get('StorageSetPartitionNumber')

	def set_StorageSetPartitionNumber(self,StorageSetPartitionNumber):
		self.add_query_param('StorageSetPartitionNumber',StorageSetPartitionNumber)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))

	def get_PrivatePoolOptionsId(self):
		return self.get_query_params().get('PrivatePoolOptions.Id')

	def set_PrivatePoolOptionsId(self,PrivatePoolOptionsId):
		self.add_query_param('PrivatePoolOptions.Id',PrivatePoolOptionsId)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_LaunchTemplateId(self):
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self,LaunchTemplateId):
		self.add_query_param('LaunchTemplateId',LaunchTemplateId)

	def get_Ipv6AddressCount(self):
		return self.get_query_params().get('Ipv6AddressCount')

	def set_Ipv6AddressCount(self,Ipv6AddressCount):
		self.add_query_param('Ipv6AddressCount',Ipv6AddressCount)

	def get_HostNamess(self):
		return self.get_query_params().get('HostNames')

	def set_HostNamess(self, HostNamess):
		for depth1 in range(len(HostNamess)):
			if HostNamess[depth1] is not None:
				self.add_query_param('HostNames.' + str(depth1 + 1) , HostNamess[depth1])

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_Ipv6Addresss(self):
		return self.get_query_params().get('Ipv6Address')

	def set_Ipv6Addresss(self, Ipv6Addresss):
		for depth1 in range(len(Ipv6Addresss)):
			if Ipv6Addresss[depth1] is not None:
				self.add_query_param('Ipv6Address.' + str(depth1 + 1) , Ipv6Addresss[depth1])

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_InternetMaxBandwidthOut(self):
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self,InternetMaxBandwidthOut):
		self.add_query_param('InternetMaxBandwidthOut',InternetMaxBandwidthOut)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_CpuOptionsThreadsPerCore(self):
		return self.get_query_params().get('CpuOptions.ThreadsPerCore')

	def set_CpuOptionsThreadsPerCore(self,CpuOptionsThreadsPerCore):
		self.add_query_param('CpuOptions.ThreadsPerCore',CpuOptionsThreadsPerCore)

	def get_SystemDiskCategory(self):
		return self.get_query_params().get('SystemDisk.Category')

	def set_SystemDiskCategory(self,SystemDiskCategory):
		self.add_query_param('SystemDisk.Category',SystemDiskCategory)

	def get_SecurityOptionsTrustedSystemMode(self):
		return self.get_query_params().get('SecurityOptions.TrustedSystemMode')

	def set_SecurityOptionsTrustedSystemMode(self,SecurityOptionsTrustedSystemMode):
		self.add_query_param('SecurityOptions.TrustedSystemMode',SecurityOptionsTrustedSystemMode)

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_HttpEndpoint(self):
		return self.get_query_params().get('HttpEndpoint')

	def set_HttpEndpoint(self,HttpEndpoint):
		self.add_query_param('HttpEndpoint',HttpEndpoint)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_NetworkInterfaces(self):
		return self.get_query_params().get('NetworkInterface')

	def set_NetworkInterfaces(self, NetworkInterfaces):
		for depth1 in range(len(NetworkInterfaces)):
			if NetworkInterfaces[depth1].get('PrimaryIpAddress') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.PrimaryIpAddress', NetworkInterfaces[depth1].get('PrimaryIpAddress'))
			if NetworkInterfaces[depth1].get('VSwitchId') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.VSwitchId', NetworkInterfaces[depth1].get('VSwitchId'))
			if NetworkInterfaces[depth1].get('SecurityGroupId') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.SecurityGroupId', NetworkInterfaces[depth1].get('SecurityGroupId'))
			if NetworkInterfaces[depth1].get('SecurityGroupIds') is not None:
				for depth2 in range(len(NetworkInterfaces[depth1].get('SecurityGroupIds'))):
					if NetworkInterfaces[depth1].get('SecurityGroupIds')[depth2] is not None:
						self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.SecurityGroupIds.' + str(depth2 + 1) , NetworkInterfaces[depth1].get('SecurityGroupIds')[depth2])
			if NetworkInterfaces[depth1].get('NetworkInterfaceName') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.NetworkInterfaceName', NetworkInterfaces[depth1].get('NetworkInterfaceName'))
			if NetworkInterfaces[depth1].get('Description') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.Description', NetworkInterfaces[depth1].get('Description'))
			if NetworkInterfaces[depth1].get('QueueNumber') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.QueueNumber', NetworkInterfaces[depth1].get('QueueNumber'))

	def get_DeploymentSetId(self):
		return self.get_query_params().get('DeploymentSetId')

	def set_DeploymentSetId(self,DeploymentSetId):
		self.add_query_param('DeploymentSetId',DeploymentSetId)

	def get_Amount(self):
		return self.get_query_params().get('Amount')

	def set_Amount(self,Amount):
		self.add_query_param('Amount',Amount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Tenancy(self):
		return self.get_query_params().get('Tenancy')

	def set_Tenancy(self,Tenancy):
		self.add_query_param('Tenancy',Tenancy)

	def get_RamRoleName(self):
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self,RamRoleName):
		self.add_query_param('RamRoleName',RamRoleName)

	def get_AutoReleaseTime(self):
		return self.get_query_params().get('AutoReleaseTime')

	def set_AutoReleaseTime(self,AutoReleaseTime):
		self.add_query_param('AutoReleaseTime',AutoReleaseTime)

	def get_CreditSpecification(self):
		return self.get_query_params().get('CreditSpecification')

	def set_CreditSpecification(self,CreditSpecification):
		self.add_query_param('CreditSpecification',CreditSpecification)

	def get_DataDisks(self):
		return self.get_query_params().get('DataDisk')

	def set_DataDisks(self, DataDisks):
		for depth1 in range(len(DataDisks)):
			if DataDisks[depth1].get('Size') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Size', DataDisks[depth1].get('Size'))
			if DataDisks[depth1].get('SnapshotId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.SnapshotId', DataDisks[depth1].get('SnapshotId'))
			if DataDisks[depth1].get('Category') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Category', DataDisks[depth1].get('Category'))
			if DataDisks[depth1].get('Encrypted') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Encrypted', DataDisks[depth1].get('Encrypted'))
			if DataDisks[depth1].get('KMSKeyId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.KMSKeyId', DataDisks[depth1].get('KMSKeyId'))
			if DataDisks[depth1].get('DiskName') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DiskName', DataDisks[depth1].get('DiskName'))
			if DataDisks[depth1].get('Description') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Description', DataDisks[depth1].get('Description'))
			if DataDisks[depth1].get('Device') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Device', DataDisks[depth1].get('Device'))
			if DataDisks[depth1].get('DeleteWithInstance') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DeleteWithInstance', DataDisks[depth1].get('DeleteWithInstance'))
			if DataDisks[depth1].get('PerformanceLevel') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.PerformanceLevel', DataDisks[depth1].get('PerformanceLevel'))
			if DataDisks[depth1].get('AutoSnapshotPolicyId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.AutoSnapshotPolicyId', DataDisks[depth1].get('AutoSnapshotPolicyId'))
			if DataDisks[depth1].get('EncryptAlgorithm') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.EncryptAlgorithm', DataDisks[depth1].get('EncryptAlgorithm'))

	def get_LaunchTemplateVersion(self):
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self,LaunchTemplateVersion):
		self.add_query_param('LaunchTemplateVersion',LaunchTemplateVersion)

	def get_StorageSetId(self):
		return self.get_query_params().get('StorageSetId')

	def set_StorageSetId(self,StorageSetId):
		self.add_query_param('StorageSetId',StorageSetId)

	def get_HttpTokens(self):
		return self.get_query_params().get('HttpTokens')

	def set_HttpTokens(self,HttpTokens):
		self.add_query_param('HttpTokens',HttpTokens)

	def get_SystemDiskDescription(self):
		return self.get_query_params().get('SystemDisk.Description')

	def set_SystemDiskDescription(self,SystemDiskDescription):
		self.add_query_param('SystemDisk.Description',SystemDiskDescription)