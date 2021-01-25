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

class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateInstance','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


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

	def get_SecurityEnhancementStrategy(self):
		return self.get_query_params().get('SecurityEnhancementStrategy')

	def set_SecurityEnhancementStrategy(self,SecurityEnhancementStrategy):
		self.add_query_param('SecurityEnhancementStrategy',SecurityEnhancementStrategy)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

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

	def get_StorageSetPartitionNumber(self):
		return self.get_query_params().get('StorageSetPartitionNumber')

	def set_StorageSetPartitionNumber(self,StorageSetPartitionNumber):
		self.add_query_param('StorageSetPartitionNumber',StorageSetPartitionNumber)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_PrivatePoolOptionsId(self):
		return self.get_query_params().get('PrivatePoolOptions.Id')

	def set_PrivatePoolOptionsId(self,PrivatePoolOptionsId):
		self.add_query_param('PrivatePoolOptions.Id',PrivatePoolOptionsId)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_NodeControllerId(self):
		return self.get_query_params().get('NodeControllerId')

	def set_NodeControllerId(self,NodeControllerId):
		self.add_query_param('NodeControllerId',NodeControllerId)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PrivateIpAddress(self):
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self,PrivateIpAddress):
		self.add_query_param('PrivateIpAddress',PrivateIpAddress)

	def get_SpotStrategy(self):
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self,SpotStrategy):
		self.add_query_param('SpotStrategy',SpotStrategy)

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

	def get_InternetMaxBandwidthIn(self):
		return self.get_query_params().get('InternetMaxBandwidthIn')

	def set_InternetMaxBandwidthIn(self,InternetMaxBandwidthIn):
		self.add_query_param('InternetMaxBandwidthIn',InternetMaxBandwidthIn)

	def get_UseAdditionalService(self):
		return self.get_query_params().get('UseAdditionalService')

	def set_UseAdditionalService(self,UseAdditionalService):
		self.add_query_param('UseAdditionalService',UseAdditionalService)

	def get_Affinity(self):
		return self.get_query_params().get('Affinity')

	def set_Affinity(self,Affinity):
		self.add_query_param('Affinity',Affinity)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_VlanId(self):
		return self.get_query_params().get('VlanId')

	def set_VlanId(self,VlanId):
		self.add_query_param('VlanId',VlanId)

	def get_SpotInterruptionBehavior(self):
		return self.get_query_params().get('SpotInterruptionBehavior')

	def set_SpotInterruptionBehavior(self,SpotInterruptionBehavior):
		self.add_query_param('SpotInterruptionBehavior',SpotInterruptionBehavior)

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

	def get_HttpEndpoint(self):
		return self.get_query_params().get('HttpEndpoint')

	def set_HttpEndpoint(self,HttpEndpoint):
		self.add_query_param('HttpEndpoint',HttpEndpoint)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_Arns(self):
		return self.get_query_params().get('Arn')

	def set_Arns(self, Arns):
		for depth1 in range(len(Arns)):
			if Arns[depth1].get('Rolearn') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.Rolearn', Arns[depth1].get('Rolearn'))
			if Arns[depth1].get('RoleType') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.RoleType', Arns[depth1].get('RoleType'))
			if Arns[depth1].get('AssumeRoleFor') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.AssumeRoleFor', Arns[depth1].get('AssumeRoleFor'))

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_DeploymentSetId(self):
		return self.get_query_params().get('DeploymentSetId')

	def set_DeploymentSetId(self,DeploymentSetId):
		self.add_query_param('DeploymentSetId',DeploymentSetId)

	def get_InnerIpAddress(self):
		return self.get_query_params().get('InnerIpAddress')

	def set_InnerIpAddress(self,InnerIpAddress):
		self.add_query_param('InnerIpAddress',InnerIpAddress)

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

	def get_DedicatedHostId(self):
		return self.get_query_params().get('DedicatedHostId')

	def set_DedicatedHostId(self,DedicatedHostId):
		self.add_query_param('DedicatedHostId',DedicatedHostId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_CreditSpecification(self):
		return self.get_query_params().get('CreditSpecification')

	def set_CreditSpecification(self,CreditSpecification):
		self.add_query_param('CreditSpecification',CreditSpecification)

	def get_SpotDuration(self):
		return self.get_query_params().get('SpotDuration')

	def set_SpotDuration(self,SpotDuration):
		self.add_query_param('SpotDuration',SpotDuration)

	def get_DataDisks(self):
		return self.get_query_params().get('DataDisk')

	def set_DataDisks(self, DataDisks):
		for depth1 in range(len(DataDisks)):
			if DataDisks[depth1].get('DiskName') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DiskName', DataDisks[depth1].get('DiskName'))
			if DataDisks[depth1].get('SnapshotId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.SnapshotId', DataDisks[depth1].get('SnapshotId'))
			if DataDisks[depth1].get('Size') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Size', DataDisks[depth1].get('Size'))
			if DataDisks[depth1].get('Encrypted') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Encrypted', DataDisks[depth1].get('Encrypted'))
			if DataDisks[depth1].get('PerformanceLevel') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.PerformanceLevel', DataDisks[depth1].get('PerformanceLevel'))
			if DataDisks[depth1].get('EncryptAlgorithm') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.EncryptAlgorithm', DataDisks[depth1].get('EncryptAlgorithm'))
			if DataDisks[depth1].get('Description') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Description', DataDisks[depth1].get('Description'))
			if DataDisks[depth1].get('Category') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Category', DataDisks[depth1].get('Category'))
			if DataDisks[depth1].get('KMSKeyId') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.KMSKeyId', DataDisks[depth1].get('KMSKeyId'))
			if DataDisks[depth1].get('Device') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Device', DataDisks[depth1].get('Device'))
			if DataDisks[depth1].get('DeleteWithInstance') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.DeleteWithInstance', DataDisks[depth1].get('DeleteWithInstance'))

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

	def get_HttpTokens(self):
		return self.get_query_params().get('HttpTokens')

	def set_HttpTokens(self,HttpTokens):
		self.add_query_param('HttpTokens',HttpTokens)

	def get_SystemDiskDescription(self):
		return self.get_query_params().get('SystemDisk.Description')

	def set_SystemDiskDescription(self,SystemDiskDescription):
		self.add_query_param('SystemDisk.Description',SystemDiskDescription)