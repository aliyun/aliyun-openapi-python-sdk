# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
class InsertK8sApplicationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'InsertK8sApplication')
		self.set_uri_pattern('/pop/v5/k8s/acs/create_k8s_app')
		self.set_method('POST')

	def get_RepoId(self):
		return self.get_query_params().get('RepoId')

	def set_RepoId(self,RepoId):
		self.add_query_param('RepoId',RepoId)

	def get_InternetTargetPort(self):
		return self.get_query_params().get('InternetTargetPort')

	def set_InternetTargetPort(self,InternetTargetPort):
		self.add_query_param('InternetTargetPort',InternetTargetPort)

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

	def get_LimitMem(self):
		return self.get_query_params().get('LimitMem')

	def set_LimitMem(self,LimitMem):
		self.add_query_param('LimitMem',LimitMem)

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_InternetSlbId(self):
		return self.get_query_params().get('InternetSlbId')

	def set_InternetSlbId(self,InternetSlbId):
		self.add_query_param('InternetSlbId',InternetSlbId)

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

	def get_Command(self):
		return self.get_query_params().get('Command')

	def set_Command(self,Command):
		self.add_query_param('Command',Command)

	def get_IntranetSlbProtocol(self):
		return self.get_query_params().get('IntranetSlbProtocol')

	def set_IntranetSlbProtocol(self,IntranetSlbProtocol):
		self.add_query_param('IntranetSlbProtocol',IntranetSlbProtocol)

	def get_ImageUrl(self):
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_query_param('ImageUrl',ImageUrl)

	def get_ApplicationDescription(self):
		return self.get_query_params().get('ApplicationDescription')

	def set_ApplicationDescription(self,ApplicationDescription):
		self.add_query_param('ApplicationDescription',ApplicationDescription)

	def get_RequestsCpu(self):
		return self.get_query_params().get('RequestsCpu')

	def set_RequestsCpu(self,RequestsCpu):
		self.add_query_param('RequestsCpu',RequestsCpu)

	def get_PostStart(self):
		return self.get_query_params().get('PostStart')

	def set_PostStart(self,PostStart):
		self.add_query_param('PostStart',PostStart)