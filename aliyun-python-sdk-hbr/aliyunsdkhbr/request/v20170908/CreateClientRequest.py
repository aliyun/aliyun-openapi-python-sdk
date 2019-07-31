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
class CreateClientRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateClient','hbr')
		self.set_protocol_type('https')

	def get_SourceTypes(self):
		return self.get_query_params().get('SourceTypes')

	def set_SourceTypes(self,SourceTypes):
		self.add_query_param('SourceTypes',SourceTypes)

	def get_ClientType(self):
		return self.get_query_params().get('ClientType')

	def set_ClientType(self,ClientType):
		self.add_query_param('ClientType',ClientType)

	def get_AlertSetting(self):
		return self.get_query_params().get('AlertSetting')

	def set_AlertSetting(self,AlertSetting):
		self.add_query_param('AlertSetting',AlertSetting)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_ContactId(self):
		return self.get_query_params().get('ContactId')

	def set_ContactId(self,ContactId):
		self.add_query_param('ContactId',ContactId)

	def get_ClientName(self):
		return self.get_query_params().get('ClientName')

	def set_ClientName(self,ClientName):
		self.add_query_param('ClientName',ClientName)

	def get_PlatformType(self):
		return self.get_query_params().get('PlatformType')

	def set_PlatformType(self,PlatformType):
		self.add_query_param('PlatformType',PlatformType)

	def get_NetworkType(self):
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_query_param('NetworkType',NetworkType)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)