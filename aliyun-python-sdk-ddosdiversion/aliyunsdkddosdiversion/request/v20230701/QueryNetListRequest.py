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

class QueryNetListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DdosDiversion', '2023-07-01', 'QueryNetList')
		self.set_method('POST')

	def get_Num(self): # Long
		return self.get_query_params().get('Num')

	def set_Num(self, Num):  # Long
		self.add_query_param('Num', Num)
	def get_MainNet(self): # String
		return self.get_query_params().get('MainNet')

	def set_MainNet(self, MainNet):  # String
		self.add_query_param('MainNet', MainNet)
	def get_Mode(self): # String
		return self.get_query_params().get('Mode')

	def set_Mode(self, Mode):  # String
		self.add_query_param('Mode', Mode)
	def get_Net(self): # String
		return self.get_query_params().get('Net')

	def set_Net(self, Net):  # String
		self.add_query_param('Net', Net)
	def get_SaleId(self): # String
		return self.get_query_params().get('SaleId')

	def set_SaleId(self, SaleId):  # String
		self.add_query_param('SaleId', SaleId)
	def get_Page(self): # Long
		return self.get_query_params().get('Page')

	def set_Page(self, Page):  # Long
		self.add_query_param('Page', Page)
