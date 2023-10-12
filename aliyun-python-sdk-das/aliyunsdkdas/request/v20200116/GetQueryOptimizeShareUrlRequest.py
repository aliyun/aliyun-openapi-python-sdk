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
from aliyunsdkdas.endpoint import endpoint_data

class GetQueryOptimizeShareUrlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'GetQueryOptimizeShareUrl')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Engine(self): # String
		return self.get_query_params().get('Engine')

	def set_Engine(self, Engine):  # String
		self.add_query_param('Engine', Engine)
	def get_InstanceIds(self): # String
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # String
		self.add_query_param('InstanceIds', InstanceIds)
	def get_TagNames(self): # String
		return self.get_query_params().get('TagNames')

	def set_TagNames(self, TagNames):  # String
		self.add_query_param('TagNames', TagNames)
	def get_Keywords(self): # String
		return self.get_query_params().get('Keywords')

	def set_Keywords(self, Keywords):  # String
		self.add_query_param('Keywords', Keywords)
	def get_LogicalOperator(self): # String
		return self.get_query_params().get('LogicalOperator')

	def set_LogicalOperator(self, LogicalOperator):  # String
		self.add_query_param('LogicalOperator', LogicalOperator)
	def get_Rules(self): # String
		return self.get_query_params().get('Rules')

	def set_Rules(self, Rules):  # String
		self.add_query_param('Rules', Rules)
	def get_DbNames(self): # String
		return self.get_query_params().get('DbNames')

	def set_DbNames(self, DbNames):  # String
		self.add_query_param('DbNames', DbNames)
	def get_Time(self): # Long
		return self.get_query_params().get('Time')

	def set_Time(self, Time):  # Long
		self.add_query_param('Time', Time)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_PageNo(self): # Integer
		return self.get_query_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_query_param('PageNo', PageNo)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_Asc(self): # Boolean
		return self.get_query_params().get('Asc')

	def set_Asc(self, Asc):  # Boolean
		self.add_query_param('Asc', Asc)
	def get_OnlyOptimizedSql(self): # Boolean
		return self.get_query_params().get('OnlyOptimizedSql')

	def set_OnlyOptimizedSql(self, OnlyOptimizedSql):  # Boolean
		self.add_query_param('OnlyOptimizedSql', OnlyOptimizedSql)
	def get_SqlIds(self): # String
		return self.get_query_params().get('SqlIds')

	def set_SqlIds(self, SqlIds):  # String
		self.add_query_param('SqlIds', SqlIds)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
	def get_User(self): # String
		return self.get_query_params().get('User')

	def set_User(self, User):  # String
		self.add_query_param('User', User)
