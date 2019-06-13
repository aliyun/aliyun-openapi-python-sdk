# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ModifyBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyBackupPolicy','rds')

	def get_PreferredBackupPeriod(self):
		return self.get_query_params().get('PreferredBackupPeriod')

	def set_PreferredBackupPeriod(self,PreferredBackupPeriod):
		self.add_query_param('PreferredBackupPeriod',PreferredBackupPeriod)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_LocalLogRetentionHours(self):
		return self.get_query_params().get('LocalLogRetentionHours')

	def set_LocalLogRetentionHours(self,LocalLogRetentionHours):
		self.add_query_param('LocalLogRetentionHours',LocalLogRetentionHours)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_LogBackupFrequency(self):
		return self.get_query_params().get('LogBackupFrequency')

	def set_LogBackupFrequency(self,LogBackupFrequency):
		self.add_query_param('LogBackupFrequency',LogBackupFrequency)

	def get_CompressType(self):
		return self.get_query_params().get('CompressType')

	def set_CompressType(self,CompressType):
		self.add_query_param('CompressType',CompressType)

	def get_BackupLog(self):
		return self.get_query_params().get('BackupLog')

	def set_BackupLog(self,BackupLog):
		self.add_query_param('BackupLog',BackupLog)

	def get_LocalLogRetentionSpace(self):
		return self.get_query_params().get('LocalLogRetentionSpace')

	def set_LocalLogRetentionSpace(self,LocalLogRetentionSpace):
		self.add_query_param('LocalLogRetentionSpace',LocalLogRetentionSpace)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Duplication(self):
		return self.get_query_params().get('Duplication')

	def set_Duplication(self,Duplication):
		self.add_query_param('Duplication',Duplication)

	def get_PreferredBackupTime(self):
		return self.get_query_params().get('PreferredBackupTime')

	def set_PreferredBackupTime(self,PreferredBackupTime):
		self.add_query_param('PreferredBackupTime',PreferredBackupTime)

	def get_BackupRetentionPeriod(self):
		return self.get_query_params().get('BackupRetentionPeriod')

	def set_BackupRetentionPeriod(self,BackupRetentionPeriod):
		self.add_query_param('BackupRetentionPeriod',BackupRetentionPeriod)

	def get_DuplicationContent(self):
		return self.get_query_params().get('DuplicationContent')

	def set_DuplicationContent(self,DuplicationContent):
		self.add_query_param('DuplicationContent',DuplicationContent)

	def get_HighSpaceUsageProtection(self):
		return self.get_query_params().get('HighSpaceUsageProtection')

	def set_HighSpaceUsageProtection(self,HighSpaceUsageProtection):
		self.add_query_param('HighSpaceUsageProtection',HighSpaceUsageProtection)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_DuplicationLocation(self):
		return self.get_query_params().get('DuplicationLocation')

	def set_DuplicationLocation(self,DuplicationLocation):
		self.add_query_param('DuplicationLocation',DuplicationLocation)

	def get_LogBackupRetentionPeriod(self):
		return self.get_query_params().get('LogBackupRetentionPeriod')

	def set_LogBackupRetentionPeriod(self,LogBackupRetentionPeriod):
		self.add_query_param('LogBackupRetentionPeriod',LogBackupRetentionPeriod)

	def get_EnableBackupLog(self):
		return self.get_query_params().get('EnableBackupLog')

	def set_EnableBackupLog(self,EnableBackupLog):
		self.add_query_param('EnableBackupLog',EnableBackupLog)

	def get_BackupPolicyMode(self):
		return self.get_query_params().get('BackupPolicyMode')

	def set_BackupPolicyMode(self,BackupPolicyMode):
		self.add_query_param('BackupPolicyMode',BackupPolicyMode)