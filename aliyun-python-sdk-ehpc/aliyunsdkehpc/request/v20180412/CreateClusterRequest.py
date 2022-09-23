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
from aliyunsdkehpc.endpoint import endpoint_data

class CreateClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'CreateCluster')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AdditionalVolumess(self): # RepeatList
		return self.get_query_params().get('AdditionalVolumes')

	def set_AdditionalVolumess(self, AdditionalVolumes):  # RepeatList
		for depth1 in range(len(AdditionalVolumes)):
			if AdditionalVolumes[depth1].get('VolumeType') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.VolumeType', AdditionalVolumes[depth1].get('VolumeType'))
			if AdditionalVolumes[depth1].get('VolumeMountOption') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.VolumeMountOption', AdditionalVolumes[depth1].get('VolumeMountOption'))
			if AdditionalVolumes[depth1].get('VolumeProtocol') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.VolumeProtocol', AdditionalVolumes[depth1].get('VolumeProtocol'))
			if AdditionalVolumes[depth1].get('LocalDirectory') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.LocalDirectory', AdditionalVolumes[depth1].get('LocalDirectory'))
			if AdditionalVolumes[depth1].get('RemoteDirectory') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.RemoteDirectory', AdditionalVolumes[depth1].get('RemoteDirectory'))
			if AdditionalVolumes[depth1].get('Roles') is not None:
				for depth2 in range(len(AdditionalVolumes[depth1].get('Roles'))):
					if AdditionalVolumes[depth1].get('Roles')[depth2].get('Name') is not None:
						self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.Roles.'  + str(depth2 + 1) + '.Name', AdditionalVolumes[depth1].get('Roles')[depth2].get('Name'))
			if AdditionalVolumes[depth1].get('VolumeId') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.VolumeId', AdditionalVolumes[depth1].get('VolumeId'))
			if AdditionalVolumes[depth1].get('VolumeMountpoint') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.VolumeMountpoint', AdditionalVolumes[depth1].get('VolumeMountpoint'))
			if AdditionalVolumes[depth1].get('Location') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.Location', AdditionalVolumes[depth1].get('Location'))
			if AdditionalVolumes[depth1].get('JobQueue') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.JobQueue', AdditionalVolumes[depth1].get('JobQueue'))
	def get_EcsOrderManagerInstanceType(self): # String
		return self.get_query_params().get('EcsOrder.Manager.InstanceType')

	def set_EcsOrderManagerInstanceType(self, EcsOrderManagerInstanceType):  # String
		self.add_query_param('EcsOrder.Manager.InstanceType', EcsOrderManagerInstanceType)
	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_SecurityGroupName(self): # String
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self, SecurityGroupName):  # String
		self.add_query_param('SecurityGroupName', SecurityGroupName)
	def get_ImageOwnerAlias(self): # String
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self, ImageOwnerAlias):  # String
		self.add_query_param('ImageOwnerAlias', ImageOwnerAlias)
	def get_DeployMode(self): # String
		return self.get_query_params().get('DeployMode')

	def set_DeployMode(self, DeployMode):  # String
		self.add_query_param('DeployMode', DeployMode)
	def get_EcsOrderManagerCount(self): # Integer
		return self.get_query_params().get('EcsOrder.Manager.Count')

	def set_EcsOrderManagerCount(self, EcsOrderManagerCount):  # Integer
		self.add_query_param('EcsOrder.Manager.Count', EcsOrderManagerCount)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_EcsOrderLoginCount(self): # Integer
		return self.get_query_params().get('EcsOrder.Login.Count')

	def set_EcsOrderLoginCount(self, EcsOrderLoginCount):  # Integer
		self.add_query_param('EcsOrder.Login.Count', EcsOrderLoginCount)
	def get_WithoutElasticIp(self): # Boolean
		return self.get_query_params().get('WithoutElasticIp')

	def set_WithoutElasticIp(self, WithoutElasticIp):  # Boolean
		self.add_query_param('WithoutElasticIp', WithoutElasticIp)
	def get_RemoteVisEnable(self): # String
		return self.get_query_params().get('RemoteVisEnable')

	def set_RemoteVisEnable(self, RemoteVisEnable):  # String
		self.add_query_param('RemoteVisEnable', RemoteVisEnable)
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
	def get_ComputeSpotPriceLimit(self): # String
		return self.get_query_params().get('ComputeSpotPriceLimit')

	def set_ComputeSpotPriceLimit(self, ComputeSpotPriceLimit):  # String
		self.add_query_param('ComputeSpotPriceLimit', ComputeSpotPriceLimit)
	def get_AutoRenewPeriod(self): # Integer
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self, AutoRenewPeriod):  # Integer
		self.add_query_param('AutoRenewPeriod', AutoRenewPeriod)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_RemoteDirectory(self): # String
		return self.get_query_params().get('RemoteDirectory')

	def set_RemoteDirectory(self, RemoteDirectory):  # String
		self.add_query_param('RemoteDirectory', RemoteDirectory)
	def get_EcsOrderComputeCount(self): # Integer
		return self.get_query_params().get('EcsOrder.Compute.Count')

	def set_EcsOrderComputeCount(self, EcsOrderComputeCount):  # Integer
		self.add_query_param('EcsOrder.Compute.Count', EcsOrderComputeCount)
	def get_ComputeSpotStrategy(self): # String
		return self.get_query_params().get('ComputeSpotStrategy')

	def set_ComputeSpotStrategy(self, ComputeSpotStrategy):  # String
		self.add_query_param('ComputeSpotStrategy', ComputeSpotStrategy)
	def get_PostInstallScripts(self): # RepeatList
		return self.get_query_params().get('PostInstallScript')

	def set_PostInstallScripts(self, PostInstallScript):  # RepeatList
		for depth1 in range(len(PostInstallScript)):
			if PostInstallScript[depth1].get('Args') is not None:
				self.add_query_param('PostInstallScript.' + str(depth1 + 1) + '.Args', PostInstallScript[depth1].get('Args'))
			if PostInstallScript[depth1].get('Url') is not None:
				self.add_query_param('PostInstallScript.' + str(depth1 + 1) + '.Url', PostInstallScript[depth1].get('Url'))
	def get_RamNodeTypess(self): # RepeatList
		return self.get_query_params().get('RamNodeTypes')

	def set_RamNodeTypess(self, RamNodeTypes):  # RepeatList
		for depth1 in range(len(RamNodeTypes)):
			self.add_query_param('RamNodeTypes.' + str(depth1 + 1), RamNodeTypes[depth1])
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_ComputeEnableHt(self): # Boolean
		return self.get_query_params().get('ComputeEnableHt')

	def set_ComputeEnableHt(self, ComputeEnableHt):  # Boolean
		self.add_query_param('ComputeEnableHt', ComputeEnableHt)
	def get_AutoRenew(self): # String
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # String
		self.add_query_param('AutoRenew', AutoRenew)
	def get_Domain(self): # String
		return self.get_query_params().get('Domain')

	def set_Domain(self, Domain):  # String
		self.add_query_param('Domain', Domain)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_VolumeId(self): # String
		return self.get_query_params().get('VolumeId')

	def set_VolumeId(self, VolumeId):  # String
		self.add_query_param('VolumeId', VolumeId)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_SccClusterId(self): # String
		return self.get_query_params().get('SccClusterId')

	def set_SccClusterId(self, SccClusterId):  # String
		self.add_query_param('SccClusterId', SccClusterId)
	def get_VolumeMountOption(self): # String
		return self.get_query_params().get('VolumeMountOption')

	def set_VolumeMountOption(self, VolumeMountOption):  # String
		self.add_query_param('VolumeMountOption', VolumeMountOption)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_SystemDiskLevel(self): # String
		return self.get_query_params().get('SystemDiskLevel')

	def set_SystemDiskLevel(self, SystemDiskLevel):  # String
		self.add_query_param('SystemDiskLevel', SystemDiskLevel)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_EhpcVersion(self): # String
		return self.get_query_params().get('EhpcVersion')

	def set_EhpcVersion(self, EhpcVersion):  # String
		self.add_query_param('EhpcVersion', EhpcVersion)
	def get_AccountType(self): # String
		return self.get_query_params().get('AccountType')

	def set_AccountType(self, AccountType):  # String
		self.add_query_param('AccountType', AccountType)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_EcsOrderComputeInstanceType(self): # String
		return self.get_query_params().get('EcsOrder.Compute.InstanceType')

	def set_EcsOrderComputeInstanceType(self, EcsOrderComputeInstanceType):  # String
		self.add_query_param('EcsOrder.Compute.InstanceType', EcsOrderComputeInstanceType)
	def get_JobQueue(self): # String
		return self.get_query_params().get('JobQueue')

	def set_JobQueue(self, JobQueue):  # String
		self.add_query_param('JobQueue', JobQueue)
	def get_VolumeType(self): # String
		return self.get_query_params().get('VolumeType')

	def set_VolumeType(self, VolumeType):  # String
		self.add_query_param('VolumeType', VolumeType)
	def get_SystemDiskType(self): # String
		return self.get_query_params().get('SystemDiskType')

	def set_SystemDiskType(self, SystemDiskType):  # String
		self.add_query_param('SystemDiskType', SystemDiskType)
	def get_VolumeProtocol(self): # String
		return self.get_query_params().get('VolumeProtocol')

	def set_VolumeProtocol(self, VolumeProtocol):  # String
		self.add_query_param('VolumeProtocol', VolumeProtocol)
	def get_ClientVersion(self): # String
		return self.get_query_params().get('ClientVersion')

	def set_ClientVersion(self, ClientVersion):  # String
		self.add_query_param('ClientVersion', ClientVersion)
	def get_OsTag(self): # String
		return self.get_query_params().get('OsTag')

	def set_OsTag(self, OsTag):  # String
		self.add_query_param('OsTag', OsTag)
	def get_ClusterVersion(self): # String
		return self.get_query_params().get('ClusterVersion')

	def set_ClusterVersion(self, ClusterVersion):  # String
		self.add_query_param('ClusterVersion', ClusterVersion)
	def get_IsComputeEss(self): # Boolean
		return self.get_query_params().get('IsComputeEss')

	def set_IsComputeEss(self, IsComputeEss):  # Boolean
		self.add_query_param('IsComputeEss', IsComputeEss)
	def get_RamRoleName(self): # String
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self, RamRoleName):  # String
		self.add_query_param('RamRoleName', RamRoleName)
	def get_Plugin(self): # String
		return self.get_query_params().get('Plugin')

	def set_Plugin(self, Plugin):  # String
		self.add_query_param('Plugin', Plugin)
	def get_Applications(self): # RepeatList
		return self.get_query_params().get('Application')

	def set_Applications(self, Application):  # RepeatList
		for depth1 in range(len(Application)):
			if Application[depth1].get('Tag') is not None:
				self.add_query_param('Application.' + str(depth1 + 1) + '.Tag', Application[depth1].get('Tag'))
	def get_EcsChargeType(self): # String
		return self.get_query_params().get('EcsChargeType')

	def set_EcsChargeType(self, EcsChargeType):  # String
		self.add_query_param('EcsChargeType', EcsChargeType)
	def get_InputFileUrl(self): # String
		return self.get_query_params().get('InputFileUrl')

	def set_InputFileUrl(self, InputFileUrl):  # String
		self.add_query_param('InputFileUrl', InputFileUrl)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_HaEnable(self): # Boolean
		return self.get_query_params().get('HaEnable')

	def set_HaEnable(self, HaEnable):  # Boolean
		self.add_query_param('HaEnable', HaEnable)
	def get_WithoutAgent(self): # Boolean
		return self.get_query_params().get('WithoutAgent')

	def set_WithoutAgent(self, WithoutAgent):  # Boolean
		self.add_query_param('WithoutAgent', WithoutAgent)
	def get_SchedulerType(self): # String
		return self.get_query_params().get('SchedulerType')

	def set_SchedulerType(self, SchedulerType):  # String
		self.add_query_param('SchedulerType', SchedulerType)
	def get_VolumeMountpoint(self): # String
		return self.get_query_params().get('VolumeMountpoint')

	def set_VolumeMountpoint(self, VolumeMountpoint):  # String
		self.add_query_param('VolumeMountpoint', VolumeMountpoint)
	def get_EcsOrderLoginInstanceType(self): # String
		return self.get_query_params().get('EcsOrder.Login.InstanceType')

	def set_EcsOrderLoginInstanceType(self, EcsOrderLoginInstanceType):  # String
		self.add_query_param('EcsOrder.Login.InstanceType', EcsOrderLoginInstanceType)
