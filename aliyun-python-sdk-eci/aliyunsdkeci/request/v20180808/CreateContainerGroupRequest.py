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
		RpcRequest.__init__(self, 'Eci', '2018-08-08', 'CreateContainerGroup', 'eci')

	def get_Containers(self):
		return self.get_query_params().get('Containers')

	def set_Containers(self, Containers):
		for i in range(len(Containers)):
			if Containers[i].get('Image') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Image', Containers[i].get('Image'))
			if Containers[i].get('Name') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Name', Containers[i].get('Name'))
			if Containers[i].get('Cpu') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Cpu', Containers[i].get('Cpu'))
			if Containers[i].get('Memory') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Memory', Containers[i].get('Memory'))
			if Containers[i].get('WorkingDir') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.WorkingDir', Containers[i].get('WorkingDir'))
			if Containers[i].get('ImagePullPolicy') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ImagePullPolicy',
									 Containers[i].get('ImagePullPolicy'))

			# ReadinessProbe
			if Containers[i].get('ReadinessProbe.HttpGet.Path') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.HttpGet.Path',
									 Containers[i].get('ReadinessProbe.HttpGet.Path'))
			if Containers[i].get('ReadinessProbe.HttpGet.Port') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.HttpGet.Port',
									 Containers[i].get('ReadinessProbe.HttpGet.Port'))
			if Containers[i].get('ReadinessProbe.HttpGet.Scheme') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.HttpGet.Scheme',
									 Containers[i].get('ReadinessProbe.HttpGet.Scheme'))
			if Containers[i].get('ReadinessProbe.InitialDelaySeconds') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.InitialDelaySeconds',
									 Containers[i].get('ReadinessProbe.InitialDelaySeconds'))
			if Containers[i].get('ReadinessProbe.PeriodSeconds') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.PeriodSeconds',
									 Containers[i].get('ReadinessProbe.PeriodSeconds'))
			if Containers[i].get('ReadinessProbe.SuccessThreshold') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.SuccessThreshold',
									 Containers[i].get('ReadinessProbe.SuccessThreshold'))
			if Containers[i].get('ReadinessProbe.FailureThreshold') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.FailureThreshold',
									 Containers[i].get('ReadinessProbe.FailureThreshold'))
			if Containers[i].get('ReadinessProbe.TimeoutSeconds') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.TimeoutSeconds',
									 Containers[i].get('ReadinessProbe.TimeoutSeconds'))
			if Containers[i].get('ReadinessProbe.Exec.Commands') is not None:
				for j in range(len(Containers[i].get('ReadinessProbe.Exec.Commands'))):
					if Containers[i].get('ReadinessProbe.Exec.Commands')[j] is not None:
						self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.Exec.Command.' + str(j + 1),
											 Containers[i].get('ReadinessProbe.Exec.Commands')[j])
			if Containers[i].get('ReadinessProbe.TcpSocket.Port') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.ReadinessProbe.TcpSocket.Port',
									 Containers[i].get('ReadinessProbe.TcpSocket.Port'))

			# LivenessProbe
			if Containers[i].get('LivenessProbe.HttpGet.Path') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.HttpGet.Path',
									 Containers[i].get('LivenessProbe.HttpGet.Path'))
			if Containers[i].get('LivenessProbe.HttpGet.Port') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.HttpGet.Port',
									 Containers[i].get('LivenessProbe.HttpGet.Port'))
			if Containers[i].get('LivenessProbe.HttpGet.Scheme') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.HttpGet.Scheme',
									 Containers[i].get('LivenessProbe.HttpGet.Scheme'))
			if Containers[i].get('LivenessProbe.InitialDelaySeconds') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.InitialDelaySeconds',
									 Containers[i].get('LivenessProbe.InitialDelaySeconds'))
			if Containers[i].get('LivenessProbe.PeriodSeconds') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.PeriodSeconds',
									 Containers[i].get('LivenessProbe.PeriodSeconds'))
			if Containers[i].get('LivenessProbe.SuccessThreshold') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.SuccessThreshold',
									 Containers[i].get('LivenessProbe.SuccessThreshold'))
			if Containers[i].get('LivenessProbe.FailureThreshold') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.FailureThreshold',
									 Containers[i].get('LivenessProbe.FailureThreshold'))
			if Containers[i].get('LivenessProbe.TimeoutSeconds') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.TimeoutSeconds',
									 Containers[i].get('LivenessProbe.TimeoutSeconds'))
			if Containers[i].get('LivenessProbe.Exec.Commands') is not None:
				for j in range(len(Containers[i].get('LivenessProbe.Exec.Commands'))):
					if Containers[i].get('LivenessProbe.Exec.Commands')[j] is not None:
						self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.Exec.Command.' + str(j + 1),
											 Containers[i].get('LivenessProbe.Exec.Commands')[j])
			if Containers[i].get('LivenessProbe.TcpSocket.Port') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LivenessProbe.TcpSocket.Port',
									 Containers[i].get('LivenessProbe.TcpSocket.Port'))
			# SecurityContext
			if Containers[i].get('SecurityContext.Capability.Adds') is not None:
				for j in range(len(Containers[i].get('SecurityContext.Capability.Adds'))):
					if Containers[i].get('SecurityContext.Capability.Adds')[j] is not None:
						self.add_query_param(
							'Container.' + str(i + 1) + '.SecurityContext.Capability.Add.' + str(j + 1),
							Containers[i].get('SecurityContext.Capability.Adds')[j])
			if Containers[i].get('SecurityContext.ReadOnlyRootFilesystem') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.SecurityContext.ReadOnlyRootFilesystem',
									 Containers[i].get('SecurityContext.ReadOnlyRootFilesystem'))
			if Containers[i].get('SecurityContext.RunAsUser') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.SecurityContext.RunAsUser',
									 Containers[i].get('SecurityContext.RunAsUser'))
			# LifecyclePostStartHandler
			if Containers[i].get('LifecyclePostStartHandlerHttpGetHost') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePostStartHandlerHttpGetHost',
									 Containers[i].get('LifecyclePostStartHandlerHttpGetHost'))
			if Containers[i].get('LifecyclePostStartHandlerHttpGetPort') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePostStartHandlerHttpGetPort',
									 Containers[i].get('LifecyclePostStartHandlerHttpGetPort'))
			if Containers[i].get('LifecyclePostStartHandlerHttpGetPath') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePostStartHandlerHttpGetPath',
									 Containers[i].get('LifecyclePostStartHandlerHttpGetPath'))
			if Containers[i].get('LifecyclePostStartHandlerHttpGetScheme') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePostStartHandlerHttpGetScheme',
									 Containers[i].get('LifecyclePostStartHandlerHttpGetScheme'))
			if Containers[i].get('LifecyclePostStartHandlerHttpGetHttpHeaders') is not None:
				for j in range(len(Containers[i].get('LifecyclePostStartHandlerHttpGetHttpHeaders'))):
					if Containers[i].get('LifecyclePostStartHandlerHttpGetHttpHeaders')[j] is not None:
						self.add_query_param(
							'Container.' + str(i + 1) + '.LifecyclePostStartHandlerHttpGetHttpHeader.' + str(
								j + 1) + '.Name',
							Containers[i].get('LifecyclePostStartHandlerHttpGetHttpHeaders')[j].get('Name'))
						self.add_query_param(
							'Container.' + str(i + 1) + '.LifecyclePostStartHandlerHttpGetHttpHeader.' + str(
								j + 1) + '.Value',
							Containers[i].get('LifecyclePostStartHandlerHttpGetHttpHeaders')[j].get('Value'))
			if Containers[i].get('LifecyclePostStartHandlerExecs') is not None:
				for j in range(len(Containers[i].get('LifecyclePostStartHandlerExecs'))):
					if Containers[i].get('LifecyclePostStartHandlerExecs')[j] is not None:
						self.add_query_param('Container.' + str(i + 1) + '.LifecyclePostStartHandlerExec.' + str(j + 1),
											 Containers[i].get('LifecyclePostStartHandlerExecs')[j])
			if Containers[i].get('LifecyclePostStartHandlerTcpSocketHost') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePostStartHandlerTcpSocketHost',
									 Containers[i].get('LifecyclePostStartHandlerTcpSocketHost'))
			if Containers[i].get('LifecyclePostStartHandlerTcpSocketPort') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePostStartHandlerTcpSocketPort',
									 Containers[i].get('LifecyclePostStartHandlerTcpSocketPort'))

			# LifecyclePreStopHandler
			if Containers[i].get('LifecyclePreStopHandlerHttpGetHost') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePreStopHandlerHttpGetHost',
									 Containers[i].get('LifecyclePreStopHandlerHttpGetHost'))
			if Containers[i].get('LifecyclePreStopHandlerHttpGetPort') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePreStopHandlerHttpGetPort',
									 Containers[i].get('LifecyclePreStopHandlerHttpGetPort'))
			if Containers[i].get('LifecyclePreStopHandlerHttpGetPath') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePreStopHandlerHttpGetPath',
									 Containers[i].get('LifecyclePreStopHandlerHttpGetPath'))
			if Containers[i].get('LifecyclePreStopHandlerHttpGetScheme') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePreStopHandlerHttpGetScheme',
									 Containers[i].get('LifecyclePreStopHandlerHttpGetScheme'))
			if Containers[i].get('LifecyclePreStopHandlerHttpGetHttpHeaders') is not None:
				for j in range(len(Containers[i].get('LifecyclePreStopHandlerHttpGetHttpHeaders'))):
					if Containers[i].get('LifecyclePreStopHandlerHttpGetHttpHeaders')[j] is not None:
						self.add_query_param(
							'Container.' + str(i + 1) + '.LifecyclePreStopHandlerHttpGetHttpHeader.' + str(
								j + 1) + '.Name',
							Containers[i].get('LifecyclePreStopHandlerHttpGetHttpHeaders')[j].get('Name'))
						self.add_query_param(
							'Container.' + str(i + 1) + '.LifecyclePreStopHandlerHttpGetHttpHeader.' + str(
								j + 1) + '.Value',
							Containers[i].get('LifecyclePreStopHandlerHttpGetHttpHeaders')[j].get('Value'))
			if Containers[i].get('LifecyclePreStopHandlerExecs') is not None:
				for j in range(len(Containers[i].get('LifecyclePreStopHandlerExecs'))):
					if Containers[i].get('LifecyclePreStopHandlerExecs')[j] is not None:
						self.add_query_param('Container.' + str(i + 1) + '.LifecyclePreStopHandlerExec.' + str(j + 1),
											 Containers[i].get('LifecyclePreStopHandlerExecs')[j])
			if Containers[i].get('LifecyclePreStopHandlerTcpSocketHost') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePreStopHandlerTcpSocketHost',
									 Containers[i].get('LifecyclePreStopHandlerTcpSocketHost'))
			if Containers[i].get('LifecyclePreStopHandlerTcpSocketPort') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.LifecyclePreStopHandlerTcpSocketPort',
									 Containers[i].get('LifecyclePreStopHandlerTcpSocketPort'))

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
						if Containers[i].get('VolumeMounts')[j].get('SubPath') is not None:
							self.add_query_param('Container.' + str(i + 1) + '.VolumeMount.' + str(j + 1) + '.SubPath',
												 Containers[i].get('VolumeMounts')[j].get('SubPath'))
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
			if Containers[i].get('Stdin') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Stdin', Containers[i].get('Stdin'))
			if Containers[i].get('StdinOnce') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.StdinOnce', Containers[i].get('StdinOnce'))
			if Containers[i].get('Tty') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Tty', Containers[i].get('Tty'))
			if Containers[i].get('Gpu') is not None:
				self.add_query_param('Container.' + str(i + 1) + '.Gpu', Containers[i].get('Gpu'))

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):
		self.add_query_param('SecurityGroupId', SecurityGroupId)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):
		self.add_query_param('ResourceGroupId', ResourceGroupId)

	def get_InitContainers(self):
		return self.get_query_params().get('InitContainers')

	def set_InitContainers(self, InitContainers):
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

			# SecurityContext
			if InitContainers[i].get('SecurityContext.Capability.Adds') is not None:
				for j in range(len(InitContainers[i].get('SecurityContext.Capability.Adds'))):
					if InitContainers[i].get('SecurityContext.Capability.Adds')[j] is not None:
						self.add_query_param(
							'InitContainer.' + str(i + 1) + '.SecurityContext.Capability.Add.' + str(j + 1),
							InitContainers[i].get('SecurityContext.Capability.Adds')[j])
			if InitContainers[i].get('SecurityContext.ReadOnlyRootFilesystem') is not None:
				self.add_query_param('InitContainer.' + str(i + 1) + '.SecurityContext.ReadOnlyRootFilesystem',
									 InitContainers[i].get('SecurityContext.ReadOnlyRootFilesystem'))
			if InitContainers[i].get('SecurityContext.RunAsUser') is not None:
				self.add_query_param('InitContainer.' + str(i + 1) + '.SecurityContext.RunAsUser',
									 InitContainers[i].get('SecurityContext.RunAsUser'))

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
						if InitContainers[i].get('VolumeMounts')[j].get('SubPath') is not None:
							self.add_query_param('InitContainer.' + str(i + 1) + '.VolumeMount.' + str(j + 1) + '.SubPath',
												 InitContainers[i].get('VolumeMounts')[j].get('SubPath'))
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

			if InitContainers[i].get('Gpu') is not None:
				self.add_query_param('InitContainer.' + str(i + 1) + '.Gpu', InitContainers[i].get('Gpu'))

	def get_ImageRegistryCredentials(self):
		return self.get_query_params().get('ImageRegistryCredentials')

	def set_ImageRegistryCredentials(self, ImageRegistryCredentials):
		if ImageRegistryCredentials is not None:
			for i in range(len(ImageRegistryCredentials)):
				if ImageRegistryCredentials[i].get('Server') is not None:
					self.add_query_param('ImageRegistryCredential.' + str(i + 1) + '.Server',
										 ImageRegistryCredentials[i].get('Server'))
				if ImageRegistryCredentials[i].get('UserName') is not None:
					self.add_query_param('ImageRegistryCredential.' + str(i + 1) + '.UserName',
										 ImageRegistryCredentials[i].get('UserName'))
				if ImageRegistryCredentials[i].get('Password') is not None:
					self.add_query_param('ImageRegistryCredential.' + str(i + 1) + '.Password',
										 ImageRegistryCredentials[i].get('Password'))

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):
		for i in range(len(Tags)):
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key', Tags[i].get('Key'))
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value', Tags[i].get('Value'))

	def get_EipInstanceId(self):
		return self.get_query_params().get('EipInstanceId')

	def set_EipInstanceId(self, EipInstanceId):
		self.add_query_param('EipInstanceId', EipInstanceId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)

	def get_RestartPolicy(self):
		return self.get_query_params().get('RestartPolicy')

	def set_RestartPolicy(self, RestartPolicy):
		self.add_query_param('RestartPolicy', RestartPolicy)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):
		self.add_query_param('OwnerAccount', OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):
		self.add_query_param('OwnerId', OwnerId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):
		self.add_query_param('VSwitchId', VSwitchId)

	def get_Volumes(self):
		return self.get_query_params().get('Volumes')

	def set_Volumes(self, Volumes):
		for i in range(len(Volumes)):
			if Volumes[i].get('Name') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.Name', Volumes[i].get('Name'))
			if Volumes[i].get('NFSVolume.Server') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.NFSVolume.Server', Volumes[i].get('NFSVolume.Server'))
			if Volumes[i].get('NFSVolume.Path') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.NFSVolume.Path', Volumes[i].get('NFSVolume.Path'))
			if Volumes[i].get('NFSVolume.ReadOnly') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.NFSVolume.ReadOnly',
									 Volumes[i].get('NFSVolume.ReadOnly'))

			if Volumes[i].get('EmptyDirVolume.Medium') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.EmptyDirVolume.Medium',
									 Volumes[i].get('EmptyDirVolume.Medium'))

			if Volumes[i].get('DiskVolume.DiskId') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.DiskVolume.DiskId', Volumes[i].get('DiskVolume.DiskId'))
			if Volumes[i].get('DiskVolume.FsType') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.DiskVolume.FsType', Volumes[i].get('DiskVolume.FsType'))
			if Volumes[i].get('DiskVolume.DiskSize') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.DiskVolume.DiskSize',Volumes[i].get('DiskVolume.DiskSize'))

			if Volumes[i].get('ConfigFileVolume.ConfigFileToPaths') is not None:
				for j in range(len(Volumes[i].get('ConfigFileVolume.ConfigFileToPaths'))):
					if Volumes[i].get('ConfigFileVolume.ConfigFileToPaths')[j] is not None:
						self.add_query_param(
							'Volume.' + str(i + 1) + '.ConfigFileVolume.ConfigFileToPath.' + str(j + 1) + '.Path',
							Volumes[i].get('ConfigFileVolume.ConfigFileToPaths')[j].get('Path'))
						self.add_query_param(
							'Volume.' + str(i + 1) + '.ConfigFileVolume.ConfigFileToPath.' + str(j + 1) + '.Content',
							Volumes[i].get('ConfigFileVolume.ConfigFileToPaths')[j].get('Content'))
			if Volumes[i].get('ConfigFileVolume.DefaultModel') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.ConfigFileVolume.DefaultModel',Volumes[i].get('ConfigFileVolume.DefaultModel'))

			if Volumes[i].get('FlexVolume.Driver') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.FlexVolume.Driver', Volumes[i].get('FlexVolume.Driver'))
			if Volumes[i].get('FlexVolume.FsType') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.FlexVolume.FsType', Volumes[i].get('FlexVolume.FsType'))
			if Volumes[i].get('FlexVolume.Options') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.FlexVolume.Options', Volumes[i].get('FlexVolume.Options'))

			if Volumes[i].get('Type') is not None:
				self.add_query_param('Volume.' + str(i + 1) + '.Type', Volumes[i].get('Type'))

	def get_ContainerGroupName(self):
		return self.get_query_params().get('ContainerGroupName')

	def set_ContainerGroupName(self, ContainerGroupName):
		self.add_query_param('ContainerGroupName', ContainerGroupName)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):
		self.add_query_param('ZoneId', ZoneId)

	# DNS config
	def get_DnsConfigNameServers(self):
		return self.get_query_params().get('DnsConfig.NameServers')

	def set_DnsConfigNameServers(self, DnsConfigNameServers):
		for i in range(len(DnsConfigNameServers)):
			if DnsConfigNameServers[i] is not None:
				self.add_query_param('DnsConfig.NameServer.' + str(i + 1), DnsConfigNameServers[i])

	def get_DnsConfigOptions(self):
		return self.get_query_params().get('DnsConfig.Options')

	def set_DnsConfigOptions(self, DnsConfigOptions):
		for i in range(len(DnsConfigOptions)):
			if DnsConfigOptions[i].get('Name') is not None:
				self.add_query_param('DnsConfig.Option.' + str(i + 1) + '.Name', DnsConfigOptions[i].get('Name'))
			if DnsConfigOptions[i].get('Value') is not None:
				self.add_query_param('DnsConfig.Option.' + str(i + 1) + '.Value', DnsConfigOptions[i].get('Value'))

	def get_DnsConfigSearchs(self):
		return self.get_query_params().get('DnsConfig.Searchs')

	def set_DnsConfigSearchs(self, DnsConfigSearchs):
		for i in range(len(DnsConfigSearchs)):
			if DnsConfigSearchs[i] is not None:
				self.add_query_param('DnsConfig.Search.' + str(i + 1), DnsConfigSearchs[i])

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):
		self.add_query_param('InstanceType', InstanceType)

	def get_SecurityContextSysctls(self):
		return self.get_query_params().get('SecurityContext.Sysctls')

	def set_SecurityContextSysctls(self, SecurityContextSysctls):
		for i in range(len(SecurityContextSysctls)):
			if SecurityContextSysctls[i].get('Name') is not None:
				self.add_query_param('SecurityContext.Sysctl.' + str(i + 1) + '.Name',
									 SecurityContextSysctls[i].get('Name'))
			if SecurityContextSysctls[i].get('Value') is not None:
				self.add_query_param('SecurityContext.Sysctl.' + str(i + 1) + '.Value',
									 SecurityContextSysctls[i].get('Value'))

	def get_HostAliases(self):
		return self.get_query_params().get('HostAliases')

	def set_HostAliases(self, HostAliases):
		for i in range(len(HostAliases)):
			if HostAliases[i].get('Ip') is not None:
				self.add_query_param('HostAliase.' + str(i + 1) + '.Ip', HostAliases[i].get('Ip'))
			for j in range(len(HostAliases[i].get('Hostnames'))):
				if HostAliases[i].get('Hostnames')[j] is not None:
					self.add_query_param('HostAliase.' + str(i + 1) + '.Hostname.' + str(j + 1),
										 HostAliases[i].get('Hostnames')[j])

	def get_DnsPolicy(self):
		return self.get_query_params().get('DnsPolicy')

	def set_DnsPolicy(self, DnsPolicy):
		self.add_query_param('DnsPolicy', DnsPolicy)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):
		self.add_query_param('ClientToken', ClientToken)

	def get_ImageSnapshotId(self):
		return self.get_query_params().get('ImageSnapshotId')

	def set_ImageSnapshotId(self, ImageSnapshotId):
		self.add_query_param('ImageSnapshotId', ImageSnapshotId)

	def get_AutoMatchImageCache(self):
		return self.get_query_params().get('AutoMatchImageCache')

	def set_AutoMatchImageCache(self, AutoMatchImageCache):
		self.add_query_param('AutoMatchImageCache', AutoMatchImageCache)

	def get_SlsEnable(self):
		return self.get_query_params().get('SlsEnable')

	def set_SlsEnable(self, SlsEnable):
		self.add_query_param('SlsEnable', SlsEnable)

	def get_Cpu(self):
		return self.get_query_params().get('Cpu')

	def set_Cpu(self, Cpu):
		self.add_query_param('Cpu', Cpu)

	def get_RamRoleName(self):
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self, RamRoleName):
		self.add_query_param('RamRoleName', RamRoleName)

	def get_Memory(self):
		return self.get_query_params().get('Memory')

	def set_Memory(self, Memory):
		self.add_query_param('Memory', Memory)

	def get_TerminationGracePeriodSeconds(self):
		return self.get_query_params().get('TerminationGracePeriodSeconds')

	def set_TerminationGracePeriodSeconds(self, TerminationGracePeriodSeconds):
		self.add_query_param('TerminationGracePeriodSeconds', TerminationGracePeriodSeconds)

	def get_NtpServers(self):
		return self.get_query_params().get('NtpServers')

	def set_NtpServers(self, NtpServers):
		for i in range(len(NtpServers)):
			if NtpServers[i] is not None:
				self.add_query_param('NtpServer.' + str(i + 1), NtpServers[i])

	def get_SpotStrategy(self):
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):
		self.add_query_param('SpotStrategy', SpotStrategy)

	def get_SpotPriceLimit(self):
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self, SpotPriceLimit):
		self.add_query_param('SpotPriceLimit', SpotPriceLimit)

