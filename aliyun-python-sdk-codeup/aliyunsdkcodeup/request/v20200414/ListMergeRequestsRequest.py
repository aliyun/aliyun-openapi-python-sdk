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

from aliyunsdkcore.request import RoaRequest

class ListMergeRequestsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'codeup', '2020-04-14', 'ListMergeRequests')
		self.set_uri_pattern('/api/v4/merge_requests/advanced_search')
		self.set_method('GET')

	def get_BeforeDate(self):
		return self.get_query_params().get('BeforeDate')

	def set_BeforeDate(self,BeforeDate):
		self.add_query_param('BeforeDate',BeforeDate)

	def get_AssigneeIdList(self):
		return self.get_query_params().get('AssigneeIdList')

	def set_AssigneeIdList(self,AssigneeIdList):
		self.add_query_param('AssigneeIdList',AssigneeIdList)

	def get_AccessToken(self):
		return self.get_query_params().get('AccessToken')

	def set_AccessToken(self,AccessToken):
		self.add_query_param('AccessToken',AccessToken)

	def get_SubscriberCodeupIdList(self):
		return self.get_query_params().get('SubscriberCodeupIdList')

	def set_SubscriberCodeupIdList(self,SubscriberCodeupIdList):
		self.add_query_param('SubscriberCodeupIdList',SubscriberCodeupIdList)

	def get_AfterDate(self):
		return self.get_query_params().get('AfterDate')

	def set_AfterDate(self,AfterDate):
		self.add_query_param('AfterDate',AfterDate)

	def get_OrganizationId(self):
		return self.get_query_params().get('OrganizationId')

	def set_OrganizationId(self,OrganizationId):
		self.add_query_param('OrganizationId',OrganizationId)

	def get_GroupIdList(self):
		return self.get_query_params().get('GroupIdList')

	def set_GroupIdList(self,GroupIdList):
		self.add_query_param('GroupIdList',GroupIdList)

	def get_Search(self):
		return self.get_query_params().get('Search')

	def set_Search(self,Search):
		self.add_query_param('Search',Search)

	def get_AuthorCodeupIdList(self):
		return self.get_query_params().get('AuthorCodeupIdList')

	def set_AuthorCodeupIdList(self,AuthorCodeupIdList):
		self.add_query_param('AuthorCodeupIdList',AuthorCodeupIdList)

	def get_AuthorIdList(self):
		return self.get_query_params().get('AuthorIdList')

	def set_AuthorIdList(self,AuthorIdList):
		self.add_query_param('AuthorIdList',AuthorIdList)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ProjectIdList(self):
		return self.get_query_params().get('ProjectIdList')

	def set_ProjectIdList(self,ProjectIdList):
		self.add_query_param('ProjectIdList',ProjectIdList)

	def get_Page(self):
		return self.get_query_params().get('Page')

	def set_Page(self,Page):
		self.add_query_param('Page',Page)

	def get_AssigneeCodeupIdList(self):
		return self.get_query_params().get('AssigneeCodeupIdList')

	def set_AssigneeCodeupIdList(self,AssigneeCodeupIdList):
		self.add_query_param('AssigneeCodeupIdList',AssigneeCodeupIdList)

	def get_State(self):
		return self.get_query_params().get('State')

	def set_State(self,State):
		self.add_query_param('State',State)

	def get_Order(self):
		return self.get_query_params().get('Order')

	def set_Order(self,Order):
		self.add_query_param('Order',Order)