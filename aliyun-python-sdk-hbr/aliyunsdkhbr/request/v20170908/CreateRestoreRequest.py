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
class CreateRestoreRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateRestore','hbr')
		self.set_protocol_type('https')

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_Excludes(self):
		return self.get_query_params().get('Excludes')

	def set_Excludes(self,Excludes):
		self.add_query_param('Excludes',Excludes)

	def get_SourceClientId(self):
		return self.get_query_params().get('SourceClientId')

	def set_SourceClientId(self,SourceClientId):
		self.add_query_param('SourceClientId',SourceClientId)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_Includes(self):
		return self.get_query_params().get('Includes')

	def set_Includes(self,Includes):
		self.add_query_param('Includes',Includes)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_ServerId(self):
		return self.get_query_params().get('ServerId')

	def set_ServerId(self,ServerId):
		self.add_query_param('ServerId',ServerId)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_RestoreName(self):
		return self.get_query_params().get('RestoreName')

	def set_RestoreName(self,RestoreName):
		self.add_query_param('RestoreName',RestoreName)

	def get_Target(self):
		return self.get_query_params().get('Target')

	def set_Target(self,Target):
		self.add_query_param('Target',Target)

	def get_SnapshotHash(self):
		return self.get_query_params().get('SnapshotHash')

	def set_SnapshotHash(self,SnapshotHash):
		self.add_query_param('SnapshotHash',SnapshotHash)

	def get_RestoreType(self):
		return self.get_query_params().get('RestoreType')

	def set_RestoreType(self,RestoreType):
		self.add_query_param('RestoreType',RestoreType)

	def get_Extra(self):
		return self.get_query_params().get('Extra')

	def set_Extra(self,Extra):
		self.add_query_param('Extra',Extra)

	def get_ContainerRestoreId(self):
		return self.get_query_params().get('ContainerRestoreId')

	def set_ContainerRestoreId(self,ContainerRestoreId):
		self.add_query_param('ContainerRestoreId',ContainerRestoreId)