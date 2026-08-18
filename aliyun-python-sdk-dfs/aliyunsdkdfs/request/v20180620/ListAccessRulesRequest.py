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

class ListAccessRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DFS', '2018-06-20', 'ListAccessRules','alidfs')
		self.set_method('POST')

	def get_AccessGroupId(self): # String
		return self.get_query_params().get('AccessGroupId')

	def set_AccessGroupId(self, AccessGroupId):  # String
		self.add_query_param('AccessGroupId', AccessGroupId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_InputRegionId(self): # String
		return self.get_query_params().get('InputRegionId')

	def set_InputRegionId(self, InputRegionId):  # String
		self.add_query_param('InputRegionId', InputRegionId)
	def get_Limit(self): # Integer
		return self.get_query_params().get('Limit')

	def set_Limit(self, Limit):  # Integer
		self.add_query_param('Limit', Limit)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_StartOffset(self): # Integer
		return self.get_query_params().get('StartOffset')

	def set_StartOffset(self, StartOffset):  # Integer
		self.add_query_param('StartOffset', StartOffset)
	def get_OrderType(self): # String
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # String
		self.add_query_param('OrderType', OrderType)
