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

class CreateVmBackupPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateVmBackupPlan','hbr')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DiffSchedule(self):
		return self.get_query_params().get('DiffSchedule')

	def set_DiffSchedule(self,DiffSchedule):
		self.add_query_param('DiffSchedule',DiffSchedule)

	def get_ServerType(self):
		return self.get_query_params().get('ServerType')

	def set_ServerType(self,ServerType):
		self.add_query_param('ServerType',ServerType)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_FullSchedule(self):
		return self.get_query_params().get('FullSchedule')

	def set_FullSchedule(self,FullSchedule):
		self.add_query_param('FullSchedule',FullSchedule)

	def get_IncSchedule(self):
		return self.get_query_params().get('IncSchedule')

	def set_IncSchedule(self,IncSchedule):
		self.add_query_param('IncSchedule',IncSchedule)

	def get_BackupSourcess(self):
		return self.get_query_params().get('BackupSources')

	def set_BackupSourcess(self, BackupSourcess):
		for depth1 in range(len(BackupSourcess)):
			if BackupSourcess[depth1].get('ClientId') is not None:
				self.add_query_param('BackupSources.' + str(depth1 + 1) + '.ClientId', BackupSourcess[depth1].get('ClientId'))
			if BackupSourcess[depth1].get('VmId') is not None:
				self.add_query_param('BackupSources.' + str(depth1 + 1) + '.VmId', BackupSourcess[depth1].get('VmId'))
			if BackupSourcess[depth1].get('UseHotAdd') is not None:
				self.add_query_param('BackupSources.' + str(depth1 + 1) + '.UseHotAdd', BackupSourcess[depth1].get('UseHotAdd'))
			if BackupSourcess[depth1].get('Extra') is not None:
				self.add_query_param('BackupSources.' + str(depth1 + 1) + '.Extra', BackupSourcess[depth1].get('Extra'))
			if BackupSourcess[depth1].get('VmInfo') is not None:
				self.add_query_param('BackupSources.' + str(depth1 + 1) + '.VmInfo', BackupSourcess[depth1].get('VmInfo'))
			if BackupSourcess[depth1].get('HypervisorId') is not None:
				self.add_query_param('BackupSources.' + str(depth1 + 1) + '.HypervisorId', BackupSourcess[depth1].get('HypervisorId'))
			if BackupSourcess[depth1].get('VmName') is not None:
				self.add_query_param('BackupSources.' + str(depth1 + 1) + '.VmName', BackupSourcess[depth1].get('VmName'))
			if BackupSourcess[depth1].get('ForceSilentSnapshot') is not None:
				self.add_query_param('BackupSources.' + str(depth1 + 1) + '.ForceSilentSnapshot', BackupSourcess[depth1].get('ForceSilentSnapshot'))

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)

	def get_RunAfterCreated(self):
		return self.get_query_params().get('RunAfterCreated')

	def set_RunAfterCreated(self,RunAfterCreated):
		self.add_query_param('RunAfterCreated',RunAfterCreated)