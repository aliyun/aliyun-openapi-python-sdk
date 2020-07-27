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
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyBackupPolicy','rds')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_LocalLogRetentionHours(self):
		return self.get_query_params().get('LocalLogRetentionHours')

	def set_LocalLogRetentionHours(self,LocalLogRetentionHours):
		self.add_query_param('LocalLogRetentionHours',LocalLogRetentionHours)

	def get_LogBackupFrequency(self):
		return self.get_query_params().get('LogBackupFrequency')

	def set_LogBackupFrequency(self,LogBackupFrequency):
		self.add_query_param('LogBackupFrequency',LogBackupFrequency)

	def get_ArchiveBackupKeepCount(self):
		return self.get_query_params().get('ArchiveBackupKeepCount')

	def set_ArchiveBackupKeepCount(self,ArchiveBackupKeepCount):
		self.add_query_param('ArchiveBackupKeepCount',ArchiveBackupKeepCount)

	def get_BackupLog(self):
		return self.get_query_params().get('BackupLog')

	def set_BackupLog(self,BackupLog):
		self.add_query_param('BackupLog',BackupLog)

	def get_BackupInterval(self):
		return self.get_query_params().get('BackupInterval')

	def set_BackupInterval(self,BackupInterval):
		self.add_query_param('BackupInterval',BackupInterval)

	def get_HighSpaceUsageProtection(self):
		return self.get_query_params().get('HighSpaceUsageProtection')

	def set_HighSpaceUsageProtection(self,HighSpaceUsageProtection):
		self.add_query_param('HighSpaceUsageProtection',HighSpaceUsageProtection)

	def get_LogBackupLocalRetentionNumber(self):
		return self.get_query_params().get('LogBackupLocalRetentionNumber')

	def set_LogBackupLocalRetentionNumber(self,LogBackupLocalRetentionNumber):
		self.add_query_param('LogBackupLocalRetentionNumber',LogBackupLocalRetentionNumber)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_EnableBackupLog(self):
		return self.get_query_params().get('EnableBackupLog')

	def set_EnableBackupLog(self,EnableBackupLog):
		self.add_query_param('EnableBackupLog',EnableBackupLog)

	def get_BackupPolicyMode(self):
		return self.get_query_params().get('BackupPolicyMode')

	def set_BackupPolicyMode(self,BackupPolicyMode):
		self.add_query_param('BackupPolicyMode',BackupPolicyMode)

	def get_PreferredBackupPeriod(self):
		return self.get_query_params().get('PreferredBackupPeriod')

	def set_PreferredBackupPeriod(self,PreferredBackupPeriod):
		self.add_query_param('PreferredBackupPeriod',PreferredBackupPeriod)

	def get_ReleasedKeepPolicy(self):
		return self.get_query_params().get('ReleasedKeepPolicy')

	def set_ReleasedKeepPolicy(self,ReleasedKeepPolicy):
		self.add_query_param('ReleasedKeepPolicy',ReleasedKeepPolicy)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_CompressType(self):
		return self.get_query_params().get('CompressType')

	def set_CompressType(self,CompressType):
		self.add_query_param('CompressType',CompressType)

	def get_LocalLogRetentionSpace(self):
		return self.get_query_params().get('LocalLogRetentionSpace')

	def set_LocalLogRetentionSpace(self,LocalLogRetentionSpace):
		self.add_query_param('LocalLogRetentionSpace',LocalLogRetentionSpace)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ArchiveBackupKeepPolicy(self):
		return self.get_query_params().get('ArchiveBackupKeepPolicy')

	def set_ArchiveBackupKeepPolicy(self,ArchiveBackupKeepPolicy):
		self.add_query_param('ArchiveBackupKeepPolicy',ArchiveBackupKeepPolicy)

	def get_PreferredBackupTime(self):
		return self.get_query_params().get('PreferredBackupTime')

	def set_PreferredBackupTime(self,PreferredBackupTime):
		self.add_query_param('PreferredBackupTime',PreferredBackupTime)

	def get_BackupRetentionPeriod(self):
		return self.get_query_params().get('BackupRetentionPeriod')

	def set_BackupRetentionPeriod(self,BackupRetentionPeriod):
		self.add_query_param('BackupRetentionPeriod',BackupRetentionPeriod)

	def get_ArchiveBackupRetentionPeriod(self):
		return self.get_query_params().get('ArchiveBackupRetentionPeriod')

	def set_ArchiveBackupRetentionPeriod(self,ArchiveBackupRetentionPeriod):
		self.add_query_param('ArchiveBackupRetentionPeriod',ArchiveBackupRetentionPeriod)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_LogBackupRetentionPeriod(self):
		return self.get_query_params().get('LogBackupRetentionPeriod')

	def set_LogBackupRetentionPeriod(self,LogBackupRetentionPeriod):
		self.add_query_param('LogBackupRetentionPeriod',LogBackupRetentionPeriod)