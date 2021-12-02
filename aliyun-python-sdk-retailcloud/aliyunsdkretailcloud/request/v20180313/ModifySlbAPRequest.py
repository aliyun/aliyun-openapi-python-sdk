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
from aliyunsdkretailcloud.endpoint import endpoint_data

class ModifySlbAPRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'ModifySlbAP')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SslCertId(self): # String
		return self.get_query_params().get('SslCertId')

	def set_SslCertId(self, SslCertId):  # String
		self.add_query_param('SslCertId', SslCertId)
	def get_EstablishedTimeout(self): # Integer
		return self.get_query_params().get('EstablishedTimeout')

	def set_EstablishedTimeout(self, EstablishedTimeout):  # Integer
		self.add_query_param('EstablishedTimeout', EstablishedTimeout)
	def get_RealServerPort(self): # Integer
		return self.get_query_params().get('RealServerPort')

	def set_RealServerPort(self, RealServerPort):  # Integer
		self.add_query_param('RealServerPort', RealServerPort)
	def get_StickySession(self): # Integer
		return self.get_query_params().get('StickySession')

	def set_StickySession(self, StickySession):  # Integer
		self.add_query_param('StickySession', StickySession)
	def get_CookieTimeout(self): # Integer
		return self.get_query_params().get('CookieTimeout')

	def set_CookieTimeout(self, CookieTimeout):  # Integer
		self.add_query_param('CookieTimeout', CookieTimeout)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_SlbAPId(self): # Long
		return self.get_query_params().get('SlbAPId')

	def set_SlbAPId(self, SlbAPId):  # Long
		self.add_query_param('SlbAPId', SlbAPId)
