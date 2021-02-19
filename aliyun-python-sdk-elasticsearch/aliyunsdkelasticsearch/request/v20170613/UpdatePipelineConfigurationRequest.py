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
from aliyunsdkelasticsearch.endpoint import endpoint_data

class UpdatePipelineConfigurationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'UpdatePipelineConfiguration','elasticsearch')
		self.set_uri_pattern('/openapi/projects/[ProjectId]/pipelines/[PipelineId]/configurations/[Id]')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Id(self):
		return self.get_path_params().get('Id')

	def set_Id(self,Id):
		self.add_path_param('Id',Id)

	def get_ProjectId(self):
		return self.get_path_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_path_param('ProjectId',ProjectId)

	def get_PipelineId(self):
		return self.get_path_params().get('PipelineId')

	def set_PipelineId(self,PipelineId):
		self.add_path_param('PipelineId',PipelineId)