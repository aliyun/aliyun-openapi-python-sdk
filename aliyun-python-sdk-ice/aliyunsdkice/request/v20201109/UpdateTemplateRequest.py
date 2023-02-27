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

class UpdateTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'UpdateTemplate','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_RelatedMediaids(self): # String
		return self.get_query_params().get('RelatedMediaids')

	def set_RelatedMediaids(self, RelatedMediaids):  # String
		self.add_query_param('RelatedMediaids', RelatedMediaids)
	def get_CoverUrl(self): # String
		return self.get_query_params().get('CoverUrl')

	def set_CoverUrl(self, CoverUrl):  # String
		self.add_query_param('CoverUrl', CoverUrl)
	def get_PreviewMedia(self): # String
		return self.get_query_params().get('PreviewMedia')

	def set_PreviewMedia(self, PreviewMedia):  # String
		self.add_query_param('PreviewMedia', PreviewMedia)
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Config(self): # String
		return self.get_query_params().get('Config')

	def set_Config(self, Config):  # String
		self.add_query_param('Config', Config)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
