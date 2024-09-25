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
import json

class CreateSiteCustomLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'CreateSiteCustomLog')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_SiteId(self): # Long
		return self.get_body_params().get('SiteId')

	def set_SiteId(self, SiteId):  # Long
		self.add_body_params('SiteId', SiteId)
	def get_RequestHeaders(self): # Array
		return self.get_body_params().get('RequestHeaders')

	def set_RequestHeaders(self, RequestHeaders):  # Array
		self.add_body_params("RequestHeaders", json.dumps(RequestHeaders))
	def get_ResponseHeaders(self): # Array
		return self.get_body_params().get('ResponseHeaders')

	def set_ResponseHeaders(self, ResponseHeaders):  # Array
		self.add_body_params("ResponseHeaders", json.dumps(ResponseHeaders))
	def get_Cookies(self): # Array
		return self.get_body_params().get('Cookies')

	def set_Cookies(self, Cookies):  # Array
		self.add_body_params("Cookies", json.dumps(Cookies))
