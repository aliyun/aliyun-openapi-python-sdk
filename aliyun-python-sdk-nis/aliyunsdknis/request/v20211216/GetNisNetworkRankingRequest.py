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
import json

class GetNisNetworkRankingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nis', '2021-12-16', 'GetNisNetworkRanking','networkana')
		self.set_method('POST')

	def get_UseCrossAccount(self): # Boolean
		return self.get_query_params().get('UseCrossAccount')

	def set_UseCrossAccount(self, UseCrossAccount):  # Boolean
		self.add_query_param('UseCrossAccount', UseCrossAccount)
	def get_TopN(self): # Integer
		return self.get_query_params().get('TopN')

	def set_TopN(self, TopN):  # Integer
		self.add_query_param('TopN', TopN)
	def get_Direction(self): # String
		return self.get_query_params().get('Direction')

	def set_Direction(self, Direction):  # String
		self.add_query_param('Direction', Direction)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_BeginTime(self): # Long
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # Long
		self.add_query_param('BeginTime', BeginTime)
	def get_GroupBy(self): # String
		return self.get_query_params().get('GroupBy')

	def set_GroupBy(self, GroupBy):  # String
		self.add_query_param('GroupBy', GroupBy)
	def get_Sort(self): # String
		return self.get_query_params().get('Sort')

	def set_Sort(self, Sort):  # String
		self.add_query_param('Sort', Sort)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_RegionNo(self): # String
		return self.get_query_params().get('RegionNo')

	def set_RegionNo(self, RegionNo):  # String
		self.add_query_param('RegionNo', RegionNo)
	def get_Filter(self): # Array
		return self.get_query_params().get('Filter')

	def set_Filter(self, Filter):  # Array
		self.add_query_param("Filter", json.dumps(Filter))
	def get_AccountIdss(self): # RepeatList
		return self.get_query_params().get('AccountIds')

	def set_AccountIdss(self, AccountIds):  # RepeatList
		for depth1 in range(len(AccountIds)):
			self.add_query_param('AccountIds.' + str(depth1 + 1), AccountIds[depth1])
