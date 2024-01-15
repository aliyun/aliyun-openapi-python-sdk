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
from aliyunsdkiot.endpoint import endpoint_data

class CreateOTAStaticUpgradeJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateOTAStaticUpgradeJob','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MultiModuleMode(self):
		return self.get_query_params().get('MultiModuleMode')

	def set_MultiModuleMode(self,MultiModuleMode):
		self.add_query_param('MultiModuleMode',MultiModuleMode)

	def get_RetryCount(self):
		return self.get_query_params().get('RetryCount')

	def set_RetryCount(self,RetryCount):
		self.add_query_param('RetryCount',RetryCount)

	def get_TimeoutInMinutes(self):
		return self.get_query_params().get('TimeoutInMinutes')

	def set_TimeoutInMinutes(self,TimeoutInMinutes):
		self.add_query_param('TimeoutInMinutes',TimeoutInMinutes)

	def get_NeedConfirm(self):
		return self.get_query_params().get('NeedConfirm')

	def set_NeedConfirm(self,NeedConfirm):
		self.add_query_param('NeedConfirm',NeedConfirm)

	def get_GroupType(self):
		return self.get_query_params().get('GroupType')

	def set_GroupType(self,GroupType):
		self.add_query_param('GroupType',GroupType)

	def get_NeedPush(self):
		return self.get_query_params().get('NeedPush')

	def set_NeedPush(self,NeedPush):
		self.add_query_param('NeedPush',NeedPush)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_DownloadProtocol(self):
		return self.get_query_params().get('DownloadProtocol')

	def set_DownloadProtocol(self,DownloadProtocol):
		self.add_query_param('DownloadProtocol',DownloadProtocol)

	def get_TargetSelection(self):
		return self.get_query_params().get('TargetSelection')

	def set_TargetSelection(self,TargetSelection):
		self.add_query_param('TargetSelection',TargetSelection)

	def get_ScheduleFinishTime(self):
		return self.get_query_params().get('ScheduleFinishTime')

	def set_ScheduleFinishTime(self,ScheduleFinishTime):
		self.add_query_param('ScheduleFinishTime',ScheduleFinishTime)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_GrayPercent(self):
		return self.get_query_params().get('GrayPercent')

	def set_GrayPercent(self,GrayPercent):
		self.add_query_param('GrayPercent',GrayPercent)

	def get_DnListFileUrl(self):
		return self.get_query_params().get('DnListFileUrl')

	def set_DnListFileUrl(self,DnListFileUrl):
		self.add_query_param('DnListFileUrl',DnListFileUrl)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_FirmwareId(self):
		return self.get_query_params().get('FirmwareId')

	def set_FirmwareId(self,FirmwareId):
		self.add_query_param('FirmwareId',FirmwareId)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_RetryInterval(self):
		return self.get_query_params().get('RetryInterval')

	def set_RetryInterval(self,RetryInterval):
		self.add_query_param('RetryInterval',RetryInterval)

	def get_SrcVersions(self):
		return self.get_query_params().get('SrcVersion')

	def set_SrcVersions(self, SrcVersions):
		for depth1 in range(len(SrcVersions)):
			if SrcVersions[depth1] is not None:
				self.add_query_param('SrcVersion.' + str(depth1 + 1) , SrcVersions[depth1])

	def get_ScheduleTime(self):
		return self.get_query_params().get('ScheduleTime')

	def set_ScheduleTime(self,ScheduleTime):
		self.add_query_param('ScheduleTime',ScheduleTime)

	def get_OverwriteMode(self):
		return self.get_query_params().get('OverwriteMode')

	def set_OverwriteMode(self,OverwriteMode):
		self.add_query_param('OverwriteMode',OverwriteMode)

	def get_MaximumPerMinute(self):
		return self.get_query_params().get('MaximumPerMinute')

	def set_MaximumPerMinute(self,MaximumPerMinute):
		self.add_query_param('MaximumPerMinute',MaximumPerMinute)

	def get_TargetDeviceNames(self):
		return self.get_query_params().get('TargetDeviceName')

	def set_TargetDeviceNames(self, TargetDeviceNames):
		for depth1 in range(len(TargetDeviceNames)):
			if TargetDeviceNames[depth1] is not None:
				self.add_query_param('TargetDeviceName.' + str(depth1 + 1) , TargetDeviceNames[depth1])