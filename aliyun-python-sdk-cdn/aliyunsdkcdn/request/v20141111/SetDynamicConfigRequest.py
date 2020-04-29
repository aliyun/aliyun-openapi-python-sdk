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
from aliyunsdkcdn.endpoint import endpoint_data

class SetDynamicConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2014-11-11', 'SetDynamicConfig')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DynamicOrigin(self):
		return self.get_query_params().get('DynamicOrigin')

	def set_DynamicOrigin(self,DynamicOrigin):
		self.add_query_param('DynamicOrigin',DynamicOrigin)

	def get_StaticType(self):
		return self.get_query_params().get('StaticType')

	def set_StaticType(self,StaticType):
		self.add_query_param('StaticType',StaticType)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_StaticUri(self):
		return self.get_query_params().get('StaticUri')

	def set_StaticUri(self,StaticUri):
		self.add_query_param('StaticUri',StaticUri)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_StaticPath(self):
		return self.get_query_params().get('StaticPath')

	def set_StaticPath(self,StaticPath):
		self.add_query_param('StaticPath',StaticPath)

	def get_DynamicCacheControl(self):
		return self.get_query_params().get('DynamicCacheControl')

	def set_DynamicCacheControl(self,DynamicCacheControl):
		self.add_query_param('DynamicCacheControl',DynamicCacheControl)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)