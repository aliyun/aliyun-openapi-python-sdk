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

class ModifyBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dds', '2015-12-01', 'ModifyBackupPolicy','dds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_CrossLogRetentionValue(self): # Integer
		return self.get_query_params().get('CrossLogRetentionValue')

	def set_CrossLogRetentionValue(self, CrossLogRetentionValue):  # Integer
		self.add_query_param('CrossLogRetentionValue', CrossLogRetentionValue)
	def get_SrcRegion(self): # String
		return self.get_query_params().get('SrcRegion')

	def set_SrcRegion(self, SrcRegion):  # String
		self.add_query_param('SrcRegion', SrcRegion)
	def get_CrossRetentionType(self): # String
		return self.get_query_params().get('CrossRetentionType')

	def set_CrossRetentionType(self, CrossRetentionType):  # String
		self.add_query_param('CrossRetentionType', CrossRetentionType)
	def get_BackupInterval(self): # String
		return self.get_query_params().get('BackupInterval')

	def set_BackupInterval(self, BackupInterval):  # String
		self.add_query_param('BackupInterval', BackupInterval)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_EnableBackupLog(self): # Long
		return self.get_query_params().get('EnableBackupLog')

	def set_EnableBackupLog(self, EnableBackupLog):  # Long
		self.add_query_param('EnableBackupLog', EnableBackupLog)
	def get_PreferredBackupPeriod(self): # String
		return self.get_query_params().get('PreferredBackupPeriod')

	def set_PreferredBackupPeriod(self, PreferredBackupPeriod):  # String
		self.add_query_param('PreferredBackupPeriod', PreferredBackupPeriod)
	def get_BackupRetentionPolicyOnClusterDeletion(self): # Integer
		return self.get_query_params().get('BackupRetentionPolicyOnClusterDeletion')

	def set_BackupRetentionPolicyOnClusterDeletion(self, BackupRetentionPolicyOnClusterDeletion):  # Integer
		self.add_query_param('BackupRetentionPolicyOnClusterDeletion', BackupRetentionPolicyOnClusterDeletion)
	def get_DestRegion(self): # String
		return self.get_query_params().get('DestRegion')

	def set_DestRegion(self, DestRegion):  # String
		self.add_query_param('DestRegion', DestRegion)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_CrossBackupType(self): # String
		return self.get_query_params().get('CrossBackupType')

	def set_CrossBackupType(self, CrossBackupType):  # String
		self.add_query_param('CrossBackupType', CrossBackupType)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SnapshotBackupType(self): # String
		return self.get_query_params().get('SnapshotBackupType')

	def set_SnapshotBackupType(self, SnapshotBackupType):  # String
		self.add_query_param('SnapshotBackupType', SnapshotBackupType)
	def get_PreferredBackupTime(self): # String
		return self.get_query_params().get('PreferredBackupTime')

	def set_PreferredBackupTime(self, PreferredBackupTime):  # String
		self.add_query_param('PreferredBackupTime', PreferredBackupTime)
	def get_BackupRetentionPeriod(self): # Long
		return self.get_query_params().get('BackupRetentionPeriod')

	def set_BackupRetentionPeriod(self, BackupRetentionPeriod):  # Long
		self.add_query_param('BackupRetentionPeriod', BackupRetentionPeriod)
	def get_HighFrequencyBackupRetention(self): # Long
		return self.get_query_params().get('HighFrequencyBackupRetention')

	def set_HighFrequencyBackupRetention(self, HighFrequencyBackupRetention):  # Long
		self.add_query_param('HighFrequencyBackupRetention', HighFrequencyBackupRetention)
	def get_EnableCrossLogBackup(self): # Integer
		return self.get_query_params().get('EnableCrossLogBackup')

	def set_EnableCrossLogBackup(self, EnableCrossLogBackup):  # Integer
		self.add_query_param('EnableCrossLogBackup', EnableCrossLogBackup)
	def get_CrossBackupPeriod(self): # String
		return self.get_query_params().get('CrossBackupPeriod')

	def set_CrossBackupPeriod(self, CrossBackupPeriod):  # String
		self.add_query_param('CrossBackupPeriod', CrossBackupPeriod)
	def get_CrossRetentionValue(self): # Integer
		return self.get_query_params().get('CrossRetentionValue')

	def set_CrossRetentionValue(self, CrossRetentionValue):  # Integer
		self.add_query_param('CrossRetentionValue', CrossRetentionValue)
	def get_CrossLogRetentionType(self): # String
		return self.get_query_params().get('CrossLogRetentionType')

	def set_CrossLogRetentionType(self, CrossLogRetentionType):  # String
		self.add_query_param('CrossLogRetentionType', CrossLogRetentionType)
	def get_LogBackupRetentionPeriod(self): # Long
		return self.get_query_params().get('LogBackupRetentionPeriod')

	def set_LogBackupRetentionPeriod(self, LogBackupRetentionPeriod):  # Long
		self.add_query_param('LogBackupRetentionPeriod', LogBackupRetentionPeriod)
