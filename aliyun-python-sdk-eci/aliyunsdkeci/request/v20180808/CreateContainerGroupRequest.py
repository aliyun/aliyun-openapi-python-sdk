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
class CreateContainerGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eci', '2018-08-08', 'CreateContainerGroup','eci')

	def get_Containers(self):
		return self.get_query_params().get('Containers')

	def set_Containers(self,Containers):
		for i in range(len(Containers)):	
			if Containers[i].get('Image') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Image' , Containers[i].get('Image'))
			if Containers[i].get('Name') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Name' , Containers[i].get('Name'))
			if Containers[i].get('Cpu') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Cpu' , Containers[i].get('Cpu'))
			if Containers[i].get('Memory') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Memory' , Containers[i].get('Memory'))
			if Containers[i].get('WorkingDir') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.WorkingDir' , Containers[i].get('WorkingDir'))
			if Containers[i].get('ImagePullPolicy') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ImagePullPolicy' , Containers[i].get('ImagePullPolicy'))

			if Containers[i].get('Commands') is not None:
				for j in range(len(Containers[i].get('Commands'))):
					if Containers[i].get('Commands')[j] is not None:
						self.add_query_param('Container.' + str(i + 1) + '.Command.' + str(j + 1),
											 Containers[i].get('Commands')[j])

			if Containers[i].get('Args') is not None:
				for j in range(len(Containers[i].get('Args'))):
					if Containers[i].get('Args')[j] is not None:
						self.add_query_param('Container.' + str(i + 1) + '.Arg.' + str(j + 1),
											 Containers[i].get('Args')[j])

			if Containers[i].get('VolumeMounts') is not None:
				for j in range(len(Containers[i].get('VolumeMounts'))):
					if Containers[i].get('VolumeMounts')[j] is not None:
						self.add_query_param('Container.' + str(i + 1) + '.VolumeMount.' + str(j + 1) + '.Name',
											 Containers[i].get('VolumeMounts')[j].get('Name'))
						self.add_query_param('Container.' + str(i + 1) + '.VolumeMount.' + str(j + 1) + '.MountPath',
											 Containers[i].get('VolumeMounts')[j].get('MountPath'))
						self.add_query_param('Container.' + str(i + 1) + '.VolumeMount.' + str(j + 1) + '.ReadOnly',
											 Containers[i].get('VolumeMounts')[j].get('ReadOnly'))

			if Containers[i].get('Ports') is not None:
				for j in range(len(Containers[i].get('Ports'))):
					if Containers[i].get('Ports')[j] is not None:
						self.add_query_param('Container.' + str(i + 1) + '.Port.' + str(j + 1) + '.Protocol',
											 Containers[i].get('Ports')[j].get('Protocol'))
						self.add_query_param('Container.' + str(i + 1) + '.Port.' + str(j + 1) + '.Port',
											 Containers[i].get('Ports')[j].get('Port'))

			if Containers[i].get('EnvironmentVars') is not None:
				for j in range(len(Containers[i].get('EnvironmentVars'))):
					if Containers[i].get('EnvironmentVars')[j] is not None:
						self.add_query_param('Container.' + str(i + 1) + '.EnvironmentVar.' + str(j + 1) + '.Key',
											 Containers[i].get('EnvironmentVars')[j].get('Key'))
						self.add_query_param('Container.' + str(i + 1) + '.EnvironmentVar.' + str(j + 1) + '.Value',
											 Containers[i].get('EnvironmentVars')[j].get('Value'))


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_InitContainers(self):
		return self.get_query_params().get('InitContainers')

	def set_InitContainers(self,InitContainers):
		for i in range(len(InitContainers)):
			if InitContainers[i].get('Image') is not None:
				self.add_query_param('InitContainer.' + str(i + 1) + '.Image', InitContainers[i].get('Image'))
			if InitContainers[i].get('Name') is not None:
				self.add_query_param('InitContainer.' + str(i + 1) + '.Name', InitContainers[i].get('Name'))
			if InitContainers[i].get('Cpu') is not None:
				self.add_query_param('InitContainer.' + str(i + 1) + '.Cpu', InitContainers[i].get('Cpu'))
			if InitContainers[i].get('Memory') is not None:
				self.add_query_param('InitContainer.' + str(i + 1) + '.Memory', InitContainers[i].get('Memory'))
			if InitContainers[i].get('WorkingDir') is not None:
				self.add_query_param('InitContainer.' + str(i + 1) + '.WorkingDir', InitContainers[i].get('WorkingDir'))
			if InitContainers[i].get('ImagePullPolicy') is not None:
				self.add_query_param('InitContainer.' + str(i + 1) + '.ImagePullPolicy',
									 InitContainers[i].get('ImagePullPolicy'))

			if InitContainers[i].get('Commands') is not None:
				for j in range(len(InitContainers[i].get('Commands'))):
					if InitContainers[i].get('Commands')[j] is not None:
						self.add_query_param('InitContainer.' + str(i + 1) + '.Command.' + str(j + 1),
											 InitContainers[i].get('Commands')[j])

			if InitContainers[i].get('Args') is not None:
				for j in range(len(InitContainers[i].get('Args'))):
					if InitContainers[i].get('Args')[j] is not None:
						self.add_query_param('InitContainer.' + str(i + 1) + '.Arg.' + str(j + 1),
											 InitContainers[i].get('Args')[j])

			if InitContainers[i].get('VolumeMounts') is not None:
				for j in range(len(InitContainers[i].get('VolumeMounts'))):
					if InitContainers[i].get('VolumeMounts')[j] is not None:
						self.add_query_param('InitContainer.' + str(i + 1) + '.VolumeMount.' + str(j + 1) + '.Name',
											 InitContainers[i].get('VolumeMounts')[j].get('Name'))
						self.add_query_param('InitContainer.' + str(i + 1) + '.VolumeMount.' + str(j + 1) + '.MountPath',
											 InitContainers[i].get('VolumeMounts')[j].get('MountPath'))
						self.add_query_param('InitContainer.' + str(i + 1) + '.VolumeMount.' + str(j + 1) + '.ReadOnly',
											 InitContainers[i].get('VolumeMounts')[j].get('ReadOnly'))

			if InitContainers[i].get('Ports') is not None:
				for j in range(len(InitContainers[i].get('Ports'))):
					if InitContainers[i].get('Ports')[j] is not None:
						self.add_query_param('InitContainer.' + str(i + 1) + '.Port.' + str(j + 1) + '.Protocol',
											 InitContainers[i].get('Ports')[j].get('Protocol'))
						self.add_query_param('InitContainer.' + str(i + 1) + '.Port.' + str(j + 1) + '.Port',
											 InitContainers[i].get('Ports')[j].get('Port'))

			if InitContainers[i].get('EnvironmentVars') is not None:
				for j in range(len(InitContainers[i].get('EnvironmentVars'))):
					if InitContainers[i].get('EnvironmentVars')[j] is not None:
						self.add_query_param('InitContainer.' + str(i + 1) + '.EnvironmentVar.' + str(j + 1) + '.Key',
											 InitContainers[i].get('EnvironmentVars')[j].get('Key'))
						self.add_query_param('InitContainer.' + str(i + 1) + '.EnvironmentVar.' + str(j + 1) + '.Value',
											 InitContainers[i].get('EnvironmentVars')[j].get('Value'))

	def get_ImageRegistryCredentials(self):
		return self.get_query_params().get('ImageRegistryCredentials')

	def set_ImageRegistryCredentials(self,ImageRegistryCredentials):
		for i in range(len(ImageRegistryCredentials)):	
			if ImageRegistryCredentials[i].get('Server') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(i + 1) + '.Server' , ImageRegistryCredentials[i].get('Server'))
			if ImageRegistryCredentials[i].get('UserName') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(i + 1) + '.UserName' , ImageRegistryCredentials[i].get('UserName'))
			if ImageRegistryCredentials[i].get('Password') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(i + 1) + '.Password' , ImageRegistryCredentials[i].get('Password'))


	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		for i in range(len(Tags)):	
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key' , Tags[i].get('Key'))
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value' , Tags[i].get('Value'))


	def get_EipInstanceId(self):
		return self.get_query_params().get('EipInstanceId')

	def set_EipInstanceId(self,EipInstanceId):
		self.add_query_param('EipInstanceId',EipInstanceId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_RestartPolicy(self):
		return self.get_query_params().get('RestartPolicy')

	def set_RestartPolicy(self,RestartPolicy):
		self.add_query_param('RestartPolicy',RestartPolicy)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_Volumes(self):
		return self.get_query_params().get('Volumes')

	def set_Volumes(self,Volumes):
		for i in range(len(Volumes)):	
			if Volumes[i].get('Name') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.Name' , Volumes[i].get('Name'))
			if Volumes[i].get('NFSVolume.Server') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.NFSVolume.Server' , Volumes[i].get('NFSVolume.Server'))
			if Volumes[i].get('NFSVolume.Path') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.NFSVolume.Path' , Volumes[i].get('NFSVolume.Path'))
			if Volumes[i].get('NFSVolume.ReadOnly') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.NFSVolume.ReadOnly' , Volumes[i].get('NFSVolume.ReadOnly'))

			if Volumes[i].get('ConfigFileVolume.ConfigFileToPaths') is not None:
				for j in range(len(Volumes[i].get('ConfigFileVolume.ConfigFileToPaths'))):
					if Volumes[i].get('ConfigFileVolume.ConfigFileToPaths')[j] is not None:
						self.add_query_param(
							'Volume.' + str(i + 1) + '.ConfigFileVolume.ConfigFileToPath.' + str(j + 1) + '.Path',
							Volumes[i].get('ConfigFileVolume.ConfigFileToPaths')[j].get('Path'))
						self.add_query_param(
							'Volume.' + str(i + 1) + '.ConfigFileVolume.ConfigFileToPath.' + str(j + 1) + '.Content',
							Volumes[i].get('ConfigFileVolume.ConfigFileToPaths')[j].get('Content'))

			if Volumes[i].get('Type') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.Type' , Volumes[i].get('Type'))


	def get_ContainerGroupName(self):
		return self.get_query_params().get('ContainerGroupName')

	def set_ContainerGroupName(self,ContainerGroupName):
		self.add_query_param('ContainerGroupName',ContainerGroupName)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)