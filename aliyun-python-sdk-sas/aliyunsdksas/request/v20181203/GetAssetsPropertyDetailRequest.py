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
from aliyunsdksas.endpoint import endpoint_data

class GetAssetsPropertyDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'GetAssetsPropertyDetail','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_Biz(self): # String
		return self.get_query_params().get('Biz')

	def set_Biz(self, Biz):  # String
		self.add_query_param('Biz', Biz)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_SearchCriteriaLists(self): # RepeatList
		return self.get_query_params().get('SearchCriteriaList')

	def set_SearchCriteriaLists(self, SearchCriteriaList):  # RepeatList
		for depth1 in range(len(SearchCriteriaList)):
			if SearchCriteriaList[depth1].get('Name') is not None:
				self.add_query_param('SearchCriteriaList.' + str(depth1 + 1) + '.Name', SearchCriteriaList[depth1].get('Name'))
			if SearchCriteriaList[depth1].get('Value') is not None:
				self.add_query_param('SearchCriteriaList.' + str(depth1 + 1) + '.Value', SearchCriteriaList[depth1].get('Value'))
	def get_ItemName(self): # String
		return self.get_query_params().get('ItemName')

	def set_ItemName(self, ItemName):  # String
		self.add_query_param('ItemName', ItemName)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
