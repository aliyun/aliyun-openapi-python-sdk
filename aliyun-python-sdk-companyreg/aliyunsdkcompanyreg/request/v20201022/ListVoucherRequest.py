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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class ListVoucherRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2020-10-22', 'ListVoucher')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_PageCount(self): # Integer
		return self.get_query_params().get('PageCount')

	def set_PageCount(self, PageCount):  # Integer
		self.add_query_param('PageCount', PageCount)
	def get_CodeSortType(self): # String
		return self.get_query_params().get('CodeSortType')

	def set_CodeSortType(self, CodeSortType):  # String
		self.add_query_param('CodeSortType', CodeSortType)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Text(self): # String
		return self.get_query_params().get('Text')

	def set_Text(self, Text):  # String
		self.add_query_param('Text', Text)
