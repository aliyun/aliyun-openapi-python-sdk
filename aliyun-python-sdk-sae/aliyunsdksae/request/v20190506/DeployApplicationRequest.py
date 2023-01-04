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

class DeployApplicationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'sae', '2019-05-06', 'DeployApplication','serverless')
		self.set_uri_pattern('/pop/v1/sam/app/deployApplication')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NasId(self): # String
		return self.get_query_params().get('NasId')

	def set_NasId(self, NasId):  # String
		self.add_query_param('NasId', NasId)
	def get_JarStartArgs(self): # String
		return self.get_query_params().get('JarStartArgs')

	def set_JarStartArgs(self, JarStartArgs):  # String
		self.add_query_param('JarStartArgs', JarStartArgs)
	def get_OssAkSecret(self): # String
		return self.get_body_params().get('OssAkSecret')

	def set_OssAkSecret(self, OssAkSecret):  # String
		self.add_body_params('OssAkSecret', OssAkSecret)
	def get_NasConfigs(self): # String
		return self.get_query_params().get('NasConfigs')

	def set_NasConfigs(self, NasConfigs):  # String
		self.add_query_param('NasConfigs', NasConfigs)
	def get_MountHost(self): # String
		return self.get_query_params().get('MountHost')

	def set_MountHost(self, MountHost):  # String
		self.add_query_param('MountHost', MountHost)
	def get_BatchWaitTime(self): # Integer
		return self.get_query_params().get('BatchWaitTime')

	def set_BatchWaitTime(self, BatchWaitTime):  # Integer
		self.add_query_param('BatchWaitTime', BatchWaitTime)
	def get_Envs(self): # String
		return self.get_query_params().get('Envs')

	def set_Envs(self, Envs):  # String
		self.add_query_param('Envs', Envs)
	def get_PhpArmsConfigLocation(self): # String
		return self.get_query_params().get('PhpArmsConfigLocation')

	def set_PhpArmsConfigLocation(self, PhpArmsConfigLocation):  # String
		self.add_query_param('PhpArmsConfigLocation', PhpArmsConfigLocation)
	def get_CustomHostAlias(self): # String
		return self.get_query_params().get('CustomHostAlias')

	def set_CustomHostAlias(self, CustomHostAlias):  # String
		self.add_query_param('CustomHostAlias', CustomHostAlias)
	def get_Deploy(self): # String
		return self.get_query_params().get('Deploy')

	def set_Deploy(self, Deploy):  # String
		self.add_query_param('Deploy', Deploy)
	def get_JarStartOptions(self): # String
		return self.get_query_params().get('JarStartOptions')

	def set_JarStartOptions(self, JarStartOptions):  # String
		self.add_query_param('JarStartOptions', JarStartOptions)
	def get_PvtzDiscoverySvc(self): # String
		return self.get_query_params().get('PvtzDiscoverySvc')

	def set_PvtzDiscoverySvc(self, PvtzDiscoverySvc):  # String
		self.add_query_param('PvtzDiscoverySvc', PvtzDiscoverySvc)
	def get_ConfigMapMountDesc(self): # String
		return self.get_body_params().get('ConfigMapMountDesc')

	def set_ConfigMapMountDesc(self, ConfigMapMountDesc):  # String
		self.add_body_params('ConfigMapMountDesc', ConfigMapMountDesc)
	def get_OssMountDescs(self): # String
		return self.get_body_params().get('OssMountDescs')

	def set_OssMountDescs(self, OssMountDescs):  # String
		self.add_body_params('OssMountDescs', OssMountDescs)
	def get_ImagePullSecrets(self): # String
		return self.get_query_params().get('ImagePullSecrets')

	def set_ImagePullSecrets(self, ImagePullSecrets):  # String
		self.add_query_param('ImagePullSecrets', ImagePullSecrets)
	def get_PreStop(self): # String
		return self.get_query_params().get('PreStop')

	def set_PreStop(self, PreStop):  # String
		self.add_query_param('PreStop', PreStop)
	def get_Python(self): # String
		return self.get_query_params().get('Python')

	def set_Python(self, Python):  # String
		self.add_query_param('Python', Python)
	def get_UpdateStrategy(self): # String
		return self.get_query_params().get('UpdateStrategy')

	def set_UpdateStrategy(self, UpdateStrategy):  # String
		self.add_query_param('UpdateStrategy', UpdateStrategy)
	def get_ChangeOrderDesc(self): # String
		return self.get_query_params().get('ChangeOrderDesc')

	def set_ChangeOrderDesc(self, ChangeOrderDesc):  # String
		self.add_query_param('ChangeOrderDesc', ChangeOrderDesc)
	def get_MinReadyInstanceRatio(self): # Integer
		return self.get_query_params().get('MinReadyInstanceRatio')

	def set_MinReadyInstanceRatio(self, MinReadyInstanceRatio):  # Integer
		self.add_query_param('MinReadyInstanceRatio', MinReadyInstanceRatio)
	def get_AutoEnableApplicationScalingRule(self): # Boolean
		return self.get_query_params().get('AutoEnableApplicationScalingRule')

	def set_AutoEnableApplicationScalingRule(self, AutoEnableApplicationScalingRule):  # Boolean
		self.add_query_param('AutoEnableApplicationScalingRule', AutoEnableApplicationScalingRule)
	def get_PackageType(self): # String
		return self.get_query_params().get('PackageType')

	def set_PackageType(self, PackageType):  # String
		self.add_query_param('PackageType', PackageType)
	def get_PostStart(self): # String
		return self.get_query_params().get('PostStart')

	def set_PostStart(self, PostStart):  # String
		self.add_query_param('PostStart', PostStart)
	def get_AssociateEip(self): # Boolean
		return self.get_body_params().get('AssociateEip')

	def set_AssociateEip(self, AssociateEip):  # Boolean
		self.add_body_params('AssociateEip', AssociateEip)
	def get_WebContainer(self): # String
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self, WebContainer):  # String
		self.add_query_param('WebContainer', WebContainer)
	def get_EnableAhas(self): # String
		return self.get_query_params().get('EnableAhas')

	def set_EnableAhas(self, EnableAhas):  # String
		self.add_query_param('EnableAhas', EnableAhas)
	def get_SlsConfigs(self): # String
		return self.get_query_params().get('SlsConfigs')

	def set_SlsConfigs(self, SlsConfigs):  # String
		self.add_query_param('SlsConfigs', SlsConfigs)
	def get_KafkaConfigs(self): # String
		return self.get_query_params().get('KafkaConfigs')

	def set_KafkaConfigs(self, KafkaConfigs):  # String
		self.add_query_param('KafkaConfigs', KafkaConfigs)
	def get_CommandArgs(self): # String
		return self.get_query_params().get('CommandArgs')

	def set_CommandArgs(self, CommandArgs):  # String
		self.add_query_param('CommandArgs', CommandArgs)
	def get_AcrAssumeRoleArn(self): # String
		return self.get_query_params().get('AcrAssumeRoleArn')

	def set_AcrAssumeRoleArn(self, AcrAssumeRoleArn):  # String
		self.add_query_param('AcrAssumeRoleArn', AcrAssumeRoleArn)
	def get_Readiness(self): # String
		return self.get_query_params().get('Readiness')

	def set_Readiness(self, Readiness):  # String
		self.add_query_param('Readiness', Readiness)
	def get_Timezone(self): # String
		return self.get_query_params().get('Timezone')

	def set_Timezone(self, Timezone):  # String
		self.add_query_param('Timezone', Timezone)
	def get_OssAkId(self): # String
		return self.get_body_params().get('OssAkId')

	def set_OssAkId(self, OssAkId):  # String
		self.add_body_params('OssAkId', OssAkId)
	def get_Liveness(self): # String
		return self.get_query_params().get('Liveness')

	def set_Liveness(self, Liveness):  # String
		self.add_query_param('Liveness', Liveness)
	def get_PackageVersion(self): # String
		return self.get_query_params().get('PackageVersion')

	def set_PackageVersion(self, PackageVersion):  # String
		self.add_query_param('PackageVersion', PackageVersion)
	def get_TomcatConfig(self): # String
		return self.get_query_params().get('TomcatConfig')

	def set_TomcatConfig(self, TomcatConfig):  # String
		self.add_query_param('TomcatConfig', TomcatConfig)
	def get_WarStartOptions(self): # String
		return self.get_query_params().get('WarStartOptions')

	def set_WarStartOptions(self, WarStartOptions):  # String
		self.add_query_param('WarStartOptions', WarStartOptions)
	def get_EdasContainerVersion(self): # String
		return self.get_query_params().get('EdasContainerVersion')

	def set_EdasContainerVersion(self, EdasContainerVersion):  # String
		self.add_query_param('EdasContainerVersion', EdasContainerVersion)
	def get_PackageUrl(self): # String
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self, PackageUrl):  # String
		self.add_query_param('PackageUrl', PackageUrl)
	def get_TerminationGracePeriodSeconds(self): # Integer
		return self.get_query_params().get('TerminationGracePeriodSeconds')

	def set_TerminationGracePeriodSeconds(self, TerminationGracePeriodSeconds):  # Integer
		self.add_query_param('TerminationGracePeriodSeconds', TerminationGracePeriodSeconds)
	def get_PhpConfig(self): # String
		return self.get_body_params().get('PhpConfig')

	def set_PhpConfig(self, PhpConfig):  # String
		self.add_body_params('PhpConfig', PhpConfig)
	def get_MicroRegistration(self): # String
		return self.get_query_params().get('MicroRegistration')

	def set_MicroRegistration(self, MicroRegistration):  # String
		self.add_query_param('MicroRegistration', MicroRegistration)
	def get_EnableGreyTagRoute(self): # Boolean
		return self.get_query_params().get('EnableGreyTagRoute')

	def set_EnableGreyTagRoute(self, EnableGreyTagRoute):  # Boolean
		self.add_query_param('EnableGreyTagRoute', EnableGreyTagRoute)
	def get_Command(self): # String
		return self.get_query_params().get('Command')

	def set_Command(self, Command):  # String
		self.add_query_param('Command', Command)
	def get_MountDesc(self): # String
		return self.get_query_params().get('MountDesc')

	def set_MountDesc(self, MountDesc):  # String
		self.add_query_param('MountDesc', MountDesc)
	def get_Jdk(self): # String
		return self.get_query_params().get('Jdk')

	def set_Jdk(self, Jdk):  # String
		self.add_query_param('Jdk', Jdk)
	def get_MinReadyInstances(self): # Integer
		return self.get_query_params().get('MinReadyInstances')

	def set_MinReadyInstances(self, MinReadyInstances):  # Integer
		self.add_query_param('MinReadyInstances', MinReadyInstances)
	def get_AcrInstanceId(self): # String
		return self.get_body_params().get('AcrInstanceId')

	def set_AcrInstanceId(self, AcrInstanceId):  # String
		self.add_body_params('AcrInstanceId', AcrInstanceId)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_ImageUrl(self): # String
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self, ImageUrl):  # String
		self.add_query_param('ImageUrl', ImageUrl)
	def get_PythonModules(self): # String
		return self.get_query_params().get('PythonModules')

	def set_PythonModules(self, PythonModules):  # String
		self.add_query_param('PythonModules', PythonModules)
	def get_PhpConfigLocation(self): # String
		return self.get_query_params().get('PhpConfigLocation')

	def set_PhpConfigLocation(self, PhpConfigLocation):  # String
		self.add_query_param('PhpConfigLocation', PhpConfigLocation)
