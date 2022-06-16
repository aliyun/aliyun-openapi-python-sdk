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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class DeployK8sApplicationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'DeployK8sApplication','Edas')
		self.set_uri_pattern('/pop/v5/k8s/acs/k8s_apps')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NasId(self): # string
		return self.get_query_params().get('NasId')

	def set_NasId(self, NasId):  # string
		self.add_query_param('NasId', NasId)
	def get_PackageVersionId(self): # string
		return self.get_query_params().get('PackageVersionId')

	def set_PackageVersionId(self, PackageVersionId):  # string
		self.add_query_param('PackageVersionId', PackageVersionId)
	def get_BatchWaitTime(self): # integer
		return self.get_query_params().get('BatchWaitTime')

	def set_BatchWaitTime(self, BatchWaitTime):  # integer
		self.add_query_param('BatchWaitTime', BatchWaitTime)
	def get_Envs(self): # string
		return self.get_query_params().get('Envs')

	def set_Envs(self, Envs):  # string
		self.add_query_param('Envs', Envs)
	def get_Annotations(self): # string
		return self.get_query_params().get('Annotations')

	def set_Annotations(self, Annotations):  # string
		self.add_query_param('Annotations', Annotations)
	def get_CpuLimit(self): # integer
		return self.get_query_params().get('CpuLimit')

	def set_CpuLimit(self, CpuLimit):  # integer
		self.add_query_param('CpuLimit', CpuLimit)
	def get_StorageType(self): # string
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # string
		self.add_query_param('StorageType', StorageType)
	def get_ConfigMountDescs(self): # string
		return self.get_query_params().get('ConfigMountDescs')

	def set_ConfigMountDescs(self, ConfigMountDescs):  # string
		self.add_query_param('ConfigMountDescs', ConfigMountDescs)
	def get_MemoryLimit(self): # integer
		return self.get_query_params().get('MemoryLimit')

	def set_MemoryLimit(self, MemoryLimit):  # integer
		self.add_query_param('MemoryLimit', MemoryLimit)
	def get_ImageTag(self): # string
		return self.get_query_params().get('ImageTag')

	def set_ImageTag(self, ImageTag):  # string
		self.add_query_param('ImageTag', ImageTag)
	def get_DeployAcrossZones(self): # string
		return self.get_query_params().get('DeployAcrossZones')

	def set_DeployAcrossZones(self, DeployAcrossZones):  # string
		self.add_query_param('DeployAcrossZones', DeployAcrossZones)
	def get_DeployAcrossNodes(self): # string
		return self.get_query_params().get('DeployAcrossNodes')

	def set_DeployAcrossNodes(self, DeployAcrossNodes):  # string
		self.add_query_param('DeployAcrossNodes', DeployAcrossNodes)
	def get_MemoryRequest(self): # integer
		return self.get_query_params().get('MemoryRequest')

	def set_MemoryRequest(self, MemoryRequest):  # integer
		self.add_query_param('MemoryRequest', MemoryRequest)
	def get_Image(self): # string
		return self.get_query_params().get('Image')

	def set_Image(self, Image):  # string
		self.add_query_param('Image', Image)
	def get_PreStop(self): # string
		return self.get_query_params().get('PreStop')

	def set_PreStop(self, PreStop):  # string
		self.add_query_param('PreStop', PreStop)
	def get_BuildPackId(self): # string
		return self.get_query_params().get('BuildPackId')

	def set_BuildPackId(self, BuildPackId):  # string
		self.add_query_param('BuildPackId', BuildPackId)
	def get_EnableEmptyPushReject(self): # boolean
		return self.get_query_params().get('EnableEmptyPushReject')

	def set_EnableEmptyPushReject(self, EnableEmptyPushReject):  # boolean
		self.add_query_param('EnableEmptyPushReject', EnableEmptyPushReject)
	def get_LocalVolume(self): # string
		return self.get_query_params().get('LocalVolume')

	def set_LocalVolume(self, LocalVolume):  # string
		self.add_query_param('LocalVolume', LocalVolume)
	def get_UpdateStrategy(self): # string
		return self.get_query_params().get('UpdateStrategy')

	def set_UpdateStrategy(self, UpdateStrategy):  # string
		self.add_query_param('UpdateStrategy', UpdateStrategy)
	def get_Labels(self): # string
		return self.get_query_params().get('Labels')

	def set_Labels(self, Labels):  # string
		self.add_query_param('Labels', Labels)
	def get_UseBodyEncoding(self): # boolean
		return self.get_query_params().get('UseBodyEncoding')

	def set_UseBodyEncoding(self, UseBodyEncoding):  # boolean
		self.add_query_param('UseBodyEncoding', UseBodyEncoding)
	def get_ChangeOrderDesc(self): # string
		return self.get_query_params().get('ChangeOrderDesc')

	def set_ChangeOrderDesc(self, ChangeOrderDesc):  # string
		self.add_query_param('ChangeOrderDesc', ChangeOrderDesc)
	def get_LosslessRuleFuncType(self): # integer
		return self.get_query_params().get('LosslessRuleFuncType')

	def set_LosslessRuleFuncType(self, LosslessRuleFuncType):  # integer
		self.add_query_param('LosslessRuleFuncType', LosslessRuleFuncType)
	def get_EmptyDirs(self): # string
		return self.get_query_params().get('EmptyDirs')

	def set_EmptyDirs(self, EmptyDirs):  # string
		self.add_query_param('EmptyDirs', EmptyDirs)
	def get_McpuLimit(self): # integer
		return self.get_query_params().get('McpuLimit')

	def set_McpuLimit(self, McpuLimit):  # integer
		self.add_query_param('McpuLimit', McpuLimit)
	def get_LosslessRuleRelated(self): # boolean
		return self.get_query_params().get('LosslessRuleRelated')

	def set_LosslessRuleRelated(self, LosslessRuleRelated):  # boolean
		self.add_query_param('LosslessRuleRelated', LosslessRuleRelated)
	def get_RuntimeClassName(self): # string
		return self.get_query_params().get('RuntimeClassName')

	def set_RuntimeClassName(self, RuntimeClassName):  # string
		self.add_query_param('RuntimeClassName', RuntimeClassName)
	def get_TrafficControlStrategy(self): # string
		return self.get_query_params().get('TrafficControlStrategy')

	def set_TrafficControlStrategy(self, TrafficControlStrategy):  # string
		self.add_query_param('TrafficControlStrategy', TrafficControlStrategy)
	def get_PostStart(self): # string
		return self.get_query_params().get('PostStart')

	def set_PostStart(self, PostStart):  # string
		self.add_query_param('PostStart', PostStart)
	def get_CustomAffinity(self): # string
		return self.get_query_params().get('CustomAffinity')

	def set_CustomAffinity(self, CustomAffinity):  # string
		self.add_query_param('CustomAffinity', CustomAffinity)
	def get_EnableLosslessRule(self): # boolean
		return self.get_query_params().get('EnableLosslessRule')

	def set_EnableLosslessRule(self, EnableLosslessRule):  # boolean
		self.add_query_param('EnableLosslessRule', EnableLosslessRule)
	def get_LosslessRuleWarmupTime(self): # integer
		return self.get_query_params().get('LosslessRuleWarmupTime')

	def set_LosslessRuleWarmupTime(self, LosslessRuleWarmupTime):  # integer
		self.add_query_param('LosslessRuleWarmupTime', LosslessRuleWarmupTime)
	def get_WebContainer(self): # string
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self, WebContainer):  # string
		self.add_query_param('WebContainer', WebContainer)
	def get_EnableAhas(self): # boolean
		return self.get_query_params().get('EnableAhas')

	def set_EnableAhas(self, EnableAhas):  # boolean
		self.add_query_param('EnableAhas', EnableAhas)
	def get_SlsConfigs(self): # string
		return self.get_query_params().get('SlsConfigs')

	def set_SlsConfigs(self, SlsConfigs):  # string
		self.add_query_param('SlsConfigs', SlsConfigs)
	def get_Readiness(self): # string
		return self.get_query_params().get('Readiness')

	def set_Readiness(self, Readiness):  # string
		self.add_query_param('Readiness', Readiness)
	def get_Liveness(self): # string
		return self.get_query_params().get('Liveness')

	def set_Liveness(self, Liveness):  # string
		self.add_query_param('Liveness', Liveness)
	def get_PackageVersion(self): # string
		return self.get_query_params().get('PackageVersion')

	def set_PackageVersion(self, PackageVersion):  # string
		self.add_query_param('PackageVersion', PackageVersion)
	def get_EnvFroms(self): # string
		return self.get_query_params().get('EnvFroms')

	def set_EnvFroms(self, EnvFroms):  # string
		self.add_query_param('EnvFroms', EnvFroms)
	def get_EdasContainerVersion(self): # string
		return self.get_query_params().get('EdasContainerVersion')

	def set_EdasContainerVersion(self, EdasContainerVersion):  # string
		self.add_query_param('EdasContainerVersion', EdasContainerVersion)
	def get_PackageUrl(self): # string
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self, PackageUrl):  # string
		self.add_query_param('PackageUrl', PackageUrl)
	def get_LosslessRuleDelayTime(self): # integer
		return self.get_query_params().get('LosslessRuleDelayTime')

	def set_LosslessRuleDelayTime(self, LosslessRuleDelayTime):  # integer
		self.add_query_param('LosslessRuleDelayTime', LosslessRuleDelayTime)
	def get_MountDescs(self): # string
		return self.get_query_params().get('MountDescs')

	def set_MountDescs(self, MountDescs):  # string
		self.add_query_param('MountDescs', MountDescs)
	def get_Replicas(self): # integer
		return self.get_query_params().get('Replicas')

	def set_Replicas(self, Replicas):  # integer
		self.add_query_param('Replicas', Replicas)
	def get_CustomTolerations(self): # string
		return self.get_query_params().get('CustomTolerations')

	def set_CustomTolerations(self, CustomTolerations):  # string
		self.add_query_param('CustomTolerations', CustomTolerations)
	def get_CpuRequest(self): # integer
		return self.get_query_params().get('CpuRequest')

	def set_CpuRequest(self, CpuRequest):  # integer
		self.add_query_param('CpuRequest', CpuRequest)
	def get_WebContainerConfig(self): # string
		return self.get_query_params().get('WebContainerConfig')

	def set_WebContainerConfig(self, WebContainerConfig):  # string
		self.add_query_param('WebContainerConfig', WebContainerConfig)
	def get_Command(self): # string
		return self.get_query_params().get('Command')

	def set_Command(self, Command):  # string
		self.add_query_param('Command', Command)
	def get_Args(self): # string
		return self.get_query_params().get('Args')

	def set_Args(self, Args):  # string
		self.add_query_param('Args', Args)
	def get_JDK(self): # string
		return self.get_query_params().get('JDK')

	def set_JDK(self, JDK):  # string
		self.add_query_param('JDK', JDK)
	def get_UriEncoding(self): # string
		return self.get_query_params().get('UriEncoding')

	def set_UriEncoding(self, UriEncoding):  # string
		self.add_query_param('UriEncoding', UriEncoding)
	def get_AppId(self): # string
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # string
		self.add_query_param('AppId', AppId)
	def get_BatchTimeout(self): # integer
		return self.get_query_params().get('BatchTimeout')

	def set_BatchTimeout(self, BatchTimeout):  # integer
		self.add_query_param('BatchTimeout', BatchTimeout)
	def get_PvcMountDescs(self): # string
		return self.get_query_params().get('PvcMountDescs')

	def set_PvcMountDescs(self, PvcMountDescs):  # string
		self.add_query_param('PvcMountDescs', PvcMountDescs)
	def get_McpuRequest(self): # integer
		return self.get_query_params().get('McpuRequest')

	def set_McpuRequest(self, McpuRequest):  # integer
		self.add_query_param('McpuRequest', McpuRequest)
	def get_VolumesStr(self): # string
		return self.get_query_params().get('VolumesStr')

	def set_VolumesStr(self, VolumesStr):  # string
		self.add_query_param('VolumesStr', VolumesStr)
	def get_LosslessRuleAligned(self): # boolean
		return self.get_query_params().get('LosslessRuleAligned')

	def set_LosslessRuleAligned(self, LosslessRuleAligned):  # boolean
		self.add_query_param('LosslessRuleAligned', LosslessRuleAligned)
	def get_JavaStartUpConfig(self): # string
		return self.get_query_params().get('JavaStartUpConfig')

	def set_JavaStartUpConfig(self, JavaStartUpConfig):  # string
		self.add_query_param('JavaStartUpConfig', JavaStartUpConfig)
