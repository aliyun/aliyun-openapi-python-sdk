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

class CreateShardingInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'R-kvstore', '2015-01-01', 'CreateShardingInstance')

	def get_ShardStorageQuantity(self):
		return self.get_query_params().get('ShardStorageQuantity')

	def set_ShardStorageQuantity(self,ShardStorageQuantity):
		self.add_query_param('ShardStorageQuantity',ShardStorageQuantity)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_CouponNo(self):
		return self.get_query_params().get('CouponNo')

	def set_CouponNo(self,CouponNo):
		self.add_query_param('CouponNo',CouponNo)

	def get_NetworkType(self):
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_query_param('NetworkType',NetworkType)

	def get_EngineVersion(self):
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self,EngineVersion):
		self.add_query_param('EngineVersion',EngineVersion)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_ShardReplicaClass(self):
		return self.get_query_params().get('ShardReplicaClass')

	def set_ShardReplicaClass(self,ShardReplicaClass):
		self.add_query_param('ShardReplicaClass',ShardReplicaClass)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_IncrementalBackupMode(self):
		return self.get_query_params().get('IncrementalBackupMode')

	def set_IncrementalBackupMode(self,IncrementalBackupMode):
		self.add_query_param('IncrementalBackupMode',IncrementalBackupMode)

	def get_BusinessInfo(self):
		return self.get_query_params().get('BusinessInfo')

	def set_BusinessInfo(self,BusinessInfo):
		self.add_query_param('BusinessInfo',BusinessInfo)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_BackupId(self):
		return self.get_query_params().get('BackupId')

	def set_BackupId(self,BackupId):
		self.add_query_param('BackupId',BackupId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PrivateIpAddress(self):
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self,PrivateIpAddress):
		self.add_query_param('PrivateIpAddress',PrivateIpAddress)

	def get_SecurityIPList(self):
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self,SecurityIPList):
		self.add_query_param('SecurityIPList',SecurityIPList)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_ProxyQuantity(self):
		return self.get_query_params().get('ProxyQuantity')

	def set_ProxyQuantity(self,ProxyQuantity):
		self.add_query_param('ProxyQuantity',ProxyQuantity)

	def get_ProxyMode(self):
		return self.get_query_params().get('ProxyMode')

	def set_ProxyMode(self,ProxyMode):
		self.add_query_param('ProxyMode',ProxyMode)

	def get_NodeType(self):
		return self.get_query_params().get('NodeType')

	def set_NodeType(self,NodeType):
		self.add_query_param('NodeType',NodeType)

	def get_InstanceClass(self):
		return self.get_query_params().get('InstanceClass')

	def set_InstanceClass(self,InstanceClass):
		self.add_query_param('InstanceClass',InstanceClass)

	def get_Capacity(self):
		return self.get_query_params().get('Capacity')

	def set_Capacity(self,Capacity):
		self.add_query_param('Capacity',Capacity)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_SrcDBInstanceId(self):
		return self.get_query_params().get('SrcDBInstanceId')

	def set_SrcDBInstanceId(self,SrcDBInstanceId):
		self.add_query_param('SrcDBInstanceId',SrcDBInstanceId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_ShardQuantity(self):
		return self.get_query_params().get('ShardQuantity')

	def set_ShardQuantity(self,ShardQuantity):
		self.add_query_param('ShardQuantity',ShardQuantity)

	def get_ShardReplicaQuantity(self):
		return self.get_query_params().get('ShardReplicaQuantity')

	def set_ShardReplicaQuantity(self,ShardReplicaQuantity):
		self.add_query_param('ShardReplicaQuantity',ShardReplicaQuantity)

	def get_ArchitectureType(self):
		return self.get_query_params().get('ArchitectureType')

	def set_ArchitectureType(self,ArchitectureType):
		self.add_query_param('ArchitectureType',ArchitectureType)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_RedisManagerClass(self):
		return self.get_query_params().get('RedisManagerClass')

	def set_RedisManagerClass(self,RedisManagerClass):
		self.add_query_param('RedisManagerClass',RedisManagerClass)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_Config(self):
		return self.get_query_params().get('Config')

	def set_Config(self,Config):
		self.add_query_param('Config',Config)