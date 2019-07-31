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
class UpdateSnapshotRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateSnapshot','hbr')
		self.set_protocol_type('https')

	def get_ErrorMessage(self):
		return self.get_query_params().get('ErrorMessage')

	def set_ErrorMessage(self,ErrorMessage):
		self.add_query_param('ErrorMessage',ErrorMessage)

	def get_ActualBytes(self):
		return self.get_query_params().get('ActualBytes')

	def set_ActualBytes(self,ActualBytes):
		self.add_query_param('ActualBytes',ActualBytes)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_ErrorFile(self):
		return self.get_query_params().get('ErrorFile')

	def set_ErrorFile(self,ErrorFile):
		self.add_query_param('ErrorFile',ErrorFile)

	def get_UserAccountId(self):
		return self.get_query_params().get('UserAccountId')

	def set_UserAccountId(self,UserAccountId):
		self.add_query_param('UserAccountId',UserAccountId)

	def get_ParentHash(self):
		return self.get_query_params().get('ParentHash')

	def set_ParentHash(self,ParentHash):
		self.add_query_param('ParentHash',ParentHash)

	def get_ExitCode(self):
		return self.get_query_params().get('ExitCode')

	def set_ExitCode(self,ExitCode):
		self.add_query_param('ExitCode',ExitCode)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_SnapshotHash(self):
		return self.get_query_params().get('SnapshotHash')

	def set_SnapshotHash(self,SnapshotHash):
		self.add_query_param('SnapshotHash',SnapshotHash)

	def get_ItemsDone(self):
		return self.get_query_params().get('ItemsDone')

	def set_ItemsDone(self,ItemsDone):
		self.add_query_param('ItemsDone',ItemsDone)

	def get_Size(self):
		return self.get_query_params().get('Size')

	def set_Size(self,Size):
		self.add_query_param('Size',Size)

	def get_ItemsTotal(self):
		return self.get_query_params().get('ItemsTotal')

	def set_ItemsTotal(self,ItemsTotal):
		self.add_query_param('ItemsTotal',ItemsTotal)

	def get_CompleteTime(self):
		return self.get_query_params().get('CompleteTime')

	def set_CompleteTime(self,CompleteTime):
		self.add_query_param('CompleteTime',CompleteTime)

	def get_ErrorCount(self):
		return self.get_query_params().get('ErrorCount')

	def set_ErrorCount(self,ErrorCount):
		self.add_query_param('ErrorCount',ErrorCount)

	def get_BytesDone(self):
		return self.get_query_params().get('BytesDone')

	def set_BytesDone(self,BytesDone):
		self.add_query_param('BytesDone',BytesDone)

	def get_BytesTotal(self):
		return self.get_query_params().get('BytesTotal')

	def set_BytesTotal(self,BytesTotal):
		self.add_query_param('BytesTotal',BytesTotal)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)