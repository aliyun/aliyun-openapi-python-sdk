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

class GetModifyBEClusterInquiryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'selectdb', '2023-05-22', 'GetModifyBEClusterInquiry')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_CacheSize(self): # Long
		return self.get_query_params().get('CacheSize')

	def set_CacheSize(self, CacheSize):  # Long
		self.add_query_param('CacheSize', CacheSize)
	def get_PreCacheSize(self): # Long
		return self.get_query_params().get('PreCacheSize')

	def set_PreCacheSize(self, PreCacheSize):  # Long
		self.add_query_param('PreCacheSize', PreCacheSize)
	def get_ComputeSize(self): # Long
		return self.get_query_params().get('ComputeSize')

	def set_ComputeSize(self, ComputeSize):  # Long
		self.add_query_param('ComputeSize', ComputeSize)
	def get_DbInstanceId(self): # String
		return self.get_query_params().get('DbInstanceId')

	def set_DbInstanceId(self, DbInstanceId):  # String
		self.add_query_param('DbInstanceId', DbInstanceId)
	def get_PreComputeSize(self): # Long
		return self.get_query_params().get('PreComputeSize')

	def set_PreComputeSize(self, PreComputeSize):  # Long
		self.add_query_param('PreComputeSize', PreComputeSize)
	def get_Quantity(self): # Long
		return self.get_query_params().get('Quantity')

	def set_Quantity(self, Quantity):  # Long
		self.add_query_param('Quantity', Quantity)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_CommodityCode(self): # String
		return self.get_query_params().get('CommodityCode')

	def set_CommodityCode(self, CommodityCode):  # String
		self.add_query_param('CommodityCode', CommodityCode)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_PricingCycle(self): # String
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self, PricingCycle):  # String
		self.add_query_param('PricingCycle', PricingCycle)
