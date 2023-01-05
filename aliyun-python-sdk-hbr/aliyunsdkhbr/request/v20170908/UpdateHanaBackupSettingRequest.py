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
from aliyunsdkhbr.endpoint import endpoint_data

class UpdateHanaBackupSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateHanaBackupSetting')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_LogBackupParameterFile(self): # String
		return self.get_query_params().get('LogBackupParameterFile')

	def set_LogBackupParameterFile(self, LogBackupParameterFile):  # String
		self.add_query_param('LogBackupParameterFile', LogBackupParameterFile)
	def get_VaultId(self): # String
		return self.get_query_params().get('VaultId')

	def set_VaultId(self, VaultId):  # String
		self.add_query_param('VaultId', VaultId)
	def get_LogBackupTimeout(self): # Long
		return self.get_query_params().get('LogBackupTimeout')

	def set_LogBackupTimeout(self, LogBackupTimeout):  # Long
		self.add_query_param('LogBackupTimeout', LogBackupTimeout)
	def get_DataBackupParameterFile(self): # String
		return self.get_query_params().get('DataBackupParameterFile')

	def set_DataBackupParameterFile(self, DataBackupParameterFile):  # String
		self.add_query_param('DataBackupParameterFile', DataBackupParameterFile)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_EnableAutoLogBackup(self): # Boolean
		return self.get_query_params().get('EnableAutoLogBackup')

	def set_EnableAutoLogBackup(self, EnableAutoLogBackup):  # Boolean
		self.add_query_param('EnableAutoLogBackup', EnableAutoLogBackup)
	def get_LogBackupUsingBackint(self): # Boolean
		return self.get_query_params().get('LogBackupUsingBackint')

	def set_LogBackupUsingBackint(self, LogBackupUsingBackint):  # Boolean
		self.add_query_param('LogBackupUsingBackint', LogBackupUsingBackint)
	def get_CatalogBackupUsingBackint(self): # Boolean
		return self.get_query_params().get('CatalogBackupUsingBackint')

	def set_CatalogBackupUsingBackint(self, CatalogBackupUsingBackint):  # Boolean
		self.add_query_param('CatalogBackupUsingBackint', CatalogBackupUsingBackint)
	def get_DatabaseName(self): # String
		return self.get_query_params().get('DatabaseName')

	def set_DatabaseName(self, DatabaseName):  # String
		self.add_query_param('DatabaseName', DatabaseName)
	def get_CatalogBackupParameterFile(self): # String
		return self.get_query_params().get('CatalogBackupParameterFile')

	def set_CatalogBackupParameterFile(self, CatalogBackupParameterFile):  # String
		self.add_query_param('CatalogBackupParameterFile', CatalogBackupParameterFile)
