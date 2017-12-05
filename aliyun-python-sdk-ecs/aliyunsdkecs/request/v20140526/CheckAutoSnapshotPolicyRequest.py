# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CheckAutoSnapshotPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CheckAutoSnapshotPolicy','ecs')

	def get_DataDiskPolicyEnabled(self):
		return self.get_query_params().get('DataDiskPolicyEnabled')

	def set_DataDiskPolicyEnabled(self,DataDiskPolicyEnabled):
		self.add_query_param('DataDiskPolicyEnabled',DataDiskPolicyEnabled)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DataDiskPolicyRetentionDays(self):
		return self.get_query_params().get('DataDiskPolicyRetentionDays')

	def set_DataDiskPolicyRetentionDays(self,DataDiskPolicyRetentionDays):
		self.add_query_param('DataDiskPolicyRetentionDays',DataDiskPolicyRetentionDays)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_SystemDiskPolicyRetentionLastWeek(self):
		return self.get_query_params().get('SystemDiskPolicyRetentionLastWeek')

	def set_SystemDiskPolicyRetentionLastWeek(self,SystemDiskPolicyRetentionLastWeek):
		self.add_query_param('SystemDiskPolicyRetentionLastWeek',SystemDiskPolicyRetentionLastWeek)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_SystemDiskPolicyTimePeriod(self):
		return self.get_query_params().get('SystemDiskPolicyTimePeriod')

	def set_SystemDiskPolicyTimePeriod(self,SystemDiskPolicyTimePeriod):
		self.add_query_param('SystemDiskPolicyTimePeriod',SystemDiskPolicyTimePeriod)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DataDiskPolicyRetentionLastWeek(self):
		return self.get_query_params().get('DataDiskPolicyRetentionLastWeek')

	def set_DataDiskPolicyRetentionLastWeek(self,DataDiskPolicyRetentionLastWeek):
		self.add_query_param('DataDiskPolicyRetentionLastWeek',DataDiskPolicyRetentionLastWeek)

	def get_SystemDiskPolicyRetentionDays(self):
		return self.get_query_params().get('SystemDiskPolicyRetentionDays')

	def set_SystemDiskPolicyRetentionDays(self,SystemDiskPolicyRetentionDays):
		self.add_query_param('SystemDiskPolicyRetentionDays',SystemDiskPolicyRetentionDays)

	def get_DataDiskPolicyTimePeriod(self):
		return self.get_query_params().get('DataDiskPolicyTimePeriod')

	def set_DataDiskPolicyTimePeriod(self,DataDiskPolicyTimePeriod):
		self.add_query_param('DataDiskPolicyTimePeriod',DataDiskPolicyTimePeriod)

	def get_SystemDiskPolicyEnabled(self):
		return self.get_query_params().get('SystemDiskPolicyEnabled')

	def set_SystemDiskPolicyEnabled(self,SystemDiskPolicyEnabled):
		self.add_query_param('SystemDiskPolicyEnabled',SystemDiskPolicyEnabled)