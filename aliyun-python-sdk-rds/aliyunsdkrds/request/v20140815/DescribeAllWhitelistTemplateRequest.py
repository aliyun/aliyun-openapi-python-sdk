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
from aliyunsdkrds.endpoint import endpoint_data

class DescribeAllWhitelistTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'DescribeAllWhitelistTemplate')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_PageNumbers(self): # Integer
		return self.get_query_params().get('PageNumbers')

	def set_PageNumbers(self, PageNumbers):  # Integer
		self.add_query_param('PageNumbers', PageNumbers)
	def get_TemplateName(self): # String
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self, TemplateName):  # String
		self.add_query_param('TemplateName', TemplateName)
	def get_FuzzySearch(self): # Boolean
		return self.get_query_params().get('FuzzySearch')

	def set_FuzzySearch(self, FuzzySearch):  # Boolean
		self.add_query_param('FuzzySearch', FuzzySearch)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_MaxRecordsPerPage(self): # Integer
		return self.get_query_params().get('MaxRecordsPerPage')

	def set_MaxRecordsPerPage(self, MaxRecordsPerPage):  # Integer
		self.add_query_param('MaxRecordsPerPage', MaxRecordsPerPage)
