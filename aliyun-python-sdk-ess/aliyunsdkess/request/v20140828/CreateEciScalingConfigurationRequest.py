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


	def get_Containers(self):
		return self.get_query_params().get('Container')

	def set_Containers(self, Containers):
		for depth1 in range(len(Containers)):
			if Containers[depth1].get('Stdin') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Stdin', Containers[depth1].get('Stdin'))
			if Containers[depth1].get('Memory') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Memory', Containers[depth1].get('Memory'))
			if Containers[depth1].get('LivenessProbe.Exec.Command') is not None:
				for depth2 in range(len(Containers[depth1].get('LivenessProbe.Exec.Command'))):
					if Containers[depth1].get('LivenessProbe.Exec.Command')[depth2] is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.Exec.Command.' + str(depth2 + 1) , Containers[depth1].get('LivenessProbe.Exec.Command')[depth2])
			if Containers[depth1].get('WorkingDir') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.WorkingDir', Containers[depth1].get('WorkingDir'))
			if Containers[depth1].get('ReadinessProbe.HttpGet.Port') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.HttpGet.Port', Containers[depth1].get('ReadinessProbe.HttpGet.Port'))
			if Containers[depth1].get('ReadinessProbe.FailureThreshold') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.FailureThreshold', Containers[depth1].get('ReadinessProbe.FailureThreshold'))
			if Containers[depth1].get('LivenessProbe.HttpGet.Port') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.HttpGet.Port', Containers[depth1].get('LivenessProbe.HttpGet.Port'))
			if Containers[depth1].get('Arg') is not None:
				for depth2 in range(len(Containers[depth1].get('Arg'))):
					if Containers[depth1].get('Arg')[depth2] is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.Arg.' + str(depth2 + 1) , Containers[depth1].get('Arg')[depth2])
			if Containers[depth1].get('ReadinessProbe.SuccessThreshold') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.SuccessThreshold', Containers[depth1].get('ReadinessProbe.SuccessThreshold'))
			if Containers[depth1].get('VolumeMount') is not None:
				for depth2 in range(len(Containers[depth1].get('VolumeMount'))):
					if Containers[depth1].get('VolumeMount')[depth2].get('MountPath') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.' + str(depth2 + 1) + '.MountPath', Containers[depth1].get('VolumeMount')[depth2].get('MountPath'))
					if Containers[depth1].get('VolumeMount')[depth2].get('ReadOnly') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.' + str(depth2 + 1) + '.ReadOnly', Containers[depth1].get('VolumeMount')[depth2].get('ReadOnly'))
					if Containers[depth1].get('VolumeMount')[depth2].get('MountPropagation') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.' + str(depth2 + 1) + '.MountPropagation', Containers[depth1].get('VolumeMount')[depth2].get('MountPropagation'))
					if Containers[depth1].get('VolumeMount')[depth2].get('Name') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.' + str(depth2 + 1) + '.Name', Containers[depth1].get('VolumeMount')[depth2].get('Name'))
					if Containers[depth1].get('VolumeMount')[depth2].get('SubPath') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.VolumeMount.' + str(depth2 + 1) + '.SubPath', Containers[depth1].get('VolumeMount')[depth2].get('SubPath'))
			if Containers[depth1].get('Image') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Image', Containers[depth1].get('Image'))
			if Containers[depth1].get('SecurityContext.Capability.Add') is not None:
				for depth2 in range(len(Containers[depth1].get('SecurityContext.Capability.Add'))):
					if Containers[depth1].get('SecurityContext.Capability.Add')[depth2] is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.SecurityContext.Capability.Add.' + str(depth2 + 1) , Containers[depth1].get('SecurityContext.Capability.Add')[depth2])
			if Containers[depth1].get('ReadinessProbe.InitialDelaySeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.InitialDelaySeconds', Containers[depth1].get('ReadinessProbe.InitialDelaySeconds'))
			if Containers[depth1].get('Cpu') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Cpu', Containers[depth1].get('Cpu'))
			if Containers[depth1].get('ReadinessProbe.Exec.Command') is not None:
				for depth2 in range(len(Containers[depth1].get('ReadinessProbe.Exec.Command'))):
					if Containers[depth1].get('ReadinessProbe.Exec.Command')[depth2] is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.Exec.Command.' + str(depth2 + 1) , Containers[depth1].get('ReadinessProbe.Exec.Command')[depth2])
			if Containers[depth1].get('ReadinessProbe.HttpGet.Scheme') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.HttpGet.Scheme', Containers[depth1].get('ReadinessProbe.HttpGet.Scheme'))
			if Containers[depth1].get('ReadinessProbe.HttpGet.Path') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.HttpGet.Path', Containers[depth1].get('ReadinessProbe.HttpGet.Path'))
			if Containers[depth1].get('Gpu') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Gpu', Containers[depth1].get('Gpu'))
			if Containers[depth1].get('StdinOnce') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.StdinOnce', Containers[depth1].get('StdinOnce'))
			if Containers[depth1].get('ImagePullPolicy') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ImagePullPolicy', Containers[depth1].get('ImagePullPolicy'))
			if Containers[depth1].get('Command') is not None:
				for depth2 in range(len(Containers[depth1].get('Command'))):
					if Containers[depth1].get('Command')[depth2] is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.Command.' + str(depth2 + 1) , Containers[depth1].get('Command')[depth2])
			if Containers[depth1].get('LivenessProbe.SuccessThreshold') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.SuccessThreshold', Containers[depth1].get('LivenessProbe.SuccessThreshold'))
			if Containers[depth1].get('SecurityContext.RunAsUser') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.SecurityContext.RunAsUser', Containers[depth1].get('SecurityContext.RunAsUser'))
			if Containers[depth1].get('LivenessProbe.HttpGet.Path') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.HttpGet.Path', Containers[depth1].get('LivenessProbe.HttpGet.Path'))
			if Containers[depth1].get('LivenessProbe.PeriodSeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.PeriodSeconds', Containers[depth1].get('LivenessProbe.PeriodSeconds'))
			if Containers[depth1].get('LivenessProbe.InitialDelaySeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.InitialDelaySeconds', Containers[depth1].get('LivenessProbe.InitialDelaySeconds'))
			if Containers[depth1].get('LivenessProbe.TimeoutSeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.TimeoutSeconds', Containers[depth1].get('LivenessProbe.TimeoutSeconds'))
			if Containers[depth1].get('LivenessProbe.TcpSocket.Port') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.TcpSocket.Port', Containers[depth1].get('LivenessProbe.TcpSocket.Port'))
			if Containers[depth1].get('Port') is not None:
				for depth2 in range(len(Containers[depth1].get('Port'))):
					if Containers[depth1].get('Port')[depth2].get('Protocol') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.Port.' + str(depth2 + 1) + '.Protocol', Containers[depth1].get('Port')[depth2].get('Protocol'))
					if Containers[depth1].get('Port')[depth2].get('Port') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.Port.' + str(depth2 + 1) + '.Port', Containers[depth1].get('Port')[depth2].get('Port'))
			if Containers[depth1].get('ReadinessProbe.PeriodSeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.PeriodSeconds', Containers[depth1].get('ReadinessProbe.PeriodSeconds'))
			if Containers[depth1].get('EnvironmentVar') is not None:
				for depth2 in range(len(Containers[depth1].get('EnvironmentVar'))):
					if Containers[depth1].get('EnvironmentVar')[depth2].get('FieldRefFieldPath') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.EnvironmentVar.' + str(depth2 + 1) + '.FieldRefFieldPath', Containers[depth1].get('EnvironmentVar')[depth2].get('FieldRefFieldPath'))
					if Containers[depth1].get('EnvironmentVar')[depth2].get('Value') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.EnvironmentVar.' + str(depth2 + 1) + '.Value', Containers[depth1].get('EnvironmentVar')[depth2].get('Value'))
					if Containers[depth1].get('EnvironmentVar')[depth2].get('Key') is not None:
						self.add_query_param('Container.' + str(depth1 + 1) + '.EnvironmentVar.' + str(depth2 + 1) + '.Key', Containers[depth1].get('EnvironmentVar')[depth2].get('Key'))
			if Containers[depth1].get('Tty') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Tty', Containers[depth1].get('Tty'))
			if Containers[depth1].get('Name') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.Name', Containers[depth1].get('Name'))
			if Containers[depth1].get('SecurityContext.ReadOnlyRootFilesystem') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.SecurityContext.ReadOnlyRootFilesystem', Containers[depth1].get('SecurityContext.ReadOnlyRootFilesystem'))
			if Containers[depth1].get('LivenessProbe.FailureThreshold') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.FailureThreshold', Containers[depth1].get('LivenessProbe.FailureThreshold'))
			if Containers[depth1].get('ReadinessProbe.TimeoutSeconds') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.TimeoutSeconds', Containers[depth1].get('ReadinessProbe.TimeoutSeconds'))
			if Containers[depth1].get('ReadinessProbe.TcpSocket.Port') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.ReadinessProbe.TcpSocket.Port', Containers[depth1].get('ReadinessProbe.TcpSocket.Port'))
			if Containers[depth1].get('LivenessProbe.HttpGet.Scheme') is not None:
				self.add_query_param('Container.' + str(depth1 + 1) + '.LivenessProbe.HttpGet.Scheme', Containers[depth1].get('LivenessProbe.HttpGet.Scheme'))

	def get_NtpServers(self):
		return self.get_query_params().get('NtpServer')

	def set_NtpServers(self, NtpServers):
		for depth1 in range(len(NtpServers)):
			if NtpServers[depth1] is not None:
				self.add_query_param('NtpServer.' + str(depth1 + 1) , NtpServers[depth1])

	def get_SpotPriceLimit(self):
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self,SpotPriceLimit):
		self.add_query_param('SpotPriceLimit',SpotPriceLimit)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_ActiveDeadlineSeconds(self):
		return self.get_query_params().get('ActiveDeadlineSeconds')

	def set_ActiveDeadlineSeconds(self,ActiveDeadlineSeconds):
		self.add_query_param('ActiveDeadlineSeconds',ActiveDeadlineSeconds)

	def get_EgressBandwidth(self):
		return self.get_query_params().get('EgressBandwidth')

	def set_EgressBandwidth(self,EgressBandwidth):
		self.add_query_param('EgressBandwidth',EgressBandwidth)

	def get_DnsConfigSearchs(self):
		return self.get_query_params().get('DnsConfigSearch')

	def set_DnsConfigSearchs(self, DnsConfigSearchs):
		for depth1 in range(len(DnsConfigSearchs)):
			if DnsConfigSearchs[depth1] is not None:
				self.add_query_param('DnsConfigSearch.' + str(depth1 + 1) , DnsConfigSearchs[depth1])

	def get_HostAliases(self):
		return self.get_query_params().get('HostAliase')

	def set_HostAliases(self, HostAliases):
		for depth1 in range(len(HostAliases)):
			if HostAliases[depth1].get('Hostname') is not None:
				for depth2 in range(len(HostAliases[depth1].get('Hostname'))):
					if HostAliases[depth1].get('Hostname')[depth2] is not None:
						self.add_query_param('HostAliase.' + str(depth1 + 1) + '.Hostname.' + str(depth2 + 1) , HostAliases[depth1].get('Hostname')[depth2])
			if HostAliases[depth1].get('Ip') is not None:
				self.add_query_param('HostAliase.' + str(depth1 + 1) + '.Ip', HostAliases[depth1].get('Ip'))

	def get_ImageSnapshotId(self):
		return self.get_query_params().get('ImageSnapshotId')

	def set_ImageSnapshotId(self,ImageSnapshotId):
		self.add_query_param('ImageSnapshotId',ImageSnapshotId)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_CpuOptionsThreadsPerCore(self):
		return self.get_query_params().get('CpuOptionsThreadsPerCore')

	def set_CpuOptionsThreadsPerCore(self,CpuOptionsThreadsPerCore):
		self.add_query_param('CpuOptionsThreadsPerCore',CpuOptionsThreadsPerCore)

	def get_Ipv6AddressCount(self):
		return self.get_query_params().get('Ipv6AddressCount')

	def set_Ipv6AddressCount(self,Ipv6AddressCount):
		self.add_query_param('Ipv6AddressCount',Ipv6AddressCount)

	def get_Cpu(self):
		return self.get_query_params().get('Cpu')

	def set_Cpu(self,Cpu):
		self.add_query_param('Cpu',Cpu)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ScalingConfigurationName(self):
		return self.get_query_params().get('ScalingConfigurationName')

	def set_ScalingConfigurationName(self,ScalingConfigurationName):
		self.add_query_param('ScalingConfigurationName',ScalingConfigurationName)

	def get_SpotStrategy(self):
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self,SpotStrategy):
		self.add_query_param('SpotStrategy',SpotStrategy)

	def get_Volumes(self):
		return self.get_query_params().get('Volume')

	def set_Volumes(self, Volumes):
		for depth1 in range(len(Volumes)):
			if Volumes[depth1].get('DiskVolume.FsType') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.DiskVolume.FsType', Volumes[depth1].get('DiskVolume.FsType'))
			if Volumes[depth1].get('NFSVolume.Path') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.NFSVolume.Path', Volumes[depth1].get('NFSVolume.Path'))
			if Volumes[depth1].get('DiskVolume.DiskId') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.DiskVolume.DiskId', Volumes[depth1].get('DiskVolume.DiskId'))
			if Volumes[depth1].get('FlexVolume.FsType') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.FlexVolume.FsType', Volumes[depth1].get('FlexVolume.FsType'))
			if Volumes[depth1].get('Type') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.Type', Volumes[depth1].get('Type'))
			if Volumes[depth1].get('FlexVolume.Driver') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.FlexVolume.Driver', Volumes[depth1].get('FlexVolume.Driver'))
			if Volumes[depth1].get('FlexVolume.Options') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.FlexVolume.Options', Volumes[depth1].get('FlexVolume.Options'))
			if Volumes[depth1].get('NFSVolume.Server') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.NFSVolume.Server', Volumes[depth1].get('NFSVolume.Server'))
			if Volumes[depth1].get('EmptyDirVolume.Medium') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.EmptyDirVolume.Medium', Volumes[depth1].get('EmptyDirVolume.Medium'))
			if Volumes[depth1].get('HostPathVolume.Path') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.HostPathVolume.Path', Volumes[depth1].get('HostPathVolume.Path'))
			if Volumes[depth1].get('Name') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.Name', Volumes[depth1].get('Name'))
			if Volumes[depth1].get('ConfigFileVolumeConfigFileToPath') is not None:
				for depth2 in range(len(Volumes[depth1].get('ConfigFileVolumeConfigFileToPath'))):
					if Volumes[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Mode') is not None:
						self.add_query_param('Volume.' + str(depth1 + 1) + '.ConfigFileVolumeConfigFileToPath.' + str(depth2 + 1) + '.Mode', Volumes[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Mode'))
					if Volumes[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Path') is not None:
						self.add_query_param('Volume.' + str(depth1 + 1) + '.ConfigFileVolumeConfigFileToPath.' + str(depth2 + 1) + '.Path', Volumes[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Path'))
					if Volumes[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Content') is not None:
						self.add_query_param('Volume.' + str(depth1 + 1) + '.ConfigFileVolumeConfigFileToPath.' + str(depth2 + 1) + '.Content', Volumes[depth1].get('ConfigFileVolumeConfigFileToPath')[depth2].get('Content'))
			if Volumes[depth1].get('DiskVolume.DiskSize') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.DiskVolume.DiskSize', Volumes[depth1].get('DiskVolume.DiskSize'))
			if Volumes[depth1].get('ConfigFileVolumeDefaultMode') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.ConfigFileVolumeDefaultMode', Volumes[depth1].get('ConfigFileVolumeDefaultMode'))
			if Volumes[depth1].get('HostPathVolume.Type') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.HostPathVolume.Type', Volumes[depth1].get('HostPathVolume.Type'))
			if Volumes[depth1].get('NFSVolume.ReadOnly') is not None:
				self.add_query_param('Volume.' + str(depth1 + 1) + '.NFSVolume.ReadOnly', Volumes[depth1].get('NFSVolume.ReadOnly'))

	def get_DnsConfigOptions(self):
		return self.get_query_params().get('DnsConfigOption')

	def set_DnsConfigOptions(self, DnsConfigOptions):
		for depth1 in range(len(DnsConfigOptions)):
			if DnsConfigOptions[depth1].get('Name') is not None:
				self.add_query_param('DnsConfigOption.' + str(depth1 + 1) + '.Name', DnsConfigOptions[depth1].get('Name'))
			if DnsConfigOptions[depth1].get('Value') is not None:
				self.add_query_param('DnsConfigOption.' + str(depth1 + 1) + '.Value', DnsConfigOptions[depth1].get('Value'))

	def get_EphemeralStorage(self):
		return self.get_query_params().get('EphemeralStorage')

	def set_EphemeralStorage(self,EphemeralStorage):
		self.add_query_param('EphemeralStorage',EphemeralStorage)

	def get_EipBandwidth(self):
		return self.get_query_params().get('EipBandwidth')

	def set_EipBandwidth(self,EipBandwidth):
		self.add_query_param('EipBandwidth',EipBandwidth)

	def get_Memory(self):
		return self.get_query_params().get('Memory')

	def set_Memory(self,Memory):
		self.add_query_param('Memory',Memory)

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_IngressBandwidth(self):
		return self.get_query_params().get('IngressBandwidth')

	def set_IngressBandwidth(self,IngressBandwidth):
		self.add_query_param('IngressBandwidth',IngressBandwidth)

	def get_DnsPolicy(self):
		return self.get_query_params().get('DnsPolicy')

	def set_DnsPolicy(self,DnsPolicy):
		self.add_query_param('DnsPolicy',DnsPolicy)

	def get_SecurityContextSysctls(self):
		return self.get_query_params().get('SecurityContextSysctl')

	def set_SecurityContextSysctls(self, SecurityContextSysctls):
		for depth1 in range(len(SecurityContextSysctls)):
			if SecurityContextSysctls[depth1].get('Name') is not None:
				self.add_query_param('SecurityContextSysctl.' + str(depth1 + 1) + '.Name', SecurityContextSysctls[depth1].get('Name'))
			if SecurityContextSysctls[depth1].get('Value') is not None:
				self.add_query_param('SecurityContextSysctl.' + str(depth1 + 1) + '.Value', SecurityContextSysctls[depth1].get('Value'))

	def get_DnsConfigNameServers(self):
		return self.get_query_params().get('DnsConfigNameServer')

	def set_DnsConfigNameServers(self, DnsConfigNameServers):
		for depth1 in range(len(DnsConfigNameServers)):
			if DnsConfigNameServers[depth1] is not None:
				self.add_query_param('DnsConfigNameServer.' + str(depth1 + 1) , DnsConfigNameServers[depth1])

	def get_InitContainers(self):
		return self.get_query_params().get('InitContainer')

	def set_InitContainers(self, InitContainers):
		for depth1 in range(len(InitContainers)):
			if InitContainers[depth1].get('Image') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Image', InitContainers[depth1].get('Image'))
			if InitContainers[depth1].get('InitContainerEnvironmentVar') is not None:
				for depth2 in range(len(InitContainers[depth1].get('InitContainerEnvironmentVar'))):
					if InitContainers[depth1].get('InitContainerEnvironmentVar')[depth2].get('FieldRefFieldPath') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerEnvironmentVar.' + str(depth2 + 1) + '.FieldRefFieldPath', InitContainers[depth1].get('InitContainerEnvironmentVar')[depth2].get('FieldRefFieldPath'))
					if InitContainers[depth1].get('InitContainerEnvironmentVar')[depth2].get('Value') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerEnvironmentVar.' + str(depth2 + 1) + '.Value', InitContainers[depth1].get('InitContainerEnvironmentVar')[depth2].get('Value'))
					if InitContainers[depth1].get('InitContainerEnvironmentVar')[depth2].get('Key') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerEnvironmentVar.' + str(depth2 + 1) + '.Key', InitContainers[depth1].get('InitContainerEnvironmentVar')[depth2].get('Key'))
			if InitContainers[depth1].get('SecurityContext.Capability.Add') is not None:
				for depth2 in range(len(InitContainers[depth1].get('SecurityContext.Capability.Add'))):
					if InitContainers[depth1].get('SecurityContext.Capability.Add')[depth2] is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.SecurityContext.Capability.Add.' + str(depth2 + 1) , InitContainers[depth1].get('SecurityContext.Capability.Add')[depth2])
			if InitContainers[depth1].get('Memory') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Memory', InitContainers[depth1].get('Memory'))
			if InitContainers[depth1].get('WorkingDir') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.WorkingDir', InitContainers[depth1].get('WorkingDir'))
			if InitContainers[depth1].get('Cpu') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Cpu', InitContainers[depth1].get('Cpu'))
			if InitContainers[depth1].get('Gpu') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Gpu', InitContainers[depth1].get('Gpu'))
			if InitContainers[depth1].get('ImagePullPolicy') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.ImagePullPolicy', InitContainers[depth1].get('ImagePullPolicy'))
			if InitContainers[depth1].get('Command') is not None:
				for depth2 in range(len(InitContainers[depth1].get('Command'))):
					if InitContainers[depth1].get('Command')[depth2] is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Command.' + str(depth2 + 1) , InitContainers[depth1].get('Command')[depth2])
			if InitContainers[depth1].get('SecurityContext.RunAsUser') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.SecurityContext.RunAsUser', InitContainers[depth1].get('SecurityContext.RunAsUser'))
			if InitContainers[depth1].get('InitContainerPort') is not None:
				for depth2 in range(len(InitContainers[depth1].get('InitContainerPort'))):
					if InitContainers[depth1].get('InitContainerPort')[depth2].get('Protocol') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerPort.' + str(depth2 + 1) + '.Protocol', InitContainers[depth1].get('InitContainerPort')[depth2].get('Protocol'))
					if InitContainers[depth1].get('InitContainerPort')[depth2].get('Port') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerPort.' + str(depth2 + 1) + '.Port', InitContainers[depth1].get('InitContainerPort')[depth2].get('Port'))
			if InitContainers[depth1].get('Arg') is not None:
				for depth2 in range(len(InitContainers[depth1].get('Arg'))):
					if InitContainers[depth1].get('Arg')[depth2] is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Arg.' + str(depth2 + 1) , InitContainers[depth1].get('Arg')[depth2])
			if InitContainers[depth1].get('Name') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.Name', InitContainers[depth1].get('Name'))
			if InitContainers[depth1].get('InitContainerVolumeMount') is not None:
				for depth2 in range(len(InitContainers[depth1].get('InitContainerVolumeMount'))):
					if InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('MountPath') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.' + str(depth2 + 1) + '.MountPath', InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('MountPath'))
					if InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('ReadOnly') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.' + str(depth2 + 1) + '.ReadOnly', InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('ReadOnly'))
					if InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('MountPropagation') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.' + str(depth2 + 1) + '.MountPropagation', InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('MountPropagation'))
					if InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('Name') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.' + str(depth2 + 1) + '.Name', InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('Name'))
					if InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('SubPath') is not None:
						self.add_query_param('InitContainer.' + str(depth1 + 1) + '.InitContainerVolumeMount.' + str(depth2 + 1) + '.SubPath', InitContainers[depth1].get('InitContainerVolumeMount')[depth2].get('SubPath'))
			if InitContainers[depth1].get('SecurityContext.ReadOnlyRootFilesystem') is not None:
				self.add_query_param('InitContainer.' + str(depth1 + 1) + '.SecurityContext.ReadOnlyRootFilesystem', InitContainers[depth1].get('SecurityContext.ReadOnlyRootFilesystem'))

	def get_TerminationGracePeriodSeconds(self):
		return self.get_query_params().get('TerminationGracePeriodSeconds')

	def set_TerminationGracePeriodSeconds(self,TerminationGracePeriodSeconds):
		self.add_query_param('TerminationGracePeriodSeconds',TerminationGracePeriodSeconds)

	def get_ImageRegistryCredentials(self):
		return self.get_query_params().get('ImageRegistryCredential')

	def set_ImageRegistryCredentials(self, ImageRegistryCredentials):
		for depth1 in range(len(ImageRegistryCredentials)):
			if ImageRegistryCredentials[depth1].get('Server') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(depth1 + 1) + '.Server', ImageRegistryCredentials[depth1].get('Server'))
			if ImageRegistryCredentials[depth1].get('Password') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(depth1 + 1) + '.Password', ImageRegistryCredentials[depth1].get('Password'))
			if ImageRegistryCredentials[depth1].get('UserName') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(depth1 + 1) + '.UserName', ImageRegistryCredentials[depth1].get('UserName'))

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_RestartPolicy(self):
		return self.get_query_params().get('RestartPolicy')

	def set_RestartPolicy(self,RestartPolicy):
		self.add_query_param('RestartPolicy',RestartPolicy)

	def get_CpuOptionsCore(self):
		return self.get_query_params().get('CpuOptionsCore')

	def set_CpuOptionsCore(self,CpuOptionsCore):
		self.add_query_param('CpuOptionsCore',CpuOptionsCore)

	def get_RamRoleName(self):
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self,RamRoleName):
		self.add_query_param('RamRoleName',RamRoleName)

	def get_AcrRegistryInfos(self):
		return self.get_query_params().get('AcrRegistryInfo')

	def set_AcrRegistryInfos(self, AcrRegistryInfos):
		for depth1 in range(len(AcrRegistryInfos)):
			if AcrRegistryInfos[depth1].get('InstanceName') is not None:
				self.add_query_param('AcrRegistryInfo.' + str(depth1 + 1) + '.InstanceName', AcrRegistryInfos[depth1].get('InstanceName'))
			if AcrRegistryInfos[depth1].get('InstanceId') is not None:
				self.add_query_param('AcrRegistryInfo.' + str(depth1 + 1) + '.InstanceId', AcrRegistryInfos[depth1].get('InstanceId'))
			if AcrRegistryInfos[depth1].get('RegionId') is not None:
				self.add_query_param('AcrRegistryInfo.' + str(depth1 + 1) + '.RegionId', AcrRegistryInfos[depth1].get('RegionId'))
			if AcrRegistryInfos[depth1].get('Domain') is not None:
				for depth2 in range(len(AcrRegistryInfos[depth1].get('Domain'))):
					if AcrRegistryInfos[depth1].get('Domain')[depth2] is not None:
						self.add_query_param('AcrRegistryInfo.' + str(depth1 + 1) + '.Domain.' + str(depth2 + 1) , AcrRegistryInfos[depth1].get('Domain')[depth2])

	def get_AutoMatchImageCache(self):
		return self.get_query_params().get('AutoMatchImageCache')

	def set_AutoMatchImageCache(self,AutoMatchImageCache):
		self.add_query_param('AutoMatchImageCache',AutoMatchImageCache)

	def get_LoadBalancerWeight(self):
		return self.get_query_params().get('LoadBalancerWeight')

	def set_LoadBalancerWeight(self,LoadBalancerWeight):
		self.add_query_param('LoadBalancerWeight',LoadBalancerWeight)

	def get_ContainerGroupName(self):
		return self.get_query_params().get('ContainerGroupName')

	def set_ContainerGroupName(self,ContainerGroupName):
		self.add_query_param('ContainerGroupName',ContainerGroupName)

	def get_AutoCreateEip(self):
		return self.get_query_params().get('AutoCreateEip')

	def set_AutoCreateEip(self,AutoCreateEip):
		self.add_query_param('AutoCreateEip',AutoCreateEip)