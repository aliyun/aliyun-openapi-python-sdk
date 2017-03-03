# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class AddCdnDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2014-11-11', 'AddCdnDomain')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_CdnType(self):
		return self.get_query_params().get('CdnType')

	def set_CdnType(self,CdnType):
		self.add_query_param('CdnType',CdnType)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_Sources(self):
		return self.get_query_params().get('Sources')

	def set_Sources(self,Sources):
		self.add_query_param('Sources',Sources)

	def get_SourcePort(self):
		return self.get_query_params().get('SourcePort')

	def set_SourcePort(self,SourcePort):
		self.add_query_param('SourcePort',SourcePort)

	def get_ServerCertificate(self):
		return self.get_query_params().get('ServerCertificate')

	def set_ServerCertificate(self,ServerCertificate):
		self.add_query_param('ServerCertificate',ServerCertificate)

	def get_PrivateKey(self):
		return self.get_query_params().get('PrivateKey')

	def set_PrivateKey(self,PrivateKey):
		self.add_query_param('PrivateKey',PrivateKey)