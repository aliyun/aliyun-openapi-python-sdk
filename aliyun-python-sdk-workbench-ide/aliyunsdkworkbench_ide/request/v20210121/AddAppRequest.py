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

class AddAppRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Workbench-ide', '2021-01-21', 'AddApp')
		self.set_method('POST')

	def get_RepoUrl(self): # String
		return self.get_query_params().get('RepoUrl')

	def set_RepoUrl(self, RepoUrl):  # String
		self.add_query_param('RepoUrl', RepoUrl)
	def get_ProductId(self): # Long
		return self.get_query_params().get('ProductId')

	def set_ProductId(self, ProductId):  # Long
		self.add_query_param('ProductId', ProductId)
	def get_CurrentOrgId(self): # String
		return self.get_query_params().get('CurrentOrgId')

	def set_CurrentOrgId(self, CurrentOrgId):  # String
		self.add_query_param('CurrentOrgId', CurrentOrgId)
	def get_ComputeType(self): # String
		return self.get_query_params().get('ComputeType')

	def set_ComputeType(self, ComputeType):  # String
		self.add_query_param('ComputeType', ComputeType)
	def get_AppDescription(self): # String
		return self.get_query_params().get('AppDescription')

	def set_AppDescription(self, AppDescription):  # String
		self.add_query_param('AppDescription', AppDescription)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_WbToken(self): # String
		return self.get_query_params().get('WbToken')

	def set_WbToken(self, WbToken):  # String
		self.add_query_param('WbToken', WbToken)
	def get_SolutionId(self): # Integer
		return self.get_query_params().get('SolutionId')

	def set_SolutionId(self, SolutionId):  # Integer
		self.add_query_param('SolutionId', SolutionId)
