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

class CreateEditingProjectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'CreateEditingProject','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BusinessConfig(self): # String
		return self.get_query_params().get('BusinessConfig')

	def set_BusinessConfig(self, BusinessConfig):  # String
		self.add_query_param('BusinessConfig', BusinessConfig)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Title(self): # String
		return self.get_query_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_query_param('Title', Title)
	def get_MaterialMaps(self): # String
		return self.get_query_params().get('MaterialMaps')

	def set_MaterialMaps(self, MaterialMaps):  # String
		self.add_query_param('MaterialMaps', MaterialMaps)
	def get_CoverURL(self): # String
		return self.get_query_params().get('CoverURL')

	def set_CoverURL(self, CoverURL):  # String
		self.add_query_param('CoverURL', CoverURL)
	def get_TemplateType(self): # String
		return self.get_query_params().get('TemplateType')

	def set_TemplateType(self, TemplateType):  # String
		self.add_query_param('TemplateType', TemplateType)
	def get_ProjectType(self): # String
		return self.get_query_params().get('ProjectType')

	def set_ProjectType(self, ProjectType):  # String
		self.add_query_param('ProjectType', ProjectType)
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_Timeline(self): # String
		return self.get_query_params().get('Timeline')

	def set_Timeline(self, Timeline):  # String
		self.add_query_param('Timeline', Timeline)
	def get_ClipsParam(self): # String
		return self.get_query_params().get('ClipsParam')

	def set_ClipsParam(self, ClipsParam):  # String
		self.add_query_param('ClipsParam', ClipsParam)
