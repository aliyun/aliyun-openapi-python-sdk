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

	def get_NasId(self): # String
		return self.get_query_params().get('NasId')

	def set_NasId(self, NasId):  # String
		self.add_query_param('NasId', NasId)
	def get_PackageVersionId(self): # String
		return self.get_query_params().get('PackageVersionId')

	def set_PackageVersionId(self, PackageVersionId):  # String
		self.add_query_param('PackageVersionId', PackageVersionId)
	def get_BatchWaitTime(self): # Integer
		return self.get_query_params().get('BatchWaitTime')

	def set_BatchWaitTime(self, BatchWaitTime):  # Integer
		self.add_query_param('BatchWaitTime', BatchWaitTime)
	def get_RequestsEphemeralStorage(self): # Integer
		return self.get_query_params().get('RequestsEphemeralStorage')

	def set_RequestsEphemeralStorage(self, RequestsEphemeralStorage):  # Integer
		self.add_query_param('RequestsEphemeralStorage', RequestsEphemeralStorage)
	def get_Envs(self): # String
		return self.get_query_params().get('Envs')

	def set_Envs(self, Envs):  # String
		self.add_query_param('Envs', Envs)
	def get_Annotations(self): # String
		return self.get_query_params().get('Annotations')

	def set_Annotations(self, Annotations):  # String
		self.add_query_param('Annotations', Annotations)
	def get_CpuLimit(self): # Integer
		return self.get_query_params().get('CpuLimit')

	def set_CpuLimit(self, CpuLimit):  # Integer
		self.add_query_param('CpuLimit', CpuLimit)
	def get_StorageType(self): # String
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # String
		self.add_query_param('StorageType', StorageType)
	def get_ConfigMountDescs(self): # String
		return self.get_query_params().get('ConfigMountDescs')

	def set_ConfigMountDescs(self, ConfigMountDescs):  # String
		self.add_query_param('ConfigMountDescs', ConfigMountDescs)
	def get_MemoryLimit(self): # Integer
		return self.get_query_params().get('MemoryLimit')

	def set_MemoryLimit(self, MemoryLimit):  # Integer
		self.add_query_param('MemoryLimit', MemoryLimit)
	def get_ImageTag(self): # String
		return self.get_query_params().get('ImageTag')

	def set_ImageTag(self, ImageTag):  # String
		self.add_query_param('ImageTag', ImageTag)
	def get_DeployAcrossZones(self): # String
		return self.get_query_params().get('DeployAcrossZones')

	def set_DeployAcrossZones(self, DeployAcrossZones):  # String
		self.add_query_param('DeployAcrossZones', DeployAcrossZones)
	def get_DeployAcrossNodes(self): # String
		return self.get_query_params().get('DeployAcrossNodes')

	def set_DeployAcrossNodes(self, DeployAcrossNodes):  # String
		self.add_query_param('DeployAcrossNodes', DeployAcrossNodes)
	def get_MemoryRequest(self): # Integer
		return self.get_query_params().get('MemoryRequest')

	def set_MemoryRequest(self, MemoryRequest):  # Integer
		self.add_query_param('MemoryRequest', MemoryRequest)
	def get_Image(self): # String
		return self.get_query_params().get('Image')

	def set_Image(self, Image):  # String
		self.add_query_param('Image', Image)
	def get_PreStop(self): # String
		return self.get_query_params().get('PreStop')

	def set_PreStop(self, PreStop):  # String
		self.add_query_param('PreStop', PreStop)
	def get_BuildPackId(self): # String
		return self.get_query_params().get('BuildPackId')

	def set_BuildPackId(self, BuildPackId):  # String
		self.add_query_param('BuildPackId', BuildPackId)
	def get_EnableEmptyPushReject(self): # Boolean
		return self.get_query_params().get('EnableEmptyPushReject')

	def set_EnableEmptyPushReject(self, EnableEmptyPushReject):  # Boolean
		self.add_query_param('EnableEmptyPushReject', EnableEmptyPushReject)
	def get_LocalVolume(self): # String
		return self.get_query_params().get('LocalVolume')

	def set_LocalVolume(self, LocalVolume):  # String
		self.add_query_param('LocalVolume', LocalVolume)
	def get_UpdateStrategy(self): # String
		return self.get_query_params().get('UpdateStrategy')

	def set_UpdateStrategy(self, UpdateStrategy):  # String
		self.add_query_param('UpdateStrategy', UpdateStrategy)
	def get_Labels(self): # String
		return self.get_query_params().get('Labels')

	def set_Labels(self, Labels):  # String
		self.add_query_param('Labels', Labels)
	def get_UseBodyEncoding(self): # Boolean
		return self.get_query_params().get('UseBodyEncoding')

	def set_UseBodyEncoding(self, UseBodyEncoding):  # Boolean
		self.add_query_param('UseBodyEncoding', UseBodyEncoding)
	def get_LimitEphemeralStorage(self): # Integer
		return self.get_query_params().get('LimitEphemeralStorage')

	def set_LimitEphemeralStorage(self, LimitEphemeralStorage):  # Integer
		self.add_query_param('LimitEphemeralStorage', LimitEphemeralStorage)
	def get_ChangeOrderDesc(self): # String
		return self.get_query_params().get('ChangeOrderDesc')

	def set_ChangeOrderDesc(self, ChangeOrderDesc):  # String
		self.add_query_param('ChangeOrderDesc', ChangeOrderDesc)
	def get_LosslessRuleFuncType(self): # Integer
		return self.get_query_params().get('LosslessRuleFuncType')

	def set_LosslessRuleFuncType(self, LosslessRuleFuncType):  # Integer
		self.add_query_param('LosslessRuleFuncType', LosslessRuleFuncType)
	def get_EmptyDirs(self): # String
		return self.get_query_params().get('EmptyDirs')

	def set_EmptyDirs(self, EmptyDirs):  # String
		self.add_query_param('EmptyDirs', EmptyDirs)
	def get_McpuLimit(self): # Integer
		return self.get_query_params().get('McpuLimit')

	def set_McpuLimit(self, McpuLimit):  # Integer
		self.add_query_param('McpuLimit', McpuLimit)
	def get_LosslessRuleRelated(self): # Boolean
		return self.get_query_params().get('LosslessRuleRelated')

	def set_LosslessRuleRelated(self, LosslessRuleRelated):  # Boolean
		self.add_query_param('LosslessRuleRelated', LosslessRuleRelated)
	def get_RuntimeClassName(self): # String
		return self.get_query_params().get('RuntimeClassName')

	def set_RuntimeClassName(self, RuntimeClassName):  # String
		self.add_query_param('RuntimeClassName', RuntimeClassName)
	def get_TrafficControlStrategy(self): # String
		return self.get_query_params().get('TrafficControlStrategy')

	def set_TrafficControlStrategy(self, TrafficControlStrategy):  # String
		self.add_query_param('TrafficControlStrategy', TrafficControlStrategy)
	def get_PostStart(self): # String
		return self.get_query_params().get('PostStart')

	def set_PostStart(self, PostStart):  # String
		self.add_query_param('PostStart', PostStart)
	def get_CustomAffinity(self): # String
		return self.get_query_params().get('CustomAffinity')

	def set_CustomAffinity(self, CustomAffinity):  # String
		self.add_query_param('CustomAffinity', CustomAffinity)
	def get_EnableLosslessRule(self): # Boolean
		return self.get_query_params().get('EnableLosslessRule')

	def set_EnableLosslessRule(self, EnableLosslessRule):  # Boolean
		self.add_query_param('EnableLosslessRule', EnableLosslessRule)
	def get_LosslessRuleWarmupTime(self): # Integer
		return self.get_query_params().get('LosslessRuleWarmupTime')

	def set_LosslessRuleWarmupTime(self, LosslessRuleWarmupTime):  # Integer
		self.add_query_param('LosslessRuleWarmupTime', LosslessRuleWarmupTime)
	def get_WebContainer(self): # String
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self, WebContainer):  # String
		self.add_query_param('WebContainer', WebContainer)
	def get_EnableAhas(self): # Boolean
		return self.get_query_params().get('EnableAhas')

	def set_EnableAhas(self, EnableAhas):  # Boolean
		self.add_query_param('EnableAhas', EnableAhas)
	def get_SlsConfigs(self): # String
		return self.get_query_params().get('SlsConfigs')

	def set_SlsConfigs(self, SlsConfigs):  # String
		self.add_query_param('SlsConfigs', SlsConfigs)
	def get_Readiness(self): # String
		return self.get_query_params().get('Readiness')

	def set_Readiness(self, Readiness):  # String
		self.add_query_param('Readiness', Readiness)
	def get_Liveness(self): # String
		return self.get_query_params().get('Liveness')

	def set_Liveness(self, Liveness):  # String
		self.add_query_param('Liveness', Liveness)
	def get_PackageVersion(self): # String
		return self.get_query_params().get('PackageVersion')

	def set_PackageVersion(self, PackageVersion):  # String
		self.add_query_param('PackageVersion', PackageVersion)
	def get_EnvFroms(self): # String
		return self.get_query_params().get('EnvFroms')

	def set_EnvFroms(self, EnvFroms):  # String
		self.add_query_param('EnvFroms', EnvFroms)
	def get_EdasContainerVersion(self): # String
		return self.get_query_params().get('EdasContainerVersion')

	def set_EdasContainerVersion(self, EdasContainerVersion):  # String
		self.add_query_param('EdasContainerVersion', EdasContainerVersion)
	def get_PackageUrl(self): # String
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self, PackageUrl):  # String
		self.add_query_param('PackageUrl', PackageUrl)
	def get_LosslessRuleDelayTime(self): # Integer
		return self.get_query_params().get('LosslessRuleDelayTime')

	def set_LosslessRuleDelayTime(self, LosslessRuleDelayTime):  # Integer
		self.add_query_param('LosslessRuleDelayTime', LosslessRuleDelayTime)
	def get_MountDescs(self): # String
		return self.get_query_params().get('MountDescs')

	def set_MountDescs(self, MountDescs):  # String
		self.add_query_param('MountDescs', MountDescs)
	def get_Replicas(self): # Integer
		return self.get_query_params().get('Replicas')

	def set_Replicas(self, Replicas):  # Integer
		self.add_query_param('Replicas', Replicas)
	def get_CustomTolerations(self): # String
		return self.get_query_params().get('CustomTolerations')

	def set_CustomTolerations(self, CustomTolerations):  # String
		self.add_query_param('CustomTolerations', CustomTolerations)
	def get_CpuRequest(self): # Integer
		return self.get_query_params().get('CpuRequest')

	def set_CpuRequest(self, CpuRequest):  # Integer
		self.add_query_param('CpuRequest', CpuRequest)
	def get_WebContainerConfig(self): # String
		return self.get_query_params().get('WebContainerConfig')

	def set_WebContainerConfig(self, WebContainerConfig):  # String
		self.add_query_param('WebContainerConfig', WebContainerConfig)
	def get_Command(self): # String
		return self.get_query_params().get('Command')

	def set_Command(self, Command):  # String
		self.add_query_param('Command', Command)
	def get_Args(self): # String
		return self.get_query_params().get('Args')

	def set_Args(self, Args):  # String
		self.add_query_param('Args', Args)
	def get_JDK(self): # String
		return self.get_query_params().get('JDK')

	def set_JDK(self, JDK):  # String
		self.add_query_param('JDK', JDK)
	def get_UriEncoding(self): # String
		return self.get_query_params().get('UriEncoding')

	def set_UriEncoding(self, UriEncoding):  # String
		self.add_query_param('UriEncoding', UriEncoding)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_BatchTimeout(self): # Integer
		return self.get_query_params().get('BatchTimeout')

	def set_BatchTimeout(self, BatchTimeout):  # Integer
		self.add_query_param('BatchTimeout', BatchTimeout)
	def get_PvcMountDescs(self): # String
		return self.get_query_params().get('PvcMountDescs')

	def set_PvcMountDescs(self, PvcMountDescs):  # String
		self.add_query_param('PvcMountDescs', PvcMountDescs)
	def get_McpuRequest(self): # Integer
		return self.get_query_params().get('McpuRequest')

	def set_McpuRequest(self, McpuRequest):  # Integer
		self.add_query_param('McpuRequest', McpuRequest)
	def get_VolumesStr(self): # String
		return self.get_query_params().get('VolumesStr')

	def set_VolumesStr(self, VolumesStr):  # String
		self.add_query_param('VolumesStr', VolumesStr)
	def get_LosslessRuleAligned(self): # Boolean
		return self.get_query_params().get('LosslessRuleAligned')

	def set_LosslessRuleAligned(self, LosslessRuleAligned):  # Boolean
		self.add_query_param('LosslessRuleAligned', LosslessRuleAligned)
	def get_JavaStartUpConfig(self): # String
		return self.get_query_params().get('JavaStartUpConfig')

	def set_JavaStartUpConfig(self, JavaStartUpConfig):  # String
		self.add_query_param('JavaStartUpConfig', JavaStartUpConfig)
