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
from aliyunsdkarms.endpoint import endpoint_data

class CreateOrUpdateWebhookContactRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreateOrUpdateWebhookContact','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_WebhookId(self): # Long
		return self.get_body_params().get('WebhookId')

	def set_WebhookId(self, WebhookId):  # Long
		self.add_body_params('WebhookId', WebhookId)
	def get_Method(self): # String
		return self.get_body_params().get('Method')

	def set_Method(self, Method):  # String
		self.add_body_params('Method', Method)
	def get_WebhookName(self): # String
		return self.get_body_params().get('WebhookName')

	def set_WebhookName(self, WebhookName):  # String
		self.add_body_params('WebhookName', WebhookName)
	def get_BizParams(self): # String
		return self.get_body_params().get('BizParams')

	def set_BizParams(self, BizParams):  # String
		self.add_body_params('BizParams', BizParams)
	def get_Body(self): # String
		return self.get_body_params().get('Body')

	def set_Body(self, Body):  # String
		self.add_body_params('Body', Body)
	def get_Url(self): # String
		return self.get_body_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_body_params('Url', Url)
	def get_BizHeaders(self): # String
		return self.get_body_params().get('BizHeaders')

	def set_BizHeaders(self, BizHeaders):  # String
		self.add_body_params('BizHeaders', BizHeaders)
	def get_RecoverBody(self): # String
		return self.get_body_params().get('RecoverBody')

	def set_RecoverBody(self, RecoverBody):  # String
		self.add_body_params('RecoverBody', RecoverBody)
