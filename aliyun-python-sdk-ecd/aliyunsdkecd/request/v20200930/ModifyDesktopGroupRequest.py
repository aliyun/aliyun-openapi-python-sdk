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

class ModifyDesktopGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'ModifyDesktopGroup')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Classify(self): # String
		return self.get_query_params().get('Classify')

	def set_Classify(self, Classify):  # String
		self.add_query_param('Classify', Classify)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_ScaleStrategyId(self): # String
		return self.get_query_params().get('ScaleStrategyId')

	def set_ScaleStrategyId(self, ScaleStrategyId):  # String
		self.add_query_param('ScaleStrategyId', ScaleStrategyId)
	def get_DisableSessionConfig(self): # Boolean
		return self.get_query_params().get('DisableSessionConfig')

	def set_DisableSessionConfig(self, DisableSessionConfig):  # Boolean
		self.add_query_param('DisableSessionConfig', DisableSessionConfig)
	def get_BindAmount(self): # Long
		return self.get_query_params().get('BindAmount')

	def set_BindAmount(self, BindAmount):  # Long
		self.add_query_param('BindAmount', BindAmount)
	def get_LoadPolicy(self): # Long
		return self.get_query_params().get('LoadPolicy')

	def set_LoadPolicy(self, LoadPolicy):  # Long
		self.add_query_param('LoadPolicy', LoadPolicy)
	def get_DesktopGroupName(self): # String
		return self.get_query_params().get('DesktopGroupName')

	def set_DesktopGroupName(self, DesktopGroupName):  # String
		self.add_query_param('DesktopGroupName', DesktopGroupName)
	def get_AllowBufferCount(self): # Integer
		return self.get_query_params().get('AllowBufferCount')

	def set_AllowBufferCount(self, AllowBufferCount):  # Integer
		self.add_query_param('AllowBufferCount', AllowBufferCount)
	def get_PolicyGroupIdss(self): # RepeatList
		return self.get_query_params().get('PolicyGroupIds')

	def set_PolicyGroupIdss(self, PolicyGroupIds):  # RepeatList
		for depth1 in range(len(PolicyGroupIds)):
			self.add_query_param('PolicyGroupIds.' + str(depth1 + 1), PolicyGroupIds[depth1])
	def get_IdleDisconnectDuration(self): # Long
		return self.get_query_params().get('IdleDisconnectDuration')

	def set_IdleDisconnectDuration(self, IdleDisconnectDuration):  # Long
		self.add_query_param('IdleDisconnectDuration', IdleDisconnectDuration)
	def get_DesktopGroupId(self): # String
		return self.get_query_params().get('DesktopGroupId')

	def set_DesktopGroupId(self, DesktopGroupId):  # String
		self.add_query_param('DesktopGroupId', DesktopGroupId)
	def get_MinDesktopsCount(self): # Integer
		return self.get_query_params().get('MinDesktopsCount')

	def set_MinDesktopsCount(self, MinDesktopsCount):  # Integer
		self.add_query_param('MinDesktopsCount', MinDesktopsCount)
	def get_MaxDesktopsCount(self): # Integer
		return self.get_query_params().get('MaxDesktopsCount')

	def set_MaxDesktopsCount(self, MaxDesktopsCount):  # Integer
		self.add_query_param('MaxDesktopsCount', MaxDesktopsCount)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
	def get_AllowAutoSetup(self): # Integer
		return self.get_query_params().get('AllowAutoSetup')

	def set_AllowAutoSetup(self, AllowAutoSetup):  # Integer
		self.add_query_param('AllowAutoSetup', AllowAutoSetup)
	def get_Comments(self): # String
		return self.get_query_params().get('Comments')

	def set_Comments(self, Comments):  # String
		self.add_query_param('Comments', Comments)
	def get_ResetType(self): # Long
		return self.get_query_params().get('ResetType')

	def set_ResetType(self, ResetType):  # Long
		self.add_query_param('ResetType', ResetType)
	def get_OwnBundleId(self): # String
		return self.get_query_params().get('OwnBundleId')

	def set_OwnBundleId(self, OwnBundleId):  # String
		self.add_query_param('OwnBundleId', OwnBundleId)
	def get_StopDuration(self): # Long
		return self.get_query_params().get('StopDuration')

	def set_StopDuration(self, StopDuration):  # Long
		self.add_query_param('StopDuration', StopDuration)
	def get_RatioThreshold(self): # Float
		return self.get_query_params().get('RatioThreshold')

	def set_RatioThreshold(self, RatioThreshold):  # Float
		self.add_query_param('RatioThreshold', RatioThreshold)
	def get_KeepDuration(self): # Long
		return self.get_query_params().get('KeepDuration')

	def set_KeepDuration(self, KeepDuration):  # Long
		self.add_query_param('KeepDuration', KeepDuration)
	def get_ConnectDuration(self): # Long
		return self.get_query_params().get('ConnectDuration')

	def set_ConnectDuration(self, ConnectDuration):  # Long
		self.add_query_param('ConnectDuration', ConnectDuration)
	def get_ProfileFollowSwitch(self): # Boolean
		return self.get_query_params().get('ProfileFollowSwitch')

	def set_ProfileFollowSwitch(self, ProfileFollowSwitch):  # Boolean
		self.add_query_param('ProfileFollowSwitch', ProfileFollowSwitch)
	def get_PolicyGroupId(self): # String
		return self.get_query_params().get('PolicyGroupId')

	def set_PolicyGroupId(self, PolicyGroupId):  # String
		self.add_query_param('PolicyGroupId', PolicyGroupId)
