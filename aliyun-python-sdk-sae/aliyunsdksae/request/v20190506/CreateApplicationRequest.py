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
from aliyunsdksae.endpoint import endpoint_data

class CreateApplicationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'sae', '2019-05-06', 'CreateApplication','serverless')
		self.set_uri_pattern('/pop/v1/sam/app/createApplication')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NasId(self):
		return self.get_query_params().get('NasId')

	def set_NasId(self,NasId):
		self.add_query_param('NasId',NasId)

	def get_JarStartArgs(self):
		return self.get_query_params().get('JarStartArgs')

	def set_JarStartArgs(self,JarStartArgs):
		self.add_query_param('JarStartArgs',JarStartArgs)

	def get_OssAkSecret(self):
		return self.get_body_params().get('OssAkSecret')

	def set_OssAkSecret(self,OssAkSecret):
		self.add_body_params('OssAkSecret', OssAkSecret)

	def get_MountHost(self):
		return self.get_query_params().get('MountHost')

	def set_MountHost(self,MountHost):
		self.add_query_param('MountHost',MountHost)

	def get_AutoConfig(self):
		return self.get_query_params().get('AutoConfig')

	def set_AutoConfig(self,AutoConfig):
		self.add_query_param('AutoConfig',AutoConfig)

	def get_Envs(self):
		return self.get_query_params().get('Envs')

	def set_Envs(self,Envs):
		self.add_query_param('Envs',Envs)

	def get_PhpArmsConfigLocation(self):
		return self.get_query_params().get('PhpArmsConfigLocation')

	def set_PhpArmsConfigLocation(self,PhpArmsConfigLocation):
		self.add_query_param('PhpArmsConfigLocation',PhpArmsConfigLocation)

	def get_CustomHostAlias(self):
		return self.get_query_params().get('CustomHostAlias')

	def set_CustomHostAlias(self,CustomHostAlias):
		self.add_query_param('CustomHostAlias',CustomHostAlias)

	def get_Deploy(self):
		return self.get_query_params().get('Deploy')

	def set_Deploy(self,Deploy):
		self.add_query_param('Deploy',Deploy)

	def get_JarStartOptions(self):
		return self.get_query_params().get('JarStartOptions')

	def set_JarStartOptions(self,JarStartOptions):
		self.add_query_param('JarStartOptions',JarStartOptions)

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_NamespaceId(self):
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self,NamespaceId):
		self.add_query_param('NamespaceId',NamespaceId)

	def get_ConfigMapMountDesc(self):
		return self.get_body_params().get('ConfigMapMountDesc')

	def set_ConfigMapMountDesc(self,ConfigMapMountDesc):
		self.add_body_params('ConfigMapMountDesc', ConfigMapMountDesc)

	def get_OssMountDescs(self):
		return self.get_body_params().get('OssMountDescs')

	def set_OssMountDescs(self,OssMountDescs):
		self.add_body_params('OssMountDescs', OssMountDescs)

	def get_PreStop(self):
		return self.get_query_params().get('PreStop')

	def set_PreStop(self,PreStop):
		self.add_query_param('PreStop',PreStop)

	def get_Cpu(self):
		return self.get_query_params().get('Cpu')

	def set_Cpu(self,Cpu):
		self.add_query_param('Cpu',Cpu)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PackageType(self):
		return self.get_query_params().get('PackageType')

	def set_PackageType(self,PackageType):
		self.add_query_param('PackageType',PackageType)

	def get_PostStart(self):
		return self.get_query_params().get('PostStart')

	def set_PostStart(self,PostStart):
		self.add_query_param('PostStart',PostStart)

	def get_AssociateEip(self):
		return self.get_body_params().get('AssociateEip')

	def set_AssociateEip(self,AssociateEip):
		self.add_body_params('AssociateEip', AssociateEip)

	def get_WebContainer(self):
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self,WebContainer):
		self.add_query_param('WebContainer',WebContainer)

	def get_Memory(self):
		return self.get_query_params().get('Memory')

	def set_Memory(self,Memory):
		self.add_query_param('Memory',Memory)

	def get_SlsConfigs(self):
		return self.get_query_params().get('SlsConfigs')

	def set_SlsConfigs(self,SlsConfigs):
		self.add_query_param('SlsConfigs',SlsConfigs)

	def get_CommandArgs(self):
		return self.get_query_params().get('CommandArgs')

	def set_CommandArgs(self,CommandArgs):
		self.add_query_param('CommandArgs',CommandArgs)

	def get_AcrAssumeRoleArn(self):
		return self.get_query_params().get('AcrAssumeRoleArn')

	def set_AcrAssumeRoleArn(self,AcrAssumeRoleArn):
		self.add_query_param('AcrAssumeRoleArn',AcrAssumeRoleArn)

	def get_Readiness(self):
		return self.get_query_params().get('Readiness')

	def set_Readiness(self,Readiness):
		self.add_query_param('Readiness',Readiness)

	def get_Timezone(self):
		return self.get_query_params().get('Timezone')

	def set_Timezone(self,Timezone):
		self.add_query_param('Timezone',Timezone)

	def get_OssAkId(self):
		return self.get_body_params().get('OssAkId')

	def set_OssAkId(self,OssAkId):
		self.add_body_params('OssAkId', OssAkId)

	def get_Liveness(self):
		return self.get_query_params().get('Liveness')

	def set_Liveness(self,Liveness):
		self.add_query_param('Liveness',Liveness)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_PackageVersion(self):
		return self.get_query_params().get('PackageVersion')

	def set_PackageVersion(self,PackageVersion):
		self.add_query_param('PackageVersion',PackageVersion)

	def get_TomcatConfig(self):
		return self.get_query_params().get('TomcatConfig')

	def set_TomcatConfig(self,TomcatConfig):
		self.add_query_param('TomcatConfig',TomcatConfig)

	def get_WarStartOptions(self):
		return self.get_query_params().get('WarStartOptions')

	def set_WarStartOptions(self,WarStartOptions):
		self.add_query_param('WarStartOptions',WarStartOptions)

	def get_EdasContainerVersion(self):
		return self.get_query_params().get('EdasContainerVersion')

	def set_EdasContainerVersion(self,EdasContainerVersion):
		self.add_query_param('EdasContainerVersion',EdasContainerVersion)

	def get_PackageUrl(self):
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self,PackageUrl):
		self.add_query_param('PackageUrl',PackageUrl)

	def get_TerminationGracePeriodSeconds(self):
		return self.get_query_params().get('TerminationGracePeriodSeconds')

	def set_TerminationGracePeriodSeconds(self,TerminationGracePeriodSeconds):
		self.add_query_param('TerminationGracePeriodSeconds',TerminationGracePeriodSeconds)

	def get_PhpConfig(self):
		return self.get_body_params().get('PhpConfig')

	def set_PhpConfig(self,PhpConfig):
		self.add_body_params('PhpConfig', PhpConfig)

	def get_Replicas(self):
		return self.get_query_params().get('Replicas')

	def set_Replicas(self,Replicas):
		self.add_query_param('Replicas',Replicas)

	def get_Command(self):
		return self.get_query_params().get('Command')

	def set_Command(self,Command):
		self.add_query_param('Command',Command)

	def get_MountDesc(self):
		return self.get_query_params().get('MountDesc')

	def set_MountDesc(self,MountDesc):
		self.add_query_param('MountDesc',MountDesc)

	def get_Jdk(self):
		return self.get_query_params().get('Jdk')

	def set_Jdk(self,Jdk):
		self.add_query_param('Jdk',Jdk)

	def get_AppDescription(self):
		return self.get_query_params().get('AppDescription')

	def set_AppDescription(self,AppDescription):
		self.add_query_param('AppDescription',AppDescription)

	def get_AcrInstanceId(self):
		return self.get_body_params().get('AcrInstanceId')

	def set_AcrInstanceId(self,AcrInstanceId):
		self.add_body_params('AcrInstanceId', AcrInstanceId)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_ImageUrl(self):
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_query_param('ImageUrl',ImageUrl)

	def get_PhpConfigLocation(self):
		return self.get_query_params().get('PhpConfigLocation')

	def set_PhpConfigLocation(self,PhpConfigLocation):
		self.add_query_param('PhpConfigLocation',PhpConfigLocation)