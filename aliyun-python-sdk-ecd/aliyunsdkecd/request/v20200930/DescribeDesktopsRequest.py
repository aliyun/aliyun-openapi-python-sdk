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

class DescribeDesktopsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'DescribeDesktops')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OfficeSiteId(self): # String
		return self.get_query_params().get('OfficeSiteId')

	def set_OfficeSiteId(self, OfficeSiteId):  # String
		self.add_query_param('OfficeSiteId', OfficeSiteId)
	def get_SnapshotPolicyId(self): # String
		return self.get_query_params().get('SnapshotPolicyId')

	def set_SnapshotPolicyId(self, SnapshotPolicyId):  # String
		self.add_query_param('SnapshotPolicyId', SnapshotPolicyId)
	def get_DesktopStatus(self): # String
		return self.get_query_params().get('DesktopStatus')

	def set_DesktopStatus(self, DesktopStatus):  # String
		self.add_query_param('DesktopStatus', DesktopStatus)
	def get_DesktopGroupId(self): # String
		return self.get_query_params().get('DesktopGroupId')

	def set_DesktopGroupId(self, DesktopGroupId):  # String
		self.add_query_param('DesktopGroupId', DesktopGroupId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_OnlyDesktopGroup(self): # Boolean
		return self.get_query_params().get('OnlyDesktopGroup')

	def set_OnlyDesktopGroup(self, OnlyDesktopGroup):  # Boolean
		self.add_query_param('OnlyDesktopGroup', OnlyDesktopGroup)
	def get_QueryFotaUpdate(self): # Boolean
		return self.get_query_params().get('QueryFotaUpdate')

	def set_QueryFotaUpdate(self, QueryFotaUpdate):  # Boolean
		self.add_query_param('QueryFotaUpdate', QueryFotaUpdate)
	def get_DirectoryId(self): # String
		return self.get_query_params().get('DirectoryId')

	def set_DirectoryId(self, DirectoryId):  # String
		self.add_query_param('DirectoryId', DirectoryId)
	def get_EndUserIds(self): # RepeatList
		return self.get_query_params().get('EndUserId')

	def set_EndUserIds(self, EndUserId):  # RepeatList
		for depth1 in range(len(EndUserId)):
			self.add_query_param('EndUserId.' + str(depth1 + 1), EndUserId[depth1])
	def get_DesktopIds(self): # RepeatList
		return self.get_query_params().get('DesktopId')

	def set_DesktopIds(self, DesktopId):  # RepeatList
		for depth1 in range(len(DesktopId)):
			self.add_query_param('DesktopId.' + str(depth1 + 1), DesktopId[depth1])
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_DesktopName(self): # String
		return self.get_query_params().get('DesktopName')

	def set_DesktopName(self, DesktopName):  # String
		self.add_query_param('DesktopName', DesktopName)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_OfficeSiteName(self): # String
		return self.get_query_params().get('OfficeSiteName')

	def set_OfficeSiteName(self, OfficeSiteName):  # String
		self.add_query_param('OfficeSiteName', OfficeSiteName)
	def get_ExcludedEndUserIds(self): # RepeatList
		return self.get_query_params().get('ExcludedEndUserId')

	def set_ExcludedEndUserIds(self, ExcludedEndUserId):  # RepeatList
		for depth1 in range(len(ExcludedEndUserId)):
			self.add_query_param('ExcludedEndUserId.' + str(depth1 + 1), ExcludedEndUserId[depth1])
	def get_FilterDesktopGroup(self): # Boolean
		return self.get_query_params().get('FilterDesktopGroup')

	def set_FilterDesktopGroup(self, FilterDesktopGroup):  # Boolean
		self.add_query_param('FilterDesktopGroup', FilterDesktopGroup)
	def get_ManagementFlag(self): # String
		return self.get_query_params().get('ManagementFlag')

	def set_ManagementFlag(self, ManagementFlag):  # String
		self.add_query_param('ManagementFlag', ManagementFlag)
	def get_ExpiredTime(self): # String
		return self.get_query_params().get('ExpiredTime')

	def set_ExpiredTime(self, ExpiredTime):  # String
		self.add_query_param('ExpiredTime', ExpiredTime)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_OsTypess(self): # RepeatList
		return self.get_query_params().get('OsTypes')

	def set_OsTypess(self, OsTypes):  # RepeatList
		for depth1 in range(len(OsTypes)):
			self.add_query_param('OsTypes.' + str(depth1 + 1), OsTypes[depth1])
	def get_ProtocolType(self): # String
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self, ProtocolType):  # String
		self.add_query_param('ProtocolType', ProtocolType)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_PolicyGroupId(self): # String
		return self.get_query_params().get('PolicyGroupId')

	def set_PolicyGroupId(self, PolicyGroupId):  # String
		self.add_query_param('PolicyGroupId', PolicyGroupId)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
