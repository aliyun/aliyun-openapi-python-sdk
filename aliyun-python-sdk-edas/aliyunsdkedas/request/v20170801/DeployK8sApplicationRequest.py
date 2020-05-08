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
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'DeployK8sApplication','edas')
		self.set_uri_pattern('/pop/v5/k8s/acs/k8s_apps')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NasId(self):
		return self.get_query_params().get('NasId')

	def set_NasId(self,NasId):
		self.add_query_param('NasId',NasId)

	def get_WebContainer(self):
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self,WebContainer):
		self.add_query_param('WebContainer',WebContainer)

	def get_Readiness(self):
		return self.get_query_params().get('Readiness')

	def set_Readiness(self,Readiness):
		self.add_query_param('Readiness',Readiness)

	def get_PackageVersionId(self):
		return self.get_query_params().get('PackageVersionId')

	def set_PackageVersionId(self,PackageVersionId):
		self.add_query_param('PackageVersionId',PackageVersionId)

	def get_BatchWaitTime(self):
		return self.get_query_params().get('BatchWaitTime')

	def set_BatchWaitTime(self,BatchWaitTime):
		self.add_query_param('BatchWaitTime',BatchWaitTime)

	def get_Liveness(self):
		return self.get_query_params().get('Liveness')

	def set_Liveness(self,Liveness):
		self.add_query_param('Liveness',Liveness)

	def get_Envs(self):
		return self.get_query_params().get('Envs')

	def set_Envs(self,Envs):
		self.add_query_param('Envs',Envs)

	def get_CpuLimit(self):
		return self.get_query_params().get('CpuLimit')

	def set_CpuLimit(self,CpuLimit):
		self.add_query_param('CpuLimit',CpuLimit)

	def get_PackageVersion(self):
		return self.get_query_params().get('PackageVersion')

	def set_PackageVersion(self,PackageVersion):
		self.add_query_param('PackageVersion',PackageVersion)

	def get_StorageType(self):
		return self.get_query_params().get('StorageType')

	def set_StorageType(self,StorageType):
		self.add_query_param('StorageType',StorageType)

	def get_EdasContainerVersion(self):
		return self.get_query_params().get('EdasContainerVersion')

	def set_EdasContainerVersion(self,EdasContainerVersion):
		self.add_query_param('EdasContainerVersion',EdasContainerVersion)

	def get_PackageUrl(self):
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self,PackageUrl):
		self.add_query_param('PackageUrl',PackageUrl)

	def get_MemoryLimit(self):
		return self.get_query_params().get('MemoryLimit')

	def set_MemoryLimit(self,MemoryLimit):
		self.add_query_param('MemoryLimit',MemoryLimit)

	def get_ImageTag(self):
		return self.get_query_params().get('ImageTag')

	def set_ImageTag(self,ImageTag):
		self.add_query_param('ImageTag',ImageTag)

	def get_MemoryRequest(self):
		return self.get_query_params().get('MemoryRequest')

	def set_MemoryRequest(self,MemoryRequest):
		self.add_query_param('MemoryRequest',MemoryRequest)

	def get_Image(self):
		return self.get_query_params().get('Image')

	def set_Image(self,Image):
		self.add_query_param('Image',Image)

	def get_PreStop(self):
		return self.get_query_params().get('PreStop')

	def set_PreStop(self,PreStop):
		self.add_query_param('PreStop',PreStop)

	def get_MountDescs(self):
		return self.get_query_params().get('MountDescs')

	def set_MountDescs(self,MountDescs):
		self.add_query_param('MountDescs',MountDescs)

	def get_Replicas(self):
		return self.get_query_params().get('Replicas')

	def set_Replicas(self,Replicas):
		self.add_query_param('Replicas',Replicas)

	def get_CpuRequest(self):
		return self.get_query_params().get('CpuRequest')

	def set_CpuRequest(self,CpuRequest):
		self.add_query_param('CpuRequest',CpuRequest)

	def get_LocalVolume(self):
		return self.get_query_params().get('LocalVolume')

	def set_LocalVolume(self,LocalVolume):
		self.add_query_param('LocalVolume',LocalVolume)

	def get_Command(self):
		return self.get_query_params().get('Command')

	def set_Command(self,Command):
		self.add_query_param('Command',Command)

	def get_UpdateStrategy(self):
		return self.get_query_params().get('UpdateStrategy')

	def set_UpdateStrategy(self,UpdateStrategy):
		self.add_query_param('UpdateStrategy',UpdateStrategy)

	def get_Args(self):
		return self.get_query_params().get('Args')

	def set_Args(self,Args):
		self.add_query_param('Args',Args)

	def get_JDK(self):
		return self.get_query_params().get('JDK')

	def set_JDK(self,JDK):
		self.add_query_param('JDK',JDK)

	def get_UseBodyEncoding(self):
		return self.get_query_params().get('UseBodyEncoding')

	def set_UseBodyEncoding(self,UseBodyEncoding):
		self.add_query_param('UseBodyEncoding',UseBodyEncoding)

	def get_ChangeOrderDesc(self):
		return self.get_query_params().get('ChangeOrderDesc')

	def set_ChangeOrderDesc(self,ChangeOrderDesc):
		self.add_query_param('ChangeOrderDesc',ChangeOrderDesc)

	def get_UriEncoding(self):
		return self.get_query_params().get('UriEncoding')

	def set_UriEncoding(self,UriEncoding):
		self.add_query_param('UriEncoding',UriEncoding)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_McpuRequest(self):
		return self.get_query_params().get('McpuRequest')

	def set_McpuRequest(self,McpuRequest):
		self.add_query_param('McpuRequest',McpuRequest)

	def get_McpuLimit(self):
		return self.get_query_params().get('McpuLimit')

	def set_McpuLimit(self,McpuLimit):
		self.add_query_param('McpuLimit',McpuLimit)

	def get_VolumesStr(self):
		return self.get_query_params().get('VolumesStr')

	def set_VolumesStr(self,VolumesStr):
		self.add_query_param('VolumesStr',VolumesStr)

	def get_PostStart(self):
		return self.get_query_params().get('PostStart')

	def set_PostStart(self,PostStart):
		self.add_query_param('PostStart',PostStart)