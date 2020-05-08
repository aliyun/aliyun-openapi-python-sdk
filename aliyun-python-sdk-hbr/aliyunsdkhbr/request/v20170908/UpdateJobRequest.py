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
class UpdateJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateJob','hbr')
		self.set_protocol_type('https')

	def get_CurrentSnapshotId(self):
		return self.get_query_params().get('CurrentSnapshotId')

	def set_CurrentSnapshotId(self,CurrentSnapshotId):
		self.add_query_param('CurrentSnapshotId',CurrentSnapshotId)

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_JobStatus(self):
		return self.get_query_params().get('JobStatus')

	def set_JobStatus(self,JobStatus):
		self.add_query_param('JobStatus',JobStatus)

	def get_UserAccountId(self):
		return self.get_query_params().get('UserAccountId')

	def set_UserAccountId(self,UserAccountId):
		self.add_query_param('UserAccountId',UserAccountId)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_Schedule(self):
		return self.get_query_params().get('Schedule')

	def set_Schedule(self,Schedule):
		self.add_query_param('Schedule',Schedule)

	def get_PolicyId(self):
		return self.get_query_params().get('PolicyId')

	def set_PolicyId(self,PolicyId):
		self.add_query_param('PolicyId',PolicyId)

	def get_LastSnapshotId(self):
		return self.get_query_params().get('LastSnapshotId')

	def set_LastSnapshotId(self,LastSnapshotId):
		self.add_query_param('LastSnapshotId',LastSnapshotId)

	def get_JobOption(self):
		return self.get_query_params().get('JobOption')

	def set_JobOption(self,JobOption):
		self.add_query_param('JobOption',JobOption)

	def get_JobName(self):
		return self.get_query_params().get('JobName')

	def set_JobName(self,JobName):
		self.add_query_param('JobName',JobName)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)