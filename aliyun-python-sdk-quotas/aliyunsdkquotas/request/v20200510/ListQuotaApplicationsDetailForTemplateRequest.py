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

class ListQuotaApplicationsDetailForTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quotas', '2020-05-10', 'ListQuotaApplicationsDetailForTemplate','quotas')
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
	def get_BatchQuotaApplicationId(self): # String
		return self.get_body_params().get('BatchQuotaApplicationId')

	def set_BatchQuotaApplicationId(self, BatchQuotaApplicationId):  # String
		self.add_body_params('BatchQuotaApplicationId', BatchQuotaApplicationId)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_QuotaCategory(self): # String
		return self.get_body_params().get('QuotaCategory')

	def set_QuotaCategory(self, QuotaCategory):  # String
		self.add_body_params('QuotaCategory', QuotaCategory)
	def get_AliyunUid(self): # String
		return self.get_body_params().get('AliyunUid')

	def set_AliyunUid(self, AliyunUid):  # String
		self.add_body_params('AliyunUid', AliyunUid)
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
