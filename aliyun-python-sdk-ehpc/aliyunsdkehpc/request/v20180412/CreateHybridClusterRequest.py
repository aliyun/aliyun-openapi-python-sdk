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

	def get_EcsOrderManagerInstanceType(self): # String
		return self.get_query_params().get('EcsOrder.Manager.InstanceType')

	def set_EcsOrderManagerInstanceType(self, EcsOrderManagerInstanceType):  # String
		self.add_query_param('EcsOrder.Manager.InstanceType', EcsOrderManagerInstanceType)
	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_MultiOs(self): # Boolean
		return self.get_query_params().get('MultiOs')

	def set_MultiOs(self, MultiOs):  # Boolean
		self.add_query_param('MultiOs', MultiOs)
	def get_SecurityGroupName(self): # String
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self, SecurityGroupName):  # String
		self.add_query_param('SecurityGroupName', SecurityGroupName)
	def get_OnPremiseVolumeRemotePath(self): # String
		return self.get_query_params().get('OnPremiseVolumeRemotePath')

	def set_OnPremiseVolumeRemotePath(self, OnPremiseVolumeRemotePath):  # String
		self.add_query_param('OnPremiseVolumeRemotePath', OnPremiseVolumeRemotePath)
	def get_ImageOwnerAlias(self): # String
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self, ImageOwnerAlias):  # String
		self.add_query_param('ImageOwnerAlias', ImageOwnerAlias)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_WinAdPar(self): # Struct
		return self.get_query_params().get('WinAdPar')

	def set_WinAdPar(self, WinAdPar):  # Struct
		if WinAdPar.get('AdUser') is not None:
			self.add_query_param('WinAdPar.AdUser', WinAdPar.get('AdUser'))
		if WinAdPar.get('AdUserPasswd') is not None:
			self.add_query_param('WinAdPar.AdUserPasswd', WinAdPar.get('AdUserPasswd'))
		if WinAdPar.get('AdIp') is not None:
			self.add_query_param('WinAdPar.AdIp', WinAdPar.get('AdIp'))
		if WinAdPar.get('AdDc') is not None:
			self.add_query_param('WinAdPar.AdDc', WinAdPar.get('AdDc'))
	def get_ComputeSpotPriceLimit(self): # Float
		return self.get_query_params().get('ComputeSpotPriceLimit')

	def set_ComputeSpotPriceLimit(self, ComputeSpotPriceLimit):  # Float
		self.add_query_param('ComputeSpotPriceLimit', ComputeSpotPriceLimit)
	def get_OnPremiseVolumeLocalPath(self): # String
		return self.get_query_params().get('OnPremiseVolumeLocalPath')

	def set_OnPremiseVolumeLocalPath(self, OnPremiseVolumeLocalPath):  # String
		self.add_query_param('OnPremiseVolumeLocalPath', OnPremiseVolumeLocalPath)
	def get_RemoteDirectory(self): # String
		return self.get_query_params().get('RemoteDirectory')

	def set_RemoteDirectory(self, RemoteDirectory):  # String
		self.add_query_param('RemoteDirectory', RemoteDirectory)
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
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
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
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_EhpcVersion(self): # String
		return self.get_query_params().get('EhpcVersion')

	def set_EhpcVersion(self, EhpcVersion):  # String
		self.add_query_param('EhpcVersion', EhpcVersion)
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
	def get_OpenldapPar(self): # Struct
		return self.get_query_params().get('OpenldapPar')

	def set_OpenldapPar(self, OpenldapPar):  # Struct
		if OpenldapPar.get('BaseDn') is not None:
			self.add_query_param('OpenldapPar.BaseDn', OpenldapPar.get('BaseDn'))
		if OpenldapPar.get('LdapServerIp') is not None:
			self.add_query_param('OpenldapPar.LdapServerIp', OpenldapPar.get('LdapServerIp'))
	def get_JobQueue(self): # String
		return self.get_query_params().get('JobQueue')

	def set_JobQueue(self, JobQueue):  # String
		self.add_query_param('JobQueue', JobQueue)
	def get_VolumeType(self): # String
		return self.get_query_params().get('VolumeType')

	def set_VolumeType(self, VolumeType):  # String
		self.add_query_param('VolumeType', VolumeType)
	def get_OnPremiseVolumeMountPoint(self): # String
		return self.get_query_params().get('OnPremiseVolumeMountPoint')

	def set_OnPremiseVolumeMountPoint(self, OnPremiseVolumeMountPoint):  # String
		self.add_query_param('OnPremiseVolumeMountPoint', OnPremiseVolumeMountPoint)
	def get_OnPremiseVolumeProtocol(self): # String
		return self.get_query_params().get('OnPremiseVolumeProtocol')

	def set_OnPremiseVolumeProtocol(self, OnPremiseVolumeProtocol):  # String
		self.add_query_param('OnPremiseVolumeProtocol', OnPremiseVolumeProtocol)
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
	def get_Nodess(self): # RepeatList
		return self.get_query_params().get('Nodes')

	def set_Nodess(self, Nodes):  # RepeatList
		for depth1 in range(len(Nodes)):
			if Nodes[depth1].get('IpAddress') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.IpAddress', Nodes[depth1].get('IpAddress'))
			if Nodes[depth1].get('HostName') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.HostName', Nodes[depth1].get('HostName'))
			if Nodes[depth1].get('Role') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.Role', Nodes[depth1].get('Role'))
			if Nodes[depth1].get('SchedulerType') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.SchedulerType', Nodes[depth1].get('SchedulerType'))
			if Nodes[depth1].get('AccountType') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.AccountType', Nodes[depth1].get('AccountType'))
			if Nodes[depth1].get('Dir') is not None:
				self.add_query_param('Nodes.' + str(depth1 + 1) + '.Dir', Nodes[depth1].get('Dir'))
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
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_VolumeMountpoint(self): # String
		return self.get_query_params().get('VolumeMountpoint')

	def set_VolumeMountpoint(self, VolumeMountpoint):  # String
		self.add_query_param('VolumeMountpoint', VolumeMountpoint)
	def get_SchedulerPreInstall(self): # Boolean
		return self.get_query_params().get('SchedulerPreInstall')

	def set_SchedulerPreInstall(self, SchedulerPreInstall):  # Boolean
		self.add_query_param('SchedulerPreInstall', SchedulerPreInstall)
	def get_Location(self): # String
		return self.get_query_params().get('Location')

	def set_Location(self, Location):  # String
		self.add_query_param('Location', Location)
