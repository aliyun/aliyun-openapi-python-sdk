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

class CreateVmMigrationPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateVmMigrationPlan','hbr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RestoreOptions(self):
		return self.get_query_params().get('RestoreOptions')

	def set_RestoreOptions(self,RestoreOptions):
		self.add_query_param('RestoreOptions',RestoreOptions)

	def get_MigrationSourcess(self):
		return self.get_query_params().get('MigrationSources')

	def set_MigrationSourcess(self, MigrationSourcess):
		for depth1 in range(len(MigrationSourcess)):
			if MigrationSourcess[depth1].get('RestoreOptions') is not None:
				self.add_query_param('MigrationSources.' + str(depth1 + 1) + '.RestoreOptions', MigrationSourcess[depth1].get('RestoreOptions'))
			if MigrationSourcess[depth1].get('VmId') is not None:
				self.add_query_param('MigrationSources.' + str(depth1 + 1) + '.VmId', MigrationSourcess[depth1].get('VmId'))
			if MigrationSourcess[depth1].get('Extra') is not None:
				self.add_query_param('MigrationSources.' + str(depth1 + 1) + '.Extra', MigrationSourcess[depth1].get('Extra'))
			if MigrationSourcess[depth1].get('HypervisorType') is not None:
				self.add_query_param('MigrationSources.' + str(depth1 + 1) + '.HypervisorType', MigrationSourcess[depth1].get('HypervisorType'))
			if MigrationSourcess[depth1].get('VmInfo') is not None:
				self.add_query_param('MigrationSources.' + str(depth1 + 1) + '.VmInfo', MigrationSourcess[depth1].get('VmInfo'))
			if MigrationSourcess[depth1].get('HypervisorId') is not None:
				self.add_query_param('MigrationSources.' + str(depth1 + 1) + '.HypervisorId', MigrationSourcess[depth1].get('HypervisorId'))
			if MigrationSourcess[depth1].get('VmName') is not None:
				self.add_query_param('MigrationSources.' + str(depth1 + 1) + '.VmName', MigrationSourcess[depth1].get('VmName'))
			if MigrationSourcess[depth1].get('ForceSilentSnapshot') is not None:
				self.add_query_param('MigrationSources.' + str(depth1 + 1) + '.ForceSilentSnapshot', MigrationSourcess[depth1].get('ForceSilentSnapshot'))

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_Mode(self):
		return self.get_query_params().get('Mode')

	def set_Mode(self,Mode):
		self.add_query_param('Mode',Mode)

	def get_IncrementalSyncSchedule(self):
		return self.get_query_params().get('IncrementalSyncSchedule')

	def set_IncrementalSyncSchedule(self,IncrementalSyncSchedule):
		self.add_query_param('IncrementalSyncSchedule',IncrementalSyncSchedule)

	def get_Delay(self):
		return self.get_query_params().get('Delay')

	def set_Delay(self,Delay):
		self.add_query_param('Delay',Delay)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)