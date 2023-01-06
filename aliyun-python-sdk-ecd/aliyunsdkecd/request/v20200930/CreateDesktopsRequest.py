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

class CreateDesktopsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'CreateDesktops')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_VolumeEncryptionKey(self): # String
		return self.get_query_params().get('VolumeEncryptionKey')

	def set_VolumeEncryptionKey(self, VolumeEncryptionKey):  # String
		self.add_query_param('VolumeEncryptionKey', VolumeEncryptionKey)
	def get_OfficeSiteId(self): # String
		return self.get_query_params().get('OfficeSiteId')

	def set_OfficeSiteId(self, OfficeSiteId):  # String
		self.add_query_param('OfficeSiteId', OfficeSiteId)
	def get_BundleId(self): # String
		return self.get_query_params().get('BundleId')

	def set_BundleId(self, BundleId):  # String
		self.add_query_param('BundleId', BundleId)
	def get_UserAssignMode(self): # String
		return self.get_query_params().get('UserAssignMode')

	def set_UserAssignMode(self, UserAssignMode):  # String
		self.add_query_param('UserAssignMode', UserAssignMode)
	def get_Hostname(self): # String
		return self.get_query_params().get('Hostname')

	def set_Hostname(self, Hostname):  # String
		self.add_query_param('Hostname', Hostname)
	def get_DesktopNameSuffix(self): # Boolean
		return self.get_query_params().get('DesktopNameSuffix')

	def set_DesktopNameSuffix(self, DesktopNameSuffix):  # Boolean
		self.add_query_param('DesktopNameSuffix', DesktopNameSuffix)
	def get_DirectoryId(self): # String
		return self.get_query_params().get('DirectoryId')

	def set_DirectoryId(self, DirectoryId):  # String
		self.add_query_param('DirectoryId', DirectoryId)
	def get_EndUserIds(self): # RepeatList
		return self.get_query_params().get('EndUserId')

	def set_EndUserIds(self, EndUserId):  # RepeatList
		for depth1 in range(len(EndUserId)):
			self.add_query_param('EndUserId.' + str(depth1 + 1), EndUserId[depth1])
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_BundleModelss(self): # RepeatList
		return self.get_query_params().get('BundleModels')

	def set_BundleModelss(self, BundleModels):  # RepeatList
		for depth1 in range(len(BundleModels)):
			if BundleModels[depth1].get('VolumeEncryptionEnabled') is not None:
				self.add_query_param('BundleModels.' + str(depth1 + 1) + '.VolumeEncryptionEnabled', BundleModels[depth1].get('VolumeEncryptionEnabled'))
			if BundleModels[depth1].get('VolumeEncryptionKey') is not None:
				self.add_query_param('BundleModels.' + str(depth1 + 1) + '.VolumeEncryptionKey', BundleModels[depth1].get('VolumeEncryptionKey'))
			if BundleModels[depth1].get('Amount') is not None:
				self.add_query_param('BundleModels.' + str(depth1 + 1) + '.Amount', BundleModels[depth1].get('Amount'))
			if BundleModels[depth1].get('DesktopName') is not None:
				self.add_query_param('BundleModels.' + str(depth1 + 1) + '.DesktopName', BundleModels[depth1].get('DesktopName'))
			if BundleModels[depth1].get('Hostname') is not None:
				self.add_query_param('BundleModels.' + str(depth1 + 1) + '.Hostname', BundleModels[depth1].get('Hostname'))
			if BundleModels[depth1].get('EndUserIds') is not None:
				for depth2 in range(len(BundleModels[depth1].get('EndUserIds'))):
					self.add_query_param('BundleModels.' + str(depth1 + 1) + '.EndUserIds.' + str(depth2 + 1), BundleModels[depth1].get('EndUserIds')[depth2])
			if BundleModels[depth1].get('BundleId') is not None:
				self.add_query_param('BundleModels.' + str(depth1 + 1) + '.BundleId', BundleModels[depth1].get('BundleId'))
	def get_VolumeEncryptionEnabled(self): # Boolean
		return self.get_query_params().get('VolumeEncryptionEnabled')

	def set_VolumeEncryptionEnabled(self, VolumeEncryptionEnabled):  # Boolean
		self.add_query_param('VolumeEncryptionEnabled', VolumeEncryptionEnabled)
	def get_DesktopName(self): # String
		return self.get_query_params().get('DesktopName')

	def set_DesktopName(self, DesktopName):  # String
		self.add_query_param('DesktopName', DesktopName)
	def get_Amount(self): # Integer
		return self.get_query_params().get('Amount')

	def set_Amount(self, Amount):  # Integer
		self.add_query_param('Amount', Amount)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_UserCommandss(self): # RepeatList
		return self.get_query_params().get('UserCommands')

	def set_UserCommandss(self, UserCommands):  # RepeatList
		for depth1 in range(len(UserCommands)):
			if UserCommands[depth1].get('ContentEncoding') is not None:
				self.add_query_param('UserCommands.' + str(depth1 + 1) + '.ContentEncoding', UserCommands[depth1].get('ContentEncoding'))
			if UserCommands[depth1].get('Content') is not None:
				self.add_query_param('UserCommands.' + str(depth1 + 1) + '.Content', UserCommands[depth1].get('Content'))
			if UserCommands[depth1].get('ContentType') is not None:
				self.add_query_param('UserCommands.' + str(depth1 + 1) + '.ContentType', UserCommands[depth1].get('ContentType'))
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_PromotionId(self): # String
		return self.get_query_params().get('PromotionId')

	def set_PromotionId(self, PromotionId):  # String
		self.add_query_param('PromotionId', PromotionId)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
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
