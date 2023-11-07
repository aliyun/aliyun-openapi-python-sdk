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
from aliyunsdkdrds.endpoint import endpoint_data

class SetBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'SetBackupPolicy','drds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BackupDbNames(self): # String
		return self.get_query_params().get('BackupDbNames')

	def set_BackupDbNames(self, BackupDbNames):  # String
		self.add_query_param('BackupDbNames', BackupDbNames)
	def get_BackupLog(self): # String
		return self.get_query_params().get('BackupLog')

	def set_BackupLog(self, BackupLog):  # String
		self.add_query_param('BackupLog', BackupLog)
	def get_PreferredBackupEndTime(self): # String
		return self.get_query_params().get('PreferredBackupEndTime')

	def set_PreferredBackupEndTime(self, PreferredBackupEndTime):  # String
		self.add_query_param('PreferredBackupEndTime', PreferredBackupEndTime)
	def get_PreferredBackupPeriod(self): # String
		return self.get_query_params().get('PreferredBackupPeriod')

	def set_PreferredBackupPeriod(self, PreferredBackupPeriod):  # String
		self.add_query_param('PreferredBackupPeriod', PreferredBackupPeriod)
	def get_PreferredBackupStartTime(self): # String
		return self.get_query_params().get('PreferredBackupStartTime')

	def set_PreferredBackupStartTime(self, PreferredBackupStartTime):  # String
		self.add_query_param('PreferredBackupStartTime', PreferredBackupStartTime)
	def get_BackupLevel(self): # String
		return self.get_query_params().get('BackupLevel')

	def set_BackupLevel(self, BackupLevel):  # String
		self.add_query_param('BackupLevel', BackupLevel)
	def get_DrdsInstanceId(self): # String
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self, DrdsInstanceId):  # String
		self.add_query_param('DrdsInstanceId', DrdsInstanceId)
	def get_DataBackupRetentionPeriod(self): # String
		return self.get_query_params().get('DataBackupRetentionPeriod')

	def set_DataBackupRetentionPeriod(self, DataBackupRetentionPeriod):  # String
		self.add_query_param('DataBackupRetentionPeriod', DataBackupRetentionPeriod)
	def get_BackupMode(self): # String
		return self.get_query_params().get('BackupMode')

	def set_BackupMode(self, BackupMode):  # String
		self.add_query_param('BackupMode', BackupMode)
	def get_LogBackupRetentionPeriod(self): # String
		return self.get_query_params().get('LogBackupRetentionPeriod')

	def set_LogBackupRetentionPeriod(self, LogBackupRetentionPeriod):  # String
		self.add_query_param('LogBackupRetentionPeriod', LogBackupRetentionPeriod)
