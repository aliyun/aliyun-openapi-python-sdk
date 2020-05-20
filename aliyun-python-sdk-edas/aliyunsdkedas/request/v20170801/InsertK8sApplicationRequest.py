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


	def get_NasId(self):
		return self.get_query_params().get('NasId')

	def set_NasId(self,NasId):
		self.add_query_param('NasId',NasId)

	def get_RepoId(self):
		return self.get_query_params().get('RepoId')

	def set_RepoId(self,RepoId):
		self.add_query_param('RepoId',RepoId)

	def get_InternetTargetPort(self):
		return self.get_query_params().get('InternetTargetPort')

	def set_InternetTargetPort(self,InternetTargetPort):
		self.add_query_param('InternetTargetPort',InternetTargetPort)

	def get_WebContainer(self):
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self,WebContainer):
		self.add_query_param('WebContainer',WebContainer)

	def get_IntranetSlbId(self):
		return self.get_query_params().get('IntranetSlbId')

	def set_IntranetSlbId(self,IntranetSlbId):
		self.add_query_param('IntranetSlbId',IntranetSlbId)

	def get_CommandArgs(self):
		return self.get_query_params().get('CommandArgs')

	def set_CommandArgs(self,CommandArgs):
		self.add_query_param('CommandArgs',CommandArgs)

	def get_Readiness(self):
		return self.get_query_params().get('Readiness')

	def set_Readiness(self,Readiness):
		self.add_query_param('Readiness',Readiness)

	def get_Liveness(self):
		return self.get_query_params().get('Liveness')

	def set_Liveness(self,Liveness):
		self.add_query_param('Liveness',Liveness)

	def get_InternetSlbPort(self):
		return self.get_query_params().get('InternetSlbPort')

	def set_InternetSlbPort(self,InternetSlbPort):
		self.add_query_param('InternetSlbPort',InternetSlbPort)

	def get_Envs(self):
		return self.get_query_params().get('Envs')

	def set_Envs(self,Envs):
		self.add_query_param('Envs',Envs)

	def get_RequestsMem(self):
		return self.get_query_params().get('RequestsMem')

	def set_RequestsMem(self,RequestsMem):
		self.add_query_param('RequestsMem',RequestsMem)

	def get_PackageVersion(self):
		return self.get_query_params().get('PackageVersion')

	def set_PackageVersion(self,PackageVersion):
		self.add_query_param('PackageVersion',PackageVersion)

	def get_StorageType(self):
		return self.get_query_params().get('StorageType')

	def set_StorageType(self,StorageType):
		self.add_query_param('StorageType',StorageType)

	def get_LimitMem(self):
		return self.get_query_params().get('LimitMem')

	def set_LimitMem(self,LimitMem):
		self.add_query_param('LimitMem',LimitMem)

	def get_LimitmCpu(self):
		return self.get_query_params().get('LimitmCpu')

	def set_LimitmCpu(self,LimitmCpu):
		self.add_query_param('LimitmCpu',LimitmCpu)

	def get_EdasContainerVersion(self):
		return self.get_query_params().get('EdasContainerVersion')

	def set_EdasContainerVersion(self,EdasContainerVersion):
		self.add_query_param('EdasContainerVersion',EdasContainerVersion)

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_InternetSlbId(self):
		return self.get_query_params().get('InternetSlbId')

	def set_InternetSlbId(self,InternetSlbId):
		self.add_query_param('InternetSlbId',InternetSlbId)

	def get_LogicalRegionId(self):
		return self.get_query_params().get('LogicalRegionId')

	def set_LogicalRegionId(self,LogicalRegionId):
		self.add_query_param('LogicalRegionId',LogicalRegionId)

	def get_PackageUrl(self):
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self,PackageUrl):
		self.add_query_param('PackageUrl',PackageUrl)

	def get_RequestsmCpu(self):
		return self.get_query_params().get('RequestsmCpu')

	def set_RequestsmCpu(self,RequestsmCpu):
		self.add_query_param('RequestsmCpu',RequestsmCpu)

	def get_DeployAcrossZones(self):
		return self.get_query_params().get('DeployAcrossZones')

	def set_DeployAcrossZones(self,DeployAcrossZones):
		self.add_query_param('DeployAcrossZones',DeployAcrossZones)

	def get_InternetSlbProtocol(self):
		return self.get_query_params().get('InternetSlbProtocol')

	def set_InternetSlbProtocol(self,InternetSlbProtocol):
		self.add_query_param('InternetSlbProtocol',InternetSlbProtocol)

	def get_IntranetSlbPort(self):
		return self.get_query_params().get('IntranetSlbPort')

	def set_IntranetSlbPort(self,IntranetSlbPort):
		self.add_query_param('IntranetSlbPort',IntranetSlbPort)

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

	def get_LimitCpu(self):
		return self.get_query_params().get('LimitCpu')

	def set_LimitCpu(self,LimitCpu):
		self.add_query_param('LimitCpu',LimitCpu)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_IntranetTargetPort(self):
		return self.get_query_params().get('IntranetTargetPort')

	def set_IntranetTargetPort(self,IntranetTargetPort):
		self.add_query_param('IntranetTargetPort',IntranetTargetPort)

	def get_LocalVolume(self):
		return self.get_query_params().get('LocalVolume')

	def set_LocalVolume(self,LocalVolume):
		self.add_query_param('LocalVolume',LocalVolume)

	def get_Command(self):
		return self.get_query_params().get('Command')

	def set_Command(self,Command):
		self.add_query_param('Command',Command)

	def get_JDK(self):
		return self.get_query_params().get('JDK')

	def set_JDK(self,JDK):
		self.add_query_param('JDK',JDK)

	def get_UseBodyEncoding(self):
		return self.get_query_params().get('UseBodyEncoding')

	def set_UseBodyEncoding(self,UseBodyEncoding):
		self.add_query_param('UseBodyEncoding',UseBodyEncoding)

	def get_UriEncoding(self):
		return self.get_query_params().get('UriEncoding')

	def set_UriEncoding(self,UriEncoding):
		self.add_query_param('UriEncoding',UriEncoding)

	def get_IntranetSlbProtocol(self):
		return self.get_query_params().get('IntranetSlbProtocol')

	def set_IntranetSlbProtocol(self,IntranetSlbProtocol):
		self.add_query_param('IntranetSlbProtocol',IntranetSlbProtocol)

	def get_ImageUrl(self):
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_query_param('ImageUrl',ImageUrl)

	def get_Namespace(self):
		return self.get_query_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_query_param('Namespace',Namespace)

	def get_ApplicationDescription(self):
		return self.get_query_params().get('ApplicationDescription')

	def set_ApplicationDescription(self,ApplicationDescription):
		self.add_query_param('ApplicationDescription',ApplicationDescription)

	def get_PackageType(self):
		return self.get_query_params().get('PackageType')

	def set_PackageType(self,PackageType):
		self.add_query_param('PackageType',PackageType)

	def get_RuntimeClassName(self):
		return self.get_query_params().get('RuntimeClassName')

	def set_RuntimeClassName(self,RuntimeClassName):
		self.add_query_param('RuntimeClassName',RuntimeClassName)

	def get_RequestsCpu(self):
		return self.get_query_params().get('RequestsCpu')

	def set_RequestsCpu(self,RequestsCpu):
		self.add_query_param('RequestsCpu',RequestsCpu)

	def get_PostStart(self):
		return self.get_query_params().get('PostStart')

	def set_PostStart(self,PostStart):
		self.add_query_param('PostStart',PostStart)