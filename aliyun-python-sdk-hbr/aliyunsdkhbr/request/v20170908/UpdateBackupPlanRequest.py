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

class UpdateBackupPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateBackupPlan','hbr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_Prefix(self):
		return self.get_query_params().get('Prefix')

	def set_Prefix(self,Prefix):
		self.add_query_param('Prefix',Prefix)

	def get_Schedule(self):
		return self.get_query_params().get('Schedule')

	def set_Schedule(self,Schedule):
		self.add_query_param('Schedule',Schedule)

	def get_Paths(self):
		return self.get_query_params().get('Path')

	def set_Paths(self, Paths):
		for depth1 in range(len(Paths)):
			if Paths[depth1] is not None:
				self.add_query_param('Path.' + str(depth1 + 1) , Paths[depth1])

	def get_SpeedLimit(self):
		return self.get_query_params().get('SpeedLimit')

	def set_SpeedLimit(self,SpeedLimit):
		self.add_query_param('SpeedLimit',SpeedLimit)

	def get_PlanName(self):
		return self.get_query_params().get('PlanName')

	def set_PlanName(self,PlanName):
		self.add_query_param('PlanName',PlanName)

	def get_PlanId(self):
		return self.get_query_params().get('PlanId')

	def set_PlanId(self,PlanId):
		self.add_query_param('PlanId',PlanId)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_Detail(self):
		return self.get_query_params().get('Detail')

	def set_Detail(self,Detail):
		self.add_query_param('Detail',Detail)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)