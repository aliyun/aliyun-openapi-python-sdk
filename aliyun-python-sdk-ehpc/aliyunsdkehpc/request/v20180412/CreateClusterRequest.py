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


	def get_AdditionalVolumess(self):
		return self.get_query_params().get('AdditionalVolumess')

	def set_AdditionalVolumess(self, AdditionalVolumess):
		for depth1 in range(len(AdditionalVolumess)):
			if AdditionalVolumess[depth1].get('VolumeType') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.VolumeType', AdditionalVolumess[depth1].get('VolumeType'))
			if AdditionalVolumess[depth1].get('VolumeProtocol') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.VolumeProtocol', AdditionalVolumess[depth1].get('VolumeProtocol'))
			if AdditionalVolumess[depth1].get('LocalDirectory') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.LocalDirectory', AdditionalVolumess[depth1].get('LocalDirectory'))
			if AdditionalVolumess[depth1].get('RemoteDirectory') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.RemoteDirectory', AdditionalVolumess[depth1].get('RemoteDirectory'))
			if AdditionalVolumess[depth1].get('Roles') is not None:
				for depth2 in range(len(AdditionalVolumess[depth1].get('Roles'))):
					if AdditionalVolumess[depth1].get('Roles')[depth2].get('Name') is not None:
						self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.Roles.' + str(depth2 + 1) + '.Name', AdditionalVolumess[depth1].get('Roles')[depth2].get('Name'))
			if AdditionalVolumess[depth1].get('VolumeId') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.VolumeId', AdditionalVolumess[depth1].get('VolumeId'))
			if AdditionalVolumess[depth1].get('VolumeMountpoint') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.VolumeMountpoint', AdditionalVolumess[depth1].get('VolumeMountpoint'))
			if AdditionalVolumess[depth1].get('Location') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.Location', AdditionalVolumess[depth1].get('Location'))
			if AdditionalVolumess[depth1].get('JobQueue') is not None:
				self.add_query_param('AdditionalVolumes.' + str(depth1 + 1) + '.JobQueue', AdditionalVolumess[depth1].get('JobQueue'))

	def get_EcsOrderManagerInstanceType(self):
		return self.get_query_params().get('EcsOrder.Manager.InstanceType')

	def set_EcsOrderManagerInstanceType(self,EcsOrderManagerInstanceType):
		self.add_query_param('EcsOrder.Manager.InstanceType',EcsOrderManagerInstanceType)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_SecurityGroupName(self):
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self,SecurityGroupName):
		self.add_query_param('SecurityGroupName',SecurityGroupName)

	def get_ImageOwnerAlias(self):
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self,ImageOwnerAlias):
		self.add_query_param('ImageOwnerAlias',ImageOwnerAlias)

	def get_DeployMode(self):
		return self.get_query_params().get('DeployMode')

	def set_DeployMode(self,DeployMode):
		self.add_query_param('DeployMode',DeployMode)

	def get_EcsOrderManagerCount(self):
		return self.get_query_params().get('EcsOrder.Manager.Count')

	def set_EcsOrderManagerCount(self,EcsOrderManagerCount):
		self.add_query_param('EcsOrder.Manager.Count',EcsOrderManagerCount)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_EcsOrderLoginCount(self):
		return self.get_query_params().get('EcsOrder.Login.Count')

	def set_EcsOrderLoginCount(self,EcsOrderLoginCount):
		self.add_query_param('EcsOrder.Login.Count',EcsOrderLoginCount)

	def get_RemoteVisEnable(self):
		return self.get_query_params().get('RemoteVisEnable')

	def set_RemoteVisEnable(self,RemoteVisEnable):
		self.add_query_param('RemoteVisEnable',RemoteVisEnable)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDiskSize',SystemDiskSize)

	def get_ComputeSpotPriceLimit(self):
		return self.get_query_params().get('ComputeSpotPriceLimit')

	def set_ComputeSpotPriceLimit(self,ComputeSpotPriceLimit):
		self.add_query_param('ComputeSpotPriceLimit',ComputeSpotPriceLimit)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_RemoteDirectory(self):
		return self.get_query_params().get('RemoteDirectory')

	def set_RemoteDirectory(self,RemoteDirectory):
		self.add_query_param('RemoteDirectory',RemoteDirectory)

	def get_EcsOrderComputeCount(self):
		return self.get_query_params().get('EcsOrder.Compute.Count')

	def set_EcsOrderComputeCount(self,EcsOrderComputeCount):
		self.add_query_param('EcsOrder.Compute.Count',EcsOrderComputeCount)

	def get_ComputeSpotStrategy(self):
		return self.get_query_params().get('ComputeSpotStrategy')

	def set_ComputeSpotStrategy(self,ComputeSpotStrategy):
		self.add_query_param('ComputeSpotStrategy',ComputeSpotStrategy)

	def get_PostInstallScripts(self):
		return self.get_query_params().get('PostInstallScripts')

	def set_PostInstallScripts(self, PostInstallScripts):
		for depth1 in range(len(PostInstallScripts)):
			if PostInstallScripts[depth1].get('Args') is not None:
				self.add_query_param('PostInstallScript.' + str(depth1 + 1) + '.Args', PostInstallScripts[depth1].get('Args'))
			if PostInstallScripts[depth1].get('Url') is not None:
				self.add_query_param('PostInstallScript.' + str(depth1 + 1) + '.Url', PostInstallScripts[depth1].get('Url'))

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_ComputeEnableHt(self):
		return self.get_query_params().get('ComputeEnableHt')

	def set_ComputeEnableHt(self,ComputeEnableHt):
		self.add_query_param('ComputeEnableHt',ComputeEnableHt)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_VolumeId(self):
		return self.get_query_params().get('VolumeId')

	def set_VolumeId(self,VolumeId):
		self.add_query_param('VolumeId',VolumeId)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_SccClusterId(self):
		return self.get_query_params().get('SccClusterId')

	def set_SccClusterId(self,SccClusterId):
		self.add_query_param('SccClusterId',SccClusterId)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_EhpcVersion(self):
		return self.get_query_params().get('EhpcVersion')

	def set_EhpcVersion(self,EhpcVersion):
		self.add_query_param('EhpcVersion',EhpcVersion)

	def get_AccountType(self):
		return self.get_query_params().get('AccountType')

	def set_AccountType(self,AccountType):
		self.add_query_param('AccountType',AccountType)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_EcsOrderComputeInstanceType(self):
		return self.get_query_params().get('EcsOrder.Compute.InstanceType')

	def set_EcsOrderComputeInstanceType(self,EcsOrderComputeInstanceType):
		self.add_query_param('EcsOrder.Compute.InstanceType',EcsOrderComputeInstanceType)

	def get_JobQueue(self):
		return self.get_query_params().get('JobQueue')

	def set_JobQueue(self,JobQueue):
		self.add_query_param('JobQueue',JobQueue)

	def get_VolumeType(self):
		return self.get_query_params().get('VolumeType')

	def set_VolumeType(self,VolumeType):
		self.add_query_param('VolumeType',VolumeType)

	def get_SystemDiskType(self):
		return self.get_query_params().get('SystemDiskType')

	def set_SystemDiskType(self,SystemDiskType):
		self.add_query_param('SystemDiskType',SystemDiskType)

	def get_VolumeProtocol(self):
		return self.get_query_params().get('VolumeProtocol')

	def set_VolumeProtocol(self,VolumeProtocol):
		self.add_query_param('VolumeProtocol',VolumeProtocol)

	def get_ClientVersion(self):
		return self.get_query_params().get('ClientVersion')

	def set_ClientVersion(self,ClientVersion):
		self.add_query_param('ClientVersion',ClientVersion)

	def get_OsTag(self):
		return self.get_query_params().get('OsTag')

	def set_OsTag(self,OsTag):
		self.add_query_param('OsTag',OsTag)

	def get_Applications(self):
		return self.get_query_params().get('Applications')

	def set_Applications(self, Applications):
		for depth1 in range(len(Applications)):
			if Applications[depth1].get('Tag') is not None:
				self.add_query_param('Application.' + str(depth1 + 1) + '.Tag', Applications[depth1].get('Tag'))

	def get_EcsChargeType(self):
		return self.get_query_params().get('EcsChargeType')

	def set_EcsChargeType(self,EcsChargeType):
		self.add_query_param('EcsChargeType',EcsChargeType)

	def get_InputFileUrl(self):
		return self.get_query_params().get('InputFileUrl')

	def set_InputFileUrl(self,InputFileUrl):
		self.add_query_param('InputFileUrl',InputFileUrl)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_HaEnable(self):
		return self.get_query_params().get('HaEnable')

	def set_HaEnable(self,HaEnable):
		self.add_query_param('HaEnable',HaEnable)

	def get_SchedulerType(self):
		return self.get_query_params().get('SchedulerType')

	def set_SchedulerType(self,SchedulerType):
		self.add_query_param('SchedulerType',SchedulerType)

	def get_VolumeMountpoint(self):
		return self.get_query_params().get('VolumeMountpoint')

	def set_VolumeMountpoint(self,VolumeMountpoint):
		self.add_query_param('VolumeMountpoint',VolumeMountpoint)

	def get_EcsOrderLoginInstanceType(self):
		return self.get_query_params().get('EcsOrder.Login.InstanceType')

	def set_EcsOrderLoginInstanceType(self,EcsOrderLoginInstanceType):
		self.add_query_param('EcsOrder.Login.InstanceType',EcsOrderLoginInstanceType)