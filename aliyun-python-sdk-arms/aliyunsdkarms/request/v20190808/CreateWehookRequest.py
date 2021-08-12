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

class CreateWehookRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreateWehook','arms')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HttpHeaders(self):
		return self.get_query_params().get('HttpHeaders')

	def set_HttpHeaders(self,HttpHeaders):
		self.add_query_param('HttpHeaders',HttpHeaders)

	def get_Method(self):
		return self.get_query_params().get('Method')

	def set_Method(self,Method):
		self.add_query_param('Method',Method)

	def get_HttpParams(self):
		return self.get_query_params().get('HttpParams')

	def set_HttpParams(self,HttpParams):
		self.add_query_param('HttpParams',HttpParams)

	def get_Body(self):
		return self.get_query_params().get('Body')

	def set_Body(self,Body):
		self.add_query_param('Body',Body)

	def get_Url(self):
		return self.get_query_params().get('Url')

	def set_Url(self,Url):
		self.add_query_param('Url',Url)

	def get_ContactName(self):
		return self.get_query_params().get('ContactName')

	def set_ContactName(self,ContactName):
		self.add_query_param('ContactName',ContactName)