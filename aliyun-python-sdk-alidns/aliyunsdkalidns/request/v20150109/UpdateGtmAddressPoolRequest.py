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
from aliyunsdkalidns.endpoint import endpoint_data

class UpdateGtmAddressPoolRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'UpdateGtmAddressPool','alidns')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_MinAvailableAddrNum(self):
		return self.get_query_params().get('MinAvailableAddrNum')

	def set_MinAvailableAddrNum(self,MinAvailableAddrNum):
		self.add_query_param('MinAvailableAddrNum',MinAvailableAddrNum)

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
		return self.get_query_params().get('Addrs')

	def set_Addrs(self,Addrs):
		for i in range(len(Addrs)):	
			if Addrs[i].get('Mode') is not None:
				self.add_query_param('Addr.' + str(i + 1) + '.Mode' , Addrs[i].get('Mode'))
			if Addrs[i].get('LbaWeight') is not None:
				self.add_query_param('Addr.' + str(i + 1) + '.LbaWeight' , Addrs[i].get('LbaWeight'))
			if Addrs[i].get('Value') is not None:
				self.add_query_param('Addr.' + str(i + 1) + '.Value' , Addrs[i].get('Value'))
