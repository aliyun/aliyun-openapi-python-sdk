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
from aliyunsdkcams.endpoint import endpoint_data

class SendMessageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cams', '2020-06-06', 'SendMessage','cams')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TemplateBodyParams(self):
		return self.get_body_params().get('TemplateBodyParams')

	def set_TemplateBodyParams(self,TemplateBodyParams):
		self.add_body_params('TemplateBodyParams', TemplateBodyParams)

	def get_Link(self):
		return self.get_body_params().get('Link')

	def set_Link(self,Link):
		self.add_body_params('Link', Link)

	def get_Caption(self):
		return self.get_body_params().get('Caption')

	def set_Caption(self,Caption):
		self.add_body_params('Caption', Caption)

	def get_Type(self):
		return self.get_body_params().get('Type')

	def set_Type(self,Type):
		self.add_body_params('Type', Type)

	def get_Body(self):
		return self.get_body_params().get('Body')

	def set_Body(self,Body):
		self.add_body_params('Body', Body)

	def get_ChannelType(self):
		return self.get_body_params().get('ChannelType')

	def set_ChannelType(self,ChannelType):
		self.add_body_params('ChannelType', ChannelType)

	def get__From(self):
		return self.get_body_params().get('From')

	def set__From(self,_From):
		self.add_body_params('From', _From)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_To(self):
		return self.get_body_params().get('To')

	def set_To(self,To):
		self.add_body_params('To', To)

	def get_TemplateCode(self):
		return self.get_body_params().get('TemplateCode')

	def set_TemplateCode(self,TemplateCode):
		self.add_body_params('TemplateCode', TemplateCode)

	def get_MediaType(self):
		return self.get_body_params().get('MediaType')

	def set_MediaType(self,MediaType):
		self.add_body_params('MediaType', MediaType)