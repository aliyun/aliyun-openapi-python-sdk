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

class ListPipelinesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'devops-rdc', '2020-03-03', 'ListPipelines')
		self.set_method('POST')

	def get_PipelineName(self):
		return self.get_body_params().get('PipelineName')

	def set_PipelineName(self,PipelineName):
		self.add_body_params('PipelineName', PipelineName)

	def get_ResultStatusList(self):
		return self.get_body_params().get('ResultStatusList')

	def set_ResultStatusList(self,ResultStatusList):
		self.add_body_params('ResultStatusList', ResultStatusList)

	def get_Creators(self):
		return self.get_body_params().get('Creators')

	def set_Creators(self,Creators):
		self.add_body_params('Creators', Creators)

	def get_ExecuteEndTime(self):
		return self.get_body_params().get('ExecuteEndTime')

	def set_ExecuteEndTime(self,ExecuteEndTime):
		self.add_body_params('ExecuteEndTime', ExecuteEndTime)

	def get_UserPk(self):
		return self.get_body_params().get('UserPk')

	def set_UserPk(self,UserPk):
		self.add_body_params('UserPk', UserPk)

	def get_OrgId(self):
		return self.get_query_params().get('OrgId')

	def set_OrgId(self,OrgId):
		self.add_query_param('OrgId',OrgId)

	def get_CreateStartTime(self):
		return self.get_body_params().get('CreateStartTime')

	def set_CreateStartTime(self,CreateStartTime):
		self.add_body_params('CreateStartTime', CreateStartTime)

	def get_Operators(self):
		return self.get_body_params().get('Operators')

	def set_Operators(self,Operators):
		self.add_body_params('Operators', Operators)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_ExecuteStartTime(self):
		return self.get_body_params().get('ExecuteStartTime')

	def set_ExecuteStartTime(self,ExecuteStartTime):
		self.add_body_params('ExecuteStartTime', ExecuteStartTime)

	def get_PageStart(self):
		return self.get_body_params().get('PageStart')

	def set_PageStart(self,PageStart):
		self.add_body_params('PageStart', PageStart)

	def get_CreateEndTime(self):
		return self.get_body_params().get('CreateEndTime')

	def set_CreateEndTime(self,CreateEndTime):
		self.add_body_params('CreateEndTime', CreateEndTime)