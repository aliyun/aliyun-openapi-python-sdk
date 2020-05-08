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
class CreateSnapshotRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateSnapshot','hbr')
		self.set_protocol_type('https')

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_SnapshotName(self):
		return self.get_query_params().get('SnapshotName')

	def set_SnapshotName(self,SnapshotName):
		self.add_query_param('SnapshotName',SnapshotName)

	def get_UserAccountId(self):
		return self.get_query_params().get('UserAccountId')

	def set_UserAccountId(self,UserAccountId):
		self.add_query_param('UserAccountId',UserAccountId)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_ParentHash(self):
		return self.get_query_params().get('ParentHash')

	def set_ParentHash(self,ParentHash):
		self.add_query_param('ParentHash',ParentHash)

	def get_ContainerSnapshotId(self):
		return self.get_query_params().get('ContainerSnapshotId')

	def set_ContainerSnapshotId(self,ContainerSnapshotId):
		self.add_query_param('ContainerSnapshotId',ContainerSnapshotId)

	def get_ServerId(self):
		return self.get_query_params().get('ServerId')

	def set_ServerId(self,ServerId):
		self.add_query_param('ServerId',ServerId)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_SnapshotOption(self):
		return self.get_query_params().get('SnapshotOption')

	def set_SnapshotOption(self,SnapshotOption):
		self.add_query_param('SnapshotOption',SnapshotOption)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_SnapshotType(self):
		return self.get_query_params().get('SnapshotType')

	def set_SnapshotType(self,SnapshotType):
		self.add_query_param('SnapshotType',SnapshotType)

	def get_Extra(self):
		return self.get_query_params().get('Extra')

	def set_Extra(self,Extra):
		self.add_query_param('Extra',Extra)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_PlanId(self):
		return self.get_query_params().get('PlanId')

	def set_PlanId(self,PlanId):
		self.add_query_param('PlanId',PlanId)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)