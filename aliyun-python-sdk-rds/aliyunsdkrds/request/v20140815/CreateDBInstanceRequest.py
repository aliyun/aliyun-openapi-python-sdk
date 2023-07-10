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
import json

class CreateDBInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateDBInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBParamGroupId(self): # String
		return self.get_query_params().get('DBParamGroupId')

	def set_DBParamGroupId(self, DBParamGroupId):  # String
		self.add_query_param('DBParamGroupId', DBParamGroupId)
	def get_BabelfishConfig(self): # String
		return self.get_query_params().get('BabelfishConfig')

	def set_BabelfishConfig(self, BabelfishConfig):  # String
		self.add_query_param('BabelfishConfig', BabelfishConfig)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DBInstanceStorage(self): # Integer
		return self.get_query_params().get('DBInstanceStorage')

	def set_DBInstanceStorage(self, DBInstanceStorage):  # Integer
		self.add_query_param('DBInstanceStorage', DBInstanceStorage)
	def get_SystemDBCharset(self): # String
		return self.get_query_params().get('SystemDBCharset')

	def set_SystemDBCharset(self, SystemDBCharset):  # String
		self.add_query_param('SystemDBCharset', SystemDBCharset)
	def get_ConnectionString(self): # String
		return self.get_query_params().get('ConnectionString')

	def set_ConnectionString(self, ConnectionString):  # String
		self.add_query_param('ConnectionString', ConnectionString)
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
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_BusinessInfo(self): # String
		return self.get_query_params().get('BusinessInfo')

	def set_BusinessInfo(self, BusinessInfo):  # String
		self.add_query_param('BusinessInfo', BusinessInfo)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_EncryptionKey(self): # String
		return self.get_query_params().get('EncryptionKey')

	def set_EncryptionKey(self, EncryptionKey):  # String
		self.add_query_param('EncryptionKey', EncryptionKey)
	def get_DBInstanceClass(self): # String
		return self.get_query_params().get('DBInstanceClass')

	def set_DBInstanceClass(self, DBInstanceClass):  # String
		self.add_query_param('DBInstanceClass', DBInstanceClass)
	def get_SecurityIPList(self): # String
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self, SecurityIPList):  # String
		self.add_query_param('SecurityIPList', SecurityIPList)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_PrivateIpAddress(self): # String
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self, PrivateIpAddress):  # String
		self.add_query_param('PrivateIpAddress', PrivateIpAddress)
	def get_TargetDedicatedHostIdForLog(self): # String
		return self.get_query_params().get('TargetDedicatedHostIdForLog')

	def set_TargetDedicatedHostIdForLog(self, TargetDedicatedHostIdForLog):  # String
		self.add_query_param('TargetDedicatedHostIdForLog', TargetDedicatedHostIdForLog)
	def get_AutoRenew(self): # String
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # String
		self.add_query_param('AutoRenew', AutoRenew)
	def get_Port(self): # String
		return self.get_query_params().get('Port')

	def set_Port(self, Port):  # String
		self.add_query_param('Port', Port)
	def get_RoleARN(self): # String
		return self.get_query_params().get('RoleARN')

	def set_RoleARN(self, RoleARN):  # String
		self.add_query_param('RoleARN', RoleARN)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_StorageAutoScale(self): # String
		return self.get_query_params().get('StorageAutoScale')

	def set_StorageAutoScale(self, StorageAutoScale):  # String
		self.add_query_param('StorageAutoScale', StorageAutoScale)
	def get_InstanceNetworkType(self): # String
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self, InstanceNetworkType):  # String
		self.add_query_param('InstanceNetworkType', InstanceNetworkType)
	def get_ConnectionMode(self): # String
		return self.get_query_params().get('ConnectionMode')

	def set_ConnectionMode(self, ConnectionMode):  # String
		self.add_query_param('ConnectionMode', ConnectionMode)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TargetDedicatedHostIdForSlave(self): # String
		return self.get_query_params().get('TargetDedicatedHostIdForSlave')

	def set_TargetDedicatedHostIdForSlave(self, TargetDedicatedHostIdForSlave):  # String
		self.add_query_param('TargetDedicatedHostIdForSlave', TargetDedicatedHostIdForSlave)
	def get_ZoneIdSlave1(self): # String
		return self.get_query_params().get('ZoneIdSlave1')

	def set_ZoneIdSlave1(self, ZoneIdSlave1):  # String
		self.add_query_param('ZoneIdSlave1', ZoneIdSlave1)
	def get_ZoneIdSlave2(self): # String
		return self.get_query_params().get('ZoneIdSlave2')

	def set_ZoneIdSlave2(self, ZoneIdSlave2):  # String
		self.add_query_param('ZoneIdSlave2', ZoneIdSlave2)
	def get_DBIsIgnoreCase(self): # String
		return self.get_query_params().get('DBIsIgnoreCase')

	def set_DBIsIgnoreCase(self, DBIsIgnoreCase):  # String
		self.add_query_param('DBIsIgnoreCase', DBIsIgnoreCase)
	def get_Engine(self): # String
		return self.get_query_params().get('Engine')

	def set_Engine(self, Engine):  # String
		self.add_query_param('Engine', Engine)
	def get_DBTimeZone(self): # String
		return self.get_query_params().get('DBTimeZone')

	def set_DBTimeZone(self, DBTimeZone):  # String
		self.add_query_param('DBTimeZone', DBTimeZone)
	def get_DBInstanceStorageType(self): # String
		return self.get_query_params().get('DBInstanceStorageType')

	def set_DBInstanceStorageType(self, DBInstanceStorageType):  # String
		self.add_query_param('DBInstanceStorageType', DBInstanceStorageType)
	def get_DedicatedHostGroupId(self): # String
		return self.get_query_params().get('DedicatedHostGroupId')

	def set_DedicatedHostGroupId(self, DedicatedHostGroupId):  # String
		self.add_query_param('DedicatedHostGroupId', DedicatedHostGroupId)
	def get_CreateStrategy(self): # String
		return self.get_query_params().get('CreateStrategy')

	def set_CreateStrategy(self, CreateStrategy):  # String
		self.add_query_param('CreateStrategy', CreateStrategy)
	def get_DBInstanceNetType(self): # String
		return self.get_query_params().get('DBInstanceNetType')

	def set_DBInstanceNetType(self, DBInstanceNetType):  # String
		self.add_query_param('DBInstanceNetType', DBInstanceNetType)
	def get_Amount(self): # Integer
		return self.get_query_params().get('Amount')

	def set_Amount(self, Amount):  # Integer
		self.add_query_param('Amount', Amount)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_ServerlessConfig(self): # Struct
		return self.get_query_params().get('ServerlessConfig')

	def set_ServerlessConfig(self, ServerlessConfig):  # Struct
		self.add_query_param("ServerlessConfig", json.dumps(ServerlessConfig))
	def get_UsedTime(self): # String
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self, UsedTime):  # String
		self.add_query_param('UsedTime', UsedTime)
	def get_BurstingEnabled(self): # Boolean
		return self.get_query_params().get('BurstingEnabled')

	def set_BurstingEnabled(self, BurstingEnabled):  # Boolean
		self.add_query_param('BurstingEnabled', BurstingEnabled)
	def get_TargetMinorVersion(self): # String
		return self.get_query_params().get('TargetMinorVersion')

	def set_TargetMinorVersion(self, TargetMinorVersion):  # String
		self.add_query_param('TargetMinorVersion', TargetMinorVersion)
	def get_UserBackupId(self): # String
		return self.get_query_params().get('UserBackupId')

	def set_UserBackupId(self, UserBackupId):  # String
		self.add_query_param('UserBackupId', UserBackupId)
	def get_StorageUpperBound(self): # Integer
		return self.get_query_params().get('StorageUpperBound')

	def set_StorageUpperBound(self, StorageUpperBound):  # Integer
		self.add_query_param('StorageUpperBound', StorageUpperBound)
	def get_StorageThreshold(self): # Integer
		return self.get_query_params().get('StorageThreshold')

	def set_StorageThreshold(self, StorageThreshold):  # Integer
		self.add_query_param('StorageThreshold', StorageThreshold)
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
