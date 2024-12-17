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
from aliyunsdkr_kvstore.endpoint import endpoint_data

class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'R-kvstore', '2015-01-01', 'CreateInstance','redisa')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ConnectionStringPrefix(self): # String
		return self.get_query_params().get('ConnectionStringPrefix')

	def set_ConnectionStringPrefix(self, ConnectionStringPrefix):  # String
		self.add_query_param('ConnectionStringPrefix', ConnectionStringPrefix)
	def get_SecondaryZoneId(self): # String
		return self.get_query_params().get('SecondaryZoneId')

	def set_SecondaryZoneId(self, SecondaryZoneId):  # String
		self.add_query_param('SecondaryZoneId', SecondaryZoneId)
	def get_SlaveReadOnlyCount(self): # Integer
		return self.get_query_params().get('SlaveReadOnlyCount')

	def set_SlaveReadOnlyCount(self, SlaveReadOnlyCount):  # Integer
		self.add_query_param('SlaveReadOnlyCount', SlaveReadOnlyCount)
	def get_CouponNo(self): # String
		return self.get_query_params().get('CouponNo')

	def set_CouponNo(self, CouponNo):  # String
		self.add_query_param('CouponNo', CouponNo)
	def get_NetworkType(self): # String
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self, NetworkType):  # String
		self.add_query_param('NetworkType', NetworkType)
	def get_EngineVersion(self): # String
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self, EngineVersion):  # String
		self.add_query_param('EngineVersion', EngineVersion)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
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
	def get_BusinessInfo(self): # String
		return self.get_query_params().get('BusinessInfo')

	def set_BusinessInfo(self, BusinessInfo):  # String
		self.add_query_param('BusinessInfo', BusinessInfo)
	def get_ShardCount(self): # Integer
		return self.get_query_params().get('ShardCount')

	def set_ShardCount(self, ShardCount):  # Integer
		self.add_query_param('ShardCount', ShardCount)
	def get_AutoRenewPeriod(self): # String
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self, AutoRenewPeriod):  # String
		self.add_query_param('AutoRenewPeriod', AutoRenewPeriod)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_BackupId(self): # String
		return self.get_query_params().get('BackupId')

	def set_BackupId(self, BackupId):  # String
		self.add_query_param('BackupId', BackupId)
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
	def get_Port(self): # String
		return self.get_query_params().get('Port')

	def set_Port(self, Port):  # String
		self.add_query_param('Port', Port)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_ReplicaCount(self): # Integer
		return self.get_query_params().get('ReplicaCount')

	def set_ReplicaCount(self, ReplicaCount):  # Integer
		self.add_query_param('ReplicaCount', ReplicaCount)
	def get_Appendonly(self): # String
		return self.get_query_params().get('Appendonly')

	def set_Appendonly(self, Appendonly):  # String
		self.add_query_param('Appendonly', Appendonly)
	def get_NodeType(self): # String
		return self.get_query_params().get('NodeType')

	def set_NodeType(self, NodeType):  # String
		self.add_query_param('NodeType', NodeType)
	def get_AutoUseCoupon(self): # String
		return self.get_query_params().get('AutoUseCoupon')

	def set_AutoUseCoupon(self, AutoUseCoupon):  # String
		self.add_query_param('AutoUseCoupon', AutoUseCoupon)
	def get_InstanceClass(self): # String
		return self.get_query_params().get('InstanceClass')

	def set_InstanceClass(self, InstanceClass):  # String
		self.add_query_param('InstanceClass', InstanceClass)
	def get_Capacity(self): # Long
		return self.get_query_params().get('Capacity')

	def set_Capacity(self, Capacity):  # Long
		self.add_query_param('Capacity', Capacity)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_DedicatedHostGroupId(self): # String
		return self.get_query_params().get('DedicatedHostGroupId')

	def set_DedicatedHostGroupId(self, DedicatedHostGroupId):  # String
		self.add_query_param('DedicatedHostGroupId', DedicatedHostGroupId)
	def get_RestoreTime(self): # String
		return self.get_query_params().get('RestoreTime')

	def set_RestoreTime(self, RestoreTime):  # String
		self.add_query_param('RestoreTime', RestoreTime)
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
	def get_GlobalInstance(self): # Boolean
		return self.get_query_params().get('GlobalInstance')

	def set_GlobalInstance(self, GlobalInstance):  # Boolean
		self.add_query_param('GlobalInstance', GlobalInstance)
	def get_RecoverConfigMode(self): # String
		return self.get_query_params().get('RecoverConfigMode')

	def set_RecoverConfigMode(self, RecoverConfigMode):  # String
		self.add_query_param('RecoverConfigMode', RecoverConfigMode)
	def get_Token(self): # String
		return self.get_query_params().get('Token')

	def set_Token(self, Token):  # String
		self.add_query_param('Token', Token)
	def get_GlobalInstanceId(self): # String
		return self.get_query_params().get('GlobalInstanceId')

	def set_GlobalInstanceId(self, GlobalInstanceId):  # String
		self.add_query_param('GlobalInstanceId', GlobalInstanceId)
	def get_ParamGroupId(self): # String
		return self.get_query_params().get('ParamGroupId')

	def set_ParamGroupId(self, ParamGroupId):  # String
		self.add_query_param('ParamGroupId', ParamGroupId)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_ReadOnlyCount(self): # Integer
		return self.get_query_params().get('ReadOnlyCount')

	def set_ReadOnlyCount(self, ReadOnlyCount):  # Integer
		self.add_query_param('ReadOnlyCount', ReadOnlyCount)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_SlaveReplicaCount(self): # Integer
		return self.get_query_params().get('SlaveReplicaCount')

	def set_SlaveReplicaCount(self, SlaveReplicaCount):  # Integer
		self.add_query_param('SlaveReplicaCount', SlaveReplicaCount)
	def get_ClusterBackupId(self): # String
		return self.get_query_params().get('ClusterBackupId')

	def set_ClusterBackupId(self, ClusterBackupId):  # String
		self.add_query_param('ClusterBackupId', ClusterBackupId)
