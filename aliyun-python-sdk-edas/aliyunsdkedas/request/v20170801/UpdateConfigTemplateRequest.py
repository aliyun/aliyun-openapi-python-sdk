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
from aliyunsdkedas.endpoint import endpoint_data

class UpdateConfigTemplateRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UpdateConfigTemplate','Edas')
		self.set_uri_pattern('/pop/v5/config_template')
		self.set_method('PUT')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Name(self): # string
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # string
		self.add_body_params('Name', Name)
	def get_Format(self): # string
		return self.get_body_params().get('Format')

	def set_Format(self, Format):  # string
		self.add_body_params('Format', Format)
	def get_Description(self): # string
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # string
		self.add_body_params('Description', Description)
	def get_Id(self): # integer
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # integer
		self.add_body_params('Id', Id)
	def get_Content(self): # string
		return self.get_body_params().get('Content')

	def set_Content(self, Content):  # string
		self.add_body_params('Content', Content)
