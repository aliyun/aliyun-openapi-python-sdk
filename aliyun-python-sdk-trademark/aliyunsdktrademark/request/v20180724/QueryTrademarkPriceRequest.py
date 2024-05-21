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
class QueryTrademarkPriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'QueryTrademarkPrice','trademark')

	def get_TmName(self):
		return self.get_query_params().get('TmName')

	def set_TmName(self,TmName):
		self.add_query_param('TmName',TmName)

	def get_TmIcon(self):
		return self.get_query_params().get('TmIcon')

	def set_TmIcon(self,TmIcon):
		self.add_query_param('TmIcon',TmIcon)

	def get_OrderData(self):
		return self.get_query_params().get('OrderData')

	def set_OrderData(self,OrderData):
		self.add_query_param('OrderData',OrderData)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)