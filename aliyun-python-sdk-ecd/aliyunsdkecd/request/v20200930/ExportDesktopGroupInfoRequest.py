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

class ExportDesktopGroupInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'ExportDesktopGroupInfo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OfficeSiteId(self): # String
		return self.get_query_params().get('OfficeSiteId')

	def set_OfficeSiteId(self, OfficeSiteId):  # String
		self.add_query_param('OfficeSiteId', OfficeSiteId)
	def get_DesktopGroupName(self): # String
		return self.get_query_params().get('DesktopGroupName')

	def set_DesktopGroupName(self, DesktopGroupName):  # String
		self.add_query_param('DesktopGroupName', DesktopGroupName)
	def get_DesktopGroupIds(self): # RepeatList
		return self.get_query_params().get('DesktopGroupId')

	def set_DesktopGroupIds(self, DesktopGroupId):  # RepeatList
		for depth1 in range(len(DesktopGroupId)):
			self.add_query_param('DesktopGroupId.' + str(depth1 + 1), DesktopGroupId[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_EndUserIds(self): # RepeatList
		return self.get_query_params().get('EndUserId')

	def set_EndUserIds(self, EndUserId):  # RepeatList
		for depth1 in range(len(EndUserId)):
			self.add_query_param('EndUserId.' + str(depth1 + 1), EndUserId[depth1])
	def get_ExpiredTime(self): # String
		return self.get_query_params().get('ExpiredTime')

	def set_ExpiredTime(self, ExpiredTime):  # String
		self.add_query_param('ExpiredTime', ExpiredTime)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_LangType(self): # String
		return self.get_query_params().get('LangType')

	def set_LangType(self, LangType):  # String
		self.add_query_param('LangType', LangType)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_PolicyGroupId(self): # String
		return self.get_query_params().get('PolicyGroupId')

	def set_PolicyGroupId(self, PolicyGroupId):  # String
		self.add_query_param('PolicyGroupId', PolicyGroupId)
