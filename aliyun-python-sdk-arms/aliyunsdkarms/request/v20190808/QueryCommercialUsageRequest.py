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
from aliyunsdkarms.endpoint import endpoint_data

class QueryCommercialUsageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'QueryCommercialUsage','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_Measuress(self): # RepeatList
		return self.get_query_params().get('Measures')

	def set_Measuress(self, Measures):  # RepeatList
		for depth1 in range(len(Measures)):
			self.add_query_param('Measures.' + str(depth1 + 1), Measures[depth1])
	def get_IntervalInSec(self): # Integer
		return self.get_query_params().get('IntervalInSec')

	def set_IntervalInSec(self, IntervalInSec):  # Integer
		self.add_query_param('IntervalInSec', IntervalInSec)
	def get_QueryType(self): # String
		return self.get_query_params().get('QueryType')

	def set_QueryType(self, QueryType):  # String
		self.add_query_param('QueryType', QueryType)
	def get_Order(self): # String
		return self.get_query_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_query_param('Order', Order)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_Metric(self): # String
		return self.get_query_params().get('Metric')

	def set_Metric(self, Metric):  # String
		self.add_query_param('Metric', Metric)
	def get_AdvancedFilterss(self): # RepeatList
		return self.get_query_params().get('AdvancedFilters')

	def set_AdvancedFilterss(self, AdvancedFilters):  # RepeatList
		for depth1 in range(len(AdvancedFilters)):
			if AdvancedFilters[depth1].get('OpType') is not None:
				self.add_query_param('AdvancedFilters.' + str(depth1 + 1) + '.OpType', AdvancedFilters[depth1].get('OpType'))
			if AdvancedFilters[depth1].get('Value') is not None:
				self.add_query_param('AdvancedFilters.' + str(depth1 + 1) + '.Value', AdvancedFilters[depth1].get('Value'))
			if AdvancedFilters[depth1].get('Key') is not None:
				self.add_query_param('AdvancedFilters.' + str(depth1 + 1) + '.Key', AdvancedFilters[depth1].get('Key'))
	def get_Dimensionss(self): # RepeatList
		return self.get_query_params().get('Dimensions')

	def set_Dimensionss(self, Dimensions):  # RepeatList
		for depth1 in range(len(Dimensions)):
			self.add_query_param('Dimensions.' + str(depth1 + 1), Dimensions[depth1])
