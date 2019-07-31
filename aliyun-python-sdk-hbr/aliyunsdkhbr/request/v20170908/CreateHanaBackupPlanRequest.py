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
class CreateHanaBackupPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateHanaBackupPlan','hbr')
		self.set_protocol_type('https')

	def get_Schedule(self):
		return self.get_query_params().get('Schedule')

	def set_Schedule(self,Schedule):
		self.add_query_param('Schedule',Schedule)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_BackupPrefix(self):
		return self.get_query_params().get('BackupPrefix')

	def set_BackupPrefix(self,BackupPrefix):
		self.add_query_param('BackupPrefix',BackupPrefix)

	def get_DatabaseName(self):
		return self.get_query_params().get('DatabaseName')

	def set_DatabaseName(self,DatabaseName):
		self.add_query_param('DatabaseName',DatabaseName)

	def get_PlanName(self):
		return self.get_query_params().get('PlanName')

	def set_PlanName(self,PlanName):
		self.add_query_param('PlanName',PlanName)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_BackupType(self):
		return self.get_query_params().get('BackupType')

	def set_BackupType(self,BackupType):
		self.add_query_param('BackupType',BackupType)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)