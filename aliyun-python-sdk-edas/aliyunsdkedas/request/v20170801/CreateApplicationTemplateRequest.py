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

class CreateApplicationTemplateRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'CreateApplicationTemplate','Edas')
		self.set_uri_pattern('/pop/v5/cnedas/app_template')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NasId(self):
		return self.get_body_params().get('NasId')

	def set_NasId(self,NasId):
		self.add_body_params('NasId', NasId)

	def get_EnableAhas(self):
		return self.get_body_params().get('EnableAhas')

	def set_EnableAhas(self,EnableAhas):
		self.add_body_params('EnableAhas', EnableAhas)

	def get_SlsConfigs(self):
		return self.get_body_params().get('SlsConfigs')

	def set_SlsConfigs(self,SlsConfigs):
		self.add_body_params('SlsConfigs', SlsConfigs)

	def get_CommandArgs(self):
		return self.get_body_params().get('CommandArgs')

	def set_CommandArgs(self,CommandArgs):
		self.add_body_params('CommandArgs', CommandArgs)

	def get_Readiness(self):
		return self.get_body_params().get('Readiness')

	def set_Readiness(self,Readiness):
		self.add_body_params('Readiness', Readiness)

	def get_Liveness(self):
		return self.get_body_params().get('Liveness')

	def set_Liveness(self,Liveness):
		self.add_body_params('Liveness', Liveness)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_Envs(self):
		return self.get_body_params().get('Envs')

	def set_Envs(self,Envs):
		self.add_body_params('Envs', Envs)

	def get_EnvFroms(self):
		return self.get_body_params().get('EnvFroms')

	def set_EnvFroms(self,EnvFroms):
		self.add_body_params('EnvFroms', EnvFroms)

	def get_RequestCpu(self):
		return self.get_body_params().get('RequestCpu')

	def set_RequestCpu(self,RequestCpu):
		self.add_body_params('RequestCpu', RequestCpu)

	def get_RequestMem(self):
		return self.get_body_params().get('RequestMem')

	def set_RequestMem(self,RequestMem):
		self.add_body_params('RequestMem', RequestMem)

	def get_ShowName(self):
		return self.get_body_params().get('ShowName')

	def set_ShowName(self,ShowName):
		self.add_body_params('ShowName', ShowName)

	def get_LimitMem(self):
		return self.get_body_params().get('LimitMem')

	def set_LimitMem(self,LimitMem):
		self.add_body_params('LimitMem', LimitMem)

	def get_ConfigMountDescs(self):
		return self.get_body_params().get('ConfigMountDescs')

	def set_ConfigMountDescs(self,ConfigMountDescs):
		self.add_body_params('ConfigMountDescs', ConfigMountDescs)

	def get_DeployAcrossZones(self):
		return self.get_body_params().get('DeployAcrossZones')

	def set_DeployAcrossZones(self,DeployAcrossZones):
		self.add_body_params('DeployAcrossZones', DeployAcrossZones)

	def get_DeployAcrossNodes(self):
		return self.get_body_params().get('DeployAcrossNodes')

	def set_DeployAcrossNodes(self,DeployAcrossNodes):
		self.add_body_params('DeployAcrossNodes', DeployAcrossNodes)

	def get_PreStop(self):
		return self.get_body_params().get('PreStop')

	def set_PreStop(self,PreStop):
		self.add_body_params('PreStop', PreStop)

	def get_Replicas(self):
		return self.get_body_params().get('Replicas')

	def set_Replicas(self,Replicas):
		self.add_body_params('Replicas', Replicas)

	def get_LimitCpu(self):
		return self.get_body_params().get('LimitCpu')

	def set_LimitCpu(self,LimitCpu):
		self.add_body_params('LimitCpu', LimitCpu)

	def get_WebContainerConfig(self):
		return self.get_body_params().get('WebContainerConfig')

	def set_WebContainerConfig(self,WebContainerConfig):
		self.add_body_params('WebContainerConfig', WebContainerConfig)

	def get_PackageConfig(self):
		return self.get_body_params().get('PackageConfig')

	def set_PackageConfig(self,PackageConfig):
		self.add_body_params('PackageConfig', PackageConfig)

	def get_IsMultilingualApp(self):
		return self.get_body_params().get('IsMultilingualApp')

	def set_IsMultilingualApp(self,IsMultilingualApp):
		self.add_body_params('IsMultilingualApp', IsMultilingualApp)

	def get_NasMountDescs(self):
		return self.get_body_params().get('NasMountDescs')

	def set_NasMountDescs(self,NasMountDescs):
		self.add_body_params('NasMountDescs', NasMountDescs)

	def get_LocalVolumes(self):
		return self.get_body_params().get('LocalVolumes')

	def set_LocalVolumes(self,LocalVolumes):
		self.add_body_params('LocalVolumes', LocalVolumes)

	def get_Command(self):
		return self.get_body_params().get('Command')

	def set_Command(self,Command):
		self.add_body_params('Command', Command)

	def get_NasStorageType(self):
		return self.get_body_params().get('NasStorageType')

	def set_NasStorageType(self,NasStorageType):
		self.add_body_params('NasStorageType', NasStorageType)

	def get_ImageConfig(self):
		return self.get_body_params().get('ImageConfig')

	def set_ImageConfig(self,ImageConfig):
		self.add_body_params('ImageConfig', ImageConfig)

	def get_SourceConfig(self):
		return self.get_body_params().get('SourceConfig')

	def set_SourceConfig(self,SourceConfig):
		self.add_body_params('SourceConfig', SourceConfig)

	def get_EmptyDirs(self):
		return self.get_body_params().get('EmptyDirs')

	def set_EmptyDirs(self,EmptyDirs):
		self.add_body_params('EmptyDirs', EmptyDirs)

	def get_PvcMountDescs(self):
		return self.get_body_params().get('PvcMountDescs')

	def set_PvcMountDescs(self,PvcMountDescs):
		self.add_body_params('PvcMountDescs', PvcMountDescs)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_Attributes(self):
		return self.get_body_params().get('Attributes')

	def set_Attributes(self,Attributes):
		self.add_body_params('Attributes', Attributes)

	def get_RuntimeClassName(self):
		return self.get_body_params().get('RuntimeClassName')

	def set_RuntimeClassName(self,RuntimeClassName):
		self.add_body_params('RuntimeClassName', RuntimeClassName)

	def get_JavaStartUpConfig(self):
		return self.get_body_params().get('JavaStartUpConfig')

	def set_JavaStartUpConfig(self,JavaStartUpConfig):
		self.add_body_params('JavaStartUpConfig', JavaStartUpConfig)

	def get_PostStart(self):
		return self.get_body_params().get('PostStart')

	def set_PostStart(self,PostStart):
		self.add_body_params('PostStart', PostStart)