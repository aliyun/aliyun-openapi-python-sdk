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

class InsertK8sApplicationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'InsertK8sApplication','Edas')
		self.set_uri_pattern('/pop/v5/k8s/acs/create_k8s_app')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NasId(self): # String
		return self.get_query_params().get('NasId')

	def set_NasId(self, NasId):  # String
		self.add_query_param('NasId', NasId)
	def get_IntranetSlbId(self): # String
		return self.get_query_params().get('IntranetSlbId')

	def set_IntranetSlbId(self, IntranetSlbId):  # String
		self.add_query_param('IntranetSlbId', IntranetSlbId)
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
	def get_RequestsMem(self): # Integer
		return self.get_query_params().get('RequestsMem')

	def set_RequestsMem(self, RequestsMem):  # Integer
		self.add_query_param('RequestsMem', RequestsMem)
	def get_StorageType(self): # String
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # String
		self.add_query_param('StorageType', StorageType)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ConfigMountDescs(self): # String
		return self.get_query_params().get('ConfigMountDescs')

	def set_ConfigMountDescs(self, ConfigMountDescs):  # String
		self.add_query_param('ConfigMountDescs', ConfigMountDescs)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_RequestsmCpu(self): # Integer
		return self.get_query_params().get('RequestsmCpu')

	def set_RequestsmCpu(self, RequestsmCpu):  # Integer
		self.add_query_param('RequestsmCpu', RequestsmCpu)
	def get_DeployAcrossZones(self): # String
		return self.get_query_params().get('DeployAcrossZones')

	def set_DeployAcrossZones(self, DeployAcrossZones):  # String
		self.add_query_param('DeployAcrossZones', DeployAcrossZones)
	def get_IntranetSlbPort(self): # Integer
		return self.get_query_params().get('IntranetSlbPort')

	def set_IntranetSlbPort(self, IntranetSlbPort):  # Integer
		self.add_query_param('IntranetSlbPort', IntranetSlbPort)
	def get_DeployAcrossNodes(self): # String
		return self.get_query_params().get('DeployAcrossNodes')

	def set_DeployAcrossNodes(self, DeployAcrossNodes):  # String
		self.add_query_param('DeployAcrossNodes', DeployAcrossNodes)
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
	def get_LosslessRuleFuncType(self): # Integer
		return self.get_query_params().get('LosslessRuleFuncType')

	def set_LosslessRuleFuncType(self, LosslessRuleFuncType):  # Integer
		self.add_query_param('LosslessRuleFuncType', LosslessRuleFuncType)
	def get_EmptyDirs(self): # String
		return self.get_query_params().get('EmptyDirs')

	def set_EmptyDirs(self, EmptyDirs):  # String
		self.add_query_param('EmptyDirs', EmptyDirs)
	def get_PackageType(self): # String
		return self.get_query_params().get('PackageType')

	def set_PackageType(self, PackageType):  # String
		self.add_query_param('PackageType', PackageType)
	def get_LosslessRuleRelated(self): # Boolean
		return self.get_query_params().get('LosslessRuleRelated')

	def set_LosslessRuleRelated(self, LosslessRuleRelated):  # Boolean
		self.add_query_param('LosslessRuleRelated', LosslessRuleRelated)
	def get_SecretName(self): # String
		return self.get_query_params().get('SecretName')

	def set_SecretName(self, SecretName):  # String
		self.add_query_param('SecretName', SecretName)
	def get_RuntimeClassName(self): # String
		return self.get_query_params().get('RuntimeClassName')

	def set_RuntimeClassName(self, RuntimeClassName):  # String
		self.add_query_param('RuntimeClassName', RuntimeClassName)
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
	def get_RepoId(self): # String
		return self.get_query_params().get('RepoId')

	def set_RepoId(self, RepoId):  # String
		self.add_query_param('RepoId', RepoId)
	def get_InternetTargetPort(self): # Integer
		return self.get_query_params().get('InternetTargetPort')

	def set_InternetTargetPort(self, InternetTargetPort):  # Integer
		self.add_query_param('InternetTargetPort', InternetTargetPort)
	def get_WebContainer(self): # String
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self, WebContainer):  # String
		self.add_query_param('WebContainer', WebContainer)
	def get_EnableAsm(self): # Boolean
		return self.get_query_params().get('EnableAsm')

	def set_EnableAsm(self, EnableAsm):  # Boolean
		self.add_query_param('EnableAsm', EnableAsm)
	def get_EnableAhas(self): # Boolean
		return self.get_query_params().get('EnableAhas')

	def set_EnableAhas(self, EnableAhas):  # Boolean
		self.add_query_param('EnableAhas', EnableAhas)
	def get_SlsConfigs(self): # String
		return self.get_query_params().get('SlsConfigs')

	def set_SlsConfigs(self, SlsConfigs):  # String
		self.add_query_param('SlsConfigs', SlsConfigs)
	def get_CommandArgs(self): # String
		return self.get_query_params().get('CommandArgs')

	def set_CommandArgs(self, CommandArgs):  # String
		self.add_query_param('CommandArgs', CommandArgs)
	def get_Readiness(self): # String
		return self.get_query_params().get('Readiness')

	def set_Readiness(self, Readiness):  # String
		self.add_query_param('Readiness', Readiness)
	def get_Liveness(self): # String
		return self.get_query_params().get('Liveness')

	def set_Liveness(self, Liveness):  # String
		self.add_query_param('Liveness', Liveness)
	def get_CsClusterId(self): # String
		return self.get_query_params().get('CsClusterId')

	def set_CsClusterId(self, CsClusterId):  # String
		self.add_query_param('CsClusterId', CsClusterId)
	def get_AppConfig(self): # String
		return self.get_query_params().get('AppConfig')

	def set_AppConfig(self, AppConfig):  # String
		self.add_query_param('AppConfig', AppConfig)
	def get_InternetSlbPort(self): # Integer
		return self.get_query_params().get('InternetSlbPort')

	def set_InternetSlbPort(self, InternetSlbPort):  # Integer
		self.add_query_param('InternetSlbPort', InternetSlbPort)
	def get_PackageVersion(self): # String
		return self.get_query_params().get('PackageVersion')

	def set_PackageVersion(self, PackageVersion):  # String
		self.add_query_param('PackageVersion', PackageVersion)
	def get_Timeout(self): # Integer
		return self.get_query_params().get('Timeout')

	def set_Timeout(self, Timeout):  # Integer
		self.add_query_param('Timeout', Timeout)
	def get_EnvFroms(self): # String
		return self.get_query_params().get('EnvFroms')

	def set_EnvFroms(self, EnvFroms):  # String
		self.add_query_param('EnvFroms', EnvFroms)
	def get_LimitMem(self): # Integer
		return self.get_query_params().get('LimitMem')

	def set_LimitMem(self, LimitMem):  # Integer
		self.add_query_param('LimitMem', LimitMem)
	def get_LimitmCpu(self): # Integer
		return self.get_query_params().get('LimitmCpu')

	def set_LimitmCpu(self, LimitmCpu):  # Integer
		self.add_query_param('LimitmCpu', LimitmCpu)
	def get_EdasContainerVersion(self): # String
		return self.get_query_params().get('EdasContainerVersion')

	def set_EdasContainerVersion(self, EdasContainerVersion):  # String
		self.add_query_param('EdasContainerVersion', EdasContainerVersion)
	def get_InternetSlbId(self): # String
		return self.get_query_params().get('InternetSlbId')

	def set_InternetSlbId(self, InternetSlbId):  # String
		self.add_query_param('InternetSlbId', InternetSlbId)
	def get_LogicalRegionId(self): # String
		return self.get_query_params().get('LogicalRegionId')

	def set_LogicalRegionId(self, LogicalRegionId):  # String
		self.add_query_param('LogicalRegionId', LogicalRegionId)
	def get_PackageUrl(self): # String
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self, PackageUrl):  # String
		self.add_query_param('PackageUrl', PackageUrl)
	def get_InternetSlbProtocol(self): # String
		return self.get_query_params().get('InternetSlbProtocol')

	def set_InternetSlbProtocol(self, InternetSlbProtocol):  # String
		self.add_query_param('InternetSlbProtocol', InternetSlbProtocol)
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
	def get_LimitCpu(self): # Integer
		return self.get_query_params().get('LimitCpu')

	def set_LimitCpu(self, LimitCpu):  # Integer
		self.add_query_param('LimitCpu', LimitCpu)
	def get_CustomTolerations(self): # String
		return self.get_query_params().get('CustomTolerations')

	def set_CustomTolerations(self, CustomTolerations):  # String
		self.add_query_param('CustomTolerations', CustomTolerations)
	def get_WebContainerConfig(self): # String
		return self.get_query_params().get('WebContainerConfig')

	def set_WebContainerConfig(self, WebContainerConfig):  # String
		self.add_query_param('WebContainerConfig', WebContainerConfig)
	def get_IsMultilingualApp(self): # Boolean
		return self.get_query_params().get('IsMultilingualApp')

	def set_IsMultilingualApp(self, IsMultilingualApp):  # Boolean
		self.add_query_param('IsMultilingualApp', IsMultilingualApp)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_ServiceConfigs(self): # String
		return self.get_query_params().get('ServiceConfigs')

	def set_ServiceConfigs(self, ServiceConfigs):  # String
		self.add_query_param('ServiceConfigs', ServiceConfigs)
	def get_IntranetTargetPort(self): # Integer
		return self.get_query_params().get('IntranetTargetPort')

	def set_IntranetTargetPort(self, IntranetTargetPort):  # Integer
		self.add_query_param('IntranetTargetPort', IntranetTargetPort)
	def get_Command(self): # String
		return self.get_query_params().get('Command')

	def set_Command(self, Command):  # String
		self.add_query_param('Command', Command)
	def get_JDK(self): # String
		return self.get_query_params().get('JDK')

	def set_JDK(self, JDK):  # String
		self.add_query_param('JDK', JDK)
	def get_UriEncoding(self): # String
		return self.get_query_params().get('UriEncoding')

	def set_UriEncoding(self, UriEncoding):  # String
		self.add_query_param('UriEncoding', UriEncoding)
	def get_IntranetSlbProtocol(self): # String
		return self.get_query_params().get('IntranetSlbProtocol')

	def set_IntranetSlbProtocol(self, IntranetSlbProtocol):  # String
		self.add_query_param('IntranetSlbProtocol', IntranetSlbProtocol)
	def get_ImageUrl(self): # String
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self, ImageUrl):  # String
		self.add_query_param('ImageUrl', ImageUrl)
	def get_PvcMountDescs(self): # String
		return self.get_query_params().get('PvcMountDescs')

	def set_PvcMountDescs(self, PvcMountDescs):  # String
		self.add_query_param('PvcMountDescs', PvcMountDescs)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_ContainerRegistryId(self): # String
		return self.get_query_params().get('ContainerRegistryId')

	def set_ContainerRegistryId(self, ContainerRegistryId):  # String
		self.add_query_param('ContainerRegistryId', ContainerRegistryId)
	def get_AppTemplateName(self): # String
		return self.get_query_params().get('AppTemplateName')

	def set_AppTemplateName(self, AppTemplateName):  # String
		self.add_query_param('AppTemplateName', AppTemplateName)
	def get_ApplicationDescription(self): # String
		return self.get_query_params().get('ApplicationDescription')

	def set_ApplicationDescription(self, ApplicationDescription):  # String
		self.add_query_param('ApplicationDescription', ApplicationDescription)
	def get_LosslessRuleAligned(self): # Boolean
		return self.get_query_params().get('LosslessRuleAligned')

	def set_LosslessRuleAligned(self, LosslessRuleAligned):  # Boolean
		self.add_query_param('LosslessRuleAligned', LosslessRuleAligned)
	def get_RequestsCpu(self): # Integer
		return self.get_query_params().get('RequestsCpu')

	def set_RequestsCpu(self, RequestsCpu):  # Integer
		self.add_query_param('RequestsCpu', RequestsCpu)
	def get_JavaStartUpConfig(self): # String
		return self.get_query_params().get('JavaStartUpConfig')

	def set_JavaStartUpConfig(self, JavaStartUpConfig):  # String
		self.add_query_param('JavaStartUpConfig', JavaStartUpConfig)
