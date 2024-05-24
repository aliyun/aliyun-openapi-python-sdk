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
from aliyunsdkdds.endpoint import endpoint_data

class CreateShardingDBInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dds', '2015-12-01', 'CreateShardingDBInstance','dds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_SecondaryZoneId(self): # String
		return self.get_query_params().get('SecondaryZoneId')

	def set_SecondaryZoneId(self, SecondaryZoneId):  # String
		self.add_query_param('SecondaryZoneId', SecondaryZoneId)
	def get_EngineVersion(self): # String
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self, EngineVersion):  # String
		self.add_query_param('EngineVersion', EngineVersion)
	def get_NetworkType(self): # String
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self, NetworkType):  # String
		self.add_query_param('NetworkType', NetworkType)
	def get_SrcRegion(self): # String
		return self.get_query_params().get('SrcRegion')

	def set_SrcRegion(self, SrcRegion):  # String
		self.add_query_param('SrcRegion', SrcRegion)
	def get_ReplicaSets(self): # RepeatList
		return self.get_query_params().get('ReplicaSet')

	def set_ReplicaSets(self, ReplicaSet):  # RepeatList
		for depth1 in range(len(ReplicaSet)):
			if ReplicaSet[depth1].get('ReadonlyReplicas') is not None:
				self.add_query_param('ReplicaSet.' + str(depth1 + 1) + '.ReadonlyReplicas', ReplicaSet[depth1].get('ReadonlyReplicas'))
			if ReplicaSet[depth1].get('Storage') is not None:
				self.add_query_param('ReplicaSet.' + str(depth1 + 1) + '.Storage', ReplicaSet[depth1].get('Storage'))
			if ReplicaSet[depth1].get('Class') is not None:
				self.add_query_param('ReplicaSet.' + str(depth1 + 1) + '.Class', ReplicaSet[depth1].get('Class'))
	def get_StorageType(self): # String
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # String
		self.add_query_param('StorageType', StorageType)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
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
	def get_GlobalSecurityGroupIds(self): # String
		return self.get_query_params().get('GlobalSecurityGroupIds')

	def set_GlobalSecurityGroupIds(self, GlobalSecurityGroupIds):  # String
		self.add_query_param('GlobalSecurityGroupIds', GlobalSecurityGroupIds)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_BackupId(self): # String
		return self.get_query_params().get('BackupId')

	def set_BackupId(self, BackupId):  # String
		self.add_query_param('BackupId', BackupId)
	def get_EncryptionKey(self): # String
		return self.get_query_params().get('EncryptionKey')

	def set_EncryptionKey(self, EncryptionKey):  # String
		self.add_query_param('EncryptionKey', EncryptionKey)
	def get_ConfigServers(self): # RepeatList
		return self.get_query_params().get('ConfigServer')

	def set_ConfigServers(self, ConfigServer):  # RepeatList
		for depth1 in range(len(ConfigServer)):
			if ConfigServer[depth1].get('Storage') is not None:
				self.add_query_param('ConfigServer.' + str(depth1 + 1) + '.Storage', ConfigServer[depth1].get('Storage'))
			if ConfigServer[depth1].get('Class') is not None:
				self.add_query_param('ConfigServer.' + str(depth1 + 1) + '.Class', ConfigServer[depth1].get('Class'))
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SecurityIPList(self): # String
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self, SecurityIPList):  # String
		self.add_query_param('SecurityIPList', SecurityIPList)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_Mongoss(self): # RepeatList
		return self.get_query_params().get('Mongos')

	def set_Mongoss(self, Mongos):  # RepeatList
		for depth1 in range(len(Mongos)):
			if Mongos[depth1].get('Class') is not None:
				self.add_query_param('Mongos.' + str(depth1 + 1) + '.Class', Mongos[depth1].get('Class'))
	def get_ProvisionedIops(self): # Long
		return self.get_query_params().get('ProvisionedIops')

	def set_ProvisionedIops(self, ProvisionedIops):  # Long
		self.add_query_param('ProvisionedIops', ProvisionedIops)
	def get_AutoRenew(self): # String
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # String
		self.add_query_param('AutoRenew', AutoRenew)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_StorageEngine(self): # String
		return self.get_query_params().get('StorageEngine')

	def set_StorageEngine(self, StorageEngine):  # String
		self.add_query_param('StorageEngine', StorageEngine)
	def get_Engine(self): # String
		return self.get_query_params().get('Engine')

	def set_Engine(self, Engine):  # String
		self.add_query_param('Engine', Engine)
	def get_HiddenZoneId(self): # String
		return self.get_query_params().get('HiddenZoneId')

	def set_HiddenZoneId(self, HiddenZoneId):  # String
		self.add_query_param('HiddenZoneId', HiddenZoneId)
	def get_RestoreTime(self): # String
		return self.get_query_params().get('RestoreTime')

	def set_RestoreTime(self, RestoreTime):  # String
		self.add_query_param('RestoreTime', RestoreTime)
	def get_DestRegion(self): # String
		return self.get_query_params().get('DestRegion')

	def set_DestRegion(self, DestRegion):  # String
		self.add_query_param('DestRegion', DestRegion)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_SrcDBInstanceId(self): # String
		return self.get_query_params().get('SrcDBInstanceId')

	def set_SrcDBInstanceId(self, SrcDBInstanceId):  # String
		self.add_query_param('SrcDBInstanceId', SrcDBInstanceId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_RestoreType(self): # String
		return self.get_query_params().get('RestoreType')

	def set_RestoreType(self, RestoreType):  # String
		self.add_query_param('RestoreType', RestoreType)
	def get_AccountPassword(self): # String
		return self.get_query_params().get('AccountPassword')

	def set_AccountPassword(self, AccountPassword):  # String
		self.add_query_param('AccountPassword', AccountPassword)
	def get_Encrypted(self): # Boolean
		return self.get_query_params().get('Encrypted')

	def set_Encrypted(self, Encrypted):  # Boolean
		self.add_query_param('Encrypted', Encrypted)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_ProtocolType(self): # String
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self, ProtocolType):  # String
		self.add_query_param('ProtocolType', ProtocolType)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
