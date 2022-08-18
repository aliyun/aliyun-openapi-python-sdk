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

	def get_NasId(self): # string
		return self.get_query_params().get('NasId')

	def set_NasId(self, NasId):  # string
		self.add_query_param('NasId', NasId)
	def get_IntranetSlbId(self): # string
		return self.get_query_params().get('IntranetSlbId')

	def set_IntranetSlbId(self, IntranetSlbId):  # string
		self.add_query_param('IntranetSlbId', IntranetSlbId)
	def get_Envs(self): # string
		return self.get_query_params().get('Envs')

	def set_Envs(self, Envs):  # string
		self.add_query_param('Envs', Envs)
	def get_Annotations(self): # string
		return self.get_query_params().get('Annotations')

	def set_Annotations(self, Annotations):  # string
		self.add_query_param('Annotations', Annotations)
	def get_RequestsMem(self): # integer
		return self.get_query_params().get('RequestsMem')

	def set_RequestsMem(self, RequestsMem):  # integer
		self.add_query_param('RequestsMem', RequestsMem)
	def get_StorageType(self): # string
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # string
		self.add_query_param('StorageType', StorageType)
	def get_ResourceGroupId(self): # string
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # string
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ConfigMountDescs(self): # string
		return self.get_query_params().get('ConfigMountDescs')

	def set_ConfigMountDescs(self, ConfigMountDescs):  # string
		self.add_query_param('ConfigMountDescs', ConfigMountDescs)
	def get_AppName(self): # string
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # string
		self.add_query_param('AppName', AppName)
	def get_RequestsmCpu(self): # integer
		return self.get_query_params().get('RequestsmCpu')

	def set_RequestsmCpu(self, RequestsmCpu):  # integer
		self.add_query_param('RequestsmCpu', RequestsmCpu)
	def get_DeployAcrossZones(self): # string
		return self.get_query_params().get('DeployAcrossZones')

	def set_DeployAcrossZones(self, DeployAcrossZones):  # string
		self.add_query_param('DeployAcrossZones', DeployAcrossZones)
	def get_IntranetSlbPort(self): # integer
		return self.get_query_params().get('IntranetSlbPort')

	def set_IntranetSlbPort(self, IntranetSlbPort):  # integer
		self.add_query_param('IntranetSlbPort', IntranetSlbPort)
	def get_DeployAcrossNodes(self): # string
		return self.get_query_params().get('DeployAcrossNodes')

	def set_DeployAcrossNodes(self, DeployAcrossNodes):  # string
		self.add_query_param('DeployAcrossNodes', DeployAcrossNodes)
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
	def get_Labels(self): # string
		return self.get_query_params().get('Labels')

	def set_Labels(self, Labels):  # string
		self.add_query_param('Labels', Labels)
	def get_UseBodyEncoding(self): # boolean
		return self.get_query_params().get('UseBodyEncoding')

	def set_UseBodyEncoding(self, UseBodyEncoding):  # boolean
		self.add_query_param('UseBodyEncoding', UseBodyEncoding)
	def get_LosslessRuleFuncType(self): # integer
		return self.get_query_params().get('LosslessRuleFuncType')

	def set_LosslessRuleFuncType(self, LosslessRuleFuncType):  # integer
		self.add_query_param('LosslessRuleFuncType', LosslessRuleFuncType)
	def get_EmptyDirs(self): # string
		return self.get_query_params().get('EmptyDirs')

	def set_EmptyDirs(self, EmptyDirs):  # string
		self.add_query_param('EmptyDirs', EmptyDirs)
	def get_PackageType(self): # string
		return self.get_query_params().get('PackageType')

	def set_PackageType(self, PackageType):  # string
		self.add_query_param('PackageType', PackageType)
	def get_LosslessRuleRelated(self): # boolean
		return self.get_query_params().get('LosslessRuleRelated')

	def set_LosslessRuleRelated(self, LosslessRuleRelated):  # boolean
		self.add_query_param('LosslessRuleRelated', LosslessRuleRelated)
	def get_RuntimeClassName(self): # string
		return self.get_query_params().get('RuntimeClassName')

	def set_RuntimeClassName(self, RuntimeClassName):  # string
		self.add_query_param('RuntimeClassName', RuntimeClassName)
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
	def get_RepoId(self): # string
		return self.get_query_params().get('RepoId')

	def set_RepoId(self, RepoId):  # string
		self.add_query_param('RepoId', RepoId)
	def get_InternetTargetPort(self): # integer
		return self.get_query_params().get('InternetTargetPort')

	def set_InternetTargetPort(self, InternetTargetPort):  # integer
		self.add_query_param('InternetTargetPort', InternetTargetPort)
	def get_WebContainer(self): # string
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self, WebContainer):  # string
		self.add_query_param('WebContainer', WebContainer)
	def get_EnableAsm(self): # boolean
		return self.get_query_params().get('EnableAsm')

	def set_EnableAsm(self, EnableAsm):  # boolean
		self.add_query_param('EnableAsm', EnableAsm)
	def get_EnableAhas(self): # boolean
		return self.get_query_params().get('EnableAhas')

	def set_EnableAhas(self, EnableAhas):  # boolean
		self.add_query_param('EnableAhas', EnableAhas)
	def get_SlsConfigs(self): # string
		return self.get_query_params().get('SlsConfigs')

	def set_SlsConfigs(self, SlsConfigs):  # string
		self.add_query_param('SlsConfigs', SlsConfigs)
	def get_CommandArgs(self): # string
		return self.get_query_params().get('CommandArgs')

	def set_CommandArgs(self, CommandArgs):  # string
		self.add_query_param('CommandArgs', CommandArgs)
	def get_Readiness(self): # string
		return self.get_query_params().get('Readiness')

	def set_Readiness(self, Readiness):  # string
		self.add_query_param('Readiness', Readiness)
	def get_Liveness(self): # string
		return self.get_query_params().get('Liveness')

	def set_Liveness(self, Liveness):  # string
		self.add_query_param('Liveness', Liveness)
	def get_CsClusterId(self): # string
		return self.get_query_params().get('CsClusterId')

	def set_CsClusterId(self, CsClusterId):  # string
		self.add_query_param('CsClusterId', CsClusterId)
	def get_AppConfig(self): # string
		return self.get_query_params().get('AppConfig')

	def set_AppConfig(self, AppConfig):  # string
		self.add_query_param('AppConfig', AppConfig)
	def get_InternetSlbPort(self): # integer
		return self.get_query_params().get('InternetSlbPort')

	def set_InternetSlbPort(self, InternetSlbPort):  # integer
		self.add_query_param('InternetSlbPort', InternetSlbPort)
	def get_PackageVersion(self): # string
		return self.get_query_params().get('PackageVersion')

	def set_PackageVersion(self, PackageVersion):  # string
		self.add_query_param('PackageVersion', PackageVersion)
	def get_Timeout(self): # integer
		return self.get_query_params().get('Timeout')

	def set_Timeout(self, Timeout):  # integer
		self.add_query_param('Timeout', Timeout)
	def get_EnvFroms(self): # string
		return self.get_query_params().get('EnvFroms')

	def set_EnvFroms(self, EnvFroms):  # string
		self.add_query_param('EnvFroms', EnvFroms)
	def get_LimitMem(self): # integer
		return self.get_query_params().get('LimitMem')

	def set_LimitMem(self, LimitMem):  # integer
		self.add_query_param('LimitMem', LimitMem)
	def get_LimitmCpu(self): # integer
		return self.get_query_params().get('LimitmCpu')

	def set_LimitmCpu(self, LimitmCpu):  # integer
		self.add_query_param('LimitmCpu', LimitmCpu)
	def get_EdasContainerVersion(self): # string
		return self.get_query_params().get('EdasContainerVersion')

	def set_EdasContainerVersion(self, EdasContainerVersion):  # string
		self.add_query_param('EdasContainerVersion', EdasContainerVersion)
	def get_InternetSlbId(self): # string
		return self.get_query_params().get('InternetSlbId')

	def set_InternetSlbId(self, InternetSlbId):  # string
		self.add_query_param('InternetSlbId', InternetSlbId)
	def get_LogicalRegionId(self): # string
		return self.get_query_params().get('LogicalRegionId')

	def set_LogicalRegionId(self, LogicalRegionId):  # string
		self.add_query_param('LogicalRegionId', LogicalRegionId)
	def get_PackageUrl(self): # string
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self, PackageUrl):  # string
		self.add_query_param('PackageUrl', PackageUrl)
	def get_InternetSlbProtocol(self): # string
		return self.get_query_params().get('InternetSlbProtocol')

	def set_InternetSlbProtocol(self, InternetSlbProtocol):  # string
		self.add_query_param('InternetSlbProtocol', InternetSlbProtocol)
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
	def get_LimitCpu(self): # integer
		return self.get_query_params().get('LimitCpu')

	def set_LimitCpu(self, LimitCpu):  # integer
		self.add_query_param('LimitCpu', LimitCpu)
	def get_CustomTolerations(self): # string
		return self.get_query_params().get('CustomTolerations')

	def set_CustomTolerations(self, CustomTolerations):  # string
		self.add_query_param('CustomTolerations', CustomTolerations)
	def get_WebContainerConfig(self): # string
		return self.get_query_params().get('WebContainerConfig')

	def set_WebContainerConfig(self, WebContainerConfig):  # string
		self.add_query_param('WebContainerConfig', WebContainerConfig)
	def get_IsMultilingualApp(self): # boolean
		return self.get_query_params().get('IsMultilingualApp')

	def set_IsMultilingualApp(self, IsMultilingualApp):  # boolean
		self.add_query_param('IsMultilingualApp', IsMultilingualApp)
	def get_ClusterId(self): # string
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # string
		self.add_query_param('ClusterId', ClusterId)
	def get_ServiceConfigs(self): # string
		return self.get_query_params().get('ServiceConfigs')

	def set_ServiceConfigs(self, ServiceConfigs):  # string
		self.add_query_param('ServiceConfigs', ServiceConfigs)
	def get_IntranetTargetPort(self): # integer
		return self.get_query_params().get('IntranetTargetPort')

	def set_IntranetTargetPort(self, IntranetTargetPort):  # integer
		self.add_query_param('IntranetTargetPort', IntranetTargetPort)
	def get_Command(self): # string
		return self.get_query_params().get('Command')

	def set_Command(self, Command):  # string
		self.add_query_param('Command', Command)
	def get_JDK(self): # string
		return self.get_query_params().get('JDK')

	def set_JDK(self, JDK):  # string
		self.add_query_param('JDK', JDK)
	def get_UriEncoding(self): # string
		return self.get_query_params().get('UriEncoding')

	def set_UriEncoding(self, UriEncoding):  # string
		self.add_query_param('UriEncoding', UriEncoding)
	def get_IntranetSlbProtocol(self): # string
		return self.get_query_params().get('IntranetSlbProtocol')

	def set_IntranetSlbProtocol(self, IntranetSlbProtocol):  # string
		self.add_query_param('IntranetSlbProtocol', IntranetSlbProtocol)
	def get_ImageUrl(self): # string
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self, ImageUrl):  # string
		self.add_query_param('ImageUrl', ImageUrl)
	def get_PvcMountDescs(self): # string
		return self.get_query_params().get('PvcMountDescs')

	def set_PvcMountDescs(self, PvcMountDescs):  # string
		self.add_query_param('PvcMountDescs', PvcMountDescs)
	def get_Namespace(self): # string
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # string
		self.add_query_param('Namespace', Namespace)
	def get_AppTemplateName(self): # string
		return self.get_query_params().get('AppTemplateName')

	def set_AppTemplateName(self, AppTemplateName):  # string
		self.add_query_param('AppTemplateName', AppTemplateName)
	def get_ApplicationDescription(self): # string
		return self.get_query_params().get('ApplicationDescription')

	def set_ApplicationDescription(self, ApplicationDescription):  # string
		self.add_query_param('ApplicationDescription', ApplicationDescription)
	def get_LosslessRuleAligned(self): # boolean
		return self.get_query_params().get('LosslessRuleAligned')

	def set_LosslessRuleAligned(self, LosslessRuleAligned):  # boolean
		self.add_query_param('LosslessRuleAligned', LosslessRuleAligned)
	def get_RequestsCpu(self): # integer
		return self.get_query_params().get('RequestsCpu')

	def set_RequestsCpu(self, RequestsCpu):  # integer
		self.add_query_param('RequestsCpu', RequestsCpu)
	def get_JavaStartUpConfig(self): # string
		return self.get_query_params().get('JavaStartUpConfig')

	def set_JavaStartUpConfig(self, JavaStartUpConfig):  # string
		self.add_query_param('JavaStartUpConfig', JavaStartUpConfig)
