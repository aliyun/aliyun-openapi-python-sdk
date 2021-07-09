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

	def get_PipelineName(self): # String
		return self.get_body_params().get('PipelineName')

	def set_PipelineName(self, PipelineName):  # String
		self.add_body_params('PipelineName', PipelineName)
	def get_ResultStatusList(self): # String
		return self.get_body_params().get('ResultStatusList')

	def set_ResultStatusList(self, ResultStatusList):  # String
		self.add_body_params('ResultStatusList', ResultStatusList)
	def get_Creators(self): # String
		return self.get_body_params().get('Creators')

	def set_Creators(self, Creators):  # String
		self.add_body_params('Creators', Creators)
	def get_ExecuteEndTime(self): # String
		return self.get_body_params().get('ExecuteEndTime')

	def set_ExecuteEndTime(self, ExecuteEndTime):  # String
		self.add_body_params('ExecuteEndTime', ExecuteEndTime)
	def get_UserPk(self): # String
		return self.get_body_params().get('UserPk')

	def set_UserPk(self, UserPk):  # String
		self.add_body_params('UserPk', UserPk)
	def get_OrgId(self): # String
		return self.get_query_params().get('OrgId')

	def set_OrgId(self, OrgId):  # String
		self.add_query_param('OrgId', OrgId)
	def get_CreateStartTime(self): # String
		return self.get_body_params().get('CreateStartTime')

	def set_CreateStartTime(self, CreateStartTime):  # String
		self.add_body_params('CreateStartTime', CreateStartTime)
	def get_Operators(self): # String
		return self.get_body_params().get('Operators')

	def set_Operators(self, Operators):  # String
		self.add_body_params('Operators', Operators)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_ExecuteStartTime(self): # String
		return self.get_body_params().get('ExecuteStartTime')

	def set_ExecuteStartTime(self, ExecuteStartTime):  # String
		self.add_body_params('ExecuteStartTime', ExecuteStartTime)
	def get_PageStart(self): # Integer
		return self.get_body_params().get('PageStart')

	def set_PageStart(self, PageStart):  # Integer
		self.add_body_params('PageStart', PageStart)
	def get_CreateEndTime(self): # String
		return self.get_body_params().get('CreateEndTime')

	def set_CreateEndTime(self, CreateEndTime):  # String
		self.add_body_params('CreateEndTime', CreateEndTime)
