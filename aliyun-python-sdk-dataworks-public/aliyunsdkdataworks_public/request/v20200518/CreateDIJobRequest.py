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

class CreateDIJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateDIJob')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SourceDataSourceType(self): # String
		return self.get_body_params().get('SourceDataSourceType')

	def set_SourceDataSourceType(self, SourceDataSourceType):  # String
		self.add_body_params('SourceDataSourceType', SourceDataSourceType)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_TransformationRules(self): # String
		return self.get_body_params().get('TransformationRules')

	def set_TransformationRules(self, TransformationRules):  # String
		self.add_body_params('TransformationRules', TransformationRules)
	def get_DestinationDataSourceType(self): # String
		return self.get_body_params().get('DestinationDataSourceType')

	def set_DestinationDataSourceType(self, DestinationDataSourceType):  # String
		self.add_body_params('DestinationDataSourceType', DestinationDataSourceType)
	def get_DestinationDataSourceSettings(self): # String
		return self.get_body_params().get('DestinationDataSourceSettings')

	def set_DestinationDataSourceSettings(self, DestinationDataSourceSettings):  # String
		self.add_body_params('DestinationDataSourceSettings', DestinationDataSourceSettings)
	def get_SourceDataSourceSettings(self): # String
		return self.get_body_params().get('SourceDataSourceSettings')

	def set_SourceDataSourceSettings(self, SourceDataSourceSettings):  # String
		self.add_body_params('SourceDataSourceSettings', SourceDataSourceSettings)
	def get_ResourceSettings(self): # String
		return self.get_body_params().get('ResourceSettings')

	def set_ResourceSettings(self, ResourceSettings):  # String
		self.add_body_params('ResourceSettings', ResourceSettings)
	def get_MigrationType(self): # String
		return self.get_body_params().get('MigrationType')

	def set_MigrationType(self, MigrationType):  # String
		self.add_body_params('MigrationType', MigrationType)
	def get_SystemDebug(self): # String
		return self.get_query_params().get('SystemDebug')

	def set_SystemDebug(self, SystemDebug):  # String
		self.add_query_param('SystemDebug', SystemDebug)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
	def get_JobName(self): # String
		return self.get_body_params().get('JobName')

	def set_JobName(self, JobName):  # String
		self.add_body_params('JobName', JobName)
	def get_TableMappings(self): # String
		return self.get_body_params().get('TableMappings')

	def set_TableMappings(self, TableMappings):  # String
		self.add_body_params('TableMappings', TableMappings)
	def get_JobSettings(self): # String
		return self.get_body_params().get('JobSettings')

	def set_JobSettings(self, JobSettings):  # String
		self.add_body_params('JobSettings', JobSettings)
