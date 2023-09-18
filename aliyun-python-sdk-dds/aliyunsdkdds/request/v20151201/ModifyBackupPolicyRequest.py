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
	def get_BackupInterval(self): # String
		return self.get_query_params().get('BackupInterval')

	def set_BackupInterval(self, BackupInterval):  # String
		self.add_query_param('BackupInterval', BackupInterval)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
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
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
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
	def get_LogBackupRetentionPeriod(self): # Long
		return self.get_query_params().get('LogBackupRetentionPeriod')

	def set_LogBackupRetentionPeriod(self, LogBackupRetentionPeriod):  # Long
		self.add_query_param('LogBackupRetentionPeriod', LogBackupRetentionPeriod)
