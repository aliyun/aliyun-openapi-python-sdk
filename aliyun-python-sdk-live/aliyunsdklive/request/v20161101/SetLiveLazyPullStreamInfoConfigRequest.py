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
from aliyunsdklive.endpoint import endpoint_data

class SetLiveLazyPullStreamInfoConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'SetLiveLazyPullStreamInfoConfig','live')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PullArgs(self):
		return self.get_query_params().get('PullArgs')

	def set_PullArgs(self,PullArgs):
		self.add_query_param('PullArgs',PullArgs)

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_LiveapiRequestFrom(self):
		return self.get_query_params().get('LiveapiRequestFrom')

	def set_LiveapiRequestFrom(self,LiveapiRequestFrom):
		self.add_query_param('LiveapiRequestFrom',LiveapiRequestFrom)

	def get_PullAuthKey(self):
		return self.get_query_params().get('PullAuthKey')

	def set_PullAuthKey(self,PullAuthKey):
		self.add_query_param('PullAuthKey',PullAuthKey)

	def get_PullAuthType(self):
		return self.get_query_params().get('PullAuthType')

	def set_PullAuthType(self,PullAuthType):
		self.add_query_param('PullAuthType',PullAuthType)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_PullDomainName(self):
		return self.get_query_params().get('PullDomainName')

	def set_PullDomainName(self,PullDomainName):
		self.add_query_param('PullDomainName',PullDomainName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PullAppName(self):
		return self.get_query_params().get('PullAppName')

	def set_PullAppName(self,PullAppName):
		self.add_query_param('PullAppName',PullAppName)

	def get_PullProtocol(self):
		return self.get_query_params().get('PullProtocol')

	def set_PullProtocol(self,PullProtocol):
		self.add_query_param('PullProtocol',PullProtocol)