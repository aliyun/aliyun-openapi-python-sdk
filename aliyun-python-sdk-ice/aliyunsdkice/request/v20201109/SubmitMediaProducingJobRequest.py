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
from aliyunsdkice.endpoint import endpoint_data

class SubmitMediaProducingJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'SubmitMediaProducingJob','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_OutputMediaTarget(self): # String
		return self.get_query_params().get('OutputMediaTarget')

	def set_OutputMediaTarget(self, OutputMediaTarget):  # String
		self.add_query_param('OutputMediaTarget', OutputMediaTarget)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_EditingProduceConfig(self): # String
		return self.get_query_params().get('EditingProduceConfig')

	def set_EditingProduceConfig(self, EditingProduceConfig):  # String
		self.add_query_param('EditingProduceConfig', EditingProduceConfig)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_OutputMediaConfig(self): # String
		return self.get_query_params().get('OutputMediaConfig')

	def set_OutputMediaConfig(self, OutputMediaConfig):  # String
		self.add_query_param('OutputMediaConfig', OutputMediaConfig)
	def get_ProjectId(self): # String
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # String
		self.add_query_param('ProjectId', ProjectId)
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_Timeline(self): # String
		return self.get_query_params().get('Timeline')

	def set_Timeline(self, Timeline):  # String
		self.add_query_param('Timeline', Timeline)
	def get_ProjectMetadata(self): # String
		return self.get_query_params().get('ProjectMetadata')

	def set_ProjectMetadata(self, ProjectMetadata):  # String
		self.add_query_param('ProjectMetadata', ProjectMetadata)
	def get_ClipsParam(self): # String
		return self.get_query_params().get('ClipsParam')

	def set_ClipsParam(self, ClipsParam):  # String
		self.add_query_param('ClipsParam', ClipsParam)
