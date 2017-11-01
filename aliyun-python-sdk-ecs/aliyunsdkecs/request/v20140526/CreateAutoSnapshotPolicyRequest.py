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
class CreateAutoSnapshotPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateAutoSnapshotPolicy','ecs')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_timePoints(self):
		return self.get_query_params().get('timePoints')

	def set_timePoints(self,timePoints):
		self.add_query_param('timePoints',timePoints)

	def get_retentionDays(self):
		return self.get_query_params().get('retentionDays')

	def set_retentionDays(self,retentionDays):
		self.add_query_param('retentionDays',retentionDays)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_repeatWeekdays(self):
		return self.get_query_params().get('repeatWeekdays')

	def set_repeatWeekdays(self,repeatWeekdays):
		self.add_query_param('repeatWeekdays',repeatWeekdays)

	def get_autoSnapshotPolicyName(self):
		return self.get_query_params().get('autoSnapshotPolicyName')

	def set_autoSnapshotPolicyName(self,autoSnapshotPolicyName):
		self.add_query_param('autoSnapshotPolicyName',autoSnapshotPolicyName)