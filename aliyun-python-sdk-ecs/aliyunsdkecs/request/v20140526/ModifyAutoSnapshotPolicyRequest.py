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
from aliyunsdkecs.endpoint import endpoint_data

class ModifyAutoSnapshotPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyAutoSnapshotPolicy','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DataDiskPolicyEnabled(self): # Boolean
		return self.get_query_params().get('DataDiskPolicyEnabled')

	def set_DataDiskPolicyEnabled(self, DataDiskPolicyEnabled):  # Boolean
		self.add_query_param('DataDiskPolicyEnabled', DataDiskPolicyEnabled)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DataDiskPolicyRetentionDays(self): # Integer
		return self.get_query_params().get('DataDiskPolicyRetentionDays')

	def set_DataDiskPolicyRetentionDays(self, DataDiskPolicyRetentionDays):  # Integer
		self.add_query_param('DataDiskPolicyRetentionDays', DataDiskPolicyRetentionDays)
	def get_SystemDiskPolicyRetentionLastWeek(self): # Boolean
		return self.get_query_params().get('SystemDiskPolicyRetentionLastWeek')

	def set_SystemDiskPolicyRetentionLastWeek(self, SystemDiskPolicyRetentionLastWeek):  # Boolean
		self.add_query_param('SystemDiskPolicyRetentionLastWeek', SystemDiskPolicyRetentionLastWeek)
	def get_SystemDiskPolicyRetentionDays(self): # Integer
		return self.get_query_params().get('SystemDiskPolicyRetentionDays')

	def set_SystemDiskPolicyRetentionDays(self, SystemDiskPolicyRetentionDays):  # Integer
		self.add_query_param('SystemDiskPolicyRetentionDays', SystemDiskPolicyRetentionDays)
	def get_DataDiskPolicyTimePeriod(self): # Integer
		return self.get_query_params().get('DataDiskPolicyTimePeriod')

	def set_DataDiskPolicyTimePeriod(self, DataDiskPolicyTimePeriod):  # Integer
		self.add_query_param('DataDiskPolicyTimePeriod', DataDiskPolicyTimePeriod)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_SystemDiskPolicyTimePeriod(self): # Integer
		return self.get_query_params().get('SystemDiskPolicyTimePeriod')

	def set_SystemDiskPolicyTimePeriod(self, SystemDiskPolicyTimePeriod):  # Integer
		self.add_query_param('SystemDiskPolicyTimePeriod', SystemDiskPolicyTimePeriod)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_DataDiskPolicyRetentionLastWeek(self): # Boolean
		return self.get_query_params().get('DataDiskPolicyRetentionLastWeek')

	def set_DataDiskPolicyRetentionLastWeek(self, DataDiskPolicyRetentionLastWeek):  # Boolean
		self.add_query_param('DataDiskPolicyRetentionLastWeek', DataDiskPolicyRetentionLastWeek)
	def get_SystemDiskPolicyEnabled(self): # Boolean
		return self.get_query_params().get('SystemDiskPolicyEnabled')

	def set_SystemDiskPolicyEnabled(self, SystemDiskPolicyEnabled):  # Boolean
		self.add_query_param('SystemDiskPolicyEnabled', SystemDiskPolicyEnabled)
