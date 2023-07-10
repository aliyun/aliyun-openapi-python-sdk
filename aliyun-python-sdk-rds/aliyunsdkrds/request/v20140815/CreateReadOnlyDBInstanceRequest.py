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
from aliyunsdkrds.endpoint import endpoint_data

class CreateReadOnlyDBInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateReadOnlyDBInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DBInstanceStorage(self): # Integer
		return self.get_query_params().get('DBInstanceStorage')

	def set_DBInstanceStorage(self, DBInstanceStorage):  # Integer
		self.add_query_param('DBInstanceStorage', DBInstanceStorage)
	def get_EngineVersion(self): # String
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self, EngineVersion):  # String
		self.add_query_param('EngineVersion', EngineVersion)
	def get_DeletionProtection(self): # Boolean
		return self.get_query_params().get('DeletionProtection')

	def set_DeletionProtection(self, DeletionProtection):  # Boolean
		self.add_query_param('DeletionProtection', DeletionProtection)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_TargetDedicatedHostIdForMaster(self): # String
		return self.get_query_params().get('TargetDedicatedHostIdForMaster')

	def set_TargetDedicatedHostIdForMaster(self, TargetDedicatedHostIdForMaster):  # String
		self.add_query_param('TargetDedicatedHostIdForMaster', TargetDedicatedHostIdForMaster)
	def get_DBInstanceDescription(self): # String
		return self.get_query_params().get('DBInstanceDescription')

	def set_DBInstanceDescription(self, DBInstanceDescription):  # String
		self.add_query_param('DBInstanceDescription', DBInstanceDescription)
	def get_GdnInstanceName(self): # String
		return self.get_query_params().get('GdnInstanceName')

	def set_GdnInstanceName(self, GdnInstanceName):  # String
		self.add_query_param('GdnInstanceName', GdnInstanceName)
	def get_TddlBizType(self): # String
		return self.get_query_params().get('TddlBizType')

	def set_TddlBizType(self, TddlBizType):  # String
		self.add_query_param('TddlBizType', TddlBizType)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_DBInstanceClass(self): # String
		return self.get_query_params().get('DBInstanceClass')

	def set_DBInstanceClass(self, DBInstanceClass):  # String
		self.add_query_param('DBInstanceClass', DBInstanceClass)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_PrivateIpAddress(self): # String
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self, PrivateIpAddress):  # String
		self.add_query_param('PrivateIpAddress', PrivateIpAddress)
	def get_AutoRenew(self): # String
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # String
		self.add_query_param('AutoRenew', AutoRenew)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_InstanceNetworkType(self): # String
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self, InstanceNetworkType):  # String
		self.add_query_param('InstanceNetworkType', InstanceNetworkType)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_InstructionSetArch(self): # String
		return self.get_query_params().get('InstructionSetArch')

	def set_InstructionSetArch(self, InstructionSetArch):  # String
		self.add_query_param('InstructionSetArch', InstructionSetArch)
	def get_TddlRegionConfig(self): # String
		return self.get_query_params().get('TddlRegionConfig')

	def set_TddlRegionConfig(self, TddlRegionConfig):  # String
		self.add_query_param('TddlRegionConfig', TddlRegionConfig)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_DBInstanceStorageType(self): # String
		return self.get_query_params().get('DBInstanceStorageType')

	def set_DBInstanceStorageType(self, DBInstanceStorageType):  # String
		self.add_query_param('DBInstanceStorageType', DBInstanceStorageType)
	def get_DedicatedHostGroupId(self): # String
		return self.get_query_params().get('DedicatedHostGroupId')

	def set_DedicatedHostGroupId(self, DedicatedHostGroupId):  # String
		self.add_query_param('DedicatedHostGroupId', DedicatedHostGroupId)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_UsedTime(self): # String
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self, UsedTime):  # String
		self.add_query_param('UsedTime', UsedTime)
	def get_BurstingEnabled(self): # Boolean
		return self.get_query_params().get('BurstingEnabled')

	def set_BurstingEnabled(self, BurstingEnabled):  # Boolean
		self.add_query_param('BurstingEnabled', BurstingEnabled)
	def get_VPCId(self): # String
		return self.get_query_params().get('VPCId')

	def set_VPCId(self, VPCId):  # String
		self.add_query_param('VPCId', VPCId)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
	def get_BpeEnabled(self): # String
		return self.get_query_params().get('BpeEnabled')

	def set_BpeEnabled(self, BpeEnabled):  # String
		self.add_query_param('BpeEnabled', BpeEnabled)
