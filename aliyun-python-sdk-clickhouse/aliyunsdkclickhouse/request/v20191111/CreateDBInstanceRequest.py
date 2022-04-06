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
from aliyunsdkclickhouse.endpoint import endpoint_data

class CreateDBInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'clickhouse', '2019-11-11', 'CreateDBInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DBClusterDescription(self): # String
		return self.get_query_params().get('DBClusterDescription')

	def set_DBClusterDescription(self, DBClusterDescription):  # String
		self.add_query_param('DBClusterDescription', DBClusterDescription)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_SourceDBClusterId(self): # String
		return self.get_query_params().get('SourceDBClusterId')

	def set_SourceDBClusterId(self, SourceDBClusterId):  # String
		self.add_query_param('SourceDBClusterId', SourceDBClusterId)
	def get_DbNodeStorageType(self): # String
		return self.get_query_params().get('DbNodeStorageType')

	def set_DbNodeStorageType(self, DbNodeStorageType):  # String
		self.add_query_param('DbNodeStorageType', DbNodeStorageType)
	def get_DBClusterCategory(self): # String
		return self.get_query_params().get('DBClusterCategory')

	def set_DBClusterCategory(self, DBClusterCategory):  # String
		self.add_query_param('DBClusterCategory', DBClusterCategory)
	def get_EncryptionType(self): # String
		return self.get_query_params().get('EncryptionType')

	def set_EncryptionType(self, EncryptionType):  # String
		self.add_query_param('EncryptionType', EncryptionType)
	def get_DBClusterNetworkType(self): # String
		return self.get_query_params().get('DBClusterNetworkType')

	def set_DBClusterNetworkType(self, DBClusterNetworkType):  # String
		self.add_query_param('DBClusterNetworkType', DBClusterNetworkType)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_DBClusterVersion(self): # String
		return self.get_query_params().get('DBClusterVersion')

	def set_DBClusterVersion(self, DBClusterVersion):  # String
		self.add_query_param('DBClusterVersion', DBClusterVersion)
	def get_DBClusterClass(self): # String
		return self.get_query_params().get('DBClusterClass')

	def set_DBClusterClass(self, DBClusterClass):  # String
		self.add_query_param('DBClusterClass', DBClusterClass)
	def get_BackupSetID(self): # String
		return self.get_query_params().get('BackupSetID')

	def set_BackupSetID(self, BackupSetID):  # String
		self.add_query_param('BackupSetID', BackupSetID)
	def get_EncryptionKey(self): # String
		return self.get_query_params().get('EncryptionKey')

	def set_EncryptionKey(self, EncryptionKey):  # String
		self.add_query_param('EncryptionKey', EncryptionKey)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_DBNodeGroupCount(self): # String
		return self.get_query_params().get('DBNodeGroupCount')

	def set_DBNodeGroupCount(self, DBNodeGroupCount):  # String
		self.add_query_param('DBNodeGroupCount', DBNodeGroupCount)
	def get_UsedTime(self): # String
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self, UsedTime):  # String
		self.add_query_param('UsedTime', UsedTime)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_DBNodeStorage(self): # String
		return self.get_query_params().get('DBNodeStorage')

	def set_DBNodeStorage(self, DBNodeStorage):  # String
		self.add_query_param('DBNodeStorage', DBNodeStorage)
	def get_VPCId(self): # String
		return self.get_query_params().get('VPCId')

	def set_VPCId(self, VPCId):  # String
		self.add_query_param('VPCId', VPCId)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
