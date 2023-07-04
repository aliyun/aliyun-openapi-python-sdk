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

class ModifyBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyBackupPolicy')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_LocalLogRetentionHours(self): # String
		return self.get_query_params().get('LocalLogRetentionHours')

	def set_LocalLogRetentionHours(self, LocalLogRetentionHours):  # String
		self.add_query_param('LocalLogRetentionHours', LocalLogRetentionHours)
	def get_BackupPriority(self): # Integer
		return self.get_query_params().get('BackupPriority')

	def set_BackupPriority(self, BackupPriority):  # Integer
		self.add_query_param('BackupPriority', BackupPriority)
	def get_LogBackupFrequency(self): # String
		return self.get_query_params().get('LogBackupFrequency')

	def set_LogBackupFrequency(self, LogBackupFrequency):  # String
		self.add_query_param('LogBackupFrequency', LogBackupFrequency)
	def get_ArchiveBackupKeepCount(self): # Integer
		return self.get_query_params().get('ArchiveBackupKeepCount')

	def set_ArchiveBackupKeepCount(self, ArchiveBackupKeepCount):  # Integer
		self.add_query_param('ArchiveBackupKeepCount', ArchiveBackupKeepCount)
	def get_BackupLog(self): # String
		return self.get_query_params().get('BackupLog')

	def set_BackupLog(self, BackupLog):  # String
		self.add_query_param('BackupLog', BackupLog)
	def get_BackupInterval(self): # String
		return self.get_query_params().get('BackupInterval')

	def set_BackupInterval(self, BackupInterval):  # String
		self.add_query_param('BackupInterval', BackupInterval)
	def get_HighSpaceUsageProtection(self): # String
		return self.get_query_params().get('HighSpaceUsageProtection')

	def set_HighSpaceUsageProtection(self, HighSpaceUsageProtection):  # String
		self.add_query_param('HighSpaceUsageProtection', HighSpaceUsageProtection)
	def get_LogBackupLocalRetentionNumber(self): # Integer
		return self.get_query_params().get('LogBackupLocalRetentionNumber')

	def set_LogBackupLocalRetentionNumber(self, LogBackupLocalRetentionNumber):  # Integer
		self.add_query_param('LogBackupLocalRetentionNumber', LogBackupLocalRetentionNumber)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_EnableBackupLog(self): # String
		return self.get_query_params().get('EnableBackupLog')

	def set_EnableBackupLog(self, EnableBackupLog):  # String
		self.add_query_param('EnableBackupLog', EnableBackupLog)
	def get_BackupPolicyMode(self): # String
		return self.get_query_params().get('BackupPolicyMode')

	def set_BackupPolicyMode(self, BackupPolicyMode):  # String
		self.add_query_param('BackupPolicyMode', BackupPolicyMode)
	def get_PreferredBackupPeriod(self): # String
		return self.get_query_params().get('PreferredBackupPeriod')

	def set_PreferredBackupPeriod(self, PreferredBackupPeriod):  # String
		self.add_query_param('PreferredBackupPeriod', PreferredBackupPeriod)
	def get_EnableIncrementDataBackup(self): # Boolean
		return self.get_query_params().get('EnableIncrementDataBackup')

	def set_EnableIncrementDataBackup(self, EnableIncrementDataBackup):  # Boolean
		self.add_query_param('EnableIncrementDataBackup', EnableIncrementDataBackup)
	def get_ReleasedKeepPolicy(self): # String
		return self.get_query_params().get('ReleasedKeepPolicy')

	def set_ReleasedKeepPolicy(self, ReleasedKeepPolicy):  # String
		self.add_query_param('ReleasedKeepPolicy', ReleasedKeepPolicy)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_CompressType(self): # String
		return self.get_query_params().get('CompressType')

	def set_CompressType(self, CompressType):  # String
		self.add_query_param('CompressType', CompressType)
	def get_LocalLogRetentionSpace(self): # String
		return self.get_query_params().get('LocalLogRetentionSpace')

	def set_LocalLogRetentionSpace(self, LocalLogRetentionSpace):  # String
		self.add_query_param('LocalLogRetentionSpace', LocalLogRetentionSpace)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ArchiveBackupKeepPolicy(self): # String
		return self.get_query_params().get('ArchiveBackupKeepPolicy')

	def set_ArchiveBackupKeepPolicy(self, ArchiveBackupKeepPolicy):  # String
		self.add_query_param('ArchiveBackupKeepPolicy', ArchiveBackupKeepPolicy)
	def get_PreferredBackupTime(self): # String
		return self.get_query_params().get('PreferredBackupTime')

	def set_PreferredBackupTime(self, PreferredBackupTime):  # String
		self.add_query_param('PreferredBackupTime', PreferredBackupTime)
	def get_BackupRetentionPeriod(self): # String
		return self.get_query_params().get('BackupRetentionPeriod')

	def set_BackupRetentionPeriod(self, BackupRetentionPeriod):  # String
		self.add_query_param('BackupRetentionPeriod', BackupRetentionPeriod)
	def get_BackupMethod(self): # String
		return self.get_query_params().get('BackupMethod')

	def set_BackupMethod(self, BackupMethod):  # String
		self.add_query_param('BackupMethod', BackupMethod)
	def get_ArchiveBackupRetentionPeriod(self): # String
		return self.get_query_params().get('ArchiveBackupRetentionPeriod')

	def set_ArchiveBackupRetentionPeriod(self, ArchiveBackupRetentionPeriod):  # String
		self.add_query_param('ArchiveBackupRetentionPeriod', ArchiveBackupRetentionPeriod)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
	def get_LogBackupRetentionPeriod(self): # String
		return self.get_query_params().get('LogBackupRetentionPeriod')

	def set_LogBackupRetentionPeriod(self, LogBackupRetentionPeriod):  # String
		self.add_query_param('LogBackupRetentionPeriod', LogBackupRetentionPeriod)
