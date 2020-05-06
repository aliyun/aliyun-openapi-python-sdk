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
		RoaRequest.__init__(self, 'sae', '2019-05-06', 'DeployApplication')
		self.set_uri_pattern('/pop/v1/sam/app/deployApplication')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NasId(self):
		return self.get_path_params().get('NasId')

	def set_NasId(self,NasId):
		self.add_path_param('NasId',NasId)

	def get_WebContainer(self):
		return self.get_query_params().get('WebContainer')

	def set_WebContainer(self,WebContainer):
		self.add_query_param('WebContainer',WebContainer)

	def get_JarStartArgs(self):
		return self.get_query_params().get('JarStartArgs')

	def set_JarStartArgs(self,JarStartArgs):
		self.add_query_param('JarStartArgs',JarStartArgs)

	def get_SlsConfigs(self):
		return self.get_query_params().get('SlsConfigs')

	def set_SlsConfigs(self,SlsConfigs):
		self.add_query_param('SlsConfigs',SlsConfigs)

	def get_CommandArgs(self):
		return self.get_query_params().get('CommandArgs')

	def set_CommandArgs(self,CommandArgs):
		self.add_query_param('CommandArgs',CommandArgs)

	def get_Readiness(self):
		return self.get_query_params().get('Readiness')

	def set_Readiness(self,Readiness):
		self.add_query_param('Readiness',Readiness)

	def get_Timezone(self):
		return self.get_query_params().get('Timezone')

	def set_Timezone(self,Timezone):
		self.add_query_param('Timezone',Timezone)

	def get_MountHost(self):
		return self.get_path_params().get('MountHost')

	def set_MountHost(self,MountHost):
		self.add_path_param('MountHost',MountHost)

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

	def get_PackageVersion(self):
		return self.get_query_params().get('PackageVersion')

	def set_PackageVersion(self,PackageVersion):
		self.add_query_param('PackageVersion',PackageVersion)

	def get_CustomHostAlias(self):
		return self.get_query_params().get('CustomHostAlias')

	def set_CustomHostAlias(self,CustomHostAlias):
		self.add_query_param('CustomHostAlias',CustomHostAlias)

	def get_WarStartOptions(self):
		return self.get_query_params().get('WarStartOptions')

	def set_WarStartOptions(self,WarStartOptions):
		self.add_query_param('WarStartOptions',WarStartOptions)

	def get_JarStartOptions(self):
		return self.get_query_params().get('JarStartOptions')

	def set_JarStartOptions(self,JarStartOptions):
		self.add_query_param('JarStartOptions',JarStartOptions)

	def get_EdasContainerVersion(self):
		return self.get_query_params().get('EdasContainerVersion')

	def set_EdasContainerVersion(self,EdasContainerVersion):
		self.add_query_param('EdasContainerVersion',EdasContainerVersion)

	def get_PackageUrl(self):
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self,PackageUrl):
		self.add_query_param('PackageUrl',PackageUrl)

	def get_PreStop(self):
		return self.get_query_params().get('PreStop')

	def set_PreStop(self,PreStop):
		self.add_query_param('PreStop',PreStop)

	def get_Command(self):
		return self.get_query_params().get('Command')

	def set_Command(self,Command):
		self.add_query_param('Command',Command)

	def get_UpdateStrategy(self):
		return self.get_query_params().get('UpdateStrategy')

	def set_UpdateStrategy(self,UpdateStrategy):
		self.add_query_param('UpdateStrategy',UpdateStrategy)

	def get_MountDesc(self):
		return self.get_path_params().get('MountDesc')

	def set_MountDesc(self,MountDesc):
		self.add_path_param('MountDesc',MountDesc)

	def get_Jdk(self):
		return self.get_query_params().get('Jdk')

	def set_Jdk(self,Jdk):
		self.add_query_param('Jdk',Jdk)

	def get_MinReadyInstances(self):
		return self.get_query_params().get('MinReadyInstances')

	def set_MinReadyInstances(self,MinReadyInstances):
		self.add_query_param('MinReadyInstances',MinReadyInstances)

	def get_ChangeOrderDesc(self):
		return self.get_query_params().get('ChangeOrderDesc')

	def set_ChangeOrderDesc(self,ChangeOrderDesc):
		self.add_query_param('ChangeOrderDesc',ChangeOrderDesc)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_ImageUrl(self):
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_query_param('ImageUrl',ImageUrl)

	def get_PostStart(self):
		return self.get_query_params().get('PostStart')

	def set_PostStart(self,PostStart):
		self.add_query_param('PostStart',PostStart)