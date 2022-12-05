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
from aliyunsdkpolardb.endpoint import endpoint_data

class ModifyBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'ModifyBackupPolicy','polardb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DataLevel2BackupRetentionPeriod(self): # String
		return self.get_query_params().get('DataLevel2BackupRetentionPeriod')

	def set_DataLevel2BackupRetentionPeriod(self, DataLevel2BackupRetentionPeriod):  # String
		self.add_query_param('DataLevel2BackupRetentionPeriod', DataLevel2BackupRetentionPeriod)
	def get_DataLevel1BackupPeriod(self): # String
		return self.get_query_params().get('DataLevel1BackupPeriod')

	def set_DataLevel1BackupPeriod(self, DataLevel1BackupPeriod):  # String
		self.add_query_param('DataLevel1BackupPeriod', DataLevel1BackupPeriod)
	def get_DataLevel2BackupPeriod(self): # String
		return self.get_query_params().get('DataLevel2BackupPeriod')

	def set_DataLevel2BackupPeriod(self, DataLevel2BackupPeriod):  # String
		self.add_query_param('DataLevel2BackupPeriod', DataLevel2BackupPeriod)
	def get_PreferredBackupPeriod(self): # String
		return self.get_query_params().get('PreferredBackupPeriod')

	def set_PreferredBackupPeriod(self, PreferredBackupPeriod):  # String
		self.add_query_param('PreferredBackupPeriod', PreferredBackupPeriod)
	def get_DataLevel1BackupRetentionPeriod(self): # String
		return self.get_query_params().get('DataLevel1BackupRetentionPeriod')

	def set_DataLevel1BackupRetentionPeriod(self, DataLevel1BackupRetentionPeriod):  # String
		self.add_query_param('DataLevel1BackupRetentionPeriod', DataLevel1BackupRetentionPeriod)
	def get_BackupRetentionPolicyOnClusterDeletion(self): # String
		return self.get_query_params().get('BackupRetentionPolicyOnClusterDeletion')

	def set_BackupRetentionPolicyOnClusterDeletion(self, BackupRetentionPolicyOnClusterDeletion):  # String
		self.add_query_param('BackupRetentionPolicyOnClusterDeletion', BackupRetentionPolicyOnClusterDeletion)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_DataLevel2BackupAnotherRegionRetentionPeriod(self): # String
		return self.get_query_params().get('DataLevel2BackupAnotherRegionRetentionPeriod')

	def set_DataLevel2BackupAnotherRegionRetentionPeriod(self, DataLevel2BackupAnotherRegionRetentionPeriod):  # String
		self.add_query_param('DataLevel2BackupAnotherRegionRetentionPeriod', DataLevel2BackupAnotherRegionRetentionPeriod)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_PreferredBackupTime(self): # String
		return self.get_query_params().get('PreferredBackupTime')

	def set_PreferredBackupTime(self, PreferredBackupTime):  # String
		self.add_query_param('PreferredBackupTime', PreferredBackupTime)
	def get_BackupFrequency(self): # String
		return self.get_query_params().get('BackupFrequency')

	def set_BackupFrequency(self, BackupFrequency):  # String
		self.add_query_param('BackupFrequency', BackupFrequency)
	def get_DataLevel1BackupFrequency(self): # String
		return self.get_query_params().get('DataLevel1BackupFrequency')

	def set_DataLevel1BackupFrequency(self, DataLevel1BackupFrequency):  # String
		self.add_query_param('DataLevel1BackupFrequency', DataLevel1BackupFrequency)
	def get_DataLevel2BackupAnotherRegionRegion(self): # String
		return self.get_query_params().get('DataLevel2BackupAnotherRegionRegion')

	def set_DataLevel2BackupAnotherRegionRegion(self, DataLevel2BackupAnotherRegionRegion):  # String
		self.add_query_param('DataLevel2BackupAnotherRegionRegion', DataLevel2BackupAnotherRegionRegion)
	def get_DataLevel1BackupTime(self): # String
		return self.get_query_params().get('DataLevel1BackupTime')

	def set_DataLevel1BackupTime(self, DataLevel1BackupTime):  # String
		self.add_query_param('DataLevel1BackupTime', DataLevel1BackupTime)
