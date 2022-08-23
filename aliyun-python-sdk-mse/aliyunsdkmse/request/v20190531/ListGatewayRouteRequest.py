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
from aliyunsdkmse.endpoint import endpoint_data
import json

class ListGatewayRouteRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'ListGatewayRoute','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MseSessionId(self): # String
		return self.get_query_params().get('MseSessionId')

	def set_MseSessionId(self, MseSessionId):  # String
		self.add_query_param('MseSessionId', MseSessionId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_OrderItem(self): # String
		return self.get_query_params().get('OrderItem')

	def set_OrderItem(self, OrderItem):  # String
		self.add_query_param('OrderItem', OrderItem)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_DescSort(self): # Boolean
		return self.get_query_params().get('DescSort')

	def set_DescSort(self, DescSort):  # Boolean
		self.add_query_param('DescSort', DescSort)
	def get_FilterParams(self): # Struct
		return self.get_query_params().get('FilterParams')

	def set_FilterParams(self, FilterParams):  # Struct
		self.add_query_param("FilterParams", json.dumps(FilterParams))
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
