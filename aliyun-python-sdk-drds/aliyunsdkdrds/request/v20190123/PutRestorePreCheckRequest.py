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

class PutRestorePreCheckRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'PutRestorePreCheck','drds')

	def get_PreferredBackupTime(self):
		return self.get_query_params().get('PreferredBackupTime')

	def set_PreferredBackupTime(self,PreferredBackupTime):
		self.add_query_param('PreferredBackupTime',PreferredBackupTime)

	def get_BackupDbNames(self):
		return self.get_query_params().get('BackupDbNames')

	def set_BackupDbNames(self,BackupDbNames):
		self.add_query_param('BackupDbNames',BackupDbNames)

	def get_BackupId(self):
		return self.get_query_params().get('BackupId')

	def set_BackupId(self,BackupId):
		self.add_query_param('BackupId',BackupId)

	def get_BackupMode(self):
		return self.get_query_params().get('BackupMode')

	def set_BackupMode(self,BackupMode):
		self.add_query_param('BackupMode',BackupMode)

	def get_BackupLevel(self):
		return self.get_query_params().get('BackupLevel')

	def set_BackupLevel(self,BackupLevel):
		self.add_query_param('BackupLevel',BackupLevel)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)