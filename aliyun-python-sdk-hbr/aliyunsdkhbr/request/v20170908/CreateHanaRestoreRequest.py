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

class CreateHanaRestoreRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateHanaRestore')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SidAdmin(self): # String
		return self.get_query_params().get('SidAdmin')

	def set_SidAdmin(self, SidAdmin):  # String
		self.add_query_param('SidAdmin', SidAdmin)
	def get_RecoveryPointInTime(self): # Long
		return self.get_query_params().get('RecoveryPointInTime')

	def set_RecoveryPointInTime(self, RecoveryPointInTime):  # Long
		self.add_query_param('RecoveryPointInTime', RecoveryPointInTime)
	def get_LogPosition(self): # Long
		return self.get_query_params().get('LogPosition')

	def set_LogPosition(self, LogPosition):  # Long
		self.add_query_param('LogPosition', LogPosition)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_ClearLog(self): # Boolean
		return self.get_query_params().get('ClearLog')

	def set_ClearLog(self, ClearLog):  # Boolean
		self.add_query_param('ClearLog', ClearLog)
	def get_Mode(self): # String
		return self.get_query_params().get('Mode')

	def set_Mode(self, Mode):  # String
		self.add_query_param('Mode', Mode)
	def get_CheckAccess(self): # Boolean
		return self.get_query_params().get('CheckAccess')

	def set_CheckAccess(self, CheckAccess):  # Boolean
		self.add_query_param('CheckAccess', CheckAccess)
	def get_BackupId(self): # Long
		return self.get_query_params().get('BackupId')

	def set_BackupId(self, BackupId):  # Long
		self.add_query_param('BackupId', BackupId)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_UseDelta(self): # Boolean
		return self.get_query_params().get('UseDelta')

	def set_UseDelta(self, UseDelta):  # Boolean
		self.add_query_param('UseDelta', UseDelta)
	def get_UseCatalog(self): # Boolean
		return self.get_query_params().get('UseCatalog')

	def set_UseCatalog(self, UseCatalog):  # Boolean
		self.add_query_param('UseCatalog', UseCatalog)
	def get_BackupPrefix(self): # String
		return self.get_query_params().get('BackupPrefix')

	def set_BackupPrefix(self, BackupPrefix):  # String
		self.add_query_param('BackupPrefix', BackupPrefix)
	def get_DatabaseName(self): # String
		return self.get_query_params().get('DatabaseName')

	def set_DatabaseName(self, DatabaseName):  # String
		self.add_query_param('DatabaseName', DatabaseName)
	def get_VolumeId(self): # Integer
		return self.get_query_params().get('VolumeId')

	def set_VolumeId(self, VolumeId):  # Integer
		self.add_query_param('VolumeId', VolumeId)
	def get_SourceClusterId(self): # String
		return self.get_query_params().get('SourceClusterId')

	def set_SourceClusterId(self, SourceClusterId):  # String
		self.add_query_param('SourceClusterId', SourceClusterId)
	def get_SystemCopy(self): # Boolean
		return self.get_query_params().get('SystemCopy')

	def set_SystemCopy(self, SystemCopy):  # Boolean
		self.add_query_param('SystemCopy', SystemCopy)
