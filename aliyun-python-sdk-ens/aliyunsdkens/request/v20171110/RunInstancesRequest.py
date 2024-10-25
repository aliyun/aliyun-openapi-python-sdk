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
import json

class RunInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'RunInstances','ens')
		self.set_method('POST')

	def get_ScheduleAreaLevel(self): # String
		return self.get_query_params().get('ScheduleAreaLevel')

	def set_ScheduleAreaLevel(self, ScheduleAreaLevel):  # String
		self.add_query_param('ScheduleAreaLevel', ScheduleAreaLevel)
	def get_UniqueSuffix(self): # Boolean
		return self.get_query_params().get('UniqueSuffix')

	def set_UniqueSuffix(self, UniqueSuffix):  # Boolean
		self.add_query_param('UniqueSuffix', UniqueSuffix)
	def get_InstanceChargeStrategy(self): # String
		return self.get_query_params().get('InstanceChargeStrategy')

	def set_InstanceChargeStrategy(self, InstanceChargeStrategy):  # String
		self.add_query_param('InstanceChargeStrategy', InstanceChargeStrategy)
	def get_SecurityId(self): # String
		return self.get_query_params().get('SecurityId')

	def set_SecurityId(self, SecurityId):  # String
		self.add_query_param('SecurityId', SecurityId)
	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_HostName(self): # String
		return self.get_query_params().get('HostName')

	def set_HostName(self, HostName):  # String
		self.add_query_param('HostName', HostName)
	def get_SystemDisk(self): # Struct
		return self.get_query_params().get('SystemDisk')

	def set_SystemDisk(self, SystemDisk):  # Struct
		self.add_query_param("SystemDisk", json.dumps(SystemDisk))
	def get_NetDistrictCode(self): # String
		return self.get_query_params().get('NetDistrictCode')

	def set_NetDistrictCode(self, NetDistrictCode):  # String
		self.add_query_param('NetDistrictCode', NetDistrictCode)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_Period(self): # Long
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Long
		self.add_query_param('Period', Period)
	def get_PublicIpIdentification(self): # Boolean
		return self.get_query_params().get('PublicIpIdentification')

	def set_PublicIpIdentification(self, PublicIpIdentification):  # Boolean
		self.add_query_param('PublicIpIdentification', PublicIpIdentification)
	def get_BillingCycle(self): # String
		return self.get_query_params().get('BillingCycle')

	def set_BillingCycle(self, BillingCycle):  # String
		self.add_query_param('BillingCycle', BillingCycle)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_PrivateIpAddress(self): # String
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self, PrivateIpAddress):  # String
		self.add_query_param('PrivateIpAddress', PrivateIpAddress)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_NetWorkId(self): # String
		return self.get_query_params().get('NetWorkId')

	def set_NetWorkId(self, NetWorkId):  # String
		self.add_query_param('NetWorkId', NetWorkId)
	def get_SchedulingPriceStrategy(self): # String
		return self.get_query_params().get('SchedulingPriceStrategy')

	def set_SchedulingPriceStrategy(self, SchedulingPriceStrategy):  # String
		self.add_query_param('SchedulingPriceStrategy', SchedulingPriceStrategy)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_InternetMaxBandwidthOut(self): # Long
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):  # Long
		self.add_query_param('InternetMaxBandwidthOut', InternetMaxBandwidthOut)
	def get_AutoUseCoupon(self): # String
		return self.get_query_params().get('AutoUseCoupon')

	def set_AutoUseCoupon(self, AutoUseCoupon):  # String
		self.add_query_param('AutoUseCoupon', AutoUseCoupon)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_PasswordInherit(self): # Boolean
		return self.get_query_params().get('PasswordInherit')

	def set_PasswordInherit(self, PasswordInherit):  # Boolean
		self.add_query_param('PasswordInherit', PasswordInherit)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_Amount(self): # Long
		return self.get_query_params().get('Amount')

	def set_Amount(self, Amount):  # Long
		self.add_query_param('Amount', Amount)
	def get_AutoReleaseTime(self): # String
		return self.get_query_params().get('AutoReleaseTime')

	def set_AutoReleaseTime(self, AutoReleaseTime):  # String
		self.add_query_param('AutoReleaseTime', AutoReleaseTime)
	def get_IpType(self): # String
		return self.get_query_params().get('IpType')

	def set_IpType(self, IpType):  # String
		self.add_query_param('IpType', IpType)
	def get_SpotDuration(self): # Integer
		return self.get_query_params().get('SpotDuration')

	def set_SpotDuration(self, SpotDuration):  # Integer
		self.add_query_param('SpotDuration', SpotDuration)
	def get_DataDisk(self): # Array
		return self.get_query_params().get('DataDisk')

	def set_DataDisk(self, DataDisk):  # Array
		self.add_query_param("DataDisk", json.dumps(DataDisk))
	def get_SchedulingStrategy(self): # String
		return self.get_query_params().get('SchedulingStrategy')

	def set_SchedulingStrategy(self, SchedulingStrategy):  # String
		self.add_query_param('SchedulingStrategy', SchedulingStrategy)
	def get_Carrier(self): # String
		return self.get_query_params().get('Carrier')

	def set_Carrier(self, Carrier):  # String
		self.add_query_param('Carrier', Carrier)
