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
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LaunchTemplateName(self):
		return self.get_query_params().get('LaunchTemplateName')

	def set_LaunchTemplateName(self,LaunchTemplateName):
		self.add_query_param('LaunchTemplateName',LaunchTemplateName)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_UniqueSuffix(self):
		return self.get_query_params().get('UniqueSuffix')

	def set_UniqueSuffix(self,UniqueSuffix):
		self.add_query_param('UniqueSuffix',UniqueSuffix)

	def get_HpcClusterId(self):
		return self.get_query_params().get('HpcClusterId')

	def set_HpcClusterId(self,HpcClusterId):
		self.add_query_param('HpcClusterId',HpcClusterId)

	def get_SecurityEnhancementStrategy(self):
		return self.get_query_params().get('SecurityEnhancementStrategy')

	def set_SecurityEnhancementStrategy(self,SecurityEnhancementStrategy):
		self.add_query_param('SecurityEnhancementStrategy',SecurityEnhancementStrategy)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_MinAmount(self):
		return self.get_query_params().get('MinAmount')

	def set_MinAmount(self,MinAmount):
		self.add_query_param('MinAmount',MinAmount)

	def get_SpotPriceLimit(self):
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self,SpotPriceLimit):
		self.add_query_param('SpotPriceLimit',SpotPriceLimit)

	def get_DeletionProtection(self):
		return self.get_query_params().get('DeletionProtection')

	def set_DeletionProtection(self,DeletionProtection):
		self.add_query_param('DeletionProtection',DeletionProtection)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_StorageSetPartitionNumber(self):
		return self.get_query_params().get('StorageSetPartitionNumber')

	def set_StorageSetPartitionNumber(self,StorageSetPartitionNumber):
		self.add_query_param('StorageSetPartitionNumber',StorageSetPartitionNumber)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		for i in range(len(Tags)):	
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key' , Tags[i].get('Key'))
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value' , Tags[i].get('Value'))


	def get_SystemDiskAutoSnapshotPolicyId(self):
		return self.get_query_params().get('SystemDisk.AutoSnapshotPolicyId')

	def set_SystemDiskAutoSnapshotPolicyId(self,SystemDiskAutoSnapshotPolicyId):
		self.add_query_param('SystemDisk.AutoSnapshotPolicyId',SystemDiskAutoSnapshotPolicyId)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

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

	def get_LaunchTemplateId(self):
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self,LaunchTemplateId):
		self.add_query_param('LaunchTemplateId',LaunchTemplateId)

	def get_Ipv6AddressCount(self):
		return self.get_query_params().get('Ipv6AddressCount')

	def set_Ipv6AddressCount(self,Ipv6AddressCount):
		self.add_query_param('Ipv6AddressCount',Ipv6AddressCount)

	def get_CpuOptionsNuma(self):
		return self.get_query_params().get('CpuOptions.Numa')

	def set_CpuOptionsNuma(self,CpuOptionsNuma):
		self.add_query_param('CpuOptions.Numa',CpuOptionsNuma)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

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

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_Ipv6Addresss(self):
		return self.get_query_params().get('Ipv6Addresss')

	def set_Ipv6Addresss(self,Ipv6Addresss):
		for i in range(len(Ipv6Addresss)):	
			if Ipv6Addresss[i] is not None:
				self.add_query_param('Ipv6Address.' + str(i + 1) , Ipv6Addresss[i]);

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

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

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

	def get_SystemDiskPerformanceLevel(self):
		return self.get_query_params().get('SystemDisk.PerformanceLevel')

	def set_SystemDiskPerformanceLevel(self,SystemDiskPerformanceLevel):
		self.add_query_param('SystemDisk.PerformanceLevel',SystemDiskPerformanceLevel)

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_PasswordInherit(self):
		return self.get_query_params().get('PasswordInherit')

	def set_PasswordInherit(self,PasswordInherit):
		self.add_query_param('PasswordInherit',PasswordInherit)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_NetworkInterfaces(self):
		return self.get_query_params().get('NetworkInterfaces')

	def set_NetworkInterfaces(self,NetworkInterfaces):
		for i in range(len(NetworkInterfaces)):	
			if NetworkInterfaces[i].get('PrimaryIpAddress') is not None:
				self.add_query_param('NetworkInterface.' + str(i + 1) + '.PrimaryIpAddress' , NetworkInterfaces[i].get('PrimaryIpAddress'))
			if NetworkInterfaces[i].get('VSwitchId') is not None:
				self.add_query_param('NetworkInterface.' + str(i + 1) + '.VSwitchId' , NetworkInterfaces[i].get('VSwitchId'))
			if NetworkInterfaces[i].get('SecurityGroupId') is not None:
				self.add_query_param('NetworkInterface.' + str(i + 1) + '.SecurityGroupId' , NetworkInterfaces[i].get('SecurityGroupId'))
			for j in range(len(NetworkInterfaces[i].get('SecurityGroupIdss'))):
				if NetworkInterfaces[i].get('SecurityGroupIdss')[j] is not None:
					self.add_query_param('NetworkInterface.' + str(i + 1) + '.SecurityGroupIds.'+str(j + 1), NetworkInterfaces[i].get('SecurityGroupIdss')[j])
			if NetworkInterfaces[i].get('NetworkInterfaceName') is not None:
				self.add_query_param('NetworkInterface.' + str(i + 1) + '.NetworkInterfaceName' , NetworkInterfaces[i].get('NetworkInterfaceName'))
			if NetworkInterfaces[i].get('Description') is not None:
				self.add_query_param('NetworkInterface.' + str(i + 1) + '.Description' , NetworkInterfaces[i].get('Description'))


	def get_DeploymentSetId(self):
		return self.get_query_params().get('DeploymentSetId')

	def set_DeploymentSetId(self,DeploymentSetId):
		self.add_query_param('DeploymentSetId',DeploymentSetId)

	def get_Amount(self):
		return self.get_query_params().get('Amount')

	def set_Amount(self,Amount):
		self.add_query_param('Amount',Amount)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Tenancy(self):
		return self.get_query_params().get('Tenancy')

	def set_Tenancy(self,Tenancy):
		self.add_query_param('Tenancy',Tenancy)

	def get_SystemDiskDiskName(self):
		return self.get_query_params().get('SystemDisk.DiskName')

	def set_SystemDiskDiskName(self,SystemDiskDiskName):
		self.add_query_param('SystemDisk.DiskName',SystemDiskDiskName)

	def get_RamRoleName(self):
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self,RamRoleName):
		self.add_query_param('RamRoleName',RamRoleName)

	def get_AutoReleaseTime(self):
		return self.get_query_params().get('AutoReleaseTime')

	def set_AutoReleaseTime(self,AutoReleaseTime):
		self.add_query_param('AutoReleaseTime',AutoReleaseTime)

	def get_DedicatedHostId(self):
		return self.get_query_params().get('DedicatedHostId')

	def set_DedicatedHostId(self,DedicatedHostId):
		self.add_query_param('DedicatedHostId',DedicatedHostId)

	def get_CreditSpecification(self):
		return self.get_query_params().get('CreditSpecification')

	def set_CreditSpecification(self,CreditSpecification):
		self.add_query_param('CreditSpecification',CreditSpecification)

	def get_SecurityGroupIdss(self):
		return self.get_query_params().get('SecurityGroupIdss')

	def set_SecurityGroupIdss(self,SecurityGroupIdss):
		for i in range(len(SecurityGroupIdss)):	
			if SecurityGroupIdss[i] is not None:
				self.add_query_param('SecurityGroupIds.' + str(i + 1) , SecurityGroupIdss[i]);

	def get_SpotDuration(self):
		return self.get_query_params().get('SpotDuration')

	def set_SpotDuration(self,SpotDuration):
		self.add_query_param('SpotDuration',SpotDuration)

	def get_DataDisks(self):
		return self.get_query_params().get('DataDisks')

	def set_DataDisks(self,DataDisks):
		for i in range(len(DataDisks)):	
			if DataDisks[i].get('Size') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Size' , DataDisks[i].get('Size'))
			if DataDisks[i].get('SnapshotId') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.SnapshotId' , DataDisks[i].get('SnapshotId'))
			if DataDisks[i].get('Category') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Category' , DataDisks[i].get('Category'))
			if DataDisks[i].get('Encrypted') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Encrypted' , DataDisks[i].get('Encrypted'))
			if DataDisks[i].get('KMSKeyId') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.KMSKeyId' , DataDisks[i].get('KMSKeyId'))
			if DataDisks[i].get('DiskName') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.DiskName' , DataDisks[i].get('DiskName'))
			if DataDisks[i].get('Description') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Description' , DataDisks[i].get('Description'))
			if DataDisks[i].get('Device') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Device' , DataDisks[i].get('Device'))
			if DataDisks[i].get('DeleteWithInstance') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.DeleteWithInstance' , DataDisks[i].get('DeleteWithInstance'))
			if DataDisks[i].get('PerformanceLevel') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.PerformanceLevel' , DataDisks[i].get('PerformanceLevel'))
			if DataDisks[i].get('AutoSnapshotPolicyId') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.AutoSnapshotPolicyId' , DataDisks[i].get('AutoSnapshotPolicyId'))
			if DataDisks[i].get('EncryptAlgorithm') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.EncryptAlgorithm' , DataDisks[i].get('EncryptAlgorithm'))


	def get_LaunchTemplateVersion(self):
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self,LaunchTemplateVersion):
		self.add_query_param('LaunchTemplateVersion',LaunchTemplateVersion)

	def get_StorageSetId(self):
		return self.get_query_params().get('StorageSetId')

	def set_StorageSetId(self,StorageSetId):
		self.add_query_param('StorageSetId',StorageSetId)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDisk.Size',SystemDiskSize)

	def get_ImageFamily(self):
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self,ImageFamily):
		self.add_query_param('ImageFamily',ImageFamily)

	def get_SystemDiskDescription(self):
		return self.get_query_params().get('SystemDisk.Description')

	def set_SystemDiskDescription(self,SystemDiskDescription):
		self.add_query_param('SystemDisk.Description',SystemDiskDescription)