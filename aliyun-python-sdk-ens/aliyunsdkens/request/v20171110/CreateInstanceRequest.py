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

class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateInstance','ens')
		self.set_method('POST')

	def get_UniqueSuffix(self): # Boolean
		return self.get_query_params().get('UniqueSuffix')

	def set_UniqueSuffix(self, UniqueSuffix):  # Boolean
		self.add_query_param('UniqueSuffix', UniqueSuffix)
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
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_AutoRenewPeriod(self): # String
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self, AutoRenewPeriod):  # String
		self.add_query_param('AutoRenewPeriod', AutoRenewPeriod)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_PublicIpIdentification(self): # Boolean
		return self.get_query_params().get('PublicIpIdentification')

	def set_PublicIpIdentification(self, PublicIpIdentification):  # Boolean
		self.add_query_param('PublicIpIdentification', PublicIpIdentification)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_PrivateIpAddress(self): # String
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self, PrivateIpAddress):  # String
		self.add_query_param('PrivateIpAddress', PrivateIpAddress)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_AutoRenew(self): # String
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # String
		self.add_query_param('AutoRenew', AutoRenew)
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
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
	def get_DataDisk1Size(self): # String
		return self.get_query_params().get('DataDisk.1.Size')

	def set_DataDisk1Size(self, DataDisk1Size):  # String
		self.add_query_param('DataDisk.1.Size', DataDisk1Size)
	def get_Quantity(self): # String
		return self.get_query_params().get('Quantity')

	def set_Quantity(self, Quantity):  # String
		self.add_query_param('Quantity', Quantity)
	def get_IpType(self): # String
		return self.get_query_params().get('IpType')

	def set_IpType(self, IpType):  # String
		self.add_query_param('IpType', IpType)
	def get_SystemDiskSize(self): # String
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self, SystemDiskSize):  # String
		self.add_query_param('SystemDisk.Size', SystemDiskSize)
	def get_PaymentType(self): # String
		return self.get_query_params().get('PaymentType')

	def set_PaymentType(self, PaymentType):  # String
		self.add_query_param('PaymentType', PaymentType)
