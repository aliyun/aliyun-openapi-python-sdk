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
from aliyunsdkunimkt.endpoint import endpoint_data

class CreateProxyBrandUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'CreateProxyBrandUser')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ContactName(self): # String
		return self.get_query_params().get('ContactName')

	def set_ContactName(self, ContactName):  # String
		self.add_query_param('ContactName', ContactName)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Company(self): # String
		return self.get_query_params().get('Company')

	def set_Company(self, Company):  # String
		self.add_query_param('Company', Company)
	def get_Industry(self): # String
		return self.get_query_params().get('Industry')

	def set_Industry(self, Industry):  # String
		self.add_query_param('Industry', Industry)
	def get_BrandUserNick(self): # String
		return self.get_query_params().get('BrandUserNick')

	def set_BrandUserNick(self, BrandUserNick):  # String
		self.add_query_param('BrandUserNick', BrandUserNick)
	def get_ContactPhone(self): # String
		return self.get_query_params().get('ContactPhone')

	def set_ContactPhone(self, ContactPhone):  # String
		self.add_query_param('ContactPhone', ContactPhone)
	def get_ProxyUserId(self): # Long
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self, ProxyUserId):  # Long
		self.add_query_param('ProxyUserId', ProxyUserId)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
