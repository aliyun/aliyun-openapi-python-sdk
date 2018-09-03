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
class DeployK8sApplicationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'DeployK8sApplication')
		self.set_uri_pattern('/pop/v5/k8s/acs/k8s_apps')
		self.set_method('POST')

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

	def get_Readiness(self):
		return self.get_query_params().get('Readiness')

	def set_Readiness(self,Readiness):
		self.add_query_param('Readiness',Readiness)

	def get_Replicas(self):
		return self.get_query_params().get('Replicas')

	def set_Replicas(self,Replicas):
		self.add_query_param('Replicas',Replicas)

	def get_BatchWaitTime(self):
		return self.get_query_params().get('BatchWaitTime')

	def set_BatchWaitTime(self,BatchWaitTime):
		self.add_query_param('BatchWaitTime',BatchWaitTime)

	def get_Liveness(self):
		return self.get_query_params().get('Liveness')

	def set_Liveness(self,Liveness):
		self.add_query_param('Liveness',Liveness)

	def get_CpuRequest(self):
		return self.get_query_params().get('CpuRequest')

	def set_CpuRequest(self,CpuRequest):
		self.add_query_param('CpuRequest',CpuRequest)

	def get_Envs(self):
		return self.get_query_params().get('Envs')

	def set_Envs(self,Envs):
		self.add_query_param('Envs',Envs)

	def get_CpuLimit(self):
		return self.get_query_params().get('CpuLimit')

	def set_CpuLimit(self,CpuLimit):
		self.add_query_param('CpuLimit',CpuLimit)

	def get_Command(self):
		return self.get_query_params().get('Command')

	def set_Command(self,Command):
		self.add_query_param('Command',Command)

	def get_Args(self):
		return self.get_query_params().get('Args')

	def set_Args(self,Args):
		self.add_query_param('Args',Args)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_MemoryLimit(self):
		return self.get_query_params().get('MemoryLimit')

	def set_MemoryLimit(self,MemoryLimit):
		self.add_query_param('MemoryLimit',MemoryLimit)

	def get_ImageTag(self):
		return self.get_query_params().get('ImageTag')

	def set_ImageTag(self,ImageTag):
		self.add_query_param('ImageTag',ImageTag)

	def get_PostStart(self):
		return self.get_query_params().get('PostStart')

	def set_PostStart(self,PostStart):
		self.add_query_param('PostStart',PostStart)