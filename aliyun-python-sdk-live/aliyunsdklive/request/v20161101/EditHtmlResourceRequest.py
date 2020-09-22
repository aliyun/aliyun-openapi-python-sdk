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
from aliyunsdklive.endpoint import endpoint_data

class EditHtmlResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'EditHtmlResource','live')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HtmlUrl(self):
		return self.get_query_params().get('HtmlUrl')

	def set_HtmlUrl(self,HtmlUrl):
		self.add_query_param('HtmlUrl',HtmlUrl)

	def get_CasterId(self):
		return self.get_query_params().get('CasterId')

	def set_CasterId(self,CasterId):
		self.add_query_param('CasterId',CasterId)

	def get_htmlContent(self):
		return self.get_query_params().get('htmlContent')

	def set_htmlContent(self,htmlContent):
		self.add_query_param('htmlContent',htmlContent)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_HtmlResourceId(self):
		return self.get_query_params().get('HtmlResourceId')

	def set_HtmlResourceId(self,HtmlResourceId):
		self.add_query_param('HtmlResourceId',HtmlResourceId)

	def get_Config(self):
		return self.get_query_params().get('Config')

	def set_Config(self,Config):
		self.add_query_param('Config',Config)