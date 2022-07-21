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
from aliyunsdkimm.endpoint import endpoint_data

class UpdateProjectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'UpdateProject','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EngineConcurrency(self): # Long
		return self.get_query_params().get('EngineConcurrency')

	def set_EngineConcurrency(self, EngineConcurrency):  # Long
		self.add_query_param('EngineConcurrency', EngineConcurrency)
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_DatasetMaxBindCount(self): # Long
		return self.get_query_params().get('DatasetMaxBindCount')

	def set_DatasetMaxBindCount(self, DatasetMaxBindCount):  # Long
		self.add_query_param('DatasetMaxBindCount', DatasetMaxBindCount)
	def get_ProjectMaxDatasetCount(self): # Long
		return self.get_query_params().get('ProjectMaxDatasetCount')

	def set_ProjectMaxDatasetCount(self, ProjectMaxDatasetCount):  # Long
		self.add_query_param('ProjectMaxDatasetCount', ProjectMaxDatasetCount)
	def get_DatasetMaxTotalFileSize(self): # Long
		return self.get_query_params().get('DatasetMaxTotalFileSize')

	def set_DatasetMaxTotalFileSize(self, DatasetMaxTotalFileSize):  # Long
		self.add_query_param('DatasetMaxTotalFileSize', DatasetMaxTotalFileSize)
	def get_ServiceRole(self): # String
		return self.get_query_params().get('ServiceRole')

	def set_ServiceRole(self, ServiceRole):  # String
		self.add_query_param('ServiceRole', ServiceRole)
	def get_ProjectQueriesPerSecond(self): # Long
		return self.get_query_params().get('ProjectQueriesPerSecond')

	def set_ProjectQueriesPerSecond(self, ProjectQueriesPerSecond):  # Long
		self.add_query_param('ProjectQueriesPerSecond', ProjectQueriesPerSecond)
	def get_DatasetMaxRelationCount(self): # Long
		return self.get_query_params().get('DatasetMaxRelationCount')

	def set_DatasetMaxRelationCount(self, DatasetMaxRelationCount):  # Long
		self.add_query_param('DatasetMaxRelationCount', DatasetMaxRelationCount)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_DatasetMaxEntityCount(self): # Long
		return self.get_query_params().get('DatasetMaxEntityCount')

	def set_DatasetMaxEntityCount(self, DatasetMaxEntityCount):  # Long
		self.add_query_param('DatasetMaxEntityCount', DatasetMaxEntityCount)
	def get_DatasetMaxFileCount(self): # Long
		return self.get_query_params().get('DatasetMaxFileCount')

	def set_DatasetMaxFileCount(self, DatasetMaxFileCount):  # Long
		self.add_query_param('DatasetMaxFileCount', DatasetMaxFileCount)
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
