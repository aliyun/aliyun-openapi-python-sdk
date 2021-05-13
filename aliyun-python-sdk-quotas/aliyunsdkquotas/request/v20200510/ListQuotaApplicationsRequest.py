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

class ListQuotaApplicationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quotas', '2020-05-10', 'ListQuotaApplications','quotas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProductCode(self):
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_body_params('ProductCode', ProductCode)

	def get_QuotaActionCode(self):
		return self.get_body_params().get('QuotaActionCode')

	def set_QuotaActionCode(self,QuotaActionCode):
		self.add_body_params('QuotaActionCode', QuotaActionCode)

	def get_NextToken(self):
		return self.get_body_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_body_params('NextToken', NextToken)

	def get_KeyWord(self):
		return self.get_body_params().get('KeyWord')

	def set_KeyWord(self,KeyWord):
		self.add_body_params('KeyWord', KeyWord)

	def get_QuotaCategory(self):
		return self.get_body_params().get('QuotaCategory')

	def set_QuotaCategory(self,QuotaCategory):
		self.add_body_params('QuotaCategory', QuotaCategory)

	def get_MaxResults(self):
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_body_params('MaxResults', MaxResults)

	def get_Status(self):
		return self.get_body_params().get('Status')

	def set_Status(self,Status):
		self.add_body_params('Status', Status)

	def get_Dimensionss(self):
		return self.get_body_params().get('Dimensions')

	def set_Dimensionss(self, Dimensionss):
		for depth1 in range(len(Dimensionss)):
			if Dimensionss[depth1].get('Key') is not None:
				self.add_body_params('Dimensions.' + str(depth1 + 1) + '.Key', Dimensionss[depth1].get('Key'))
			if Dimensionss[depth1].get('Value') is not None:
				self.add_body_params('Dimensions.' + str(depth1 + 1) + '.Value', Dimensionss[depth1].get('Value'))