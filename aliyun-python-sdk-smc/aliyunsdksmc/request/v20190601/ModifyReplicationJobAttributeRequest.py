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

class ModifyReplicationJobAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'smc', '2019-06-01', 'ModifyReplicationJobAttribute','smc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TargetType(self): # String
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_query_param('TargetType', TargetType)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Frequency(self): # Integer
		return self.get_query_params().get('Frequency')

	def set_Frequency(self, Frequency):  # Integer
		self.add_query_param('Frequency', Frequency)
	def get_JobId(self): # String
		return self.get_query_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_query_param('JobId', JobId)
	def get_ReplicationParameters(self): # String
		return self.get_query_params().get('ReplicationParameters')

	def set_ReplicationParameters(self, ReplicationParameters):  # String
		self.add_query_param('ReplicationParameters', ReplicationParameters)
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
	def get_SystemDiskSize(self): # Integer
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self, SystemDiskSize):  # Integer
		self.add_query_param('SystemDiskSize', SystemDiskSize)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_ContainerRepository(self): # String
		return self.get_query_params().get('ContainerRepository')

	def set_ContainerRepository(self, ContainerRepository):  # String
		self.add_query_param('ContainerRepository', ContainerRepository)
	def get_NetMode(self): # Integer
		return self.get_query_params().get('NetMode')

	def set_NetMode(self, NetMode):  # Integer
		self.add_query_param('NetMode', NetMode)
	def get_ContainerTag(self): # String
		return self.get_query_params().get('ContainerTag')

	def set_ContainerTag(self, ContainerTag):  # String
		self.add_query_param('ContainerTag', ContainerTag)
	def get_ContainerNamespace(self): # String
		return self.get_query_params().get('ContainerNamespace')

	def set_ContainerNamespace(self, ContainerNamespace):  # String
		self.add_query_param('ContainerNamespace', ContainerNamespace)
	def get_LaunchTemplateId(self): # String
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self, LaunchTemplateId):  # String
		self.add_query_param('LaunchTemplateId', LaunchTemplateId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_ValidTime(self): # String
		return self.get_query_params().get('ValidTime')

	def set_ValidTime(self, ValidTime):  # String
		self.add_query_param('ValidTime', ValidTime)
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
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
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
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_MaxNumberOfImageToKeep(self): # Integer
		return self.get_query_params().get('MaxNumberOfImageToKeep')

	def set_MaxNumberOfImageToKeep(self, MaxNumberOfImageToKeep):  # Integer
		self.add_query_param('MaxNumberOfImageToKeep', MaxNumberOfImageToKeep)
