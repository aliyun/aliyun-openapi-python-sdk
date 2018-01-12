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
class SaveTaskForModifyingDomainDnsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2016-05-11', 'SaveTaskForModifyingDomainDns')

	def get_SaleId(self):
		return self.get_query_params().get('SaleId')

	def set_SaleId(self,SaleId):
		self.add_query_param('SaleId',SaleId)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_AliyunDns(self):
		return self.get_query_params().get('AliyunDns')

	def set_AliyunDns(self,AliyunDns):
		self.add_query_param('AliyunDns',AliyunDns)

	def get_DnsLists(self):
		return self.get_query_params().get('DnsLists')

	def set_DnsLists(self,DnsLists):
		for i in range(len(DnsLists)):	
			self.add_query_param('DnsList.' + str(i + 1) , DnsLists[i]);