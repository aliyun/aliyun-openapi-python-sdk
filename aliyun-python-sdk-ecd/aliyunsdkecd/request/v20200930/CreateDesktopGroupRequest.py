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

class CreateDesktopGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'CreateDesktopGroup')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DesktopGroupName(self): # String
		return self.get_query_params().get('DesktopGroupName')

	def set_DesktopGroupName(self, DesktopGroupName):  # String
		self.add_query_param('DesktopGroupName', DesktopGroupName)
	def get_AllowBufferCount(self): # Integer
		return self.get_query_params().get('AllowBufferCount')

	def set_AllowBufferCount(self, AllowBufferCount):  # Integer
		self.add_query_param('AllowBufferCount', AllowBufferCount)
	def get_AllClassifyUsers(self): # Boolean
		return self.get_query_params().get('AllClassifyUsers')

	def set_AllClassifyUsers(self, AllClassifyUsers):  # Boolean
		self.add_query_param('AllClassifyUsers', AllClassifyUsers)
	def get_MaxDesktopsCount(self): # Integer
		return self.get_query_params().get('MaxDesktopsCount')

	def set_MaxDesktopsCount(self, MaxDesktopsCount):  # Integer
		self.add_query_param('MaxDesktopsCount', MaxDesktopsCount)
	def get_VolumeEncryptionEnabled(self): # Boolean
		return self.get_query_params().get('VolumeEncryptionEnabled')

	def set_VolumeEncryptionEnabled(self, VolumeEncryptionEnabled):  # Boolean
		self.add_query_param('VolumeEncryptionEnabled', VolumeEncryptionEnabled)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_AllowAutoSetup(self): # Integer
		return self.get_query_params().get('AllowAutoSetup')

	def set_AllowAutoSetup(self, AllowAutoSetup):  # Integer
		self.add_query_param('AllowAutoSetup', AllowAutoSetup)
	def get_ResetType(self): # Long
		return self.get_query_params().get('ResetType')

	def set_ResetType(self, ResetType):  # Long
		self.add_query_param('ResetType', ResetType)
	def get_RatioThreshold(self): # Float
		return self.get_query_params().get('RatioThreshold')

	def set_RatioThreshold(self, RatioThreshold):  # Float
		self.add_query_param('RatioThreshold', RatioThreshold)
	def get_KeepDuration(self): # Long
		return self.get_query_params().get('KeepDuration')

	def set_KeepDuration(self, KeepDuration):  # Long
		self.add_query_param('KeepDuration', KeepDuration)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_ProfileFollowSwitch(self): # Boolean
		return self.get_query_params().get('ProfileFollowSwitch')

	def set_ProfileFollowSwitch(self, ProfileFollowSwitch):  # Boolean
		self.add_query_param('ProfileFollowSwitch', ProfileFollowSwitch)
	def get_PolicyGroupId(self): # String
		return self.get_query_params().get('PolicyGroupId')

	def set_PolicyGroupId(self, PolicyGroupId):  # String
		self.add_query_param('PolicyGroupId', PolicyGroupId)
	def get_VolumeEncryptionKey(self): # String
		return self.get_query_params().get('VolumeEncryptionKey')

	def set_VolumeEncryptionKey(self, VolumeEncryptionKey):  # String
		self.add_query_param('VolumeEncryptionKey', VolumeEncryptionKey)
	def get_OfficeSiteId(self): # String
		return self.get_query_params().get('OfficeSiteId')

	def set_OfficeSiteId(self, OfficeSiteId):  # String
		self.add_query_param('OfficeSiteId', OfficeSiteId)
	def get_Classify(self): # String
		return self.get_query_params().get('Classify')

	def set_Classify(self, Classify):  # String
		self.add_query_param('Classify', Classify)
	def get_EndUserIdss(self): # RepeatList
		return self.get_query_params().get('EndUserIds')

	def set_EndUserIdss(self, EndUserIds):  # RepeatList
		for depth1 in range(len(EndUserIds)):
			self.add_query_param('EndUserIds.' + str(depth1 + 1), EndUserIds[depth1])
	def get_ScaleStrategyId(self): # String
		return self.get_query_params().get('ScaleStrategyId')

	def set_ScaleStrategyId(self, ScaleStrategyId):  # String
		self.add_query_param('ScaleStrategyId', ScaleStrategyId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_BundleId(self): # String
		return self.get_query_params().get('BundleId')

	def set_BundleId(self, BundleId):  # String
		self.add_query_param('BundleId', BundleId)
	def get_BindAmount(self): # Long
		return self.get_query_params().get('BindAmount')

	def set_BindAmount(self, BindAmount):  # Long
		self.add_query_param('BindAmount', BindAmount)
	def get_LoadPolicy(self): # Long
		return self.get_query_params().get('LoadPolicy')

	def set_LoadPolicy(self, LoadPolicy):  # Long
		self.add_query_param('LoadPolicy', LoadPolicy)
	def get_DefaultInitDesktopCount(self): # Integer
		return self.get_query_params().get('DefaultInitDesktopCount')

	def set_DefaultInitDesktopCount(self, DefaultInitDesktopCount):  # Integer
		self.add_query_param('DefaultInitDesktopCount', DefaultInitDesktopCount)
	def get_IdleDisconnectDuration(self): # Long
		return self.get_query_params().get('IdleDisconnectDuration')

	def set_IdleDisconnectDuration(self, IdleDisconnectDuration):  # Long
		self.add_query_param('IdleDisconnectDuration', IdleDisconnectDuration)
	def get_DirectoryId(self): # String
		return self.get_query_params().get('DirectoryId')

	def set_DirectoryId(self, DirectoryId):  # String
		self.add_query_param('DirectoryId', DirectoryId)
	def get_MinDesktopsCount(self): # Integer
		return self.get_query_params().get('MinDesktopsCount')

	def set_MinDesktopsCount(self, MinDesktopsCount):  # Integer
		self.add_query_param('MinDesktopsCount', MinDesktopsCount)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_Comments(self): # String
		return self.get_query_params().get('Comments')

	def set_Comments(self, Comments):  # String
		self.add_query_param('Comments', Comments)
	def get_OwnType(self): # Integer
		return self.get_query_params().get('OwnType')

	def set_OwnType(self, OwnType):  # Integer
		self.add_query_param('OwnType', OwnType)
	def get_StopDuration(self): # Long
		return self.get_query_params().get('StopDuration')

	def set_StopDuration(self, StopDuration):  # Long
		self.add_query_param('StopDuration', StopDuration)
	def get_ConnectDuration(self): # Long
		return self.get_query_params().get('ConnectDuration')

	def set_ConnectDuration(self, ConnectDuration):  # Long
		self.add_query_param('ConnectDuration', ConnectDuration)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
