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
from aliyunsdkcloudapi.endpoint import endpoint_data

class SetDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'SetDomain','apigateway')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_IsHttpRedirectToHttps(self): # Boolean
		return self.get_query_params().get('IsHttpRedirectToHttps')

	def set_IsHttpRedirectToHttps(self, IsHttpRedirectToHttps):  # Boolean
		self.add_query_param('IsHttpRedirectToHttps', IsHttpRedirectToHttps)
	def get_CustomDomainType(self): # String
		return self.get_query_params().get('CustomDomainType')

	def set_CustomDomainType(self, CustomDomainType):  # String
		self.add_query_param('CustomDomainType', CustomDomainType)
	def get_BindStageName(self): # String
		return self.get_query_params().get('BindStageName')

	def set_BindStageName(self, BindStageName):  # String
		self.add_query_param('BindStageName', BindStageName)
	def get_IsForce(self): # Boolean
		return self.get_query_params().get('IsForce')

	def set_IsForce(self, IsForce):  # Boolean
		self.add_query_param('IsForce', IsForce)
