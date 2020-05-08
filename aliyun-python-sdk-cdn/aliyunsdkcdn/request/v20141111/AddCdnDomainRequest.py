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

class AddCdnDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2014-11-11', 'AddCdnDomain')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Sources(self):
		return self.get_query_params().get('Sources')

	def set_Sources(self,Sources):
		self.add_query_param('Sources',Sources)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_SourcePort(self):
		return self.get_query_params().get('SourcePort')

	def set_SourcePort(self,SourcePort):
		self.add_query_param('SourcePort',SourcePort)

	def get_Priorities(self):
		return self.get_query_params().get('Priorities')

	def set_Priorities(self,Priorities):
		self.add_query_param('Priorities',Priorities)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_CdnType(self):
		return self.get_query_params().get('CdnType')

	def set_CdnType(self,CdnType):
		self.add_query_param('CdnType',CdnType)

	def get_Scope(self):
		return self.get_query_params().get('Scope')

	def set_Scope(self,Scope):
		self.add_query_param('Scope',Scope)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_TopLevelDomain(self):
		return self.get_query_params().get('TopLevelDomain')

	def set_TopLevelDomain(self,TopLevelDomain):
		self.add_query_param('TopLevelDomain',TopLevelDomain)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_CheckUrl(self):
		return self.get_query_params().get('CheckUrl')

	def set_CheckUrl(self,CheckUrl):
		self.add_query_param('CheckUrl',CheckUrl)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)