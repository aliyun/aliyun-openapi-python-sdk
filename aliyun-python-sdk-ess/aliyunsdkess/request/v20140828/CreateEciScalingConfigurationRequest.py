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
from aliyunsdkess.endpoint import endpoint_data

class CreateEciScalingConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'CreateEciScalingConfiguration','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Containers(self): # RepeatList
		return self.get_query_params().get('Container')

	def set_Containers(self, Container):  # RepeatList
		for depth1 in range(len(Container)):
			if Container[depth1].get('Stdin') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Stdin', Container[depth1].get('Stdin'))
			if Container[depth1].get('Memory') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Memory', Container[depth1].get('Memory'))
			if Container[depth1].get('LivenessProbe.Exec.Command') is not None:
				for depth2 in range(len(Container[depth1].get('LivenessProbe.Exec.Command'))):
					self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.Exec.Command.' + str(depth2 + 1), Container[depth1].get('LivenessProbe.Exec.Command')[depth2])
			if Container[depth1].get('WorkingDir') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.WorkingDir', Container[depth1].get('WorkingDir'))
			if Container[depth1].get('ReadinessProbe.HttpGet.Port') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.HttpGet.Port', Container[depth1].get('ReadinessProbe.HttpGet.Port'))
			if Container[depth1].get('ReadinessProbe.FailureThreshold') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.FailureThreshold', Container[depth1].get('ReadinessProbe.FailureThreshold'))
			if Container[depth1].get('LivenessProbe.HttpGet.Port') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.HttpGet.Port', Container[depth1].get('LivenessProbe.HttpGet.Port'))
			if Container[depth1].get('Arg') is not None:
				for depth2 in range(len(Container[depth1].get('Arg'))):
					self.add_query_param('Container.' + str(depth1 + 1) + '.Arg.' + str(depth2 + 1), Container[depth1].get('Arg')[depth2])
			if Container[depth1].get('ReadinessProbe.SuccessThreshold') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.SuccessThreshold', Container[depth1].get('ReadinessProbe.SuccessThreshold'))
			if Container[depth1].get('VolumeMount') is not None:
				for depth2 in range(len(Container[depth1].get('VolumeMount'))):
					if Container[depth1].get('VolumeMount')[depth2].get('MountPath') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.'  + str(depth2 + 1) + '.MountPath', Container[depth1].get('VolumeMount')[depth2].get('MountPath'))
					if Container[depth1].get('VolumeMount')[depth2].get('ReadOnly') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.'  + str(depth2 + 1) + '.ReadOnly', Container[depth1].get('VolumeMount')[depth2].get('ReadOnly'))
					if Container[depth1].get('VolumeMount')[depth2].get('MountPropagation') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.'  + str(depth2 + 1) + '.MountPropagation', Container[depth1].get('VolumeMount')[depth2].get('MountPropagation'))
					if Container[depth1].get('VolumeMount')[depth2].get('Name') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.'  + str(depth2 + 1) + '.Name', Container[depth1].get('VolumeMount')[depth2].get('Name'))
					if Container[depth1].get('VolumeMount')[depth2].get('SubPath') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.'  + str(depth2 + 1) + '.SubPath', Container[depth1].get('VolumeMount')[depth2].get('SubPath'))
			if Container[depth1].get('Image') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Image', Container[depth1].get('Image'))
			if Container[depth1].get('SecurityContext.Capability.Add') is not None:
				for depth2 in range(len(Container[depth1].get('SecurityContext.Capability.Add'))):
					self.add_query_param('Container.' + str(depth1 + 1) + '.SecurityContext.Capability.Add.' + str(depth2 + 1), Container[depth1].get('SecurityContext.Capability.Add')[depth2])
			if Container[depth1].get('ReadinessProbe.InitialDelaySeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.InitialDelaySeconds', Container[depth1].get('ReadinessProbe.InitialDelaySeconds'))
			if Container[depth1].get('Cpu') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Cpu', Container[depth1].get('Cpu'))
			if Container[depth1].get('ReadinessProbe.Exec.Command') is not None:
				for depth2 in range(len(Container[depth1].get('ReadinessProbe.Exec.Command'))):
					self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.Exec.Command.' + str(depth2 + 1), Container[depth1].get('ReadinessProbe.Exec.Command')[depth2])
			if Container[depth1].get('ReadinessProbe.HttpGet.Scheme') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.HttpGet.Scheme', Container[depth1].get('ReadinessProbe.HttpGet.Scheme'))
			if Container[depth1].get('ReadinessProbe.HttpGet.Path') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.HttpGet.Path', Container[depth1].get('ReadinessProbe.HttpGet.Path'))
			if Container[depth1].get('Gpu') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Gpu', Container[depth1].get('Gpu'))
			if Container[depth1].get('StdinOnce') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.StdinOnce', Container[depth1].get('StdinOnce'))
			if Container[depth1].get('ImagePullPolicy') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ImagePullPolicy', Container[depth1].get('ImagePullPolicy'))
			if Container[depth1].get('Command') is not None:
				for depth2 in range(len(Container[depth1].get('Command'))):
					self.add_query_param('Container.' + str(depth1 + 1) + '.Command.' + str(depth2 + 1), Container[depth1].get('Command')[depth2])
			if Container[depth1].get('LivenessProbe.SuccessThreshold') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.SuccessThreshold', Container[depth1].get('LivenessProbe.SuccessThreshold'))
			if Container[depth1].get('SecurityContext.RunAsUser') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.SecurityContext.RunAsUser', Container[depth1].get('SecurityContext.RunAsUser'))
			if Container[depth1].get('LivenessProbe.HttpGet.Path') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.HttpGet.Path', Container[depth1].get('LivenessProbe.HttpGet.Path'))
			if Container[depth1].get('LivenessProbe.PeriodSeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.PeriodSeconds', Container[depth1].get('LivenessProbe.PeriodSeconds'))
			if Container[depth1].get('LivenessProbe.InitialDelaySeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.InitialDelaySeconds', Container[depth1].get('LivenessProbe.InitialDelaySeconds'))
			if Container[depth1].get('LivenessProbe.TimeoutSeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.TimeoutSeconds', Container[depth1].get('LivenessProbe.TimeoutSeconds'))
			if Container[depth1].get('LivenessProbe.TcpSocket.Port') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.TcpSocket.Port', Container[depth1].get('LivenessProbe.TcpSocket.Port'))
			if Container[depth1].get('Port') is not None:
				for depth2 in range(len(Container[depth1].get('Port'))):
					if Container[depth1].get('Port')[depth2].get('Protocol') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.Port.'  + str(depth2 + 1) + '.Protocol', Container[depth1].get('Port')[depth2].get('Protocol'))
					if Container[depth1].get('Port')[depth2].get('Port') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.Port.'  + str(depth2 + 1) + '.Port', Container[depth1].get('Port')[depth2].get('Port'))
			if Container[depth1].get('ReadinessProbe.PeriodSeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.PeriodSeconds', Container[depth1].get('ReadinessProbe.PeriodSeconds'))
			if Container[depth1].get('EnvironmentVar') is not None:
				for depth2 in range(len(Container[depth1].get('EnvironmentVar'))):
					if Container[depth1].get('EnvironmentVar')[depth2].get('FieldRefFieldPath') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.EnvironmentVar.'  + str(depth2 + 1) + '.FieldRefFieldPath', Container[depth1].get('EnvironmentVar')[depth2].get('FieldRefFieldPath'))
					if Container[depth1].get('EnvironmentVar')[depth2].get('Value') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.EnvironmentVar.'  + str(depth2 + 1) + '.Value', Container[depth1].get('EnvironmentVar')[depth2].get('Value'))
					if Container[depth1].get('EnvironmentVar')[depth2].get('Key') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.EnvironmentVar.'  + str(depth2 + 1) + '.Key', Container[depth1].get('EnvironmentVar')[depth2].get('Key'))
			if Container[depth1].get('Tty') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Tty', Container[depth1].get('Tty'))
			if Container[depth1].get('Name') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Name', Container[depth1].get('Name'))
			if Container[depth1].get('SecurityContext.ReadOnlyRootFilesystem') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.SecurityContext.ReadOnlyRootFilesystem', Container[depth1].get('SecurityContext.ReadOnlyRootFilesystem'))
			if Container[depth1].get('LivenessProbe.FailureThreshold') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.FailureThreshold', Container[depth1].get('LivenessProbe.FailureThreshold'))
			if Container[depth1].get('ReadinessProbe.TimeoutSeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.TimeoutSeconds', Container[depth1].get('ReadinessProbe.TimeoutSeconds'))
			if Container[depth1].get('ReadinessProbe.TcpSocket.Port') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.TcpSocket.Port', Container[depth1].get('ReadinessProbe.TcpSocket.Port'))
			if Container[depth1].get('LivenessProbe.HttpGet.Scheme') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.HttpGet.Scheme', Container[depth1].get('LivenessProbe.HttpGet.Scheme'))
	def get_NtpServers(self): # RepeatList
		return self.get_query_params().get('NtpServer')

	def set_NtpServers(self, NtpServer):  # RepeatList
		for depth1 in range(len(NtpServer)):
			self.add_query_param('NtpServer.' + str(depth1 + 1), NtpServer[depth1])
	def get_SpotPriceLimit(self): # Float
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self, SpotPriceLimit):  # Float
		self.add_query_param('SpotPriceLimit', SpotPriceLimit)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_HostName(self): # String
		return self.get_query_params().get('HostName')

	def set_HostName(self, HostName):  # String
		self.add_query_param('HostName', HostName)
	def get_ActiveDeadlineSeconds(self): # Long
		return self.get_query_params().get('ActiveDeadlineSeconds')

	def set_ActiveDeadlineSeconds(self, ActiveDeadlineSeconds):  # Long
		self.add_query_param('ActiveDeadlineSeconds', ActiveDeadlineSeconds)
	def get_EgressBandwidth(self): # Long
		return self.get_query_params().get('EgressBandwidth')

	def set_EgressBandwidth(self, EgressBandwidth):  # Long
		self.add_query_param('EgressBandwidth', EgressBandwidth)
	def get_DnsConfigSearchs(self): # RepeatList
		return self.get_query_params().get('DnsConfigSearch')

	def set_DnsConfigSearchs(self, DnsConfigSearch):  # RepeatList
		for depth1 in range(len(DnsConfigSearch)):
			self.add_query_param('DnsConfigSearch.' + str(depth1 + 1), DnsConfigSearch[depth1])
	def get_HostAliases(self): # RepeatList
		return self.get_query_params().get('HostAliase')

	def set_HostAliases(self, HostAliase):  # RepeatList
		for depth1 in range(len(HostAliase)):
			if HostAliase[depth1].get('Hostname') is not None:
				for depth2 in range(len(HostAliase[depth1].get('Hostname'))):
					self.add_query_param('HostAliase.' + str(depth1 + 1) + '.Hostname.' + str(depth2 + 1), HostAliase[depth1].get('Hostname')[depth2])
			if HostAliase[depth1].get('Ip') is not None:
				self.add_query_param('HostAliase.' + str(depth1 + 1) + '.Ip', HostAliase[depth1].get('Ip'))
	def get_ImageSnapshotId(self): # String
		return self.get_query_params().get('ImageSnapshotId')

	def set_ImageSnapshotId(self, ImageSnapshotId):  # String
		self.add_query_param('ImageSnapshotId', ImageSnapshotId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_CpuOptionsThreadsPerCore(self): # Integer
		return self.get_query_params().get('CpuOptionsThreadsPerCore')

	def set_CpuOptionsThreadsPerCore(self, CpuOptionsThreadsPerCore):  # Integer
		self.add_query_param('CpuOptionsThreadsPerCore', CpuOptionsThreadsPerCore)
	def get_Ipv6AddressCount(self): # Integer
		return self.get_query_params().get('Ipv6AddressCount')

	def set_Ipv6AddressCount(self, Ipv6AddressCount):  # Integer
		self.add_query_param('Ipv6AddressCount', Ipv6AddressCount)
	def get_Cpu(self): # Float
		return self.get_query_params().get('Cpu')

	def set_Cpu(self, Cpu):  # Float
		self.add_query_param('Cpu', Cpu)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ScalingConfigurationName(self): # String
		return self.get_query_params().get('ScalingConfigurationName')

	def set_ScalingConfigurationName(self, ScalingConfigurationName):  # String
		self.add_query_param('ScalingConfigurationName', ScalingConfigurationName)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_Volumes(self): # RepeatList
		return self.get_query_params().get('Volume')

	def set_Volumes(self, Volume):  # RepeatList
		for depth1 in range(len(Volume)):
			if Volume[depth1].get('DiskVolume.FsType') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.DiskVolume.FsType', Volume[depth1].get('DiskVolume.FsType'))
			if Volume[depth1].get('NFSVolume.Path') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.NFSVolume.Path', Volume[depth1].get('NFSVolume.Path'))
			if Volume[depth1].get('DiskVolume.DiskId') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.DiskVolume.DiskId', Volume[depth1].get('DiskVolume.DiskId'))
			if Volume[depth1].get('FlexVolume.FsType') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.FlexVolume.FsType', Volume[depth1].get('FlexVolume.FsType'))
			if Volume[depth1].get('Type') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.Type', Volume[depth1].get('Type'))
			if Volume[depth1].get('FlexVolume.Driver') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.FlexVolume.Driver', Volume[depth1].get('FlexVolume.Driver'))
			if Volume[depth1].get('FlexVolume.Options') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.FlexVolume.Options', Volume[depth1].get('FlexVolume.Options'))
			if Volume[depth1].get('NFSVolume.Server') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.NFSVolume.Server', Volume[depth1].get('NFSVolume.Server'))
			if Volume[depth1].get('EmptyDirVolume.Medium') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.EmptyDirVolume.Medium', Volume[depth1].get('EmptyDirVolume.Medium'))
			if Volume[depth1].get('HostPathVolume.Path') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.HostPathVolume.Path', Volume[depth1].get('HostPathVolume.Path'))
			if Volume[depth1].get('Name') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.Name', Volume[depth1].get('Name'))
			if Volume[depth1].get('ConfigFileVolumeConfigFileToPath') is not None:
				for depth2 in range(len(Volume[depth1].get('ConfigFileVolumeConfigFileToPath'))):
					if Volume[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Mode') is not None:
						self.add_query_param('Volume.' + str(depth1 + 1) + '.ConfigFileVolumeConfigFileToPath.'  + str(depth2 + 1) + '.Mode', Volume[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Mode'))
					if Volume[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Path') is not None:
						self.add_query_param('Volume.' + str(depth1 + 1) + '.ConfigFileVolumeConfigFileToPath.'  + str(depth2 + 1) + '.Path', Volume[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Path'))
					if Volume[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Content') is not None:
						self.add_query_param('Volume.' + str(depth1 + 1) + '.ConfigFileVolumeConfigFileToPath.'  + str(depth2 + 1) + '.Content', Volume[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Content'))
			if Volume[depth1].get('DiskVolume.DiskSize') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.DiskVolume.DiskSize', Volume[depth1].get('DiskVolume.DiskSize'))
			if Volume[depth1].get('ConfigFileVolumeDefaultMode') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.ConfigFileVolumeDefaultMode', Volume[depth1].get('ConfigFileVolumeDefaultMode'))
			if Volume[depth1].get('HostPathVolume.Type') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.HostPathVolume.Type', Volume[depth1].get('HostPathVolume.Type'))
			if Volume[depth1].get('NFSVolume.ReadOnly') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.NFSVolume.ReadOnly', Volume[depth1].get('NFSVolume.ReadOnly'))
	def get_InstanceFamilyLevel(self): # String
		return self.get_query_params().get('InstanceFamilyLevel')

	def set_InstanceFamilyLevel(self, InstanceFamilyLevel):  # String
		self.add_query_param('InstanceFamilyLevel', InstanceFamilyLevel)
	def get_DnsConfigOptions(self): # RepeatList
		return self.get_query_params().get('DnsConfigOption')

	def set_DnsConfigOptions(self, DnsConfigOption):  # RepeatList
		for depth1 in range(len(DnsConfigOption)):
			if DnsConfigOption[depth1].get('Name') is not None:
				self.add_query_param('DnsConfigOption.' + str(depth1 + 1) + '.Name', DnsConfigOption[depth1].get('Name'))
			if DnsConfigOption[depth1].get('Value') is not None:
				self.add_query_param('DnsConfigOption.' + str(depth1 + 1) + '.Value', DnsConfigOption[depth1].get('Value'))
	def get_EphemeralStorage(self): # Integer
		return self.get_query_params().get('EphemeralStorage')

	def set_EphemeralStorage(self, EphemeralStorage):  # Integer
		self.add_query_param('EphemeralStorage', EphemeralStorage)
	def get_EipBandwidth(self): # Integer
		return self.get_query_params().get('EipBandwidth')

	def set_EipBandwidth(self, EipBandwidth):  # Integer
		self.add_query_param('EipBandwidth', EipBandwidth)
	def get_CostOptimization(self): # Boolean
		return self.get_query_params().get('CostOptimization')

	def set_CostOptimization(self, CostOptimization):  # Boolean
		self.add_query_param('CostOptimization', CostOptimization)
	def get_Memory(self): # Float
		return self.get_query_params().get('Memory')

	def set_Memory(self, Memory):  # Float
		self.add_query_param('Memory', Memory)
	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_IngressBandwidth(self): # Long
		return self.get_query_params().get('IngressBandwidth')

	def set_IngressBandwidth(self, IngressBandwidth):  # Long
		self.add_query_param('IngressBandwidth', IngressBandwidth)
	def get_DnsPolicy(self): # String
		return self.get_query_params().get('DnsPolicy')

	def set_DnsPolicy(self, DnsPolicy):  # String
		self.add_query_param('DnsPolicy', DnsPolicy)
	def get_SecurityContextSysctls(self): # RepeatList
		return self.get_query_params().get('SecurityContextSysctl')

	def set_SecurityContextSysctls(self, SecurityContextSysctl):  # RepeatList
		for depth1 in range(len(SecurityContextSysctl)):
			if SecurityContextSysctl[depth1].get('Name') is not None:
				self.add_query_param('SecurityContextSysctl.' + str(depth1 + 1) + '.Name', SecurityContextSysctl[depth1].get('Name'))
			if SecurityContextSysctl[depth1].get('Value') is not None:
				self.add_query_param('SecurityContextSysctl.' + str(depth1 + 1) + '.Value', SecurityContextSysctl[depth1].get('Value'))
	def get_DnsConfigNameServers(self): # RepeatList
		return self.get_query_params().get('DnsConfigNameServer')

	def set_DnsConfigNameServers(self, DnsConfigNameServer):  # RepeatList
		for depth1 in range(len(DnsConfigNameServer)):
			self.add_query_param('DnsConfigNameServer.' + str(depth1 + 1), DnsConfigNameServer[depth1])
	def get_InitContainers(self): # RepeatList
		return self.get_query_params().get('InitContainer')

	def set_InitContainers(self, InitContainer):  # RepeatList
		for depth1 in range(len(InitContainer)):
			if InitContainer[depth1].get('Image') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Image', InitContainer[depth1].get('Image'))
			if InitContainer[depth1].get('InitContainerEnvironmentVar') is not None:
				for depth2 in range(len(InitContainer[depth1].get('InitContainerEnvironmentVar'))):
					if InitContainer[depth1].get('InitContainerEnvironmentVar')[depth2].get('FieldRefFieldPath') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerEnvironmentVar.'  + str(depth2 + 1) + '.FieldRefFieldPath', InitContainer[depth1].get('InitContainerEnvironmentVar')[depth2].get('FieldRefFieldPath'))
					if InitContainer[depth1].get('InitContainerEnvironmentVar')[depth2].get('Value') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerEnvironmentVar.'  + str(depth2 + 1) + '.Value', InitContainer[depth1].get('InitContainerEnvironmentVar')[depth2].get('Value'))
					if InitContainer[depth1].get('InitContainerEnvironmentVar')[depth2].get('Key') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerEnvironmentVar.'  + str(depth2 + 1) + '.Key', InitContainer[depth1].get('InitContainerEnvironmentVar')[depth2].get('Key'))
			if InitContainer[depth1].get('SecurityContext.Capability.Add') is not None:
				for depth2 in range(len(InitContainer[depth1].get('SecurityContext.Capability.Add'))):
					self.add_query_param('InitContainer.' + str(depth1 + 1) + '.SecurityContext.Capability.Add.' + str(depth2 + 1), InitContainer[depth1].get('SecurityContext.Capability.Add')[depth2])
			if InitContainer[depth1].get('Memory') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Memory', InitContainer[depth1].get('Memory'))
			if InitContainer[depth1].get('WorkingDir') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.WorkingDir', InitContainer[depth1].get('WorkingDir'))
			if InitContainer[depth1].get('Cpu') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Cpu', InitContainer[depth1].get('Cpu'))
			if InitContainer[depth1].get('Gpu') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Gpu', InitContainer[depth1].get('Gpu'))
			if InitContainer[depth1].get('ImagePullPolicy') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.ImagePullPolicy', InitContainer[depth1].get('ImagePullPolicy'))
			if InitContainer[depth1].get('Command') is not None:
				for depth2 in range(len(InitContainer[depth1].get('Command'))):
					self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Command.' + str(depth2 + 1), InitContainer[depth1].get('Command')[depth2])
			if InitContainer[depth1].get('SecurityContext.RunAsUser') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.SecurityContext.RunAsUser', InitContainer[depth1].get('SecurityContext.RunAsUser'))
			if InitContainer[depth1].get('InitContainerPort') is not None:
				for depth2 in range(len(InitContainer[depth1].get('InitContainerPort'))):
					if InitContainer[depth1].get('InitContainerPort')[depth2].get('Protocol') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerPort.'  + str(depth2 + 1) + '.Protocol', InitContainer[depth1].get('InitContainerPort')[depth2].get('Protocol'))
					if InitContainer[depth1].get('InitContainerPort')[depth2].get('Port') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerPort.'  + str(depth2 + 1) + '.Port', InitContainer[depth1].get('InitContainerPort')[depth2].get('Port'))
			if InitContainer[depth1].get('Arg') is not None:
				for depth2 in range(len(InitContainer[depth1].get('Arg'))):
					self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Arg.' + str(depth2 + 1), InitContainer[depth1].get('Arg')[depth2])
			if InitContainer[depth1].get('Name') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Name', InitContainer[depth1].get('Name'))
			if InitContainer[depth1].get('InitContainerVolumeMount') is not None:
				for depth2 in range(len(InitContainer[depth1].get('InitContainerVolumeMount'))):
					if InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('MountPath') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.'  + str(depth2 + 1) + '.MountPath', InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('MountPath'))
					if InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('ReadOnly') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.'  + str(depth2 + 1) + '.ReadOnly', InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('ReadOnly'))
					if InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('MountPropagation') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.'  + str(depth2 + 1) + '.MountPropagation', InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('MountPropagation'))
					if InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('Name') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.'  + str(depth2 + 1) + '.Name', InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('Name'))
					if InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('SubPath') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.'  + str(depth2 + 1) + '.SubPath', InitContainer[depth1].get('InitContainerVolumeMount')[depth2].get('SubPath'))
			if InitContainer[depth1].get('SecurityContext.ReadOnlyRootFilesystem') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.SecurityContext.ReadOnlyRootFilesystem', InitContainer[depth1].get('SecurityContext.ReadOnlyRootFilesystem'))
	def get_TerminationGracePeriodSeconds(self): # Long
		return self.get_query_params().get('TerminationGracePeriodSeconds')

	def set_TerminationGracePeriodSeconds(self, TerminationGracePeriodSeconds):  # Long
		self.add_query_param('TerminationGracePeriodSeconds', TerminationGracePeriodSeconds)
	def get_ImageRegistryCredentials(self): # RepeatList
		return self.get_query_params().get('ImageRegistryCredential')

	def set_ImageRegistryCredentials(self, ImageRegistryCredential):  # RepeatList
		for depth1 in range(len(ImageRegistryCredential)):
			if ImageRegistryCredential[depth1].get('Server') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(depth1 + 1) + '.Server', ImageRegistryCredential[depth1].get('Server'))
			if ImageRegistryCredential[depth1].get('Password') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(depth1 + 1) + '.Password', ImageRegistryCredential[depth1].get('Password'))
			if ImageRegistryCredential[depth1].get('UserName') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(depth1 + 1) + '.UserName', ImageRegistryCredential[depth1].get('UserName'))
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_RestartPolicy(self): # String
		return self.get_query_params().get('RestartPolicy')

	def set_RestartPolicy(self, RestartPolicy):  # String
		self.add_query_param('RestartPolicy', RestartPolicy)
	def get_CpuOptionsCore(self): # Integer
		return self.get_query_params().get('CpuOptionsCore')

	def set_CpuOptionsCore(self, CpuOptionsCore):  # Integer
		self.add_query_param('CpuOptionsCore', CpuOptionsCore)
	def get_RamRoleName(self): # String
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self, RamRoleName):  # String
		self.add_query_param('RamRoleName', RamRoleName)
	def get_AcrRegistryInfos(self): # RepeatList
		return self.get_query_params().get('AcrRegistryInfo')

	def set_AcrRegistryInfos(self, AcrRegistryInfo):  # RepeatList
		for depth1 in range(len(AcrRegistryInfo)):
			if AcrRegistryInfo[depth1].get('InstanceName') is not None:
				self.add_query_param('AcrRegistryInfo.' + str(depth1 + 1) + '.InstanceName', AcrRegistryInfo[depth1].get('InstanceName'))
			if AcrRegistryInfo[depth1].get('InstanceId') is not None:
				self.add_query_param('AcrRegistryInfo.' + str(depth1 + 1) + '.InstanceId', AcrRegistryInfo[depth1].get('InstanceId'))
			if AcrRegistryInfo[depth1].get('RegionId') is not None:
				self.add_query_param('AcrRegistryInfo.' + str(depth1 + 1) + '.RegionId', AcrRegistryInfo[depth1].get('RegionId'))
			if AcrRegistryInfo[depth1].get('Domain') is not None:
				for depth2 in range(len(AcrRegistryInfo[depth1].get('Domain'))):
					self.add_query_param('AcrRegistryInfo.' + str(depth1 + 1) + '.Domain.' + str(depth2 + 1), AcrRegistryInfo[depth1].get('Domain')[depth2])
	def get_AutoMatchImageCache(self): # Boolean
		return self.get_query_params().get('AutoMatchImageCache')

	def set_AutoMatchImageCache(self, AutoMatchImageCache):  # Boolean
		self.add_query_param('AutoMatchImageCache', AutoMatchImageCache)
	def get_LoadBalancerWeight(self): # Integer
		return self.get_query_params().get('LoadBalancerWeight')

	def set_LoadBalancerWeight(self, LoadBalancerWeight):  # Integer
		self.add_query_param('LoadBalancerWeight', LoadBalancerWeight)
	def get_ContainerGroupName(self): # String
		return self.get_query_params().get('ContainerGroupName')

	def set_ContainerGroupName(self, ContainerGroupName):  # String
		self.add_query_param('ContainerGroupName', ContainerGroupName)
	def get_AutoCreateEip(self): # Boolean
		return self.get_query_params().get('AutoCreateEip')

	def set_AutoCreateEip(self, AutoCreateEip):  # Boolean
		self.add_query_param('AutoCreateEip', AutoCreateEip)
