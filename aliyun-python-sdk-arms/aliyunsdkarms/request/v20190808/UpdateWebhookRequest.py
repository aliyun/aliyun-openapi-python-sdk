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

class UpdateWebhookRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'UpdateWebhook','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_HttpHeaders(self): # String
		return self.get_query_params().get('HttpHeaders')

	def set_HttpHeaders(self, HttpHeaders):  # String
		self.add_query_param('HttpHeaders', HttpHeaders)
	def get_Method(self): # String
		return self.get_query_params().get('Method')

	def set_Method(self, Method):  # String
		self.add_query_param('Method', Method)
	def get_ContactId(self): # Long
		return self.get_query_params().get('ContactId')

	def set_ContactId(self, ContactId):  # Long
		self.add_query_param('ContactId', ContactId)
	def get_HttpParams(self): # String
		return self.get_query_params().get('HttpParams')

	def set_HttpParams(self, HttpParams):  # String
		self.add_query_param('HttpParams', HttpParams)
	def get_Body(self): # String
		return self.get_query_params().get('Body')

	def set_Body(self, Body):  # String
		self.add_query_param('Body', Body)
	def get_Url(self): # String
		return self.get_query_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_query_param('Url', Url)
	def get_ContactName(self): # String
		return self.get_query_params().get('ContactName')

	def set_ContactName(self, ContactName):  # String
		self.add_query_param('ContactName', ContactName)
	def get_RecoverBody(self): # String
		return self.get_query_params().get('RecoverBody')

	def set_RecoverBody(self, RecoverBody):  # String
		self.add_query_param('RecoverBody', RecoverBody)
