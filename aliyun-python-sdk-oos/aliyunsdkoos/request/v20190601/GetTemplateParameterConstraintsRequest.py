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
from aliyunsdkoos.endpoint import endpoint_data

class GetTemplateParameterConstraintsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'GetTemplateParameterConstraints','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TemplateURL(self): # String
		return self.get_query_params().get('TemplateURL')

	def set_TemplateURL(self, TemplateURL):  # String
		self.add_query_param('TemplateURL', TemplateURL)
	def get_TemplateVersion(self): # String
		return self.get_query_params().get('TemplateVersion')

	def set_TemplateVersion(self, TemplateVersion):  # String
		self.add_query_param('TemplateVersion', TemplateVersion)
	def get_TemplateName(self): # String
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self, TemplateName):  # String
		self.add_query_param('TemplateName', TemplateName)
	def get_TemplateContent(self): # String
		return self.get_query_params().get('TemplateContent')

	def set_TemplateContent(self, TemplateContent):  # String
		self.add_query_param('TemplateContent', TemplateContent)
	def get_Parameters(self): # String
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # String
		self.add_query_param('Parameters', Parameters)
