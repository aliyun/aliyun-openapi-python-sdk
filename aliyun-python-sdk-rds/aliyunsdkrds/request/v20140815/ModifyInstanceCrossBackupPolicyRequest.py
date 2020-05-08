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

class ModifyInstanceCrossBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyInstanceCrossBackupPolicy','rds')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RetentType(self):
		return self.get_query_params().get('RetentType')

	def set_RetentType(self,RetentType):
		self.add_query_param('RetentType',RetentType)

	def get_BackupEnabled(self):
		return self.get_query_params().get('BackupEnabled')

	def set_BackupEnabled(self,BackupEnabled):
		self.add_query_param('BackupEnabled',BackupEnabled)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_CrossBackupType(self):
		return self.get_query_params().get('CrossBackupType')

	def set_CrossBackupType(self,CrossBackupType):
		self.add_query_param('CrossBackupType',CrossBackupType)

	def get_LogBackupEnabled(self):
		return self.get_query_params().get('LogBackupEnabled')

	def set_LogBackupEnabled(self,LogBackupEnabled):
		self.add_query_param('LogBackupEnabled',LogBackupEnabled)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_CrossBackupRegion(self):
		return self.get_query_params().get('CrossBackupRegion')

	def set_CrossBackupRegion(self,CrossBackupRegion):
		self.add_query_param('CrossBackupRegion',CrossBackupRegion)