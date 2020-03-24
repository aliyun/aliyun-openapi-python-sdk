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
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HpcClusterId(self):
		return self.get_query_params().get('HpcClusterId')

	def set_HpcClusterId(self,HpcClusterId):
		self.add_query_param('HpcClusterId',HpcClusterId)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_SpotPriceLimits(self):
		return self.get_query_params().get('SpotPriceLimits')

	def set_SpotPriceLimits(self,SpotPriceLimits):
		for i in range(len(SpotPriceLimits)):	
			if SpotPriceLimits[i].get('InstanceType') is not None:
				self.add_query_param('SpotPriceLimit.' + str(i + 1) + '.InstanceType' , SpotPriceLimits[i].get('InstanceType'))
			if SpotPriceLimits[i].get('PriceLimit') is not None:
				self.add_query_param('SpotPriceLimit.' + str(i + 1) + '.PriceLimit' , SpotPriceLimits[i].get('PriceLimit'))


	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_InstanceDescription(self):
		return self.get_query_params().get('InstanceDescription')

	def set_InstanceDescription(self,InstanceDescription):
		self.add_query_param('InstanceDescription',InstanceDescription)

	def get_SystemDiskAutoSnapshotPolicyId(self):
		return self.get_query_params().get('SystemDisk.AutoSnapshotPolicyId')

	def set_SystemDiskAutoSnapshotPolicyId(self,SystemDiskAutoSnapshotPolicyId):
		self.add_query_param('SystemDisk.AutoSnapshotPolicyId',SystemDiskAutoSnapshotPolicyId)

	def get_Ipv6AddressCount(self):
		return self.get_query_params().get('Ipv6AddressCount')

	def set_Ipv6AddressCount(self,Ipv6AddressCount):
		self.add_query_param('Ipv6AddressCount',Ipv6AddressCount)

	def get_Cpu(self):
		return self.get_query_params().get('Cpu')

	def set_Cpu(self,Cpu):
		self.add_query_param('Cpu',Cpu)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ScalingConfigurationName(self):
		return self.get_query_params().get('ScalingConfigurationName')

	def set_ScalingConfigurationName(self,ScalingConfigurationName):
		self.add_query_param('ScalingConfigurationName',ScalingConfigurationName)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_ScalingConfigurationId(self):
		return self.get_query_params().get('ScalingConfigurationId')

	def set_ScalingConfigurationId(self,ScalingConfigurationId):
		self.add_query_param('ScalingConfigurationId',ScalingConfigurationId)

	def get_SpotStrategy(self):
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self,SpotStrategy):
		self.add_query_param('SpotStrategy',SpotStrategy)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_Memory(self):
		return self.get_query_params().get('Memory')

	def set_Memory(self,Memory):
		self.add_query_param('Memory',Memory)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_InstanceTypess(self):
		return self.get_query_params().get('InstanceTypess')

	def set_InstanceTypess(self,InstanceTypess):
		for i in range(len(InstanceTypess)):	
			if InstanceTypess[i] is not None:
				self.add_query_param('InstanceTypes.' + str(i + 1) , InstanceTypess[i]);

	def get_InternetMaxBandwidthOut(self):
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self,InternetMaxBandwidthOut):
		self.add_query_param('InternetMaxBandwidthOut',InternetMaxBandwidthOut)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_SystemDiskCategory(self):
		return self.get_query_params().get('SystemDisk.Category')

	def set_SystemDiskCategory(self,SystemDiskCategory):
		self.add_query_param('SystemDisk.Category',SystemDiskCategory)

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_PasswordInherit(self):
		return self.get_query_params().get('PasswordInherit')

	def set_PasswordInherit(self,PasswordInherit):
		self.add_query_param('PasswordInherit',PasswordInherit)

	def get_ImageName(self):
		return self.get_query_params().get('ImageName')

	def set_ImageName(self,ImageName):
		self.add_query_param('ImageName',ImageName)

	def get_Override(self):
		return self.get_query_params().get('Override')

	def set_Override(self,Override):
		self.add_query_param('Override',Override)

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

	def get_SecurityGroupIdss(self):
		return self.get_query_params().get('SecurityGroupIdss')

	def set_SecurityGroupIdss(self,SecurityGroupIdss):
		for i in range(len(SecurityGroupIdss)):	
			if SecurityGroupIdss[i] is not None:
				self.add_query_param('SecurityGroupIds.' + str(i + 1) , SecurityGroupIdss[i]);

	def get_DataDisks(self):
		return self.get_query_params().get('DataDisks')

	def set_DataDisks(self,DataDisks):
		for i in range(len(DataDisks)):	
			if DataDisks[i].get('DiskName') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.DiskName' , DataDisks[i].get('DiskName'))
			if DataDisks[i].get('SnapshotId') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.SnapshotId' , DataDisks[i].get('SnapshotId'))
			if DataDisks[i].get('Size') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Size' , DataDisks[i].get('Size'))
			if DataDisks[i].get('Encrypted') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Encrypted' , DataDisks[i].get('Encrypted'))
			if DataDisks[i].get('AutoSnapshotPolicyId') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.AutoSnapshotPolicyId' , DataDisks[i].get('AutoSnapshotPolicyId'))
			if DataDisks[i].get('Description') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Description' , DataDisks[i].get('Description'))
			if DataDisks[i].get('Category') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Category' , DataDisks[i].get('Category'))
			if DataDisks[i].get('KMSKeyId') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.KMSKeyId' , DataDisks[i].get('KMSKeyId'))
			if DataDisks[i].get('Device') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Device' , DataDisks[i].get('Device'))
			if DataDisks[i].get('DeleteWithInstance') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.DeleteWithInstance' , DataDisks[i].get('DeleteWithInstance'))


	def get_LoadBalancerWeight(self):
		return self.get_query_params().get('LoadBalancerWeight')

	def set_LoadBalancerWeight(self,LoadBalancerWeight):
		self.add_query_param('LoadBalancerWeight',LoadBalancerWeight)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDisk.Size',SystemDiskSize)

	def get_SystemDiskDescription(self):
		return self.get_query_params().get('SystemDisk.Description')

	def set_SystemDiskDescription(self,SystemDiskDescription):
		self.add_query_param('SystemDisk.Description',SystemDiskDescription)