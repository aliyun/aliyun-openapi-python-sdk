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

class FilterUsersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eds-user', '2021-03-08', 'FilterUsers','eds-user')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IsQueryAllSubOrgs(self): # Boolean
		return self.get_query_params().get('IsQueryAllSubOrgs')

	def set_IsQueryAllSubOrgs(self, IsQueryAllSubOrgs):  # Boolean
		self.add_query_param('IsQueryAllSubOrgs', IsQueryAllSubOrgs)
	def get_OrderParam(self): # Struct
		return self.get_query_params().get('OrderParam')

	def set_OrderParam(self, OrderParam):  # Struct
		self.add_query_param("OrderParam", json.dumps(OrderParam))
	def get_ExcludeEndUserIdss(self): # RepeatList
		return self.get_query_params().get('ExcludeEndUserIds')

	def set_ExcludeEndUserIdss(self, ExcludeEndUserIds):  # RepeatList
		for depth1 in range(len(ExcludeEndUserIds)):
			self.add_query_param('ExcludeEndUserIds.' + str(depth1 + 1), ExcludeEndUserIds[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_IncludeDesktopCount(self): # Boolean
		return self.get_query_params().get('IncludeDesktopCount')

	def set_IncludeDesktopCount(self, IncludeDesktopCount):  # Boolean
		self.add_query_param('IncludeDesktopCount', IncludeDesktopCount)
	def get_IncludeSupportIdps(self): # Boolean
		return self.get_query_params().get('IncludeSupportIdps')

	def set_IncludeSupportIdps(self, IncludeSupportIdps):  # Boolean
		self.add_query_param('IncludeSupportIdps', IncludeSupportIdps)
	def get_PropertyFilterParams(self): # RepeatList
		return self.get_query_params().get('PropertyFilterParam')

	def set_PropertyFilterParams(self, PropertyFilterParam):  # RepeatList
		for depth1 in range(len(PropertyFilterParam)):
			if PropertyFilterParam[depth1].get('PropertyId') is not None:
				self.add_query_param('PropertyFilterParam.' + str(depth1 + 1) + '.PropertyId', PropertyFilterParam[depth1].get('PropertyId'))
			if PropertyFilterParam[depth1].get('PropertyValueIds') is not None:
				self.add_query_param('PropertyFilterParam.' + str(depth1 + 1) + '.PropertyValueIds', PropertyFilterParam[depth1].get('PropertyValueIds'))
	def get_IncludeOrgInfo(self): # Boolean
		return self.get_query_params().get('IncludeOrgInfo')

	def set_IncludeOrgInfo(self, IncludeOrgInfo):  # Boolean
		self.add_query_param('IncludeOrgInfo', IncludeOrgInfo)
	def get_IncludeDesktopGroupCount(self): # Boolean
		return self.get_query_params().get('IncludeDesktopGroupCount')

	def set_IncludeDesktopGroupCount(self, IncludeDesktopGroupCount):  # Boolean
		self.add_query_param('IncludeDesktopGroupCount', IncludeDesktopGroupCount)
	def get_OrgId(self): # String
		return self.get_query_params().get('OrgId')

	def set_OrgId(self, OrgId):  # String
		self.add_query_param('OrgId', OrgId)
	def get_Filter(self): # String
		return self.get_query_params().get('Filter')

	def set_Filter(self, Filter):  # String
		self.add_query_param('Filter', Filter)
	def get_PropertyKeyValueFilterParams(self): # RepeatList
		return self.get_query_params().get('PropertyKeyValueFilterParam')

	def set_PropertyKeyValueFilterParams(self, PropertyKeyValueFilterParam):  # RepeatList
		for depth1 in range(len(PropertyKeyValueFilterParam)):
			if PropertyKeyValueFilterParam[depth1].get('PropertyKey') is not None:
				self.add_query_param('PropertyKeyValueFilterParam.' + str(depth1 + 1) + '.PropertyKey', PropertyKeyValueFilterParam[depth1].get('PropertyKey'))
			if PropertyKeyValueFilterParam[depth1].get('PropertyValues') is not None:
				self.add_query_param('PropertyKeyValueFilterParam.' + str(depth1 + 1) + '.PropertyValues', PropertyKeyValueFilterParam[depth1].get('PropertyValues'))
	def get_OwnerType(self): # String
		return self.get_query_params().get('OwnerType')

	def set_OwnerType(self, OwnerType):  # String
		self.add_query_param('OwnerType', OwnerType)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
