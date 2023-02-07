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
from aliyunsdkbssopenapi.endpoint import endpoint_data
import json

class QuerySkuPriceListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'QuerySkuPriceList','bssopenapi')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NextPageToken(self): # String
		return self.get_query_params().get('NextPageToken')

	def set_NextPageToken(self, NextPageToken):  # String
		self.add_query_param('NextPageToken', NextPageToken)
	def get_CommodityCode(self): # String
		return self.get_query_params().get('CommodityCode')

	def set_CommodityCode(self, CommodityCode):  # String
		self.add_query_param('CommodityCode', CommodityCode)
	def get_PriceFactorConditionMap(self): # Map
		return self.get_query_params().get('PriceFactorConditionMap')

	def set_PriceFactorConditionMap(self, PriceFactorConditionMap):  # Map
		self.add_query_param("PriceFactorConditionMap", json.dumps(PriceFactorConditionMap))
	def get_PriceEntityCode(self): # String
		return self.get_query_params().get('PriceEntityCode')

	def set_PriceEntityCode(self, PriceEntityCode):  # String
		self.add_query_param('PriceEntityCode', PriceEntityCode)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
