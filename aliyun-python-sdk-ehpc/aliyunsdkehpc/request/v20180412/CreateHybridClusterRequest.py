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

class CreateHybridClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'CreateHybridCluster')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_MultiOs(self):
		return self.get_query_params().get('MultiOs')

	def set_MultiOs(self,MultiOs):
		self.add_query_param('MultiOs',MultiOs)

	def get_SecurityGroupName(self):
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self,SecurityGroupName):
		self.add_query_param('SecurityGroupName',SecurityGroupName)

	def get_OnPremiseVolumeRemotePath(self):
		return self.get_query_params().get('OnPremiseVolumeRemotePath')

	def set_OnPremiseVolumeRemotePath(self,OnPremiseVolumeRemotePath):
		self.add_query_param('OnPremiseVolumeRemotePath',OnPremiseVolumeRemotePath)

	def get_ImageOwnerAlias(self):
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self,ImageOwnerAlias):
		self.add_query_param('ImageOwnerAlias',ImageOwnerAlias)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_ComputeSpotPriceLimit(self):
		return self.get_query_params().get('ComputeSpotPriceLimit')

	def set_ComputeSpotPriceLimit(self,ComputeSpotPriceLimit):
		self.add_query_param('ComputeSpotPriceLimit',ComputeSpotPriceLimit)

	def get_OnPremiseVolumeLocalPath(self):
		return self.get_query_params().get('OnPremiseVolumeLocalPath')

	def set_OnPremiseVolumeLocalPath(self,OnPremiseVolumeLocalPath):
		self.add_query_param('OnPremiseVolumeLocalPath',OnPremiseVolumeLocalPath)

	def get_RemoteDirectory(self):
		return self.get_query_params().get('RemoteDirectory')

	def set_RemoteDirectory(self,RemoteDirectory):
		self.add_query_param('RemoteDirectory',RemoteDirectory)

	def get_ComputeSpotStrategy(self):
		return self.get_query_params().get('ComputeSpotStrategy')

	def set_ComputeSpotStrategy(self,ComputeSpotStrategy):
		self.add_query_param('ComputeSpotStrategy',ComputeSpotStrategy)

	def get_PostInstallScripts(self):
		return self.get_query_params().get('PostInstallScript')

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

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)

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

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_EhpcVersion(self):
		return self.get_query_params().get('EhpcVersion')

	def set_EhpcVersion(self,EhpcVersion):
		self.add_query_param('EhpcVersion',EhpcVersion)

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

	def get_OnPremiseVolumeMountPoint(self):
		return self.get_query_params().get('OnPremiseVolumeMountPoint')

	def set_OnPremiseVolumeMountPoint(self,OnPremiseVolumeMountPoint):
		self.add_query_param('OnPremiseVolumeMountPoint',OnPremiseVolumeMountPoint)

	def get_OnPremiseVolumeProtocol(self):
		return self.get_query_params().get('OnPremiseVolumeProtocol')

	def set_OnPremiseVolumeProtocol(self,OnPremiseVolumeProtocol):
		self.add_query_param('OnPremiseVolumeProtocol',OnPremiseVolumeProtocol)

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

	def get_Nodess(self):
		return self.get_query_params().get('Nodes')

	def set_Nodess(self, Nodess):
		for depth1 in range(len(Nodess)):
			if Nodess[depth1].get('IpAddress') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.IpAddress', Nodess[depth1].get('IpAddress'))
			if Nodess[depth1].get('HostName') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.HostName', Nodess[depth1].get('HostName'))
			if Nodess[depth1].get('Role') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.Role', Nodess[depth1].get('Role'))
			if Nodess[depth1].get('AccountType') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.AccountType', Nodess[depth1].get('AccountType'))
			if Nodess[depth1].get('SchedulerType') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.SchedulerType', Nodess[depth1].get('SchedulerType'))

	def get_Applications(self):
		return self.get_query_params().get('Application')

	def set_Applications(self, Applications):
		for depth1 in range(len(Applications)):
			if Applications[depth1].get('Tag') is not None:
				self.add_query_param('Application.' + str(depth1 + 1) + '.Tag', Applications[depth1].get('Tag'))

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_VolumeMountpoint(self):
		return self.get_query_params().get('VolumeMountpoint')

	def set_VolumeMountpoint(self,VolumeMountpoint):
		self.add_query_param('VolumeMountpoint',VolumeMountpoint)

	def get_SchedulerPreInstall(self):
		return self.get_query_params().get('SchedulerPreInstall')

	def set_SchedulerPreInstall(self,SchedulerPreInstall):
		self.add_query_param('SchedulerPreInstall',SchedulerPreInstall)

	def get_Location(self):
		return self.get_query_params().get('Location')

	def set_Location(self,Location):
		self.add_query_param('Location',Location)