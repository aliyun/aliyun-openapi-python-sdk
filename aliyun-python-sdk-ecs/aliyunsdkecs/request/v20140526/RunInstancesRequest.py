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
class RunInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'RunInstances','ecs')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

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

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		for i in range(len(Tags)):	
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key' , Tags[i].get('Key'))
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value' , Tags[i].get('Value'))


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

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

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

	def get_SystemDiskCategory(self):
		return self.get_query_params().get('SystemDisk.Category')

	def set_SystemDiskCategory(self,SystemDiskCategory):
		self.add_query_param('SystemDisk.Category',SystemDiskCategory)

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

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
			if NetworkInterfaces[i].get('NetworkInterfaceName') is not None:
				self.add_query_param('NetworkInterface.' + str(i + 1) + '.NetworkInterfaceName' , NetworkInterfaces[i].get('NetworkInterfaceName'))
			if NetworkInterfaces[i].get('Description') is not None:
				self.add_query_param('NetworkInterface.' + str(i + 1) + '.Description' , NetworkInterfaces[i].get('Description'))


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
			if DataDisks[i].get('DiskName') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.DiskName' , DataDisks[i].get('DiskName'))
			if DataDisks[i].get('Description') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Description' , DataDisks[i].get('Description'))
			if DataDisks[i].get('DeleteWithInstance') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.DeleteWithInstance' , DataDisks[i].get('DeleteWithInstance'))


	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDisk.Size',SystemDiskSize)

	def get_SystemDiskDescription(self):
		return self.get_query_params().get('SystemDisk.Description')

	def set_SystemDiskDescription(self,SystemDiskDescription):
		self.add_query_param('SystemDisk.Description',SystemDiskDescription)