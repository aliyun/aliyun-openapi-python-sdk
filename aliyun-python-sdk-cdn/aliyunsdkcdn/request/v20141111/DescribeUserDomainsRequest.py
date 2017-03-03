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
class DescribeUserDomainsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2014-11-11', 'DescribeUserDomains')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_DomainStatus(self):
		return self.get_query_params().get('DomainStatus')

	def set_DomainStatus(self,DomainStatus):
		self.add_query_param('DomainStatus',DomainStatus)

	def get_DomainSearchType(self):
		return self.get_query_params().get('DomainSearchType')

	def set_DomainSearchType(self,DomainSearchType):
		self.add_query_param('DomainSearchType',DomainSearchType)

	def get_Sources(self):
		return self.get_query_params().get('Sources')

	def set_Sources(self,Sources):
		self.add_query_param('Sources',Sources)

	def get_CdnType(self):
		return self.get_query_params().get('CdnType')

	def set_CdnType(self,CdnType):
		self.add_query_param('CdnType',CdnType)