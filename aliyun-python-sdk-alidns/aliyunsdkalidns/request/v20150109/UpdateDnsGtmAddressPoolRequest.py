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

class UpdateDnsGtmAddressPoolRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'UpdateDnsGtmAddressPool','alidns')
		self.set_method('POST')

	def get_LbaStrategy(self):
		return self.get_query_params().get('LbaStrategy')

	def set_LbaStrategy(self,LbaStrategy):
		self.add_query_param('LbaStrategy',LbaStrategy)

	def get_AddrPoolId(self):
		return self.get_query_params().get('AddrPoolId')

	def set_AddrPoolId(self,AddrPoolId):
		self.add_query_param('AddrPoolId',AddrPoolId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Addrs(self):
		return self.get_query_params().get('Addr')

	def set_Addrs(self, Addrs):
		for depth1 in range(len(Addrs)):
			if Addrs[depth1].get('Mode') is not None:
				self.add_query_param('Addr.' + str(depth1 + 1) + '.Mode', Addrs[depth1].get('Mode'))
			if Addrs[depth1].get('AttributeInfo') is not None:
				self.add_query_param('Addr.' + str(depth1 + 1) + '.AttributeInfo', Addrs[depth1].get('AttributeInfo'))
			if Addrs[depth1].get('Remark') is not None:
				self.add_query_param('Addr.' + str(depth1 + 1) + '.Remark', Addrs[depth1].get('Remark'))
			if Addrs[depth1].get('Addr') is not None:
				self.add_query_param('Addr.' + str(depth1 + 1) + '.Addr', Addrs[depth1].get('Addr'))
			if Addrs[depth1].get('LbaWeight') is not None:
				self.add_query_param('Addr.' + str(depth1 + 1) + '.LbaWeight', Addrs[depth1].get('LbaWeight'))