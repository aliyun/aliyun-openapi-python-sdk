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

class DescribeMetricRuleBlackListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'DescribeMetricRuleBlackList','cms')
		self.set_method('POST')

	def get_ScopeType(self): # String
		return self.get_query_params().get('ScopeType')

	def set_ScopeType(self, ScopeType):  # String
		self.add_query_param('ScopeType', ScopeType)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Order(self): # Integer
		return self.get_query_params().get('Order')

	def set_Order(self, Order):  # Integer
		self.add_query_param('Order', Order)
	def get_IsEnable(self): # Boolean
		return self.get_query_params().get('IsEnable')

	def set_IsEnable(self, IsEnable):  # Boolean
		self.add_query_param('IsEnable', IsEnable)
	def get_InstanceIds(self): # Array
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # Array
		for index1, value1 in enumerate(InstanceIds):
			self.add_query_param('InstanceIds.' + str(index1 + 1), value1)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Idss(self): # RepeatList
		return self.get_query_params().get('Ids')

	def set_Idss(self, Ids):  # RepeatList
		for depth1 in range(len(Ids)):
			self.add_query_param('Ids.' + str(depth1 + 1), Ids[depth1])
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
