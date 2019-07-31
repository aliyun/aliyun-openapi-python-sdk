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
class UpdateSqlServerRestoreRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateSqlServerRestore','hbr')

	def get_ErrorMessage(self):
		return self.get_query_params().get('ErrorMessage')

	def set_ErrorMessage(self,ErrorMessage):
		self.add_query_param('ErrorMessage',ErrorMessage)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_Percentage(self):
		return self.get_query_params().get('Percentage')

	def set_Percentage(self,Percentage):
		self.add_query_param('Percentage',Percentage)

	def get_RestoreId(self):
		return self.get_query_params().get('RestoreId')

	def set_RestoreId(self,RestoreId):
		self.add_query_param('RestoreId',RestoreId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_BytesTotal(self):
		return self.get_query_params().get('BytesTotal')

	def set_BytesTotal(self,BytesTotal):
		self.add_query_param('BytesTotal',BytesTotal)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)