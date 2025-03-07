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
from aliyunsdksmc.endpoint import endpoint_data

class CreateReplicationJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'smc', '2019-06-01', 'CreateReplicationJob','smc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Frequency(self): # Integer
		return self.get_query_params().get('Frequency')

	def set_Frequency(self, Frequency):  # Integer
		self.add_query_param('Frequency', Frequency)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ReplicationParameters(self): # String
		return self.get_query_params().get('ReplicationParameters')

	def set_ReplicationParameters(self, ReplicationParameters):  # String
		self.add_query_param('ReplicationParameters', ReplicationParameters)
	def get_SystemDiskSize(self): # Integer
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self, SystemDiskSize):  # Integer
		self.add_query_param('SystemDiskSize', SystemDiskSize)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_NetMode(self): # Integer
		return self.get_query_params().get('NetMode')

	def set_NetMode(self, NetMode):  # Integer
		self.add_query_param('NetMode', NetMode)
	def get_LicenseType(self): # String
		return self.get_query_params().get('LicenseType')

	def set_LicenseType(self, LicenseType):  # String
		self.add_query_param('LicenseType', LicenseType)
	def get_ContainerNamespace(self): # String
		return self.get_query_params().get('ContainerNamespace')

	def set_ContainerNamespace(self, ContainerNamespace):  # String
		self.add_query_param('ContainerNamespace', ContainerNamespace)
	def get_LaunchTemplateId(self): # String
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self, LaunchTemplateId):  # String
		self.add_query_param('LaunchTemplateId', LaunchTemplateId)
	def get_ValidTime(self): # String
		return self.get_query_params().get('ValidTime')

	def set_ValidTime(self, ValidTime):  # String
		self.add_query_param('ValidTime', ValidTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_JobType(self): # Integer
		return self.get_query_params().get('JobType')

	def set_JobType(self, JobType):  # Integer
		self.add_query_param('JobType', JobType)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_ScheduledStartTime(self): # String
		return self.get_query_params().get('ScheduledStartTime')

	def set_ScheduledStartTime(self, ScheduledStartTime):  # String
		self.add_query_param('ScheduledStartTime', ScheduledStartTime)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_InstanceRamRole(self): # String
		return self.get_query_params().get('InstanceRamRole')

	def set_InstanceRamRole(self, InstanceRamRole):  # String
		self.add_query_param('InstanceRamRole', InstanceRamRole)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_MaxNumberOfImageToKeep(self): # Integer
		return self.get_query_params().get('MaxNumberOfImageToKeep')

	def set_MaxNumberOfImageToKeep(self, MaxNumberOfImageToKeep):  # Integer
		self.add_query_param('MaxNumberOfImageToKeep', MaxNumberOfImageToKeep)
	def get_TargetType(self): # String
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_query_param('TargetType', TargetType)
	def get_Disks(self): # Struct
		return self.get_query_params().get('Disks')

	def set_Disks(self, Disks):  # Struct
		if Disks.get('System') is not None:
			if Disks.get('System').get('LVM') is not None:
				self.add_query_param('Disks.System.LVM', Disks.get('System').get('LVM'))
			if Disks.get('System').get('Size') is not None:
				self.add_query_param('Disks.System.Size', Disks.get('System').get('Size'))
			if Disks.get('System').get('Part') is not None:
				for index1, value1 in enumerate(Disks.get('System').get('Part')):
					if value1.get('Path') is not None:
						self.add_query_param('Disks.System.Part.' + str(index1 + 1) + '.Path', value1.get('Path'))
					if value1.get('SizeBytes') is not None:
						self.add_query_param('Disks.System.Part.' + str(index1 + 1) + '.SizeBytes', value1.get('SizeBytes'))
					if value1.get('Block') is not None:
						self.add_query_param('Disks.System.Part.' + str(index1 + 1) + '.Block', value1.get('Block'))
		if Disks.get('Data') is not None:
			for index1, value1 in enumerate(Disks.get('Data')):
				if value1.get('LVM') is not None:
					self.add_query_param('Disks.Data.' + str(index1 + 1) + '.LVM', value1.get('LVM'))
				if value1.get('Size') is not None:
					self.add_query_param('Disks.Data.' + str(index1 + 1) + '.Size', value1.get('Size'))
				if value1.get('Part') is not None:
					for index2, value2 in enumerate(value1.get('Part')):
						if value2.get('Path') is not None:
							self.add_query_param('Disks.Data.' + str(index1 + 1) + '.Part.' + str(index2 + 1) + '.Path', value2.get('Path'))
						if value2.get('SizeBytes') is not None:
							self.add_query_param('Disks.Data.' + str(index1 + 1) + '.Part.' + str(index2 + 1) + '.SizeBytes', value2.get('SizeBytes'))
						if value2.get('Block') is not None:
							self.add_query_param('Disks.Data.' + str(index1 + 1) + '.Part.' + str(index2 + 1) + '.Block', value2.get('Block'))
				if value1.get('DiskId') is not None:
					self.add_query_param('Disks.Data.' + str(index1 + 1) + '.DiskId', value1.get('DiskId'))
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_ContainerRepository(self): # String
		return self.get_query_params().get('ContainerRepository')

	def set_ContainerRepository(self, ContainerRepository):  # String
		self.add_query_param('ContainerRepository', ContainerRepository)
	def get_ContainerTag(self): # String
		return self.get_query_params().get('ContainerTag')

	def set_ContainerTag(self, ContainerTag):  # String
		self.add_query_param('ContainerTag', ContainerTag)
	def get_SourceId(self): # String
		return self.get_query_params().get('SourceId')

	def set_SourceId(self, SourceId):  # String
		self.add_query_param('SourceId', SourceId)
	def get_RunOnce(self): # Boolean
		return self.get_query_params().get('RunOnce')

	def set_RunOnce(self, RunOnce):  # Boolean
		self.add_query_param('RunOnce', RunOnce)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_SystemDiskParts(self): # RepeatList
		return self.get_query_params().get('SystemDiskPart')

	def set_SystemDiskParts(self, SystemDiskPart):  # RepeatList
		for depth1 in range(len(SystemDiskPart)):
			if SystemDiskPart[depth1].get('SizeBytes') is not None:
				self.add_query_param('SystemDiskPart.' + str(depth1 + 1) + '.SizeBytes', SystemDiskPart[depth1].get('SizeBytes'))
			if SystemDiskPart[depth1].get('Block') is not None:
				self.add_query_param('SystemDiskPart.' + str(depth1 + 1) + '.Block', SystemDiskPart[depth1].get('Block'))
			if SystemDiskPart[depth1].get('Device') is not None:
				self.add_query_param('SystemDiskPart.' + str(depth1 + 1) + '.Device', SystemDiskPart[depth1].get('Device'))
	def get_LaunchTemplateVersion(self): # String
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self, LaunchTemplateVersion):  # String
		self.add_query_param('LaunchTemplateVersion', LaunchTemplateVersion)
	def get_DataDisks(self): # RepeatList
		return self.get_query_params().get('DataDisk')

	def set_DataDisks(self, DataDisk):  # RepeatList
		for depth1 in range(len(DataDisk)):
			if DataDisk[depth1].get('Size') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Size', DataDisk[depth1].get('Size'))
			if DataDisk[depth1].get('Part') is not None:
				for depth2 in range(len(DataDisk[depth1].get('Part'))):
					if DataDisk[depth1].get('Part')[depth2].get('SizeBytes') is not None:
						self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Part.'  + str(depth2 + 1) + '.SizeBytes', DataDisk[depth1].get('Part')[depth2].get('SizeBytes'))
					if DataDisk[depth1].get('Part')[depth2].get('Block') is not None:
						self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Part.'  + str(depth2 + 1) + '.Block', DataDisk[depth1].get('Part')[depth2].get('Block'))
					if DataDisk[depth1].get('Part')[depth2].get('Device') is not None:
						self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Part.'  + str(depth2 + 1) + '.Device', DataDisk[depth1].get('Part')[depth2].get('Device'))
			if DataDisk[depth1].get('Index') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Index', DataDisk[depth1].get('Index'))
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
