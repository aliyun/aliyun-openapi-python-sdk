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
class UpdateHanaRestoreRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateHanaRestore','hbr')
		self.set_protocol_type('https')

	def get_Phase(self):
		return self.get_query_params().get('Phase')

	def set_Phase(self,Phase):
		self.add_query_param('Phase',Phase)

	def get_UtcReachedTime(self):
		return self.get_query_params().get('UtcReachedTime')

	def set_UtcReachedTime(self,UtcReachedTime):
		self.add_query_param('UtcReachedTime',UtcReachedTime)

	def get_SysEndTime(self):
		return self.get_query_params().get('SysEndTime')

	def set_SysEndTime(self,SysEndTime):
		self.add_query_param('SysEndTime',SysEndTime)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_SysStartTime(self):
		return self.get_query_params().get('SysStartTime')

	def set_SysStartTime(self,SysStartTime):
		self.add_query_param('SysStartTime',SysStartTime)

	def get_RestoreId(self):
		return self.get_query_params().get('RestoreId')

	def set_RestoreId(self,RestoreId):
		self.add_query_param('RestoreId',RestoreId)

	def get_MaxPhase(self):
		return self.get_query_params().get('MaxPhase')

	def set_MaxPhase(self,MaxPhase):
		self.add_query_param('MaxPhase',MaxPhase)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Message(self):
		return self.get_query_params().get('Message')

	def set_Message(self,Message):
		self.add_query_param('Message',Message)

	def get_DatabaseRestoreId(self):
		return self.get_query_params().get('DatabaseRestoreId')

	def set_DatabaseRestoreId(self,DatabaseRestoreId):
		self.add_query_param('DatabaseRestoreId',DatabaseRestoreId)

	def get_MaxProgress(self):
		return self.get_query_params().get('MaxProgress')

	def set_MaxProgress(self,MaxProgress):
		self.add_query_param('MaxProgress',MaxProgress)

	def get_CurrentProgress(self):
		return self.get_query_params().get('CurrentProgress')

	def set_CurrentProgress(self,CurrentProgress):
		self.add_query_param('CurrentProgress',CurrentProgress)

	def get_UtcEndTime(self):
		return self.get_query_params().get('UtcEndTime')

	def set_UtcEndTime(self,UtcEndTime):
		self.add_query_param('UtcEndTime',UtcEndTime)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_CurrentPhase(self):
		return self.get_query_params().get('CurrentPhase')

	def set_CurrentPhase(self,CurrentPhase):
		self.add_query_param('CurrentPhase',CurrentPhase)

	def get_UtcStartTime(self):
		return self.get_query_params().get('UtcStartTime')

	def set_UtcStartTime(self,UtcStartTime):
		self.add_query_param('UtcStartTime',UtcStartTime)

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)

	def get_State(self):
		return self.get_query_params().get('State')

	def set_State(self,State):
		self.add_query_param('State',State)

	def get_SysReachedTime(self):
		return self.get_query_params().get('SysReachedTime')

	def set_SysReachedTime(self,SysReachedTime):
		self.add_query_param('SysReachedTime',SysReachedTime)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)