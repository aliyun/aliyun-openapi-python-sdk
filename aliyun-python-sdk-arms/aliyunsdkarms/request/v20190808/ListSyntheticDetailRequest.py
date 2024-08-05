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
import json

class ListSyntheticDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'ListSyntheticDetail','arms')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_Filters(self): # Map
		return self.get_query_params().get('Filters')

	def set_Filters(self, Filters):  # Map
		self.add_query_param("Filters", json.dumps(Filters))
	def get_ExactFilters(self): # Array
		return self.get_query_params().get('ExactFilters')

	def set_ExactFilters(self, ExactFilters):  # Array
		self.add_query_param("ExactFilters", json.dumps(ExactFilters))
	def get_SyntheticType(self): # Integer
		return self.get_query_params().get('SyntheticType')

	def set_SyntheticType(self, SyntheticType):  # Integer
		self.add_query_param('SyntheticType', SyntheticType)
	def get_AdvancedFilters(self): # Array
		return self.get_query_params().get('AdvancedFilters')

	def set_AdvancedFilters(self, AdvancedFilters):  # Array
		self.add_query_param("AdvancedFilters", json.dumps(AdvancedFilters))
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Detail(self): # String
		return self.get_query_params().get('Detail')

	def set_Detail(self, Detail):  # String
		self.add_query_param('Detail', Detail)
	def get_Page(self): # Integer
		return self.get_query_params().get('Page')

	def set_Page(self, Page):  # Integer
		self.add_query_param('Page', Page)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
	def get_Order(self): # String
		return self.get_query_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_query_param('Order', Order)
