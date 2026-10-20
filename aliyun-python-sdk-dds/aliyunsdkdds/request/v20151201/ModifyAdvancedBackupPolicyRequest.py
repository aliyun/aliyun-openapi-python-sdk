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
from aliyunsdkdds.endpoint import endpoint_data
import json

class ModifyAdvancedBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dds', '2015-12-01', 'ModifyAdvancedBackupPolicy','dds')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AdvancedBackupDataPolicies(self): # Array
		return self.get_query_params().get('AdvancedBackupDataPolicies')

	def set_AdvancedBackupDataPolicies(self, AdvancedBackupDataPolicies):  # Array
		self.add_query_param("AdvancedBackupDataPolicies", json.dumps(AdvancedBackupDataPolicies))
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_BackupRetentionPolicyOnClusterDeletion(self): # Integer
		return self.get_query_params().get('BackupRetentionPolicyOnClusterDeletion')

	def set_BackupRetentionPolicyOnClusterDeletion(self, BackupRetentionPolicyOnClusterDeletion):  # Integer
		self.add_query_param('BackupRetentionPolicyOnClusterDeletion', BackupRetentionPolicyOnClusterDeletion)
	def get_AdvancedBackupLogPolicies(self): # Array
		return self.get_query_params().get('AdvancedBackupLogPolicies')

	def set_AdvancedBackupLogPolicies(self, AdvancedBackupLogPolicies):  # Array
		self.add_query_param("AdvancedBackupLogPolicies", json.dumps(AdvancedBackupLogPolicies))
	def get_SnapshotBackupType(self): # String
		return self.get_query_params().get('SnapshotBackupType')

	def set_SnapshotBackupType(self, SnapshotBackupType):  # String
		self.add_query_param('SnapshotBackupType', SnapshotBackupType)
	def get_PreferredBackupTime(self): # String
		return self.get_query_params().get('PreferredBackupTime')

	def set_PreferredBackupTime(self, PreferredBackupTime):  # String
		self.add_query_param('PreferredBackupTime', PreferredBackupTime)
