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
from aliyunsdkcs.endpoint import endpoint_data

class UpdateTemplateRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'CS', '2015-12-15', 'UpdateTemplate')
		self.set_uri_pattern('/templates/[TemplateId]')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_template(self):
		return self.get_body_params().get('template')

	def set_template(self,template):
		self.add_body_params('template', template)

	def get_name(self):
		return self.get_body_params().get('name')

	def set_name(self,name):
		self.add_body_params('name', name)

	def get_description(self):
		return self.get_body_params().get('description')

	def set_description(self,description):
		self.add_body_params('description', description)

	def get_template_type(self):
		return self.get_body_params().get('template_type')

	def set_template_type(self,template_type):
		self.add_body_params('template_type', template_type)

	def get_TemplateId(self):
		return self.get_path_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_path_param('TemplateId',TemplateId)

	def get_tags(self):
		return self.get_body_params().get('tags')

	def set_tags(self,tags):
		self.add_body_params('tags', tags)