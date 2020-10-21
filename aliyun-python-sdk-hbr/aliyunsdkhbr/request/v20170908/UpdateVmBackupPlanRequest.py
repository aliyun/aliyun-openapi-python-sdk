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

class UpdateVmBackupPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateVmBackupPlan','hbr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DiffSchedule(self):
		return self.get_query_params().get('DiffSchedule')

	def set_DiffSchedule(self,DiffSchedule):
		self.add_query_param('DiffSchedule',DiffSchedule)

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

	def get_DispatchPolicy(self):
		return self.get_query_params().get('DispatchPolicy')

	def set_DispatchPolicy(self,DispatchPolicy):
		self.add_query_param('DispatchPolicy',DispatchPolicy)

	def get_DispatchClientId(self):
		return self.get_query_params().get('DispatchClientId')

	def set_DispatchClientId(self,DispatchClientId):
		self.add_query_param('DispatchClientId',DispatchClientId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_PlanId(self):
		return self.get_query_params().get('PlanId')

	def set_PlanId(self,PlanId):
		self.add_query_param('PlanId',PlanId)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)