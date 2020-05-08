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
class CreateBackupPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateBackupPlan','hbr')

	def get_CreateTime(self):
		return self.get_query_params().get('CreateTime')

	def set_CreateTime(self,CreateTime):
		self.add_query_param('CreateTime',CreateTime)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_Prefix(self):
		return self.get_query_params().get('Prefix')

	def set_Prefix(self,Prefix):
		self.add_query_param('Prefix',Prefix)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Bucket(self):
		return self.get_query_params().get('Bucket')

	def set_Bucket(self,Bucket):
		self.add_query_param('Bucket',Bucket)

	def get_Schedule(self):
		return self.get_query_params().get('Schedule')

	def set_Schedule(self,Schedule):
		self.add_query_param('Schedule',Schedule)

	def get_Paths(self):
		return self.get_query_params().get('Paths')

	def set_Paths(self,Paths):
		for i in range(len(Paths)):	
			if Paths[i] is not None:
				self.add_query_param('Path.' + str(i + 1) , Paths[i]);

	def get_PlanName(self):
		return self.get_query_params().get('PlanName')

	def set_PlanName(self,PlanName):
		self.add_query_param('PlanName',PlanName)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_BackupSourceGroupId(self):
		return self.get_query_params().get('BackupSourceGroupId')

	def set_BackupSourceGroupId(self,BackupSourceGroupId):
		self.add_query_param('BackupSourceGroupId',BackupSourceGroupId)

	def get_BackupType(self):
		return self.get_query_params().get('BackupType')

	def set_BackupType(self,BackupType):
		self.add_query_param('BackupType',BackupType)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)

	def get_FileSystemId(self):
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self,FileSystemId):
		self.add_query_param('FileSystemId',FileSystemId)