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
from aliyunsdkquotas.endpoint import endpoint_data

class ListProductQuotasRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quotas', '2020-05-10', 'ListProductQuotas','quotas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_body_params('ProductCode', ProductCode)
	def get_QuotaActionCode(self): # String
		return self.get_body_params().get('QuotaActionCode')

	def set_QuotaActionCode(self, QuotaActionCode):  # String
		self.add_body_params('QuotaActionCode', QuotaActionCode)
	def get_GroupCode(self): # String
		return self.get_body_params().get('GroupCode')

	def set_GroupCode(self, GroupCode):  # String
		self.add_body_params('GroupCode', GroupCode)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_SortOrder(self): # String
		return self.get_body_params().get('SortOrder')

	def set_SortOrder(self, SortOrder):  # String
		self.add_body_params('SortOrder', SortOrder)
	def get_KeyWord(self): # String
		return self.get_body_params().get('KeyWord')

	def set_KeyWord(self, KeyWord):  # String
		self.add_body_params('KeyWord', KeyWord)
	def get_QuotaCategory(self): # String
		return self.get_body_params().get('QuotaCategory')

	def set_QuotaCategory(self, QuotaCategory):  # String
		self.add_body_params('QuotaCategory', QuotaCategory)
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
	def get_SortField(self): # String
		return self.get_body_params().get('SortField')

	def set_SortField(self, SortField):  # String
		self.add_body_params('SortField', SortField)
	def get_Dimensionss(self): # RepeatList
		return self.get_body_params().get('Dimensions')

	def set_Dimensionss(self, Dimensions):  # RepeatList
		for depth1 in range(len(Dimensions)):
			if Dimensions[depth1].get('Key') is not None:
				self.add_body_params('Dimensions.' + str(depth1 + 1) + '.Key', Dimensions[depth1].get('Key'))
			if Dimensions[depth1].get('Value') is not None:
				self.add_body_params('Dimensions.' + str(depth1 + 1) + '.Value', Dimensions[depth1].get('Value'))
