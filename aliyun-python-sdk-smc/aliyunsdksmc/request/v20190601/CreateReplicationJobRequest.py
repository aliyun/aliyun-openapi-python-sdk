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


	def get_Frequency(self):
		return self.get_query_params().get('Frequency')

	def set_Frequency(self,Frequency):
		self.add_query_param('Frequency',Frequency)

	def get_ReplicationParameters(self):
		return self.get_query_params().get('ReplicationParameters')

	def set_ReplicationParameters(self,ReplicationParameters):
		self.add_query_param('ReplicationParameters',ReplicationParameters)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDiskSize',SystemDiskSize)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_NetMode(self):
		return self.get_query_params().get('NetMode')

	def set_NetMode(self,NetMode):
		self.add_query_param('NetMode',NetMode)

	def get_LicenseType(self):
		return self.get_query_params().get('LicenseType')

	def set_LicenseType(self,LicenseType):
		self.add_query_param('LicenseType',LicenseType)

	def get_ContainerNamespace(self):
		return self.get_query_params().get('ContainerNamespace')

	def set_ContainerNamespace(self,ContainerNamespace):
		self.add_query_param('ContainerNamespace',ContainerNamespace)

	def get_LaunchTemplateId(self):
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self,LaunchTemplateId):
		self.add_query_param('LaunchTemplateId',LaunchTemplateId)

	def get_ValidTime(self):
		return self.get_query_params().get('ValidTime')

	def set_ValidTime(self,ValidTime):
		self.add_query_param('ValidTime',ValidTime)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_ScheduledStartTime(self):
		return self.get_query_params().get('ScheduledStartTime')

	def set_ScheduledStartTime(self,ScheduledStartTime):
		self.add_query_param('ScheduledStartTime',ScheduledStartTime)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_InstanceRamRole(self):
		return self.get_query_params().get('InstanceRamRole')

	def set_InstanceRamRole(self,InstanceRamRole):
		self.add_query_param('InstanceRamRole',InstanceRamRole)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_MaxNumberOfImageToKeep(self):
		return self.get_query_params().get('MaxNumberOfImageToKeep')

	def set_MaxNumberOfImageToKeep(self,MaxNumberOfImageToKeep):
		self.add_query_param('MaxNumberOfImageToKeep',MaxNumberOfImageToKeep)

	def get_TargetType(self):
		return self.get_query_params().get('TargetType')

	def set_TargetType(self,TargetType):
		self.add_query_param('TargetType',TargetType)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_ImageName(self):
		return self.get_query_params().get('ImageName')

	def set_ImageName(self,ImageName):
		self.add_query_param('ImageName',ImageName)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_ContainerRepository(self):
		return self.get_query_params().get('ContainerRepository')

	def set_ContainerRepository(self,ContainerRepository):
		self.add_query_param('ContainerRepository',ContainerRepository)

	def get_ContainerTag(self):
		return self.get_query_params().get('ContainerTag')

	def set_ContainerTag(self,ContainerTag):
		self.add_query_param('ContainerTag',ContainerTag)

	def get_SourceId(self):
		return self.get_query_params().get('SourceId')

	def set_SourceId(self,SourceId):
		self.add_query_param('SourceId',SourceId)

	def get_RunOnce(self):
		return self.get_query_params().get('RunOnce')

	def set_RunOnce(self,RunOnce):
		self.add_query_param('RunOnce',RunOnce)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_SystemDiskParts(self):
		return self.get_query_params().get('SystemDiskPart')

	def set_SystemDiskParts(self, SystemDiskParts):
		for depth1 in range(len(SystemDiskParts)):
			if SystemDiskParts[depth1].get('SizeBytes') is not None:
				self.add_query_param('SystemDiskPart.' + str(depth1 + 1) + '.SizeBytes', SystemDiskParts[depth1].get('SizeBytes'))
			if SystemDiskParts[depth1].get('Block') is not None:
				self.add_query_param('SystemDiskPart.' + str(depth1 + 1) + '.Block', SystemDiskParts[depth1].get('Block'))
			if SystemDiskParts[depth1].get('Device') is not None:
				self.add_query_param('SystemDiskPart.' + str(depth1 + 1) + '.Device', SystemDiskParts[depth1].get('Device'))

	def get_DataDisks(self):
		return self.get_query_params().get('DataDisk')

	def set_DataDisks(self, DataDisks):
		for depth1 in range(len(DataDisks)):
			if DataDisks[depth1].get('Size') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Size', DataDisks[depth1].get('Size'))
			if DataDisks[depth1].get('Part') is not None:
				for depth2 in range(len(DataDisks[depth1].get('Part'))):
					if DataDisks[depth1].get('Part')[depth2].get('SizeBytes') is not None:
						self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Part.' + str(depth2 + 1) + '.SizeBytes', DataDisks[depth1].get('Part')[depth2].get('SizeBytes'))
					if DataDisks[depth1].get('Part')[depth2].get('Block') is not None:
						self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Part.' + str(depth2 + 1) + '.Block', DataDisks[depth1].get('Part')[depth2].get('Block'))
					if DataDisks[depth1].get('Part')[depth2].get('Device') is not None:
						self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Part.' + str(depth2 + 1) + '.Device', DataDisks[depth1].get('Part')[depth2].get('Device'))
			if DataDisks[depth1].get('Index') is not None:
				self.add_query_param('DataDisk.' + str(depth1 + 1) + '.Index', DataDisks[depth1].get('Index'))

	def get_LaunchTemplateVersion(self):
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self,LaunchTemplateVersion):
		self.add_query_param('LaunchTemplateVersion',LaunchTemplateVersion)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)