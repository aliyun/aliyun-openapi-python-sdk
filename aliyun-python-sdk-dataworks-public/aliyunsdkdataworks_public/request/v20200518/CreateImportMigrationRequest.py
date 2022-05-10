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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class CreateImportMigrationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateImportMigration')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_CommitRule(self): # String
		return self.get_body_params().get('CommitRule')

	def set_CommitRule(self, CommitRule):  # String
		self.add_body_params('CommitRule', CommitRule)
	def get_WorkspaceMap(self): # String
		return self.get_body_params().get('WorkspaceMap')

	def set_WorkspaceMap(self, WorkspaceMap):  # String
		self.add_body_params('WorkspaceMap', WorkspaceMap)
	def get_CalculateEngineMap(self): # String
		return self.get_body_params().get('CalculateEngineMap')

	def set_CalculateEngineMap(self, CalculateEngineMap):  # String
		self.add_body_params('CalculateEngineMap', CalculateEngineMap)
	def get_PackageFile(self): # String
		return self.get_body_params().get('PackageFile')

	def set_PackageFile(self, PackageFile):  # String
		self.add_body_params('PackageFile', PackageFile)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_PackageType(self): # String
		return self.get_body_params().get('PackageType')

	def set_PackageType(self, PackageType):  # String
		self.add_body_params('PackageType', PackageType)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
	def get_ResourceGroupMap(self): # String
		return self.get_body_params().get('ResourceGroupMap')

	def set_ResourceGroupMap(self, ResourceGroupMap):  # String
		self.add_body_params('ResourceGroupMap', ResourceGroupMap)
