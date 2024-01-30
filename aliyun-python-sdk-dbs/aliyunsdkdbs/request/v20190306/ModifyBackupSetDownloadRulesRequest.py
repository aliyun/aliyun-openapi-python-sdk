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
from aliyunsdkdbs.endpoint import endpoint_data

class ModifyBackupSetDownloadRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dbs', '2019-03-06', 'ModifyBackupSetDownloadRules','cbs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FullDataFormat(self): # String
		return self.get_query_params().get('FullDataFormat')

	def set_FullDataFormat(self, FullDataFormat):  # String
		self.add_query_param('FullDataFormat', FullDataFormat)
	def get_BackupGatewayId(self): # Long
		return self.get_query_params().get('BackupGatewayId')

	def set_BackupGatewayId(self, BackupGatewayId):  # Long
		self.add_query_param('BackupGatewayId', BackupGatewayId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_BackupSetDownloadTargetType(self): # String
		return self.get_query_params().get('BackupSetDownloadTargetType')

	def set_BackupSetDownloadTargetType(self, BackupSetDownloadTargetType):  # String
		self.add_query_param('BackupSetDownloadTargetType', BackupSetDownloadTargetType)
	def get_BackupPlanId(self): # String
		return self.get_query_params().get('BackupPlanId')

	def set_BackupPlanId(self, BackupPlanId):  # String
		self.add_query_param('BackupPlanId', BackupPlanId)
	def get_BackupSetDownloadTargetTypeLocation(self): # String
		return self.get_query_params().get('BackupSetDownloadTargetTypeLocation')

	def set_BackupSetDownloadTargetTypeLocation(self, BackupSetDownloadTargetTypeLocation):  # String
		self.add_query_param('BackupSetDownloadTargetTypeLocation', BackupSetDownloadTargetTypeLocation)
	def get_BackupSetDownloadDir(self): # String
		return self.get_query_params().get('BackupSetDownloadDir')

	def set_BackupSetDownloadDir(self, BackupSetDownloadDir):  # String
		self.add_query_param('BackupSetDownloadDir', BackupSetDownloadDir)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_OpenAutoDownload(self): # Boolean
		return self.get_query_params().get('OpenAutoDownload')

	def set_OpenAutoDownload(self, OpenAutoDownload):  # Boolean
		self.add_query_param('OpenAutoDownload', OpenAutoDownload)
	def get_IncrementDataFormat(self): # String
		return self.get_query_params().get('IncrementDataFormat')

	def set_IncrementDataFormat(self, IncrementDataFormat):  # String
		self.add_query_param('IncrementDataFormat', IncrementDataFormat)
