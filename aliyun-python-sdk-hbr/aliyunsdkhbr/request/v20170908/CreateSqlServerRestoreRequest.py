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
class CreateSqlServerRestoreRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateSqlServerRestore','hbr')

	def get_TargetDatabaseName(self):
		return self.get_query_params().get('TargetDatabaseName')

	def set_TargetDatabaseName(self,TargetDatabaseName):
		self.add_query_param('TargetDatabaseName',TargetDatabaseName)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_FileDestination(self):
		return self.get_query_params().get('FileDestination')

	def set_FileDestination(self,FileDestination):
		self.add_query_param('FileDestination',FileDestination)

	def get_SourceDatabaseName(self):
		return self.get_query_params().get('SourceDatabaseName')

	def set_SourceDatabaseName(self,SourceDatabaseName):
		self.add_query_param('SourceDatabaseName',SourceDatabaseName)

	def get_SourceClusterId(self):
		return self.get_query_params().get('SourceClusterId')

	def set_SourceClusterId(self,SourceClusterId):
		self.add_query_param('SourceClusterId',SourceClusterId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ReplaceDatabase(self):
		return self.get_query_params().get('ReplaceDatabase')

	def set_ReplaceDatabase(self,ReplaceDatabase):
		self.add_query_param('ReplaceDatabase',ReplaceDatabase)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_PointInTime(self):
		return self.get_query_params().get('PointInTime')

	def set_PointInTime(self,PointInTime):
		self.add_query_param('PointInTime',PointInTime)