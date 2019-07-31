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
class CreatePlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreatePlan','hbr')
		self.set_protocol_type('https')

	def get_DiffPolicyId(self):
		return self.get_query_params().get('DiffPolicyId')

	def set_DiffPolicyId(self,DiffPolicyId):
		self.add_query_param('DiffPolicyId',DiffPolicyId)

	def get_ScheduleType(self):
		return self.get_query_params().get('ScheduleType')

	def set_ScheduleType(self,ScheduleType):
		self.add_query_param('ScheduleType',ScheduleType)

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_ServerType(self):
		return self.get_query_params().get('ServerType')

	def set_ServerType(self,ServerType):
		self.add_query_param('ServerType',ServerType)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_IncPolicyId(self):
		return self.get_query_params().get('IncPolicyId')

	def set_IncPolicyId(self,IncPolicyId):
		self.add_query_param('IncPolicyId',IncPolicyId)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_ServerId(self):
		return self.get_query_params().get('ServerId')

	def set_ServerId(self,ServerId):
		self.add_query_param('ServerId',ServerId)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_PlanName(self):
		return self.get_query_params().get('PlanName')

	def set_PlanName(self,PlanName):
		self.add_query_param('PlanName',PlanName)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_FullPolicyId(self):
		return self.get_query_params().get('FullPolicyId')

	def set_FullPolicyId(self,FullPolicyId):
		self.add_query_param('FullPolicyId',FullPolicyId)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)