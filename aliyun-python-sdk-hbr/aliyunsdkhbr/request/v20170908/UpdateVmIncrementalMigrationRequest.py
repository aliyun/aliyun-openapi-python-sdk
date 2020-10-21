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

class UpdateVmIncrementalMigrationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateVmIncrementalMigration','hbr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Applying(self):
		return self.get_query_params().get('Applying')

	def set_Applying(self,Applying):
		self.add_query_param('Applying',Applying)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_VmId(self):
		return self.get_query_params().get('VmId')

	def set_VmId(self,VmId):
		self.add_query_param('VmId',VmId)

	def get_Applied(self):
		return self.get_query_params().get('Applied')

	def set_Applied(self,Applied):
		self.add_query_param('Applied',Applied)

	def get_ApplyErrorMessage(self):
		return self.get_query_params().get('ApplyErrorMessage')

	def set_ApplyErrorMessage(self,ApplyErrorMessage):
		self.add_query_param('ApplyErrorMessage',ApplyErrorMessage)

	def get_VmSnapshotId(self):
		return self.get_query_params().get('VmSnapshotId')

	def set_VmSnapshotId(self,VmSnapshotId):
		self.add_query_param('VmSnapshotId',VmSnapshotId)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_SyncId(self):
		return self.get_query_params().get('SyncId')

	def set_SyncId(self,SyncId):
		self.add_query_param('SyncId',SyncId)

	def get_PlanId(self):
		return self.get_query_params().get('PlanId')

	def set_PlanId(self,PlanId):
		self.add_query_param('PlanId',PlanId)