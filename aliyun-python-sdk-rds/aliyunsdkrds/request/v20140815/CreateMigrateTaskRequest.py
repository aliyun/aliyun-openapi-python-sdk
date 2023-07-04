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

class CreateMigrateTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateMigrateTask')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_IsOnlineDB(self): # String
		return self.get_query_params().get('IsOnlineDB')

	def set_IsOnlineDB(self, IsOnlineDB):  # String
		self.add_query_param('IsOnlineDB', IsOnlineDB)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_MigrateTaskId(self): # String
		return self.get_query_params().get('MigrateTaskId')

	def set_MigrateTaskId(self, MigrateTaskId):  # String
		self.add_query_param('MigrateTaskId', MigrateTaskId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_OssObjectPositions(self): # String
		return self.get_query_params().get('OssObjectPositions')

	def set_OssObjectPositions(self, OssObjectPositions):  # String
		self.add_query_param('OssObjectPositions', OssObjectPositions)
	def get_OSSUrls(self): # String
		return self.get_query_params().get('OSSUrls')

	def set_OSSUrls(self, OSSUrls):  # String
		self.add_query_param('OSSUrls', OSSUrls)
	def get_DBName(self): # String
		return self.get_query_params().get('DBName')

	def set_DBName(self, DBName):  # String
		self.add_query_param('DBName', DBName)
	def get_BackupMode(self): # String
		return self.get_query_params().get('BackupMode')

	def set_BackupMode(self, BackupMode):  # String
		self.add_query_param('BackupMode', BackupMode)
	def get_CheckDBMode(self): # String
		return self.get_query_params().get('CheckDBMode')

	def set_CheckDBMode(self, CheckDBMode):  # String
		self.add_query_param('CheckDBMode', CheckDBMode)
