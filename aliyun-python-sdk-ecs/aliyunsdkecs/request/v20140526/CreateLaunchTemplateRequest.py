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

class CreateLaunchTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateLaunchTemplate','ecs')
		self.set_method('POST')
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

	def get_SecurityEnhancementStrategy(self):
		return self.get_query_params().get('SecurityEnhancementStrategy')

	def set_SecurityEnhancementStrategy(self,SecurityEnhancementStrategy):
		self.add_query_param('SecurityEnhancementStrategy',SecurityEnhancementStrategy)

	def get_NetworkType(self):
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_query_param('NetworkType',NetworkType)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_SpotPriceLimit(self):
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self,SpotPriceLimit):
		self.add_query_param('SpotPriceLimit',SpotPriceLimit)

	def get_ImageOwnerAlias(self):
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self,ImageOwnerAlias):
		self.add_query_param('ImageOwnerAlias',ImageOwnerAlias)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_SystemDiskIops(self):
		return self.get_query_params().get('SystemDisk.Iops')

	def set_SystemDiskIops(self,SystemDiskIops):
		self.add_query_param('SystemDisk.Iops',SystemDiskIops)

	def get_TemplateTags(self):
		return self.get_query_params().get('TemplateTag')

	def set_TemplateTags(self, TemplateTags):
		for depth1 in range(len(TemplateTags)):
			if TemplateTags[depth1].get('Key') is not None:
				self.add_query_param('TemplateTag.' + str(depth1 + 1) + '.Key', TemplateTags[depth1].get('Key'))
			if TemplateTags[depth1].get('Value') is not None:
				self.add_query_param('TemplateTag.' + str(depth1 + 1) + '.Value', TemplateTags[depth1].get('Value'))

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_TemplateResourceGroupId(self):
		return self.get_query_params().get('TemplateResourceGroupId')

	def set_TemplateResourceGroupId(self,TemplateResourceGroupId):
		self.add_query_param('TemplateResourceGroupId',TemplateResourceGroupId)

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

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_InternetMaxBandwidthIn(self):
		return self.get_query_params().get('InternetMaxBandwidthIn')

	def set_InternetMaxBandwidthIn(self,InternetMaxBandwidthIn):
		self.add_query_param('InternetMaxBandwidthIn',InternetMaxBandwidthIn)

	def get_VersionDescription(self):
		return self.get_query_params().get('VersionDescription')

	def set_VersionDescription(self,VersionDescription):
		self.add_query_param('VersionDescription',VersionDescription)

	def get_SystemDiskDeleteWithInstance(self):
		return self.get_query_params().get('SystemDisk.DeleteWithInstance')

	def set_SystemDiskDeleteWithInstance(self,SystemDiskDeleteWithInstance):
		self.add_query_param('SystemDisk.DeleteWithInstance',SystemDiskDeleteWithInstance)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

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

	def get_EnableVmOsConfig(self):
		return self.get_query_params().get('EnableVmOsConfig')

	def set_EnableVmOsConfig(self,EnableVmOsConfig):
		self.add_query_param('EnableVmOsConfig',EnableVmOsConfig)

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
			if NetworkInterfaces[depth1].get('NetworkInterfaceName') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.NetworkInterfaceName', NetworkInterfaces[depth1].get('NetworkInterfaceName'))
			if NetworkInterfaces[depth1].get('Description') is not None:
				self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.Description', NetworkInterfaces[depth1].get('Description'))
			if NetworkInterfaces[depth1].get('SecurityGroupIds') is not None:
				for depth2 in range(len(NetworkInterfaces[depth1].get('SecurityGroupIds'))):
					if NetworkInterfaces[depth1].get('SecurityGroupIds')[depth2] is not None:
						self.add_query_param('NetworkInterface.' + str(depth1 + 1) + '.SecurityGroupIds.' + str(depth2 + 1) , NetworkInterfaces[depth1].get('SecurityGroupIds')[depth2])

	def get_DeploymentSetId(self):
		return self.get_query_params().get('DeploymentSetId')

	def set_DeploymentSetId(self,DeploymentSetId):
		self.add_query_param('DeploymentSetId',DeploymentSetId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

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

	def get_SpotDuration(self):
		return self.get_query_params().get('SpotDuration')

	def set_SpotDuration(self,SpotDuration):
		self.add_query_param('SpotDuration',SpotDuration)

	def get_SecurityGroupIdss(self):
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIdss(self, SecurityGroupIdss):
		for depth1 in range(len(SecurityGroupIdss)):
			if SecurityGroupIdss[depth1] is not None:
				self.add_query_param('SecurityGroupIds.' + str(depth1 + 1) , SecurityGroupIdss[depth1])

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
			if DataDisks[depth1].get('DiskName') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DiskName', DataDisks[depth1].get('DiskName'))
			if DataDisks[depth1].get('Description') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Description', DataDisks[depth1].get('Description'))
			if DataDisks[depth1].get('DeleteWithInstance') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DeleteWithInstance', DataDisks[depth1].get('DeleteWithInstance'))
			if DataDisks[depth1].get('Device') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Device', DataDisks[depth1].get('Device'))
			if DataDisks[depth1].get('PerformanceLevel') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.PerformanceLevel', DataDisks[depth1].get('PerformanceLevel'))

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDisk.Size',SystemDiskSize)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_SystemDiskDescription(self):
		return self.get_query_params().get('SystemDisk.Description')

	def set_SystemDiskDescription(self,SystemDiskDescription):
		self.add_query_param('SystemDisk.Description',SystemDiskDescription)