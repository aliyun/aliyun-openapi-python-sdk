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

from aliyunsdkcore.request import RpcRequest

class DeployAppRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Workbench-ide', '2021-01-21', 'DeployApp')
		self.set_method('POST')

	def get_DeployStage(self):
		return self.get_query_params().get('DeployStage')

	def set_DeployStage(self,DeployStage):
		self.add_query_param('DeployStage',DeployStage)

	def get_CurrentOrgId(self):
		return self.get_query_params().get('CurrentOrgId')

	def set_CurrentOrgId(self,CurrentOrgId):
		self.add_query_param('CurrentOrgId',CurrentOrgId)

	def get_DeployMode(self):
		return self.get_query_params().get('DeployMode')

	def set_DeployMode(self,DeployMode):
		self.add_query_param('DeployMode',DeployMode)

	def get_PackageUrl(self):
		return self.get_query_params().get('PackageUrl')

	def set_PackageUrl(self,PackageUrl):
		self.add_query_param('PackageUrl',PackageUrl)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_ImageUrl(self):
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_query_param('ImageUrl',ImageUrl)

	def get_FcRoutes(self):
		return self.get_query_params().get('FcRoutes')

	def set_FcRoutes(self,FcRoutes):
		self.add_query_param('FcRoutes',FcRoutes)