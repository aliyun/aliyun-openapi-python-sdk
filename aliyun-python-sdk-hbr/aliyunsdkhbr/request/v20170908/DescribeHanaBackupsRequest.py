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
class DescribeHanaBackupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'DescribeHanaBackups','hbr')
		self.set_protocol_type('https')

	def get_RecoveryPointInTime(self):
		return self.get_query_params().get('RecoveryPointInTime')

	def set_RecoveryPointInTime(self,RecoveryPointInTime):
		self.add_query_param('RecoveryPointInTime',RecoveryPointInTime)

	def get_LogPosition(self):
		return self.get_query_params().get('LogPosition')

	def set_LogPosition(self,LogPosition):
		self.add_query_param('LogPosition',LogPosition)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_IncludeLog(self):
		return self.get_query_params().get('IncludeLog')

	def set_IncludeLog(self,IncludeLog):
		self.add_query_param('IncludeLog',IncludeLog)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_Mode(self):
		return self.get_query_params().get('Mode')

	def set_Mode(self,Mode):
		self.add_query_param('Mode',Mode)

	def get_IncludeIncremental(self):
		return self.get_query_params().get('IncludeIncremental')

	def set_IncludeIncremental(self,IncludeIncremental):
		self.add_query_param('IncludeIncremental',IncludeIncremental)

	def get_UseBackint(self):
		return self.get_query_params().get('UseBackint')

	def set_UseBackint(self,UseBackint):
		self.add_query_param('UseBackint',UseBackint)

	def get_DatabaseName(self):
		return self.get_query_params().get('DatabaseName')

	def set_DatabaseName(self,DatabaseName):
		self.add_query_param('DatabaseName',DatabaseName)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_VolumeId(self):
		return self.get_query_params().get('VolumeId')

	def set_VolumeId(self,VolumeId):
		self.add_query_param('VolumeId',VolumeId)

	def get_SourceClusterId(self):
		return self.get_query_params().get('SourceClusterId')

	def set_SourceClusterId(self,SourceClusterId):
		self.add_query_param('SourceClusterId',SourceClusterId)

	def get_IncludeDifferential(self):
		return self.get_query_params().get('IncludeDifferential')

	def set_IncludeDifferential(self,IncludeDifferential):
		self.add_query_param('IncludeDifferential',IncludeDifferential)

	def get_SystemCopy(self):
		return self.get_query_params().get('SystemCopy')

	def set_SystemCopy(self,SystemCopy):
		self.add_query_param('SystemCopy',SystemCopy)