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
import json

class ListSitesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'ListSites')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_Coverage(self): # String
		return self.get_query_params().get('Coverage')

	def set_Coverage(self, Coverage):  # String
		self.add_query_param('Coverage', Coverage)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_AccessType(self): # String
		return self.get_query_params().get('AccessType')

	def set_AccessType(self, AccessType):  # String
		self.add_query_param('AccessType', AccessType)
	def get_OnlyEnterprise(self): # Boolean
		return self.get_query_params().get('OnlyEnterprise')

	def set_OnlyEnterprise(self, OnlyEnterprise):  # Boolean
		self.add_query_param('OnlyEnterprise', OnlyEnterprise)
	def get_PlanSubscribeType(self): # String
		return self.get_query_params().get('PlanSubscribeType')

	def set_PlanSubscribeType(self, PlanSubscribeType):  # String
		self.add_query_param('PlanSubscribeType', PlanSubscribeType)
	def get_SiteSearchType(self): # String
		return self.get_query_params().get('SiteSearchType')

	def set_SiteSearchType(self, SiteSearchType):  # String
		self.add_query_param('SiteSearchType', SiteSearchType)
	def get_SiteName(self): # String
		return self.get_query_params().get('SiteName')

	def set_SiteName(self, SiteName):  # String
		self.add_query_param('SiteName', SiteName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_TagFilter(self): # Array
		return self.get_query_params().get('TagFilter')

	def set_TagFilter(self, TagFilter):  # Array
		self.add_query_param("TagFilter", json.dumps(TagFilter))
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
