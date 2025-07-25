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
from aliyunsdkrds.endpoint import endpoint_data

class CreateBackupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateBackup','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_BackupStrategy(self): # String
		return self.get_query_params().get('BackupStrategy')

	def set_BackupStrategy(self, BackupStrategy):  # String
		self.add_query_param('BackupStrategy', BackupStrategy)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_BackupType(self): # String
		return self.get_query_params().get('BackupType')

	def set_BackupType(self, BackupType):  # String
		self.add_query_param('BackupType', BackupType)
	def get_BackupMethod(self): # String
		return self.get_query_params().get('BackupMethod')

	def set_BackupMethod(self, BackupMethod):  # String
		self.add_query_param('BackupMethod', BackupMethod)
	def get_BackupRetentionPeriod(self): # Long
		return self.get_query_params().get('BackupRetentionPeriod')

	def set_BackupRetentionPeriod(self, BackupRetentionPeriod):  # Long
		self.add_query_param('BackupRetentionPeriod', BackupRetentionPeriod)
	def get_DBName(self): # String
		return self.get_query_params().get('DBName')

	def set_DBName(self, DBName):  # String
		self.add_query_param('DBName', DBName)
