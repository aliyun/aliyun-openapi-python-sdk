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

class CloneDBInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CloneDBInstance','rds')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DBInstanceStorage(self):
		return self.get_query_params().get('DBInstanceStorage')

	def set_DBInstanceStorage(self,DBInstanceStorage):
		self.add_query_param('DBInstanceStorage',DBInstanceStorage)

	def get_TableMeta(self):
		return self.get_query_params().get('TableMeta')

	def set_TableMeta(self,TableMeta):
		self.add_query_param('TableMeta',TableMeta)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_DBInstanceStorageType(self):
		return self.get_query_params().get('DBInstanceStorageType')

	def set_DBInstanceStorageType(self,DBInstanceStorageType):
		self.add_query_param('DBInstanceStorageType',DBInstanceStorageType)

	def get_DedicatedHostGroupId(self):
		return self.get_query_params().get('DedicatedHostGroupId')

	def set_DedicatedHostGroupId(self,DedicatedHostGroupId):
		self.add_query_param('DedicatedHostGroupId',DedicatedHostGroupId)

	def get_BackupType(self):
		return self.get_query_params().get('BackupType')

	def set_BackupType(self,BackupType):
		self.add_query_param('BackupType',BackupType)

	def get_RestoreTime(self):
		return self.get_query_params().get('RestoreTime')

	def set_RestoreTime(self,RestoreTime):
		self.add_query_param('RestoreTime',RestoreTime)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_BackupId(self):
		return self.get_query_params().get('BackupId')

	def set_BackupId(self,BackupId):
		self.add_query_param('BackupId',BackupId)

	def get_RestoreTable(self):
		return self.get_query_params().get('RestoreTable')

	def set_RestoreTable(self,RestoreTable):
		self.add_query_param('RestoreTable',RestoreTable)

	def get_UsedTime(self):
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self,UsedTime):
		self.add_query_param('UsedTime',UsedTime)

	def get_DBInstanceClass(self):
		return self.get_query_params().get('DBInstanceClass')

	def set_DBInstanceClass(self,DBInstanceClass):
		self.add_query_param('DBInstanceClass',DBInstanceClass)

	def get_DbNames(self):
		return self.get_query_params().get('DbNames')

	def set_DbNames(self,DbNames):
		self.add_query_param('DbNames',DbNames)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PrivateIpAddress(self):
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self,PrivateIpAddress):
		self.add_query_param('PrivateIpAddress',PrivateIpAddress)

	def get_VPCId(self):
		return self.get_query_params().get('VPCId')

	def set_VPCId(self,VPCId):
		self.add_query_param('VPCId',VPCId)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)

	def get_InstanceNetworkType(self):
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self,InstanceNetworkType):
		self.add_query_param('InstanceNetworkType',InstanceNetworkType)