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
from aliyunsdkmultimediaai.endpoint import endpoint_data

class CreateGifTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'multimediaai', '2019-08-10', 'CreateGifTask')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TemplateId(self):
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_query_param('TemplateId',TemplateId)

	def get_VideoUrl(self):
		return self.get_query_params().get('VideoUrl')

	def set_VideoUrl(self,VideoUrl):
		self.add_query_param('VideoUrl',VideoUrl)

	def get_VideoName(self):
		return self.get_query_params().get('VideoName')

	def set_VideoName(self,VideoName):
		self.add_query_param('VideoName',VideoName)

	def get_CallbackUrl(self):
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self,CallbackUrl):
		self.add_query_param('CallbackUrl',CallbackUrl)

	def get_ApplicationId(self):
		return self.get_query_params().get('ApplicationId')

	def set_ApplicationId(self,ApplicationId):
		self.add_query_param('ApplicationId',ApplicationId)