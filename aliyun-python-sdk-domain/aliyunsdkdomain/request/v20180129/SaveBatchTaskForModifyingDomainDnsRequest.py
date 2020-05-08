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


class SaveBatchTaskForModifyingDomainDnsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveBatchTaskForModifyingDomainDns')

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_DomainNames(self):
		return self.get_query_params().get('DomainNames')

	def set_DomainNames(self,DomainNames):
		for i in range(len(DomainNames)):	
			if DomainNames[i] is not None:
				self.add_query_param('DomainName.' + str(i + 1) , DomainNames[i]);

	def get_DomainNameServers(self):
		return self.get_query_params().get('DomainNameServers')

	def set_DomainNameServers(self,DomainNameServers):
		for i in range(len(DomainNameServers)):	
			if DomainNameServers[i] is not None:
				self.add_query_param('DomainNameServer.' + str(i + 1) , DomainNameServers[i]);

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_AliyunDns(self):
		return self.get_query_params().get('AliyunDns')

	def set_AliyunDns(self,AliyunDns):
		self.add_query_param('AliyunDns',AliyunDns)