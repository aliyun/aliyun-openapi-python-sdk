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
from aliyunsdkeds_user.endpoint import endpoint_data
import json

class DescribeUsersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eds-user', '2021-03-08', 'DescribeUsers','eds-user')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IsQueryAllSubOrgs(self): # Boolean
		return self.get_body_params().get('IsQueryAllSubOrgs')

	def set_IsQueryAllSubOrgs(self, IsQueryAllSubOrgs):  # Boolean
		self.add_body_params('IsQueryAllSubOrgs', IsQueryAllSubOrgs)
	def get_EndUserIdss(self): # RepeatList
		return self.get_body_params().get('EndUserIds')

	def set_EndUserIdss(self, EndUserIds):  # RepeatList
		for depth1 in range(len(EndUserIds)):
			self.add_body_params('EndUserIds.' + str(depth1 + 1), EndUserIds[depth1])
	def get_ExcludeEndUserIdss(self): # RepeatList
		return self.get_body_params().get('ExcludeEndUserIds')

	def set_ExcludeEndUserIdss(self, ExcludeEndUserIds):  # RepeatList
		for depth1 in range(len(ExcludeEndUserIds)):
			self.add_body_params('ExcludeEndUserIds.' + str(depth1 + 1), ExcludeEndUserIds[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_SolutionId(self): # String
		return self.get_body_params().get('SolutionId')

	def set_SolutionId(self, SolutionId):  # String
		self.add_body_params('SolutionId', SolutionId)
	def get_FilterWithAssignedResources(self): # Map
		return self.get_body_params().get('FilterWithAssignedResources')

	def set_FilterWithAssignedResources(self, FilterWithAssignedResources):  # Map
		self.add_body_params("FilterWithAssignedResources", json.dumps(FilterWithAssignedResources))
	def get_GroupId(self): # String
		return self.get_body_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_body_params('GroupId', GroupId)
	def get_OrgId(self): # String
		return self.get_body_params().get('OrgId')

	def set_OrgId(self, OrgId):  # String
		self.add_body_params('OrgId', OrgId)
	def get_FilterWithAssignedResource(self): # Map
		return self.get_query_params().get('FilterWithAssignedResource')

	def set_FilterWithAssignedResource(self, FilterWithAssignedResource):  # Map
		self.add_query_param("FilterWithAssignedResource", json.dumps(FilterWithAssignedResource))
	def get_Filter(self): # String
		return self.get_query_params().get('Filter')

	def set_Filter(self, Filter):  # String
		self.add_query_param('Filter', Filter)
	def get_BizType(self): # String
		return self.get_body_params().get('BizType')

	def set_BizType(self, BizType):  # String
		self.add_body_params('BizType', BizType)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
	def get_ShowExtras(self): # Map
		return self.get_body_params().get('ShowExtras')

	def set_ShowExtras(self, ShowExtras):  # Map
		self.add_body_params("ShowExtras", json.dumps(ShowExtras))
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
