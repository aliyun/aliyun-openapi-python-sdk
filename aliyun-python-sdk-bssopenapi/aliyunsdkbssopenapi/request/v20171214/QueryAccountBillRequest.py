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

class QueryAccountBillRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'QueryAccountBill')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_query_param('ProductCode', ProductCode)
	def get_BillingCycle(self): # String
		return self.get_query_params().get('BillingCycle')

	def set_BillingCycle(self, BillingCycle):  # String
		self.add_query_param('BillingCycle', BillingCycle)
	def get_PageNum(self): # Integer
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # Integer
		self.add_query_param('PageNum', PageNum)
	def get_OwnerID(self): # Long
		return self.get_query_params().get('OwnerID')

	def set_OwnerID(self, OwnerID):  # Long
		self.add_query_param('OwnerID', OwnerID)
	def get_BillOwnerId(self): # Long
		return self.get_query_params().get('BillOwnerId')

	def set_BillOwnerId(self, BillOwnerId):  # Long
		self.add_query_param('BillOwnerId', BillOwnerId)
	def get_BillingDate(self): # String
		return self.get_query_params().get('BillingDate')

	def set_BillingDate(self, BillingDate):  # String
		self.add_query_param('BillingDate', BillingDate)
	def get_IsGroupByProduct(self): # Boolean
		return self.get_query_params().get('IsGroupByProduct')

	def set_IsGroupByProduct(self, IsGroupByProduct):  # Boolean
		self.add_query_param('IsGroupByProduct', IsGroupByProduct)
	def get_Granularity(self): # String
		return self.get_query_params().get('Granularity')

	def set_Granularity(self, Granularity):  # String
		self.add_query_param('Granularity', Granularity)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
