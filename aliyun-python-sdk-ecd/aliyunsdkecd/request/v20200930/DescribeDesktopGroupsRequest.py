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
from aliyunsdkecd.endpoint import endpoint_data

class DescribeDesktopGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'DescribeDesktopGroups')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OfficeSiteId(self): # String
		return self.get_query_params().get('OfficeSiteId')

	def set_OfficeSiteId(self, OfficeSiteId):  # String
		self.add_query_param('OfficeSiteId', OfficeSiteId)
	def get_EndUserIdss(self): # RepeatList
		return self.get_query_params().get('EndUserIds')

	def set_EndUserIdss(self, EndUserIds):  # RepeatList
		for depth1 in range(len(EndUserIds)):
			self.add_query_param('EndUserIds.' + str(depth1 + 1), EndUserIds[depth1])
	def get_DesktopGroupName(self): # String
		return self.get_query_params().get('DesktopGroupName')

	def set_DesktopGroupName(self, DesktopGroupName):  # String
		self.add_query_param('DesktopGroupName', DesktopGroupName)
	def get_DesktopGroupId(self): # String
		return self.get_query_params().get('DesktopGroupId')

	def set_DesktopGroupId(self, DesktopGroupId):  # String
		self.add_query_param('DesktopGroupId', DesktopGroupId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_OwnType(self): # Long
		return self.get_query_params().get('OwnType')

	def set_OwnType(self, OwnType):  # Long
		self.add_query_param('OwnType', OwnType)
	def get_ExcludedEndUserIdss(self): # RepeatList
		return self.get_query_params().get('ExcludedEndUserIds')

	def set_ExcludedEndUserIdss(self, ExcludedEndUserIds):  # RepeatList
		for depth1 in range(len(ExcludedEndUserIds)):
			self.add_query_param('ExcludedEndUserIds.' + str(depth1 + 1), ExcludedEndUserIds[depth1])
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_ProtocolType(self): # String
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self, ProtocolType):  # String
		self.add_query_param('ProtocolType', ProtocolType)
	def get_PolicyGroupId(self): # String
		return self.get_query_params().get('PolicyGroupId')

	def set_PolicyGroupId(self, PolicyGroupId):  # String
		self.add_query_param('PolicyGroupId', PolicyGroupId)
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
